#Crea uan funcion que encuentre todas las combinaciones de los numeros de una lista que suman el valor objeto
# - La funfion recibira una lista de numeros enteros positov y un valor objetivo.
# - Para obtener la combinacion solo se puede usar una vez cada elemento de la lista (pero pueden exister elementos repetido en ella )
#Ejemplo: Lista = [1,5,3,2], obejtivo = 6
#Soluciones: [1,5] y [1,3,2] ambas conbinaciones suman 6 
#(Sino existen combianciones retornar una lista vacia)
#Estrategia a usar: backtrack

def find_sums(numbers:list, target:int) -> list:

    #Funcion recursiva, se llama asi misma
    def find_sum(start: int ,target:int, combination: list):

        #Solucion encontrada
        if target == 0:
            result.append(combination[:])
            return
    
        #No encontrar solucion (No posee solucion)
        if target < 0 or start == len(numbers):
           return
        

        # Busqueda
        for index in range(start, len(numbers)):
            if numbers[index] == numbers[index - 1]:
                continue

            combination.append(numbers[index])
            find_sum(index + 1, target - numbers[index], combination)
            combination.pop()
    
        #backtrack

    numbers.sort()
    result = []
    find_sum(0, target, [])
    return result
     

print (find_sums([1,5,3,2], 6))