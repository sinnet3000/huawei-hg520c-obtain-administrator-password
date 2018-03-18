print "\n  ########################################################################"
print "  #      Huawei Echo Life HG520 SSID2WEP Lookup v0.2                     #"
print "  #      Genera words.txt en la carpeta donde esta el script             #"
print "  #      con las posibles WEP key                                        #"
print "  #      Luis Colunga - sinnet3000.blogspot.com                          #"
print "  ########################################################################"

try:
    from bsddb import db
except ImportError:
    from bsddb3 import db
adb = db.DB( )
adb.open('rainbow_table_berkeleydb_hash.db', db.DB_HASH, db.DB_DIRTY_READ )

passwords = open('words.txt', 'w')                    
ssid = raw_input("\n  Ingresa el prefijo del SSID: ")

cursor = adb.cursor()

wep = cursor.set(ssid)
resultado = wep[1] + "\n"
passwords.write(resultado)

while (cursor.next_dup() != None):
    wep = cursor.next_dup()
    resultado = wep[1] + "\n"
    passwords.write(resultado)
    if cursor.next_dup() is None:
        break

adb.close()
passwords.close()

print "El archivo ha sido generado"
