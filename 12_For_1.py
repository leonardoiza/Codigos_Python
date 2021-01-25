listasw=[]
listarouter=[]
listapc=[]
lista=["R1",'R2','R3','S1','S2','S3','R4','R5','PC1','PC2','PC3']
for i in lista:
    if 'S' in i:
        listasw.append(i)
    elif 'R' in i:
        listarouter.append(i)
    else:
        listapc.append(i)
print('Switches: ',listasw,'\nRouters: ',listarouter,'\nDispositivos: ',listapc)

