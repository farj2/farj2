# FELIPE RAMOS JERIA -- 07-04-2026
# L1 Análisis de caso
# Lección 1: Introducción al Lenguaje Python
'''
En el presente script se pretende desarrollar una herramienta de
Registro y Organización para datos básicos de empleados, los cuales
contienen "Nombre", "Edad" y "Puesto"
El propósito es calcular el año de jubilación de cada empleado en
en base de su edad y el límite de jubilación (65 años promedio)
'''
#Se declaran nombre, edad y puesto del empleado
nombre="Felipe"
edad=24
puesto="data scientist junior"

#Se declara el anio actual para en base a este calcular el anio de jubilación
anio_actual=2026

#Para calcular el anio de jubilación primero se obtienen cuántos
#anios le faltan al empleado para cumplir los 65
#luego se calcula el anio de jubilación teniendo los anios que
#le faltan al empleado sumados al anio actual
anios_para_jubilar=65-edad
anio_jubilacion=anio_actual+anios_para_jubilar

#Se desplega el anio de jubilación del empleado
print(nombre,"se va a jubilar el anio: ",anio_jubilacion)