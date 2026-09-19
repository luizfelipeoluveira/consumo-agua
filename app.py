tipo_imóvel = input("Escolha o número da alternativa do tipo do seu imóvel: \n 1. Casa\n 2. Imóveis Comerciais e Corporativos\n 3. Apartamento\n")
consumo_mensal_agua = float(input("Insira o seu cosummo mensal de água em metros cúbicos(m³): "))

if tipo_imóvel == "2":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif tipo_imóvel == "3" and consumo_mensal_agua <= 10:
    print("Consumo econômico – excelente controle de água!")
elif (tipo_imóvel ==  "1" or tipo_imóvel == "3") and consumo_mensal_agua <= 25:
    print("Consumo moderado – dentro do padrão residencial.")
else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
