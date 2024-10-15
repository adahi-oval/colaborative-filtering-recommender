import modules.myParser as myParser
import modules.functions as functions

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Main para testear, comprueben con el otro archivo de matriz2.txt también que seguro lo pedirá en clase y en la corrección

args = myParser.Parser()

filename = args.file
nombre_salida = args.output

numeroVecinos = args.neighbours
opcion_p = args.pearson
opcion_c = args.cosine
opcion_e = args.euclidean
opcion_s = args.simple
opcion_m = args.media

if opcion_p:
    metrica = 'pearson'
if opcion_c:
    metrica = 'cosine'
if opcion_e:
    metrica = 'euclidean'

if opcion_s:
    tipoPrediccion = 'simple'
if opcion_m:
    tipoPrediccion = 'media'


ratings, min_val, max_val = functions.readMatrix(filename)


predictionMatrix = functions.calculatePredictions(ratings, metrica, numeroVecinos, tipoPrediccion, min_val, max_val)


string = ''
output = ''

for row in predictionMatrix:
    output += "\t"
    for item in row:
        if type(item) is int or type(item) is float:
            string += "'" + str(item) + "'" + " "
            output += f"{GREEN}{str(item)}{RESET} "
        else:
            string += item + " "
            output += item + " "
    string += '\n'
    output += '\n'

with open(nombre_salida, 'w') as outputFile:
    outputFile.write(string)

print(f"\nMatriz rellena con las predicciones:\n\n{output}")