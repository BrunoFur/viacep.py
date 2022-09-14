import requests

print('#########################')
print('######Consultar CEP######')
print()

cep_input = input('Digite o seu CEP: ')

if len(cep_input) != 8:
    print('Quantidade de digitos invalida')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:

    print('CEP: {}'.format(address_data['cep']))
    print('Logradouro: {}'.format(address_data['logradouro']))
    print('Complemento: {}'.format(address_data['complemento']))
    print('Bairro: {}'.format(address_data['bairro']))
    print('Localidade: {}'.format(address_data['localidade']))
    print('UF: {}'.format(address_data['uf']))
    print('IBGE: {}'.format(address_data['ibge']))
    print('GIA: {}'.format(address_data['gia']))
    print('DDD: {}'.format(address_data['ddd']))
    print('SIAFI: {}'.format(address_data['siafi']))

else:
    print('{}: CEP Invalido.'.format())
    exit()

