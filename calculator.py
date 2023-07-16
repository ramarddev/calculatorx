dineroTotal = float(input("Ingresa el dinero a invertir: "))
monedasInicio = float(input("Ingresa las monedas compradas en la entrada: "))
precioEntrada = float(input("Ingresa el precio de entrada de la moneda: "))
monedasAdicionalPorc = float(input("Ingresa el porcentaje adicional de monedas a comprar: "))
distanciaRecompra = float(input("Ingresa el porcentaje de distancia entre cada recompra nueva: "))
usdtGastado = float(round(monedasInicio * precioEntrada, 2))
usdtRestante = float(round(dineroTotal - monedasInicio * precioEntrada, 2))
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

    monedasAdicional = round(monedasInicio * (monedasAdicionalPorc / 100), 4)
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
        contador, dineroTotal, saldoRestante, "{:.2f}".format(monedasInicio + monedasAdicional), nuevoPrecio, montoAdicionalGastado,
        width=column_width
    ))

    # Actualizar las variables para la próxima iteración
    dineroTotal = dineroTotal
    monedasInicio += monedasAdicional
    precioEntrada = nuevoPrecio
    usdtGastado = totalGastado
    usdtRestante = saldoRestante



