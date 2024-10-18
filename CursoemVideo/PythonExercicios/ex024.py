cidade = str(input('Digite o nome da cidade: ')).strip().split()

print('A cidade começa com o nome "SANTO"?: {}'.format('SANTO' in cidade[0].upper()))