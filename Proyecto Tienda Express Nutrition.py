import textwrap
class Producto:

    def __init__(self, nombre, descripcion, categoria, marca, precio, decorador,disponibles):
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.marca = marca
        self.precio = precio
        self.decorador = decorador
        self.disponibles = disponibles
    
    def atributos(self):

        print(self.decorador,)
        print("·Descripción:\n", self.descripcion)
        print("·Categoría:", self.categoria)
        print("·Marca:", self.marca)
        print("·Precio:", self.precio)
        print("·Dispobibles:", self.disponibles)
        return  ''


    def margendescripcion(self):
        self.descripcion = "\n".join(textwrap.wrap(self.descripcion, width=45))


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append({"producto": producto, "cantidad": cantidad})

    def ver_carrito(self):
        total = 0
        if len(self.items) == 0:
            print("""\
╔══════════════════════════════════════════════╗
║         Carrito de Express Nutrition         ║
╠══════════════════════════════════════════════╣
║ Tu carrito está Vacío                        ║
║                                              ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
            return False
        else:
            print("""\
╔══════════════════════════════════════════════╗
║         Carrito de Express Nutrition         ║
╠══════════════════════════════════════════════╣
""")
            for item in self.items:
                producto = item["producto"]
                cantidad = item["cantidad"]
                total += producto.precio * cantidad
                print(f"● {producto.nombre}: {cantidad} unidades x ${producto.precio} cada unidad")
            print(f"� Total a pagar: ${total}")
            return True
        
        

    def realizar_pedido(self):

        print("""
╔══════════════════════════════════════════════╗
║           Formulario de Pedido               ║
╚══════════════════════════════════════════════╝
""")
        total = 0
    # Solicitar información al cliente
        
        nombre = input("Ingrese su nombre: ")
        direccion = input("Ingrese su dirección de envío: ")
        telefono = input("Ingrese su número de teléfono: ")
        metodo = input("Ingrese su metodo de pago: ")
        print("""
╔══════════════════════════════════════════════╗
║             Resumen del Pedido               ║
╚══════════════════════════════════════════════╝
■ Nombre: {}
■ Dirección: {}
■ Teléfono: {}
■ Metodo de pago: {}
        """.format(nombre, direccion, telefono, metodo))
        for item in self.items:
                producto = item["producto"]
                cantidad = item["cantidad"]
                total += producto.precio * cantidad
                print(f"{producto.nombre}: {cantidad} unidades x ${producto.precio} cada unidad")
        print(f"▬ Valor del pedido: ${total} ▬")
        #Elimina los productos del stock
        producto.disponibles = producto.disponibles - cantidad

        print("»» Pedido realizado. Gracias por su compra! «««")
        contador = 3
        salirovolver = int(input('Presione 1 Para ♥CONTINUAR♥ comercio, Presione 0 ♦SALIR♦ del comercio: '))
        if contador == 0:
            volveralmenufiltradoshortcut()
        while True:
            if salirovolver == 1:
                menu()
                opcionesmenu()
            elif salirovolver == 0:
                fin_del_programa()
            else:
                print('Opcion fuera de rango, intentalo de nuevo, te quedan', contador-1 ,'intentos')
                contador -= 1



#---------------------------------------------------------------------------------------------
def menu():
        print("""\
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║ Por favor, seleccione una categoría:         ║
║                                              ║
║   [1] Filtrar                                ║
║   [2] Buscar por palabra                     ║
║   [3] Ver Carrito                            ║
║   [4] Salir de la Web                        ║
║                                              ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
        
def menudos():
    print("""\
╔══════════════════════════════════════════════╗
║           ¿QUE PRODUCTO DETALLAR?            ║
╠══════════════════════════════════════════════╣
║   [0] Para volver al menú                    ║
║   [-1] Agregar algun producto                ║
║                                              ║
║   SI GUSTA VER ALGUN PRODUCTO EN DETALLE     ║
║      PRESIONE EL NUMERO DEL PRODUCTO         ║
║                                              ║
║   SIENDO 1 EL PRODUCTO EN LA PARTE SUPERIOR  ║
║          Y ASÍ SUCESIVAMENTE                 ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")

def menufiltrado():
        print("""\
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║ ¿Como desea filtrar los productos?           ║
║                                              ║
║   [1] Categoria (Proteinas,Aminos,etc.)      ║
║   [2] Marca                                  ║
║   [3] Precio                                 ║
║   [4] Salir del Programa                     ║
║                                              ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
#--------------------------------------------------------------------------------------------------
def filtro_categoria(filtro):
    contador = 3
    opcion = int(input('Seleccione una opción: '))
    while True:
        if filtro == 'categoria':
            if opcion == 1:
                string = 'Proteinas Hipercaloricas'
            elif opcion == 2:
                string = 'Creatinas'
            elif opcion == 3:
                string = 'Aminoacidos'
            elif opcion == 4:
                string = 'Pre-entreno'
            break
        elif filtro == 'marca':
            if opcion == 1:
                string = 'TNTSUPERNUTRITION'
            elif opcion == 2:
                string = 'VITANAS'
            elif opcion == 3:
                string = 'OPTIMUN NUTRITION'
            elif opcion == 4:
                string = 'MUSCLETECH'
            elif opcion == 5:
                string = 'HEALTHY SPORTS'
            elif opcion == 6:
                string = 'MUTANT'
            elif opcion == 7:
                string = 'NUTRAAMERICAN'
            elif opcion == 8:
                string = 'PROSCIENCE'
            elif opcion == 9:
                string = 'CELLUCOR'
            break
        elif filtro == 'precio':
            if opcion == 1:
                string = 1
            elif opcion == 2:
                string = 2
            elif opcion == 3:
                string = 3
            break
        else:
                    print('Vuelve a intentarlo, te quedan', contador-1 ,'intentos')
                    contador -= 1
    return string 
def menufiltrocategorias():
        print("""
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║ Por favor, seleccione una categoría:         ║
║                                              ║
║   [1] Proteínas Hipercaloricas               ║
║   [2] Creatinas                              ║
║   [3] Aminoácidos                            ║
║   [4] Pre entreno                            ║
║   [5] Volver al menú                         ║
║                                              ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
        return busquedafiltrada('categoria',filtro_categoria('categoria'))


def busquedafiltrada(filtro,string):
    listaprovicional= []
    print(f'''\
     ═════════════════════════════════════════════
            🡻 {string}🡻    
     ═════════════════════════════════════════════
    ''')
    for cada_producto in objetos:
                    if getattr(cada_producto, filtro, None) == string:
                        listaprovicional.append(cada_producto)
                        #Aquí muestra el objeto en el menú
                        print(cada_producto.decorador)
    
    return listaprovicional
    
def menufiltromarca():
        print("""\
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║ Por favor, seleccione una Marca:             ║
║                                              ║
║   [1] TNTSUPERNUTRITION                      ║
║   [2] VITANAS                                ║
║   [3] ON                                     ║
║   [4] MUSCLETECH                             ║
║   [5] HEALTHY SPORTS                         ║
║   [6] MUTANT                                 ║
║   [7] NUTRAAMERICAN                          ║
║   [8] PROSCIENCE                             ║
║   [9] CELLUCOR                               ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
        return busquedafiltrada('marca',filtro_categoria('marca'))

def busquedafiltrada_precio(string):
    listaprovicional= []
    print('''\
     ═════════════════════════════════════════════
        🡻 Aquí estan los productos filtrados🡻    
     ═════════════════════════════════════════════
    ''')
    if string == 1:
        print("Clases con precio menor a 100.000:")
        for cada_producto in objetos:
            if cada_producto.precio < 100000:
                listaprovicional.append(cada_producto)
                print(cada_producto.decorador)
    elif string == 2:
        print("Clases con precio entre 100.000 y 200.000:")
        for cada_producto in objetos:
            if 100000 <= cada_producto.precio <= 200000:
                listaprovicional.append(cada_producto)
                print(cada_producto.decorador)
    elif string == 3:
        print("Clases con precio mayor a 200.000:")
        for cada_producto in objetos:
            if cada_producto.precio > 200000:
                listaprovicional.append(cada_producto)
                print(cada_producto.decorador)
    return listaprovicional

def menufiltroprecio():
        print("""\
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║ Por favor, seleccione un Rango de precio:    ║
║                                              ║
║   [1] Menores a 100.000                      ║
║   [2] Entre 100.000 y 200.000                ║
║   [3] Mayores a 200.000                      ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
""")
        return busquedafiltrada_precio(filtro_categoria('precio'))

#--------------------------------------------------------------------------------------------

def mostrar_atributos(listaprovicional):
    contador = 3
    while True:
        seleccionopcion=int(input("""\
╔══════════════════════════════════════════════╗
║        Bienvenido a Express Nutrition        ║
╠══════════════════════════════════════════════╣
║  Por favor, seleccione algun producto:       ║
║  Siendo 1 el producto en la parte superior,  ║
║  es decir el primero impreso en consola      ║
║  Y así sucesivamente                         ║
║                                              ║
║  ◘◘◘ SI NO VE NINGUN PRODUCTO                ║
║      AGRANDE EL TAMAÑO DE LA CONSOLA  ◘◘◘    ║
║                                              ║
║                                              ║
║   𝑀𝒶𝒹𝑒 𝒷y : 𝒜𝓃𝒹𝓇é𝓈 𝒢𝒶𝒸𝒽𝒶𝓇𝓃á                  ║
╚══════════════════════════════════════════════╝
 Digite su opcion: """))
        if contador == 0:
            volveralmenufiltradoshortcut()
        if 0 <= seleccionopcion <= len(listaprovicional):
            print(listaprovicional[seleccionopcion-1].atributos())
            desicion =  int(input('▼ Presione 1 Si desea agregar al carrito o Presione 0 para volver al menú principal: '))
            contador = 3
            while True:
                if desicion == 1:
                    while True:
                        if listaprovicional[seleccionopcion-1].disponibles == 0:
                            print('(  一_一) Lo sentimos. Este producto no está en stock actualmente')
                            volveralmenuprincipalshortcut()

                        cantidad = int(input('  ▼ Cuantos productos quiere: '))
                        if listaprovicional[seleccionopcion-1].disponibles >= cantidad and cantidad>0:
                            carrito.agregar_producto(listaprovicional[seleccionopcion-1], cantidad)
                            print('(っ◕‿◕)っ SU PRODUCTO HA SIDO AÑADIDO AL CARRITO DE FORMA EXITOSA.')
                            volveralmenuprincipalshortcut()
                            
                        else:
                            print('Has solicitado más unidades de las disponibles intentalo de nuevo')
                elif desicion == 0:
                    volveralmenuprincipalshortcut()
        else:
            print('Opcion fuera de rango, intentalo de nuevo, te quedan', contador-1 ,'intentos')
            contador -= 1

#-----FUNCIONES PARA ACORTAR LA PEREZA------
def volveralmenuprincipalshortcut():
    menu()
    opcionesmenu()
def volveralmenufiltradoshortcut():
    menufiltrado()
    opcionesmenufiltrado()
def fin_del_programa():
    print('GRACIAS POR HABER VISITADO EXPRESS NUTRITION')
    quit()
#-------------------------------------------

def opcionesmenu():
    contador = 3
    while True:
        opcion = int(input('(menu) Arriba está el menú de opciones disponibles, por favor digite una: '))
        if contador == 0:
                print('Has exedido el limite de intentos //Error 576 ¿Tas dislexico?')
                quit()
        if opcion == 1:
            volveralmenufiltradoshortcut()
        elif opcion == 2:
            mostrar_atributos(busquedaporpalabra(objetos))
        elif opcion == 3:
            print('test')
            if carrito.ver_carrito() == True:
                realizarpedido = int(input('Presione 1 Si desea realizar el pedido o Presione 0 para volver: '))
                if realizarpedido == 1:
                    carrito.realizar_pedido()
                elif realizarpedido == 0:
                    volveralmenuprincipalshortcut()
        elif opcion == 4:
            fin_del_programa()
        else:
                print('Vuelve a intentarlo, te quedan', contador-1 ,'intentos')
                contador -= 1

def opcionesmenufiltrado():
    contador = 3
    while True:
        opcion = int(input('(menu filtrado) Arriba está el menú de opciones disponibles, por favor digite una: '))
        if contador == 0:
                print('Has exedido el limite de intentos //Error 576 ¿Tas dislexico?')
                quit()
        if opcion == 1:
            mostrar_atributos(menufiltrocategorias())
        elif opcion == 2:
            mostrar_atributos(menufiltromarca())
        elif opcion == 3:
            mostrar_atributos(menufiltroprecio())
        else:
                print('Vuelve a intentarlo, te quedan', contador-1 ,'intentos')
                contador -= 1

def busquedaporpalabra(objetos):
    listaprovicional = []
    letras = str(input('Digite el producto que quiera buscar: '))
    print('''\
     ═════════════════════════════════════════════
     🡻 Aquí estan los resultados de tu busqueda🡻    
     ═════════════════════════════════════════════
    ''')
    for cada_objeto in objetos:
        if letras in cada_objeto.nombre.lower():
            listaprovicional.append(cada_objeto)
            print(cada_objeto.decorador)
    return listaprovicional


if __name__ == "__main__":


    #CREACION DE PRODUCTOS

    #PROTEINAS HIPERCALORICAS
    tnt_hipercalorica = Producto("TNT MEGA MASS GAINER 10 LBS", 'Es una de las proteínas más hipercalóricas del mercado aportando 90 gramos de proteína y 1900 calorías en 6 scoops. Contiene creatina monohidratada y BCCAS. \n', 'Proteinas Hipercaloricas', 'TNTSUPERNUTRITION', 180000,
                                 """\
    ╔═════════════════════════════════════════════╗
    ║        TNT MEGA MASS GAINER 10 LBS          ║
    ╚═════════════════════════════════════════════╝
""", 4)
    vitanas_hipercalorica = Producto("VITANAS TITAN ARMY 12 LBS", 'Es una proteína hipercalórica de suero concentrado. Modo de uso: Adultos, tomar 1 servicio (8 Cucharas medidoras) al día. Dividir el servicio de TITÁN ARMY® en tres (3) tomas diarias. Disolver cada una en 12 oz. de agua hasta obtener una mezcla homogénea.', 'Proteinas Hipercaloricas', 'VITANAS', 180000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║        VITANAS TITAN ARMY 12 LBS            ║
    ╚═════════════════════════════════════════════╝
""", 5)
    seriousmass_hipercalorica = Producto("OPTIMUN NUTRITION SERIOUS MASS 12 LBS", 'Un aumento de peso importante requiere muchas calorías. Sin embargo, aquellos que más necesitan calorías adicionales, a menudo tienen más dificultades para consumir suficientes calorías. Para muchos que aspiran a ser más grandes, los metabolismos altamente activos, el apetito más débil y los estilos de vida ajetreados hacen que consumir suficientes calorías a través de alimentos integrales sea un verdadero desafío. Con Serious Mass, no tienes nada que perder y mucho que ganar.', 'Proteinas Hipercaloricas', 'OPTIMUN NUTRITION', 350000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║    OPTIMUN NUTRITION SERIOUS MASS 12 LBS    ║
    ╚═════════════════════════════════════════════╝
""", 8)
    #CREATINAS
    platinum_creatina = Producto("Creatina Platinum Muscletech 400grs", 'Creatina monohidratada y micronizada.', 'Creatinas', 'MUSCLETECH', 170000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║     Creatina Platinum Muscletech 400grs     ║
    ╚═════════════════════════════════════════════╝
""", 15)
    healthy_creatina = Producto("Creatina Healthy Sport 300grs", 'La Creatina es un suplemento que puede ayudarte a mejorar el rendimiento físico y aumentar la masa muscular. Al ser micronizada su absorción es mucho mejor y evita problemas gastrointestinales. 3000 mg de creatina monohidrato micronizada Por servicio', 'Creatinas', 'HEALTHY SPORTS', 120000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║        Creatina Healthy Sport 300grs        ║
    ╚═════════════════════════════════════════════╝
""", 5)
    
    #AMINOACIDOS O BCAA ES LO MISMO
    bcaamutant_aminos = Producto("Bcaa 9.7 Mutant", 'Ingredientes: Maltodextrina, mezcla de aminoácidos (L-leucina, L-Valina, L-isoleucina), ácido cítrico (regulador de ácidez), taurina, glicina, Lglutamina, L-arginina, L-tirosina, oxido de magnesio (regulador de ácidez), citrato de potasio, fosfato tricálcico (emulsionante), lactato de calcio, bicarbonato de sodio, citrato de calcio, cloruro de sodio, aceite MCT, extracto de pimienta negra, acesulfame de potasio (Acentuador de sabor), sucralosa (edulcorante), dióxido de silicio, lecitina de soya, sabor natural y artificial, color (polvo de remolacha roja).', 'Aminoacidos', 'MUTANT', 95000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║               Bcaa 9.7 Mutant               ║
    ╚═════════════════════════════════════════════╝
""", 7)
    nitrochock_aminos = Producto("Nitro Chock Aminoácidos", 'Nitro Shock, es una avanzada fórmula de rápida absorción que combina los aminoácidos más degradados por el músculo durante la actividad física; Los BCAA que son transformados en energía durante la actividad física y la L-Glutamina que es el 60%_de la masa muscular.', 'Aminoacidos', 'NUTRAMERICAN', 94900,
                           """\
    ╔═════════════════════════════════════════════╗
    ║           Nitro Chock Aminoácidos           ║
    ╚═════════════════════════════════════════════╝
""", 13)
    
    #PRE ENTRENOS

    intenze_preentreno= Producto("Intenze", 'Alimento en polvo de frutas deshidratadas con polvo de frutos rojos y polvo de remolacha.', 'Pre-entreno', 'PROSCIENCE', 135000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║                    Intenze                  ║
    ╚═════════════════════════════════════════════╝
""", 5)
    
    cecuatro_preentreno = Producto("C4 Original Pre Work", 'Ingredientes: vitamina C (como ácido ascórbico), niacina (como niacinamida), vitamina B6 (como piridoxal-5-fosfato), ácido fólico, vitamina B12 (como metilcobalamina), calcio, beta alanina, nitrato de creatina, arginina AKG, mezcla de energía explosiva, N-acetil-L-tirosina, cafeína anhidrohidrohidrohidroxico. US (1500) mg), extracto de semillas de grano de terciopelo (Mucuna pruriens), ácido tetrametilúrico TeaCor.', 'Pre-entreno', 'CELLUCOR', 160000,
                           """\
    ╔═════════════════════════════════════════════╗
    ║            C4 Original Pre Work             ║
    ╚═════════════════════════════════════════════╝
""", 3)
    
    # ACÁ SE CREA EL CARRITO
    carrito = Carrito()
    # Se crea una lista de los productos para hacer más sencillo la optencion de cada uno
    objetos = [tnt_hipercalorica,vitanas_hipercalorica,seriousmass_hipercalorica,platinum_creatina,healthy_creatina,bcaamutant_aminos,nitrochock_aminos,intenze_preentreno,cecuatro_preentreno]
    
    # ACÁ SE LE DA EL FORMATO A TODAS LAS DESCRIPCIONES DE LOS PRODUCTOS PARA IMPRIMIRLOS EN CONSOLA
    for cada_objeto in objetos:
        cada_objeto.margendescripcion()
    #Arranque de programa
    volveralmenuprincipalshortcut()