import ast

def base_update(k,v):
        key=k
        value=v
        file=open('parking_base.txt','r+')
        d=file.read()
        global r
        r=ast.literal_eval(d)

        dict2={key:value}
    

        if bl=="A" and r['a']>0:
            r.update(dict2)
            r['a']-=1
            file.truncate(0)
            file.close()
        elif r['a']<=0:
            print("NO SLOTS TO PARK IN A BLOCK")

        elif bl=="B" and r['b']>0:
            r.update(dict2)
            r['b']-=1
            file.truncate(0)
            file.close()
        else:
            print("NO SLOTS TO PARK IN B BLOCK")

        
        file=open('parking_base.txt','w')
        w=file.write(str(r))

name=input("Enter name: ")
ph=int(input("Enter phone number: "))
days=int(input("Enter number of days needed to park: "))
bl=input("Enter which block you need for parking: ").upper()
cost=days*50
base_update(name,(ph,days,cost))
