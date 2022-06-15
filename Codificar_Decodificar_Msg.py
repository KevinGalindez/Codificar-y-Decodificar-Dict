import json
import base64

# Valores obtenidos por otros modulos
valores_obtenidos_previamente_frecuencia = 60
valores_obtenidos_previamente_volt = -5
valores_obtenidos_previamente_temp = 18.5
valores_obtenidos_previamente_version = "V01203"
string_a_codificar = "0"

# Diccionario de formato
format1 = {}

def llenardic(clave, valor, diccionario):

    if type(valor) is int:
        typex = "int"
    elif type(valor) is float:
        typex = "float"
    elif type(valor) is str:
        typex = "str"

    diccionario[clave] = {
            "valor": valor,
            "type": typex,
            "len": len(str(valor))
            }

def codificar_mensaje(diccionario):

    mensaje = str(diccionario)
    mensaje_salida_ascii = mensaje.encode('ascii')
    mensaje_salida_byte = base64.b64encode(mensaje_salida_ascii)
    return mensaje_salida_byte

def de_codificar_mensaje(bytestring):

    mensaje_recibido_bytes = base64.b64decode(bytestring)
    mensaje_recibido_ascii = mensaje_recibido_bytes.decode('ascii')
    mensaje_recibido_ascii = mensaje_recibido_ascii.replace("'", "\"")
    dict_salida = json.loads(mensaje_recibido_ascii)
    return dict_salida


llenardic("frecuencia", valores_obtenidos_previamente_frecuencia, format1)
llenardic("volt", valores_obtenidos_previamente_volt, format1)
llenardic("temp", valores_obtenidos_previamente_temp, format1)
llenardic("version", valores_obtenidos_previamente_version, format1)

print(format1, type(format1))
print()

mensaje_salida = codificar_mensaje(format1)

print(mensaje_salida, type(mensaje_salida))
print()

mensaje_recibido = de_codificar_mensaje(mensaje_salida)

print(mensaje_recibido, type(mensaje_recibido))
print()

