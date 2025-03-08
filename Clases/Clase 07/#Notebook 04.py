#Notebook 04
# %% [markdown]
# # NOTEBOOK 04 - PARTE II Ejecución Condicional, Bucles, Listas y su Procesamiento
# 
# ## Fundamentos de Python | UMCA
# 
# ## Profesor: Ing. Andrés Mena Abarca
# 
# ### <mark>**Nombre del estudiante:**</mark>
# 
# * * *
# 
# ## **¿Qué son las Listas en Python?**
# 
# Imagina que tienes una caja mágica que puede contener todo tipo de objetos: desde libros, juguetes, hasta otros contenedores con más objetos dentro. No solo eso, esta caja tiene la capacidad de cambiar su contenido en cualquier momento; puedes agregar nuevos objetos, eliminar los que ya no necesitas o reorganizar su interior. En Python, esta caja mágica es lo que llamamos una **lista**.
# 
# ## **Definición Formal:**
# 
# Una **lista** en Python es una estructura de datos **ordenada** y **mutable** que puede contener una colección de elementos, los cuales pueden ser de diferentes tipos (enteros, cadenas, booleanos, otras listas, etc.). Las listas son muy versátiles y son una de las estructuras más utilizadas en Python debido a su flexibilidad y facilidad de uso.
# 
# ### **Características Clave de las Listas**
# 
# 1. **Ordenadas:** Mantienen el orden de los elementos tal y como fueron agregados.
# 2. **Mutables:** Puedes modificar su contenido sin crear una nueva lista.
# 3. **Indexadas:** Cada elemento tiene una posición (índice) que permite acceder a él.
# 4. **Heterogéneas:** Pueden contener elementos de diferentes tipos.
# 
# ### **Analogía Creativa: La Lista como un Tren**
# 
# Imagina una lista como un tren compuesto por varios vagones. Cada vagón (elemento) tiene un número (índice) y puede contener cualquier cosa: pasajeros, carga, incluso otros vagones (listas anidadas). Puedes:
# 
# - **Acceder** a un vagón específico usando su número.
# - **Agregar** o **eliminar** vagones en cualquier posición.
# - **Reordenar** los vagones según tus necesidades.
# 
# ### **1\. Creación de Listas**
# 
# ### 
# 
# **Sintaxis básica:**
# 
# ```
# mi_lista = [elemento1, elemento2, elemento3]
# ```
# 
# Puedes crear listas de varias formas:
# 
# 1. **Lista Vacía:**

# %%
# 0 1 2 3 4
datos_luis = [110315689, 'Luis','Chacón',True,99.7]
#Trabajemos con la lista Datos_Luis
print(datos_luis[1])


print(f'El señor {datos_luis[1]} {datos_luis[2]}, es estudiante de Python: {datos_luis[3]}')


# %% [markdown]
# 2. **Lista con Elementos:**

# %%
#Crea tres tipo de listas diferentes

# %% [markdown]
# 3. **Usando la Función list():**

# %%
#Convertir en lista la cadena 'abcdefghijk'

# %% [markdown]
# ### **2\. Acceso a Elementos**
# 
# Puedes acceder a los elementos de una lista usando índices.
# 
# **Ejemplo:**

# %%
#Trabajemos con la lista fr
# 0 1 2 3 4
datos_luis = [110315689, 'Luis','Chacón',True,99.7]
#Trabajemos con la l[1])ista Datos_Luis
print(datos_luis


print(f'El señor {datos_luis[1]} {datos_luis[2]}, es estudiante de Python: {datos_luis[3]}')



# %% [markdown]
# ### **3\. Modificación de Elementos**
# 
# Al ser mutables, puedes cambiar los valores de los elementos existentes.
# 
# **Ejemplo:**

# %%


# %% [markdown]
# ### **4\. Slicing (Segmentación)**
# 
# Puedes obtener sublistas usando la notación de slicing.
# 
# **Sintaxis:**
# 
# ```
# sub_lista = lista[inicio:fin:paso]
# ```

# %%
numeros = [0, 1, 2, 3, 4, 5, 6]

# Output: [2, 3, 4]
print(numeros[2:5])
#nota el primer indice el el inicial y el ultimo el que esta despues 
print(numeros[0:3])

# Output: [0, 1, 2]
print('\nOutput: [6, 5, 4, 3, 2, 1, 0]')
print(numeros[:3])

# Output: [2, 3, 4]
# Output: [6, 5, 4, 3, 2, 1, 0]
print('\nOutput: [6, 5, 4, 3, 2, 1, 0]')
print(numeros[::-1])

# Output: [3, 4, 5, 6]


# Output: [0, 2, 4, 6]


# Output: [6, 5, 4, 3, 2, 1, 0]

# %% [markdown]
# ### **5\. Operaciones Básicas con Listas**
# 
# ### 
# 
# - **Concatenación:**

# %%
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

#Concatenar las dos listas
lista_concatenada = lista1 + lista2
print(lista_concatenada)

# %% [markdown]
# - **Repetición:**

# %%
#Repetir la lista1 tres veces
estudiantes = ["Aylin", "Carlos", "Daniela"]
print(estudiantes*3)


# %% [markdown]
# ### **6\. Métodos Comunes de Listas**
# 
# 1. **Agregar Elementos:**
#     
# - **append(elemento):** Añade un elemento al final.

# %%
#Agregar una nuevo elementofrutas = ['manzana', 'uva', 'pera', 'aguacate']
print(frutas)
frutas.append('naranja')
print(frutas)
frutas.extend(['banano', 'kiwi'])
print(frutas)


# %% [markdown]
# - **extend(iterable):** Extiende la lista con elementos de un iterable.

# %%
#Agregar dos elementos mas a la lista
print(frutas)

# %% [markdown]
# - **insert(índice, elemento):** Inserta un elemento en una posición específica.

# %%

#Insertar en un posición especifica 1
frutas = ['manzana', 'uva', 'pera', 'aguacate', 'naranja', 'kiwi', 'banano']
print(frutas)


frutas.insert(1,'kiwi')
print(frutas)


# %% [markdown]
# **2\. Eliminar Elementos:**
# 
# - **remove(elemento):** Elimina el primer elemento con el valor especificado.

# %%
#Insertar en un posición especifica 1
frutas = ['manzana', 'uva', 'pera', 'aguacate', 'naranja', 'kiwi', 'banano','kiwi']
print(frutas)
frutas.remove('kiwi')
print(frutas)


# %% [markdown]
# #Insertar en un posición especifica 1
# frutas = ['manzana', 'uva', 'pera', 'aguacate', 'naranja', 'kiwi', 'banano']
# print(frutas)
# 
# 
# frutas.insert(1,'kiwi')
# print(frutas)
# 

# %% [markdown]
# 

# %% [markdown]
# **pop(índice):** Elimina y devuelve el elemento en el índice especificado.

# %%
frutas = ['manzana', 'uva', 'pera', 'aguacate', 'naranja', 'kiwi', 'banano','kiwi']
print(frutas)

fruta = frutas.pop(6)
print(f'Fruta eliminada{fruta}')
print(frutas)

# %% [markdown]
# - **clear():** Elimina todos los elementos de la lista.

# %%
frutas.clear()
print(frutas)

# %% [markdown]
# 3. **Ordenar y Revertir:**
# 
# - **sort():** Ordena la lista en orden ascendente.

# %%
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
print(numeros)



# %% [markdown]
# **reverse():** <span style="color: var(--vscode-foreground);"> Invierte el orden de la lista.</span>

# %% [markdown]
# 

# %%
# Output: [9, 5, 4, 3, 1, 1]
numeros.reverse()
print(numeros)



# %% [markdown]
# ### **Iteración sobre Listas**
# 
# - **Usando un Bucle `for`:**

# %%
#['manzana', 'banana', 'cereza']:
 for fruta in ['manzana', 'uva', 'pera', 'aguacate', 'naranja', 'kiwi', 'banano','kiwi']
    print(f'Me gusta la [fruta]')


# %% [markdown]
# 

# %%
nombres = ['ana', 'luis', 'maría']



# %% [markdown]
# - **Usando un Bucle `while`:**

# %%
numeros = [0, 1, 2, 3, 4]
print(len)
i = 0 
tamano = len(numeros)

while i < tamano:
    print(numeros)

# %% [markdown]
# - **Comprobación de Pertenencia:**

# %%
estudiantes = ['Carlos','Javier','Jafet','Daniela','Pamela']
print('Daniela' in estudiantes)
if ' Daniela' in estudiantes:
    
    print('Daniela es una estudiante de Python')
else:
    print('Daniela no es estudiante de Python')

# %% [markdown]
# ### **7\. Copiando Listas**
# 
# - **Asignación Directa (Referencias):**
#     
# 
# Ambas variables apuntan a la misma lista en memoria.

# %%
lista_original = [1, 2, 3]
lista_copia = lista_original
lista_copia.append(4)
print(lista_original)  # Output: [1, 2, 3, 4]

# %% [markdown]
# - **Copia Superficial:**
# 
# Se crea una nueva lista, pero si contiene objetos mutables, estos no se copian profundamente.

# %%
lista_copia = lista_original.copy()
# O
lista_copia = lista_original[:]


# %% [markdown]
# - **Copia Profunda:**
# 
# Copia completamente independiente, incluso para objetos mutables anidados.

# %%
import copy
lista_copia_profunda = copy.deepcopy(lista_original)


# %% [markdown]
# ### 
# 
# - **Listas Anidadas**
# 
# Las listas pueden contener otras listas.

# %%
lista_anidada = [[1, 2], [3, 4], [5, 6]]
print(lista_anidada[1][0])  # Output: 3


# %% [markdown]
# ### **10. Funciones Integradas Útiles**
# 
# numeros = \[1, 2, 3, 4, 5, 6\]
# 
# - **len(lista):** Devuelve el número de elementos.
#     
#     ```python
#     print(len(numeros))  # Output: 6
#     ```
#     
# - **sum(lista):** Suma los elementos (si son numéricos).
#     
#    ```python
#     print(sum(numeros))  # Output: 21
#     ```
#     
# - **min(lista), max(lista):** Devuelve el valor mínimo y máximo.
#     
#      ```python
#     print(min(numeros))  # Output: 1print(max(numeros))  # Output: 6
#     
#     ```
#     
# 
# ### **Aplicaciones Prácticas de las Listas**

# %%
numeros = [1, 2, 3, 4, 5, 6]
print(len(numeros))
print(sum(numeros)) 
print(min(numeros)) 

# %% [markdown]
# # **Actividad Interactiva: Análisis de Datos Simple con Listas**
# 
# **Objetivo:** Aplicar los conceptos aprendidos sobre listas para realizar un análisis de datos sencillo.
# 
# **Descripción de la Actividad:**
# 
# Trabajaremos con una lista de temperaturas registradas durante una semana y realizarán varias operaciones para extraer información útil.
# 
# **Pasos de la Actividad:**
# 
# 1. **Creación de la Lista de Datos:**

# %%
#               Lu  Ma  Mi  Ju  Vi  Sa  Do
temperaturas = [22, 24, 19, 23, 25, 20, 21, 14, 25, 26]
promedio = sum(temperaturas)/ len(temperaturas)
print(promedio)
print(f'temperatura media/promedio: {promedio}°C')

# %% [markdown]
# 2. **Calcular la Temperatura Media de la Semana:**

# %%
#               Lu  Ma  Mi  Ju  Vi  Sa  Do
temperaturas = [22, 24, 19, 23, 25, 20, 21, 14, 25, 26]
promedio = sum(temperaturas)/ len(temperaturas)
print(int(promedio))
print(f'temperatura media/promedio: {promedio:2f}°C')

# %% [markdown]
# 3. **Encontrar la Temperatura Máxima y Mínima:**

# %%
temperaturas = [22, 24, 19, 23, 25, 20, 21, 14, 25, 26]
temp_max = max(temperaturas)
temp_min = min(temperaturas)
print(f'temperatura minima: {temp_min:2f}°C')
print(f'temperatura maxima: {temp_max:2f}°C')

# %% [markdown]
# 4. **Días con Temperatura por Encima de la Media:**

# %%
# Lu Ma Mi Ju Vi Sa Do
temperaturas = [22, 24, 19, 23, 25, 20, 21]


promedio = sum(temperaturas) / len(temperaturas)


dia = 0
while dia < len (temperaturas):
    if temperaturas[dia] > promedio:
        print(f' El día {dia + 1} es cálido, con una temperatura de {temperaturas[dia]}')
    dia += 1


# %% [markdown]
# 5. **Modificar la Lista para Incluir una Nueva Temperatura y Recalcular:**
# 
# - Agregar la temperatura del día extra:

# %% [markdown]
# 

# %%


# %% [markdown]
# - **Recalcular la temperatura media:**

# %%


# %% [markdown]
# 6. **Ordenar las Temperaturas y Mostrar el Resultado:**

# %%


# %% [markdown]
# **Extensión de la Actividad:**
# 
# - **Visualización Simple:**
#     
#     Los estudiantes pueden crear un gráfico de las temperaturas usando `matplotlib` (si se ha visto previamente).

# %%
import matplotlib.pyplot as plt

dias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom', 'Extra']
plt.plot(dias, temperaturas, marker='o')
plt.title('Temperaturas Semanales')
plt.xlabel('Días')
plt.ylabel('Temperatura (°C)')
plt.show()



