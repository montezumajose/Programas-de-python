contadorValido = 0
contadorinvalido = 0

provincias = {'1' : 'Region Metropolitana: Panamá, Colón y Panamá Oeste',
             '2' : 'Region Oriental: Darién y por las comarcas Emberá-Wounaan, Guna Yala, Madugandí y Wargandí',
             '3' : 'Region Occidental: Chiriquí, Bocas del Toro, Ngöbe Buglé, Naso Tjer Dï',
             '4' : 'Region Central: Coclé, Veraguas, Los Santos, Herrera'
             }

nivelDeEducacion = {'5' : 'Universitario',
                    '6' : 'Bachiller',
                    '7' : 'Primaria',
                    '8' : 'Sin especificar'
                    }

tipoDeOperacion = {'15' : 'ganadera',
                   '28' : 'agricultura',
                   '30' : 'sector bancario',
                   '60' : 'actividad Portuaria',
                   '82' : 'otra'
                   }

numero = 1
while(numero != 0000):
    print("Digite 0000 para salir del programa\n")
    try:
        numero = int(input("Digite Código: "))
        if(len(str(numero)) == 4):
            tem = str(numero)
            print("Region Economica: ",provincias[tem[:-3]])
            print("Nivel de Educacion: ",nivelDeEducacion[tem[1:2]])
            print("Tipo de Operacion: ",tipoDeOperacion[tem[2:]])
            contadorValido += 1
            
        else:
            contadorinvalido += 1
            print("ERROR: CODIGO INVALIDO")
    except:
        print("ERROR DE UN CÓDIGO")
        contadorinvalido += 1

print("Codigos validos :",contadorValido)
print("Codigos invalidos: ",contadorinvalido)