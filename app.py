print("⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")

aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência do aparelho (W): "))
horas_dia = float(input("Tempo médio de uso diário (horas): "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo = consumo_mensal * 0.75

print("\n📊 RESULTADO")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f} por mês")
print("💡 Dica: reduzir o tempo de uso pode ajudar a economizar energia!")