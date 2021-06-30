# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:16:51 2019

@author: Elvin
"""
import time
def ext_trunc_gcd(a, b):
    x0, x1, y0, y1, i = 1, 0, 0, 1, 1
    while b != 0:
        q = a//b
        b, a, r = a % b, b, b 

        x1, x0 = x0 - x1*q, x1
        y1, y0 = y0 - y1*q, y1

        if b > r//2:
            b = r - b
            x1, y1 = x0 - x1, y0 - y1
        print(" This is step number ", i, "\n", "x = ", x0, "\n", "y = ", y0, "\n", "r = ", r, "\n")
        i += 1
    print(" x = ", x0, "\n", "y = ", y0, "\n", "GCD = ", a, "\n")
    #print("Lineal representaion: ", 54483686959007493763 * x0 + 18560558022652223623 * y0)



#def ext_trunc_gcd1(a, b):
#    x=[]
#    y=[]
#    q=[]
#    r=[]
#    if(a>b):
#        r=[a,b]
#        x=[1,0]
#        y=[0,1]
#        q=[0,int(a/b)]
#        
#    else:
#        r=[b,a]
#        x=[1,0]
#        y=[0,1]
#        q=[0,int(b/a)]
#    i=1
#    while (r[i]!=0) and i<10 :
#        #r.append(r[i-1]-r[i]*q[i])
#        r.append(r[i-1]%r[i])# остаток от деления
#        x.append(x[i-1]-q[i]*x[i])
#        y.append(y[i-1]-q[i]*y[i])
#        if(r[i+1]>r[i]//2):
#            r[i+1]=r[i]-r[i+1]
#            x[i+1]=x[i]-x[i+1]
#            y[i+1]=y[i]-y[i+1]
#
#        if(r[i+1]!=0):
#         q.append(r[i]//r[i+1])
#        i=i+1
#    return(r,x,y,q,i)


























def binary_gcd(a,b):
    u=[a]
    v=[b]
    g=1 # 2^n  делили пополам
    while( a&1==0 and b&1==0): #четные числа делим пополам 
        a=a>>1
        b=b>>1
        g=g<<1
    u.append(a)
    v.append(b)
    a_big=[1]
    b_big=[0]
    c_big=[0]
    d_big=[1]
    while(u[len(u)-1]!=0):
        while(u[len(u)-1]&1==0): # если четное - делим пополам 
            u.append(u[len(u)-1]>>1)
            v.append(v[len(v)-1])
            if( a_big[len(a_big)-1]&1==0 and b_big[len(b_big)-1]&1==0):
                a_big.append(a_big[len(a_big)-1]>>1)
                b_big.append(b_big[len(b_big)-1]>>1)
                c_big.append(c_big[len(c_big)-1])
                d_big.append(d_big[len(d_big)-1])

                
            else:
                a_big.append((a_big[len(a_big)-1]+b)>>1)
                b_big.append((b_big[len(b_big)-1]-a)>>1)
                c_big.append(c_big[len(c_big)-1])
                d_big.append(d_big[len(d_big)-1])

        while(v[len(v)-1]&1==0):
            v.append(v[len(v)-1]>>1)
            u.append(u[len(u)-1])
            if( c_big[len(c_big)-1]&1==0 and d_big[len(d_big)-1]&1==0):
                c_big.append(c_big[len(c_big)-1]>>1)
                d_big.append(d_big[len(d_big)-1]>>1)
                a_big.append(a_big[len(a_big)-1])
                b_big.append(b_big[len(b_big)-1])
            else:
                c_big.append((c_big[len(c_big)-1]+b)>>1)
                d_big.append((d_big[len(d_big)-1]-a)>>1)
                a_big.append(a_big[len(a_big)-1])
                b_big.append(b_big[len(b_big)-1])
       
        if(u[len(u)-1]>=v[len(v)-1]):
            u.append(u[len(u)-1]-v[len(v)-1])
            v.append(v[len(v)-1])
            #a_big=a_big-c_big
            #b_big=b_big-d_big
            c_big.append(c_big[len(c_big)-1])
            d_big.append(d_big[len(d_big)-1])
            a_big.append(a_big[len(a_big)-1]-c_big[len(c_big)-1])
            b_big.append(b_big[len(b_big)-1]-d_big[len(d_big)-1])
        else:
#            v=v-u
#            c_big=c_big-a_big
#            d_big=d_big-b_big
            u.append(u[len(u)-1])
            v.append(v[len(v)-1]-u[len(u)-1])
            c_big.append(c_big[len(c_big)-1]-a_big[len(a_big)-1])
            d_big.append(d_big[len(d_big)-1]-b_big[len(b_big)-1])
            a_big.append(a_big[len(a_big)-1])
            b_big.append(b_big[len(b_big)-1])
            
    d=g*v[len(v)-1]
    x=c_big
    y=d_big
    
    return u,v,g,a_big,b_big,c_big,d_big
    
#print("x=",c_big[i])
#    print("y=",d_big[i])
#    print("r=",v[i])
#    print("\n")
def print_binary(u,v,c_big,d_big):
    #for i in range (len(u)-1):
            i=len(u)-1
            j=0
            if len(u)-1<=20:
                while(j!=i):
                    print("This is step number ",j)
                    print("x=",c_big[j])
                    print("y=",d_big[j])
                    print("r=",v[j])
                    print("\n")
                    j=j+1
            else:
                j=0
                k=0
                while(k<=5):
                    print("This is step number ",j)
                    print("x=",c_big[j])
                    print("y=",d_big[j])
                    print("r=",v[j])
                    print("\n")
                    j=j+1
                    k=k+1
                k=i-5
                while(k<i):
                    print("This is step number ",k)
                    print("x=",c_big[k])
                    print("y=",d_big[k])
                    print("r=",v[k])
                    print("\n")
                    k=k+1
    
    
    
    
    
    
    
    
    
    
def lcf(a, b):
    x=[]
    y=[]
    q=[]
    r=[]
    if(a>b):
        r=[a,b]
        x=[1,0]
        y=[0,1]
        q=[0,int(a/b)]
        
    else:
        r=[b,a]
        x=[1,0]
        y=[0,1]
        q=[0,int(b/a)]
    i=1
    #and i<10
    while (r[i]!=0) :
        r.append(r[i-1]-r[i]*q[i])
        x.append(x[i-1]-q[i]*x[i])
        y.append(y[i-1]-q[i]*y[i])
        if(r[i+1]!=0):
            q.append(int(r[i]/r[i+1]))
        i=i+1
    return(r,x,y,q,i)



def print_lcf(r,x,y,q,i):
            j=0
            if i<=20:
                while(j!=i):
                    print("This is step number ",j)
                    print("x=",x[j])
                    print("y=",y[j])
                    print("r=",r[j])
                    print("\n")
                    j=j+1
            else:
                k=0
                while(k<=5):
                    print("This is step number ",j)
                    print("x=",x[j])
                    print("y=",y[j])
                    print("r=",r[j])
                    print("\n")
                    j=j+1
                    k=k+1
                k=i-5
                while(k<=i):
                    print("This is step number ",k)
                    print("x=",x[k])
                    print("y=",y[k])
                    print("r=",r[k])
                    print("\n")
                    k=k+1
                    
    
#print(r,x,y,q,i)
            c=r[0]*x[i-1]+r[1]*y[i-1] #линейное представление
            print("GCD is ",c,"\n")
            
    
a=54483686959007493763
b=18560558022652223623
start_timer=time.time()
w=0
while(w!=40): 
    r,x,y,q,i=lcf(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
print_lcf(r,x,y,q,i)

a=789562977113236900734581316386890915207
b=1005985211191154203111699030262914561477
start_timer=time.time()
w=0
while(w!=40):
    r,x,y,q,i=lcf(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
print_lcf(r,x,y,q,i)

a=10558827912399769907376935948275939778780300395755458219204344728087472959384733
b=43128934157413675086381537882840913408474198240046464548432550782694303777981327

start_timer=time.time()
w=0
while(w!=40):
    r,x,y,q,i=lcf(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
print_lcf(r,x,y,q,i)
#j=0
#if i<=20:
#    while(j!=i):
#        print("This is step number ",j)
#        print("x=",x[j])
#        print("y=",y[j])
#        print("r=",r[j])
#        print("\n")
#        j=j+1
#else:
#    k=0
#    while(k<=5):
#        print("This is step number ",j)
#        print("x=",x[j])
#        print("y=",y[j])
#        print("r=",r[j])
#        print("\n")
#        j=j+1
#    k=i-5
#    while(k<=i):
#        print("This is step number ",k)
#        print("x=",x[k])
#        print("y=",y[k])
#        print("r=",r[k])
#        print("\n")
#        k=k+1
#    
##print(r,x,y,q,i)
#c=r[0]*x[i-1]+r[1]*y[i-1] #линейное представление
#print(c)
###"-----------------------------------------------
print("----------------:SECOND TASK:------------")
#расширенный бинарный алгоритм Евклида 
a=54483686959007493763
b=18560558022652223623
start_timer=time.time()
w=0
while(w!=40): 
    u,v,g,a_big,b_big,c_big,d_big=binary_gcd(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
#print(u,v,g,a_big,b_big,c_big,d_big)
print("GCD is ",a*c_big[len(c_big)-1]+b*d_big[len(d_big)-1]) # линейное представление
print_binary(u,v,c_big,d_big)

#for i in range (len(u)-1):
#    print("Step number ",i)
#   # print("x= ",u[i], v[i],c_big[i],d_big[i]) 
#    print("x=",c_big[i])
#    print("y=",d_big[i])
#    print("r=",v[i])
#    print("\n")

a=789562977113236900734581316386890915207
b=1005985211191154203111699030262914561477
start_timer=time.time()
w=0
while(w!=40): 
    u,v,g,a_big,b_big,c_big,d_big=binary_gcd(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
print("GCD is ",a*c_big[len(c_big)-1]+b*d_big[len(d_big)-1]) # линейное представление
print_binary(u,v,c_big,d_big)


a=10558827912399769907376935948275939778780300395755458219204344728087472959384733
b=43128934157413675086381537882840913408474198240046464548432550782694303777981327
start_timer=time.time()
w=0
while(w!=40): 
    u,v,g,a_big,b_big,c_big,d_big=binary_gcd(a,b)
    w=w+1
print("time of work:",(time.time()-start_timer)/40,"\n")
print("GCD is ",a*c_big[len(c_big)-1]+b*d_big[len(d_big)-1]) # линейное представление
print_binary(u,v,c_big,d_big)
k=0;
print("--------------------3 TASK------------------")

#c=a*x+b*y
#print(c)
a=504
b=140
#start_timer=time.time()
#w=0
#while(w!=40):
ext_trunc_gcd(a, b)
#    w=w+1
#print("time of work:",(time.time()-start_timer)/40,"\n")
#print("GCD",a*x[i-1]+b*y[i-1])#lineral
#print(r,x,y,q,i)
#print_lcf(r,x,y,q,i)

a=789562977113236900734581316386890915207
b=1005985211191154203111699030262914561477
#start_timer=time.time()
#w=0
#while(w!=40):
ext_trunc_gcd(a, b)
#    w=w+1
#print("time of work:",(time.time()-start_timer)/40,"\n")
#print("GCD",a*x[i-1]+b*y[i-1])#lineral
#print(r,x,y,q,i)
#print_lcf(r,x,y,q,i)

a=10558827912399769907376935948275939778780300395755458219204344728087472959384733
b=43128934157413675086381537882840913408474198240046464548432550782694303777981327
#start_timer=time.time()
#w=0
#while(w!=40):
ext_trunc_gcd(a, b)
#    w=w+1
#print("time of work:",(time.time()-start_timer)/40,"\n")
#print("GCD",a*x[i-1]+b*y[i-1])#lineral
#print(r,x,y,q,i)
#print_lcf(r,x,y,q,i)

