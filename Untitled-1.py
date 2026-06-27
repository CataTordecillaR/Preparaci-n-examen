items = {
    "MAG001" : ["Agonía de Escarcha", "Arma", "Legendaria", "Hielo"],
    "MAG002" : ["Anillo de Sauron", "Accesorio", "Epica", "Magia"],
    "MAG003" : ["Poción curativa", "Consumible", "Comun", "Vida"],
    "MAG004" : ["Corona Nemesis", "Armadura", "Legendaria", "Dragon"],
    "MAG005" : ["Baston Lunar de Lileath", "Arma", "Epica", "Hechizo"],
    "MAG006" : ["Cristal de Hielo", "Material", "Rara", "Hielo"]
}

inventario = {
    "MAG001" : [5000,3],
    "MAG002" : [2500,8],
    "MAG003" : [100,50],
    "MAG004" : [10000,1],
    "MAG005" : [3500,4],
    "MAG006" : [800,0]

}

while True:

    print("=== ALDRICEL COMERCIANTE ARCANO ===")
    print("1.- Stock por categoría")
    print("2.- Búsqueda por precio")
    print("3.- Actualizar precio")
    print("4.- Salir")

    opcion = int(input("Ingrese la opción a elegir"))

    if opcion == 1:
