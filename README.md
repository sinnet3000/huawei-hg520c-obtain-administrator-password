# Huawei-HG-520C-Rainbow-Table
Método para reducir las posibilidades y obtener casi instantáneamente la contraseña de administrador default de los modems Huawei HG-520C remotamente.

Previamente se habia descubierto una manera de obtener la contraseña basado en la MAC Address del equipo, que tambien esta estrechamente relacionado con el SSID. Entonces se me ocurrio hacer una rainbow table que contenga SSIDs con su respectivas contraseñas.

Por cada SSID se obtienen 768 posibilidades de contraseñas. 

Para poder utilizar este metodo, primeramente hay que generar la rainbow table con el script rainbow_table_generator.py. Usa BerkeleyDB, esto fue porque con bases de datos relacional se ponia lento para la creacion (a final de cuentas solo lo usas una vez a menos que sea necesario meter nuevas MAC Address de Huawei) pero especialmente ayuda bastante a la consultas.

La forma que se ejecuta el ataque es asi: 

Primeramente obtenemos el SSID con una vulnerabilidad que tienen estos modems, podemos entrar a:

http:// ((( IP REMOTA ))) /Listadeparametros.html 
  
Esta url no tiene validacion de autenticacion en los Huawei HG-520C.

Despues que tenemos el SSID, con el script possible_wep_keys_generator.py, consultamos las posibles 768 contraseñas el script genera un .txt listo para meterlo en tools como Brutus para realizar un ataque "diccionario".

## Links

Aca un demo corriendo el ataque:

https://www.youtube.com/watch?v=esjCkwipv9k

Articulo original que publique en el 2011:

https://www.underground.org.mx/index.php?topic=26664.0
