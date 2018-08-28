import pandas as pd
import calendar

df = pd.read_csv("velocidades.csv")

# def registrosBD():
#     print("¿Cuántos registros tiene la base de datos?")
#     print(df['id'].count())
# registrosBD()

# def tiposVehiculos():
#     print("¿Cuántos vehículos existen en la base de datos?")
#     dfVehiculo = df.groupby( by=['Vehiculo']).count()
#     print(dfVehiculo['id'].count())
# tiposVehiculos()

# def diasRegistros():
#     print("¿Cuantos dias aparecen, y de que fecha a que fecha son los registros?")
#     print(df['fecha'].min())
#     print(df['fecha'].max())
#     dfFecha = df.groupby( by=['fecha']).count()
#     print(dfFecha['id'].count())
# diasRegistros()

# def mesesCompletos():
#     print("¿Cuántos meses completos de información se tienen?")
#     fechaInicio = pd.to_datetime(df['fecha'].min())
#     fechaFin = pd.to_datetime(df['fecha'].max())
#     resultado = fechaFin.month - fechaInicio.month + 1
#     if fechaInicio.day != 1:
#         resultado = resultado - 1
#     if fechaFin.day != calendar.monthrange(fechaFin.year, fechaFin.month)[1]:
#         resultado = resultado - 1
#     print("Meses totales entre fechas: ", resultado)
# mesesCompletos()

# print("¿En qué horario trabaja la flota?")
# dfRango = df[(df['hora'] > "05:00:00") & (df['hora'] < "05:30:00")]
# dfGroup = dfRango.groupby(by=['hora']).count()
# print(dfGroup)


#7000   0-2
#7000   2-4
#6000   4-6
#300    6-8
#552    8-10
#6000    10-12
#7000    12-14
#7000    14-16
#7000    16-18
#7000    18-20
#7000    20-22
#7000    22-24

#dfSuma = dfmayor.groupby(by=['hora']).count()

# # ¿Cuál es la velocidad máxima registrada y que vehículo es?

# print(df['velocidad'].max())
# dfMaxVel = df[df['velocidad'] == df['velocidad'].max()]
# dfVehiculo = dfMaxVel['Vehiculo'].drop_duplicates()
# print(dfVehiculo.to_string(index=False))

#
# # El límite de velocidad máximo permitido es de 80 Km/h, ¿Cuántos vehículos lo rebasan y cuales son?
# dfMaxVel = df[df['velocidad'] > 80]
# print(dfMaxVel['Vehiculo'].count())
# print(dfMaxVel['Vehiculo'].drop_duplicates().to_string(index=False))

#
# # ¿Cuál es la hora con mayor frecuencia de excesos velocidad?
def horaExcesoVelocidad():
    numeroExcesosMaximo = 0
    horaExcesoInicio = "00:00:00"
    horaExcesoFin = "01:00:00"
    dfMaxVel = df[df['velocidad'] > 80]
    horas = ["00:00:00", "01:00:00", "02:00:00", "03:00:00", "04:00:00", "05:00:00",
             "06:00:00", "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
             "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00", "17:00:00",
             "18:00:00", "19:00:00", "20:00:00", "21:00:00", "22:00:00", "23:00:00"]
    for i in range(0, 24):
        horaActualInicio =  horas[i]
        horaActualFin = horas[(i + 1) % 24]
        dfHora = dfMaxVel[(dfMaxVel['hora'] > horaActualInicio) & (dfMaxVel['hora'] < horaActualFin)]
        print(dfHora['hora'].count())
        numeroExcesosHora = dfHora['id'].count()
        if numeroExcesosMaximo < numeroExcesosHora:
            numeroExcesosMaximo = dfHora['id'].count()
            horaExcesoInicio = horaActualInicio
            horaExcesoFin = horaActualFin
    print(numeroExcesosMaximo)
    print(horaExcesoInicio)
    print(horaExcesoFin)
horaExcesoVelocidad()

# group by
#
# # Tomando en cuenta los meses completos, ¿Cuál es la velocidad promedio de cada mes?
#
