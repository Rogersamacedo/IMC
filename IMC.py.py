#IMC#
P = float(input("Digite o seu peso em KG:  "))
A = float(input("Digite o altura em cm:  "))
IMC = P /(A * A)
if IMC <= 18:
      print("muito abaixo so peso")
if IMC >= 18.1 and IMC< 24.9:
      print("Peso normal")
if IMC >= 25 and IMC<= 29.9:
      print("acima do peso")
if IMC >= 30 and IMC<= 34.9:
      print("Obesidade grau 1")
if IMC >= 35 and IMC<= 40:
      print("Obesidade grau 2")
elif IMC> 40:
      print("Obesidade grau 3")
print(IMC)

