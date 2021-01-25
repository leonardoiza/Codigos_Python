acl = int(input("Ingrese el # de ACL: "))
if acl >= 1 and acl <= 99:
    print("Es una ACL estándar")
elif acl >=100 and acl <= 199:
    print("Es una ACL extendida")
else:
    print("No es un # de ACL válida")
