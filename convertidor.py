import masa 
import tiempo as time
import temperatura as temp

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsius" and unidad_destino == "fahrenheit" :
        return temp.celsius_fahrenheit(valor)
    
    if unidad_origen == "celsius" and unidad_destino == "kelvin" :
        return temp.celsius_kelvin(valor)
    

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "gramos" :
        return masa.kilogramos_gramos(valor)
    
    if unidad_origen == "toneladas" and unidad_destino == "gramos" :
        return masa.toneladas_gramos(valor)


def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "minutos" and unidad_destino == "segundos" :
        return time.minutos_segundos(valor)
    
    if unidad_origen == "horas" and unidad_destino == "minutos" :
        return time.horas_minutos(valor)


if __name__ == "__main__":

    medida = input("Digite su magnitud de medida: ")

    if medida == "temperatura":

            unidad_origen = input("Digite primer medida (celsius a fahrenheit, celsius a kelvin): ")
            unidad_destino = input("Digite segunda medida (celsius a kelvin, celsius fahrenheit): ")
            valor = int(input("Digite su valor: "))
            convertir = convertir_temperatura(valor, unidad_origen, unidad_destino)

            print(f"{valor} de {unidad_origen} son equivalentes a {convertir} de {unidad_destino}")


    if medida == "masa":

            unidad_origen = input("Digite primer medida (kilogramos a gramos, toneladas a gramos): ")
            unidad_destino = input("Digite segunda medida (kilogramos a gramos, toneladas a gramos): ")
            valor = int(input("Digite su valor: "))
            convertir = convertir_masa(valor, unidad_origen, unidad_destino)

            print(f"{valor} de {unidad_origen} son equivalentes a {convertir} de {unidad_destino}")


    if medida == "tiempo":

            unidad_origen = input("Digite primer medida (minutos a segundos, horas a minutos): ")
            unidad_destino = input("Digite segunda medida (minutos a segundos, horas a minutos): ")
            valor = int(input("Digite su valor: "))
            convertir = convertir_tiempo(valor, unidad_origen, unidad_destino)

            print(f"{valor} de {unidad_origen} son equivalentes a {convertir} de {unidad_destino}")