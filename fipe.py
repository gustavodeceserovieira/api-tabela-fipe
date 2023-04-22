import requests

def requisicao(cotacao):
	requisicao = requests.get(cotacao,verify=False)
	return requisicao.json()

def menu():
	print("1-Mostar carros")
	print("2-Mostrar caminhões")
	print("3-Mostrar motos")

def retorna_marca_carros():
	req = f"https://parallelum.com.br/fipe/api/v1/carros/marcas"
	lista = requisicao(req)
	for elementos in lista:
		print(elementos)

def retorna_marca_caminhoes():
	req_1 = f"https://parallelum.com.br/fipe/api/v1/caminhoes/marcas"
	lista_1 = requisicao(req_1)
	for elementos in lista_1:
		print(elementos)

def retorna_marca_motos():
	req_2 = f"https://parallelum.com.br/fipe/api/v1/motos/marcas"
	lista_2 = requisicao(req_2)
	for elementos in lista_2:
		print(elementos)

def retorna_modelos_carros(marca):
	req_3 = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos"
	dict = {}
	dict[0] = requisicao(req_3)
	for elementos in dict.values():
		for i in elementos['modelos']:
			print(i)

def retorna_modelos_caminhoes(marca):
	req_4 = f"https://parallelum.com.br/fipe/api/v1/caminhoes/marcas/{marca}/modelos"
	dict_1 = {}
	dict_1[0] = requisicao(req_4)
	for elementos in dict_1.values():
		for i in elementos['modelos']:
			print(i)

def retorna_modelos_motos(marca):
	req_5 = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{marca}/modelos"
	dict_2 = {}
	dict_2[0] = requisicao(req_5)
	for elementos in dict_2.values():
		for i in elementos['modelos']:
			print(i)


def carros(marca,modelo):
	req_6 = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos/{modelo}/anos"
	dict_3 = {}
	dict_3[0] = requisicao(req_6)
	for elementos in dict_3.values():
		for i in elementos:
			print(i)

def caminhoes(marca,modelo):
	req_7 = f"https://parallelum.com.br/fipe/api/v1/caminhoes/marcas/{marca}/modelos/{modelo}/anos"
	dict_4 = {}
	dict_4[0] = requisicao(req_7)
	for elementos in dict_4.values():
		for i in elementos:
			print(i)

def motos(marca,modelo):
	req_8 = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{marca}/modelos/{modelo}/anos"
	dict_5 = {}
	dict_5[0] = requisicao(req_8)
	for elementos in dict_5.values():
		for i in elementos:
			print(i)						

def modelo_carro(marca,modelo,ano):
	req_9 = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos/{modelo}/anos/{ano}"
	dict_6 = {}
	dict_6[0] = requisicao(req_9)
	print("Informações do Veículo")
	print("----------------------------")
	for key, value in dict_6[0].items():
		print(key,":",value)
		print("------------------------")

def modelo_caminhao(marca,modelo,ano):
	req_10 = f"https://parallelum.com.br/fipe/api/v1/caminhoes/marcas/{marca}/modelos/{modelo}/anos/{ano}"
	dict_7 = {}
	dict_7[0] = requisicao(req_10)
	print("Informações do Veículo")
	print("----------------------------")
	for key, value in dict_7[0].items():
		print(key,":",value)
		print("------------------------")

def modelo_moto(marca,modelo,ano):
	req_11 = f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{marca}/modelos/{modelo}/anos/{ano}"
	dict_8 = {}
	dict_8[0] = requisicao(req_11)
	print("Informações do Veículo")
	print("----------------------------")
	for key, value in dict_8[0].items():
		print(key,":",value)
		print("------------------------")

def main():
	menu()
	try:
		op = int(input("Escolha uma opção: "))
		if(op == 1):
			retorna_marca_carros()
			codigo = int(input("Escolha uma marca: "))
			retorna_modelos_carros(codigo)
			modelo = int(input("Escolha um modelo: "))
			carros(codigo,modelo)
			ano = input("Esoolha o ano: ")
			modelo_carro(codigo,modelo,ano)
		elif(op == 2):
			retorna_marca_caminhoes()
			codigo = int(input("Escolha uma marca: "))
			retorna_modelos_caminhoes(codigo)
			modelo = int(input("Escolha um modelo: "))
			caminhoes(codigo,modelo)
			ano = input("Esoolha o ano: ")
			modelo_caminhao(codigo,modelo,ano)
		elif(op == 3):
			retorna_marca_motos()
			codigo = int(input("Escolha uma marca: "))
			retorna_modelos_motos(codigo)
			modelo = int(input("Escolha o código do modelo: "))
			motos(codigo,modelo)
			ano = input("Esoolha o código referente ao ano: ")
			modelo_moto(codigo,modelo,ano)
		else:
			print("Opção inválida,tente novamente")
			main()	
	except:
		print("Erro na requisição, tente novamente")
		main()			
main()	