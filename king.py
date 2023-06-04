dineroTotal = 100
monedasInicio = 30
precioEntrada = 0.19852
usdtGastado = round(monedasInicio * precioEntrada, 2)
usdtRestante = round(dineroTotal - monedasInicio * precioEntrada, 2)
contador = 1

# Definir el ancho de cada columna
column_width = 15

# Imprimir encabezados
print("{:<{width}} | {:<{width}} | {:<{width}} | {:<{width}} | {:<{width}} | {:<{width}}".format(
    "Contador", "Dinero Total", "Dinero Restante", "Monedas Inicio", "Precio Entrada", "USDT Gastado",
    width=column_width
))
print("-" * (column_width * 6 + 5))

# Imprimir valores de la tabla
print("{:^{width}} | {:^{width}} | {:^{width}} | {:^{width}} | {:^{width}} | {:^{width}}".format(
    contador, dineroTotal,usdtRestante, monedasInicio, precioEntrada, usdtGastado, 
    width=column_width
))

# Ciclo hasta que se agote el dinero
while usdtRestante > 0:
    monedasAdicionalPorc = 40
    distanciaRecompra = 3

    monedasAdicional = round(monedasInicio * (monedasAdicionalPorc / 100), 2)
    nuevoPrecio = round(precioEntrada - (precioEntrada * (distanciaRecompra / 100)), 5)
    montoAdicionalGastado = round(monedasAdicional * nuevoPrecio, 2)
    totalGastado = round(usdtGastado + montoAdicionalGastado, 2)
    saldoRestante = round(usdtRestante - montoAdicionalGastado, 2)

    # Incrementar el contador para la nueva operación
    contador += 1

    # Verificar si el saldo restante es negativo
    if saldoRestante < 0:
        break

    # Imprimir valores de la tabla para la nueva operación
    print("{:^{width}} | {:^{width}} | {:^{width}} | {:^{width}} | {:^{width}} | {:^{width}}".format(
        contador, dineroTotal, saldoRestante, monedasInicio + monedasAdicional, nuevoPrecio, montoAdicionalGastado,
        width=column_width
    ))

    # Actualizar las variables para la próxima iteración
    dineroTotal = dineroTotal
    monedasInicio += monedasAdicional
    precioEntrada = nuevoPrecio
    usdtGastado = totalGastado
    usdtRestante = saldoRestante


