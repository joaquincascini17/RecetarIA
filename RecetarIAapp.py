import streamlit as st
import random

# ==========================================
# 1. BASE DE DATOS DE RECETAS
# ==========================================
RECETAS = [
    {
        "titulo": "Pastel de Papa con Aceitunas",
        "ingredientes_clave": ["carne", "papa", "aceituna", "cebolla", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 gramos carne\n- 4 papas grandes\n- 1 puñado aceitunas\n- 1 cebolla chica colorada\n- 1 cebolla chica común\n- 2 huevos duros\n- A gusto condimentos""",
        "pasos": """1. En una sartén cocinamos la carne cortada en trocitos con las cebollas con condimentos a gusto!\n2. Hervimos las papas cortadas en cubos, las pisamos cuando ya están listas y le ponemos un chorrito de aceite y sal!\n3. En un molde ponemos el puré, tapando toda la parte de abajo. Luego la carne ya cocida con huevo duro cortado en trocitos y las aceitunas cortadas. Y por último, arriba ponemos otra capa de puré!\n4. Le podemos poner aceitunas o queso rallado arriba! La llevamos al horno a temperatura media hasta que esté calentito!"""
    },
    {
        "titulo": "Guiso de Carne y Papa",
        "ingredientes_clave": ["ajo", "cebolla", "carne", "papa", "tomate"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 dientes ajo\n- 1 cebolla grande\n- 500 grs carne (roast beef)\n- 2 papas\n- 1 lata de tomate cubeteado\n- Condimentos varios""",
        "pasos": """1. Poner un chorrito de aceite en una cacerola, picar los ajos, agregar.\n2. Picar la cebolla.\n3. Cortar la carne en láminas finas, agregar hasta dorar la cebolla y que cambie de color la carne.\n4. Agregar los condimentos.\n5. Pelar, cortar la papa en trocitos pequeños.\n6. Agregar la lata de tomate cubeteado y 2 latas de agua.\n7. Agregar las papas, cocinar a fuego medio semitapado hasta que estén las papas y reduzca."""
    },
    {
        "titulo": "Milanesa de Cerdo",
        "ingredientes_clave": ["cerdo", "huevo", "ajo", "pan rallado"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1,5 kg carne o nalga de cerdo\n- 6 huevos\n- 4 dientes ajo\n- 600 grs pan rallado\n- Perejil\n- Aceite para freír""",
        "pasos": """1. Pedirle al carnicero que te corte en bifes finitos para hacer milanesas. Salar la carne. Pasar huevo mezclado con el ajo y perejil bien picaditos. Después por pan rallado, apretar bien el pan sobre la carne.\n2. Calentar el aceite en una sartén y freír. Cuando estén doraditas las sacas y las vas amontonando sobre papel de cocina para escurrir."""
    },
    {
        "titulo": "Tortilla de Papa Fit",
        "ingredientes_clave": ["papa", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 4 Papas Grandes\n- 5 Huevos\n- c/n Aceite, Pimienta, Pimentón, Orégano, Ají Molido Picante, Ajo en Polvo, Polvo de Cebollas""",
        "pasos": """1. Pelamos, lavamos y cortamos en cubos no muy grandes las papas y ponemos a hervir en abundante agua.\n2. Una vez cocidas las pasamos a una fuente.\n3. En un bowl ponemos los huevos junto con los condimentos y batimos muy bien.\n4. Ponemos las papas dentro del bowl con los huevos.\n5. Calentamos aceite en la tortillera. Añadimos la mezcla y dejamos cocinar. Le damos la vuelta.\n6. Desmoldamos en un plato."""
    },
    {
        "titulo": "Helado Cremoso de Frutas",
        "ingredientes_clave": ["kiwi", "yogurt"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 10 kiwis chicos (o cualquier fruta)\n- 1 pote de yogurt natural\n- C/n edulcorante líquido""",
        "pasos": """1. Pelar y cortar todos los kiwis en el bowl. Agregar el yogurt y el edulcorante.\n2. Mixear hasta que quede uniforme, sin grumos.\n3. Pasar a un recipiente o bolsitas.\n4. Dejar congelar unas horas (o toda la noche)."""
    },
    {
        "titulo": "Bocaditos de Arroz",
        "ingredientes_clave": ["arroz", "harina", "huevo"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 ración de arroz\n- 1 cucharadita grande de perejil\n- 1-2 cucharadas harina leudante\n- Sal a gusto\n- 2 huevos""",
        "pasos": """1. En un bol ponemos el arroz con los huevos y mezclamos.\n2. Luego ponemos el perejil con la sal.\n3. Agregamos la harina y mezclamos.\n4. Le hacemos forma con la mano o cuchara y las ponemos en una placa enmantecada. Lo llevamos al horno hasta que queden listos."""
    },
    {
        "titulo": "Zapallitos Rellenos",
        "ingredientes_clave": ["zapallito", "zanahoria", "cebolla", "morron", "ajo", "carne", "caldo", "huevo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 6 zapallitos verdes medianos\n- 1 zanahoria, 2 cebollas, 1 morrón, 1 ajo\n- 1/2 kg carne picada\n- 1 cubo caldo de verduras\n- 1 huevo\n- 200 g queso cremoso en cubitos\n- Chorrito vino tinto o blanco""",
        "pasos": """1. Hervir los zapallitos en agua con sal hasta que ablanden. Enfriar y ahuecar.\n2. En una olla calentar aceite y dorar la carne picada, agregar las verduras picadas.\n3. Sumar condimentos, caldo y un chorrito de vino. Cocinar hasta integrar.\n4. Rellenar cada zapallito hasta la mitad, agregar un cubito de queso, terminar de rellenar y coronar con más queso.\n5. Acomodar en bandeja, verter huevo batido por encima y llevar al horno por 25 minutos."""
    },
    {
        "titulo": "Revuelto de papa, sofrito y huevo",
        "ingredientes_clave": ["papa", "cebolla", "zanahoria", "morron", "ajo", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 papas medianas\n- 1 cebolla, 1 zanahoria, 1/2 morrón, 2 dientes ajo\n- 3 huevos\n- c/n sal, pimienta, nuez moscada, cúrcuma, cayena, perejil""",
        "pasos": """1. Picar bien fino cebolla, morrón y ajo. Cortar la papa y zanahoria en cubos chiquitos.\n2. Calentar aceite y rehogar todas las verduras juntas hasta que las papas estén casi hechas.\n3. Agregar los huevos y condimentos y cocinar revolviendo hasta que cuajen."""
    },
    {
        "titulo": "Tarta de Zucchini con Base de Papa Dorada",
        "ingredientes_clave": ["papa", "zucchini", "huevo", "queso", "cebolla", "morron"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 papas\n- 3 zucchinis\n- 5 huevos M\n- 1 trozo queso cremoso\n- 1 cebolla chica, 1/3 morrón\n- c/n pimienta, sal, nuez moscada""",
        "pasos": """1. Cortar la papa en rodajas finas. Aceitar la tartera, disponer las rodajas encimadas y hornear a fuego fuerte.\n2. Cortar el zucchini, salar y masajear. Picar cebolla y morrón y agregar.\n3. Sumar huevos y condimentos.\n4. Verter el relleno sobre las papas a medio hacer. A media cocción agregar queso por encima y gratinar."""
    },
    {
        "titulo": "Tortilla en freidora de aire",
        "ingredientes_clave": ["papa", "cebolla de verdeo", "cebolla", "morron", "jamon", "huevo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 papas medianas\n- 2 cdas cebolla de verdeo, 1 cda cebolla común, 1 cda morrón\n- 2 fetas jamón cocido\n- 5 huevos\n- 2 cdas queso rallado""",
        "pasos": """1. Pelar y cortar las papas muy chiquitas. Picar verduras.\n2. Poner en el molde de freidora con aceite en spray. Cocinar a 180° por 18 min revolviendo.\n3. A mitad de cocción sumar el jamón picado.\n4. Mezclar huevos con queso y sal. Incorporar las verduras listas y dejar reposar 5 min.\n5. Cocinar en molde rociado a 175° por 17 minutos."""
    },
    {
        "titulo": "Papas Rellenas Deliciosas",
        "ingredientes_clave": ["papa", "pollo", "zanahoria", "cebolla", "morron", "ajo", "huevo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 6 papas medianas\n- 2 pata muslo\n- 2 zanahorias, 4 cebollas, 1/2 morrón, 2 ajos\n- 3 huevos (2 duros, 1 crudo)\n- 300 g queso cremoso""",
        "pasos": """1. Hervir las papas con piel. Hervir el pollo.\n2. Hervir 2 huevos.\n3. Trozar el pollo cocido. Saltear verduras picadas y mezclar con el pollo y huevos duros picados.\n4. Ahuecar las papas (ya blandas).\n5. Rellenar las papas con la mezcla. Meter al horno, coronar con queso y rociar con el huevo crudo.\n6. Cocinar hasta dorar."""
    },
    {
        "titulo": "Pan de Carne con Verduras Horneadas",
        "ingredientes_clave": ["carne", "huevo", "zanahoria"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 gr carne picada\n- 2 huevos\n- 1 cda Provenzal, Orégano, Sal, Mostaza\n- 1 Zanahoria (y más verduras a gusto)""",
        "pasos": """1. Hierve los huevos.\n2. Mezcla la carne con provenzal, orégano, sal y mostaza. Distribuye plano, pon los huevos en el medio y enrolla.\n3. Pon la carne en una asadera enaceitada.\n4. Corta verduras en daditos, condimenta y pon en otra asadera.\n5. Cocinar carne y verduras en horno a 180 grados por 40 minutos."""
    },
    {
        "titulo": "Albóndigas en Salsa de Zapallo Calabaza y Arroz",
        "ingredientes_clave": ["carne", "ajo", "morron", "cebolla", "galletitas", "leche", "maicena", "zapallo", "caldo", "arroz"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 800 g Carne picada\n- 1 diente Ajo\n- 1/4 unidad Morrón colorado\n- 1/2 unidad Cebolla\n- 50 g Restos de galletitas de agua\n- 50 ml Leche\n- 2 cucharadas Maicena\n- 300 g Zapallo calabaza asado\n- 1 litro Caldo\n- Arroz blanco""",
        "pasos": """1. Pica ajo, morrón y cebolla. Mezcla con la carne picada en un bol.\n2. Añade galletitas, leche, sal, pimienta y maicena. Mezcla bien y forma bolitas.\n3. Licúa el zapallo asado con el caldo hasta obtener una salsa cremosa.\n4. Vierte la salsa en una cacerola y lleva a ebullición.\n5. Agrega las albóndigas, cocina hasta que hierva, baja el fuego y deja media hora hasta que la salsa reduzca."""
    },
    {
        "titulo": "Salteado de Pollo y Puerros con Arroz",
        "ingredientes_clave": ["arroz", "pollo", "puerro", "verdeo", "ajo", "morron", "vino", "crema de leche"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 4 jarritos de arroz\n- 2 mitades pechugas pollo\n- 3 varas de puerro\n- 3 varas de verdeo\n- 3 dientes ajo\n- 1 pimiento rojo\n- 1/2 vaso vino blanco\n- 3 cucharadas de crema de leche""",
        "pasos": """1. Hervir el arroz y reservar.\n2. Picar el pollo en cubos y dorar en wok. Retirar.\n3. Picar pimiento, ajos, puerro, verdeo y cocinar en el wok.\n4. Pasados 15 min unir verduras con el pollo, agregar vino blanco y reducir.\n5. Agregar crema de leche y servir sobre el arroz."""
    },
    {
        "titulo": "Arroz Blanco Perfecto",
        "ingredientes_clave": ["arroz", "ajo"],
        "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 tazas arroz\n- 2 1/2 tazas agua\n- 1 ajo entero o picado""",
        "pasos": """1. Colocar el arroz y el agua en una cacerola.\n2. Agregar aceite, sal y el ajo. Mezclar.\n3. Tapar y fuego medio/bajo por 10 minutos.\n4. Cuando el agua se consuma, bajar a mínimo, tapar con una bolsa limpia haciendo honguito, apagar el fuego y dejar 5 minutos más."""
    },
    {
        "titulo": "Carne al Wok con Arroz Blanco",
        "ingredientes_clave": ["carne", "cebolla", "morron", "ajo", "arroz", "salsa de soja", "vino"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 800 grs nalga o cuadrada\n- 2 cebollas grandes\n- 1 morrón mediano\n- 3 dientes ajo\n- 4 tacitas de arroz\n- Salsa de soja, sal, pimienta, jengibre molido\n- 100 ml vino blanco""",
        "pasos": """1. Filetear la carne y sellar en wok. Retirar.\n2. Rehogar cebolla y morrón. Cuando transparenta, agregar ajos y vino.\n3. Evaporar el alcohol e incorporar la carne. Condimentar a gusto.\n4. Hervir el arroz y servir junto con la carne."""
    },
    {
        "titulo": "Pollo al curry con arroz blanco",
        "ingredientes_clave": ["arroz", "pollo", "crema de leche", "cebolla", "curry"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 tazas arroz\n- 2 supremas de pollo\n- 250 ml crema\n- 1 cebolla\n- a gusto Sal, pimienta, curry en polvo""",
        "pasos": """1. Hervir el arroz blanco, reservar.\n2. Picar la cebolla y sofreírla en una olla hasta transparentar.\n3. Agregar el pollo cubeteado y dorar.\n4. Agregar condimentos y la crema."""
    },
    {
        "titulo": "Arroz blanco con Pollo frito",
        "ingredientes_clave": ["arroz", "ajo", "pollo", "morron"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 taza Arroz largo fino\n- 2 1/2 tazas Agua\n- Hoja laurel y un diente ajo\n- Sal fina\n- Para Freír: Aceite girasol\n- 4 Pata de pollo\n- Sal, pimienta, pimentón, perejil fresco\n- 1 pedazo Morrón rojo""",
        "pasos": """1. En una ollita poner agua, hoja de laurel y ajo. Cuando rompa el hervor agregar el arroz.\n2. Echar sal a gusto y revolver, cocinar unos minutos. Colocar la tapa y bajar el fuego.\n3. Sacar el ajo y laurel. Arroz listo.\n4. Para el pollo: En un wok poner aceite con pimentón, el morrón y perejil.\n5. Condimentar las patas de pollo con sal y pimienta. Freír en pequeñas cantidades en aceite caliente."""
    },
    {
        "titulo": "Pollo a la Cazadora con Arroz Blanco",
        "ingredientes_clave": ["pollo", "cebolla", "zanahoria", "verdeo", "puerro", "morron", "ajo", "tomate", "pure de tomate", "arroz"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 Patas y Muslos\n- 3 cebollas medianas\n- 2 Zanahorias medianas\n- 1 cebolla de Verdeo\n- 1 Puerro\n- 1/2 Morrón Colorado\n- 2 Dientes Ajo\n- 1 Tomate\n- 1 Puré de Tomate\n- Arroz""",
        "pasos": """1. Picar todas las verduras. Limpiar las patas y muslos sacando la piel.\n2. En una olla profunda colocar aceite y dorar las presas de pollo. Retirar y reservar.\n3. En la misma olla poner los vegetales duros (cebolla, zanahoria, morrón, verdeo, puerro). Cuando transparenta agregar ajos y tomate.\n4. Salpimentar, agregar puré de tomate y cocinar 15 minutos.\n5. Agregar las presas de pollo y cocinar a fuego medio 35-40 min.\n6. Hervir el arroz con sal y aceite (o caldo). Servir el pollo sobre el arroz."""
    },
    {
        "titulo": "Hígado con arroz blanco",
        "ingredientes_clave": ["higado", "caldo", "cebolla", "morron", "arroz"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 bifes de hígado\n- 1 caldo\n- 1 cebolla\n- 1/4 de ají morrón\n- 1/4 de taza de arroz""",
        "pasos": """1. Cortamos los bifes al medio, los colocamos en el fondo de una cacerola junto con las verduras picadas y el caldo a fuego lento, unos 25 a 30 minutos.\n2. Se hará una salsita espesa. Aparte cocinamos el arroz en abundante agua por 15 minutos.\n3. Servimos todo junto."""
    },
    {
        "titulo": "Milanesas con Fideos, Queso y Salsa Blanca",
        "ingredientes_clave": ["milanesa", "fideo", "salsa blanca", "leche", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 6 U. Milanesas (carne o pollo)\n- 1/2 Paquete Spaghetti\n- 1 Sobre Polvo para Salsa Blanca\n- 600 ml. Leche\n- 1 Sobre Ajinomoto sabor Verdura\n- Queso Cremoso\n- Orégano, Nuez Moscada, Ají Molido Picante, Aceite, Pimienta""",
        "pasos": """1. Pincelar una placa para horno con aceite y colocar las milanesas.\n2. En una olla mezclar el polvo de salsa blanca, la leche, saborizante, pimienta y nuez moscada. Revolvemos al fuego hasta que espese.\n3. Hervir agua y cocinar los fideos. Al mismo tiempo cocinar las milanesas al horno.\n4. Colar los fideos y mezclarlos con la salsa blanca.\n5. Dar vuelta las milanesas doradas, colocarles encima fideos con salsa, fetas de queso cremoso, orégano y ají molido. Gratinar en el horno.\n6. Emplatar."""
    },
    {
        "titulo": "Guiso de Fideos Moñito",
        "ingredientes_clave": ["carne", "chorizo", "panceta", "salchicha", "morron", "cebolla", "zanahoria", "verdeo", "apio", "ajo", "zapallo", "fideo", "arveja", "pure de tomate", "caldo"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 kg roast beef cortado en trocitos\n- 2 chorizos, 200 g panceta, 2 salchichas parrilleras\n- 1/2 ají verde, 1 cebolla grande, 1/2 ají rojo\n- 1 zanahoria, 1 penca de verdeo, 1 penca de apio, 2 dientes ajo\n- 1 rodaja calabacita\n- 500 g fideos moñito, 1 lata de arvejas\n- 500 g puré de tomate, caldo, condimentos""",
        "pasos": """1. Rehogar panceta. Retirar y dorar chorizos y salchichas. Retirar.\n2. Dorar la carne en tandas y retirar.\n3. Picar las verduras y ablandarlas en la misma sartén 10 min.\n4. Pasar todo a una olla grande (carne, verduras, embutidos). Incorporar puré de tomate, caldo, agua y condimentos.\n5. Cocinar semitapado 1.5 hs.\n6. Agregar fideos y cocinar. Al final sumar las arvejas, apagar el fuego y dejar asentar."""
    },
    {
        "titulo": "Fideos con salsa",
        "ingredientes_clave": ["pure de tomate", "cebolla", "morron", "carne", "fideo"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 g Puré de tomate\n- 1 cebolla\n- 1/2 morrón rojo, 1/2 morrón verde\n- Condimentos y sal a gusto\n- 600 g Carne picada\n- 1 paquete fideos (a gusto)""",
        "pasos": """1. Cortar la cebolla y los morrones en cubitos, rehogarlos en aceite.\n2. Agregar la carne picada y condimentar.\n3. Cuando la carne esté cocinada, incorporar el puré de tomate.\n4. En una olla hervir agua y cocinar los fideos a gusto.\n5. Colar los fideos, servir y agregar la salsa."""
    },
    {
        "titulo": "Tarta souflee de choclo",
        "ingredientes_clave": ["choclo", "huevo", "crema de leche", "queso", "tapa de tarta"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 2 latas de maíz cremoso amarillo\n- 5 huevos\n- 1 pote chico de crema\n- 2 sobres queso rallado\n- 5 fetas de queso de barra cortado en tiritas\n- 1 sobre masa de tarta""",
        "pasos": """1. En un bol poner 2 latas de choclo 5 huevos y un pote de crema. Mixar todo quedará una crema\n2. Agregaremos el queso rallado y 5 fetas de queso de barra cortado en tiritas mezclar todo\n3. Enmantecar y forrar un molde de tarta con una de las hojas de masa volcar el relleno y tapar con la otra hoja de masa apretando los bordes para cerrar bien\n4. Recortar los excedentes de la masa y llevar a horno hasta dorar."""
    },
    {
        "titulo": "Tarta de Manzana invertida",
        "ingredientes_clave": ["azucar", "manzana", "huevo", "leche", "harina"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """Caramelo:\n- 3/4 taza Azúcar\n- 2 manzanas grandes\nMezcla:\n- 2 huevos\n- 1 taza azúcar\n- 1/2 taza aceite\n- 1 taza leche\n- 1 cucharadita Esencia de vainilla\n- Ralladura de 1 limón\n- 3 tazas harina leudante""",
        "pasos": """1. Enmantecar y enharinar el molde, poner azúcar, poner las manzanas y reservar. En un bol mezclar los huevos con el azúcar.\n2. Agregar el aceite, mezclar, luego integrar la leche, esencia, ralladura.\n3. Agregar la harina tamizada, mezclar. Agregar la mezcla al molde.\n4. Cocinar en horno a 180° por 45 minutos aproximadamente.\n5. Desmoldar en caliente para que no se pegue el caramelo."""
    },
    {
        "titulo": "Tarta salada de remolacha y queso cottage",
        "ingredientes_clave": ["almendra", "manteca", "huevo", "cebolla", "ajo", "remolacha", "queso crema", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """Masa:\n- 150 g almendras molidas\n- 30 g ghee casero o manteca\n- 1 huevo\nRelleno:\n- 1 cda aceite de oliva\n- 1 cebolla mediana\n- 2 dientes ajo\n- 3 huevos\n- 3 (o 4) remolachas ya cocidas\n- 3 cdas soperas colmadas de queso cottage\n- 1 feta queso protein (aprox. 70 gramos)""",
        "pasos": """1. Mezclar ingredientes de la masa. Extender sobre asadera. Pinchar con tenedor. Llevar a horno medio 15 a 20 minutos.\n2. Sofreír la cebolla y ajos. Picar las remolachas y agregarlas.\n3. Batir los huevos con el cottage. Condimentar. Agregar el rehogado y mezclar. Agregar queso.\n4. Agregar el relleno a la base y llevar nuevamente al horno, hasta dorar."""
    },
    {
        "titulo": "Tarta Invertida de Banana",
        "ingredientes_clave": ["huevo", "azucar", "banana", "harina"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 2 huevos\n- 1/2 taza Azúcar\n- 2 bananas\n- 1/2 taza aceite\n- 1 cucharadita Esencia de vainilla\n- 1/2 taza Harina leudante\nCaramelo:\n- 1/2 taza Azúcar""",
        "pasos": """1. Caramelo: hacer el caramelo en sartén. Poner en fuente y arriba rodajas de banana.\n2. Mezclar huevos y azúcar. Incorporar aceite y esencia.\n3. Incorporar harina tamizada. (Si queda denso agregar leche).\n4. Poner mezcla en molde y hornear a baño maría 120° por 55 minutos (o horno convencional).\n5. Desmoldar en caliente."""
    },
    {
        "titulo": "Tarta de cebolla con masa de garbanzos",
        "ingredientes_clave": ["garbanzo", "harina", "cebolla", "huevo", "queso", "leche"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """Masa:\n- 1 lata de garbanzos (o 200 grs cocidos)\n- 3 cds aceite\n- 4 cds aproximadamente harina\nRelleno:\n- 3 cebebollas\n- 3 huevos\n- 100 grs queso rallado\n- 200 grs queso cremoso o mozzarella\n- 4 cdas harina\n- 100 cc leche""",
        "pasos": """1. Masa: mixear garbanzos con aceite y condimentos. Incorporar harina hasta formar masa.\n2. Cortar cebolla en Juliana y rehogar.\n3. En bol mezclar huevos, leche, harina. Agregar cebolla y quesos.\n4. Forrar molde con la masa, volcar relleno y espolvorear queso. Cocinar en horno fuerte."""
    },
    {
        "titulo": "Relleno tarta de acelga",
        "ingredientes_clave": ["acelga", "morron", "cebolla", "queso crema", "huevo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 huevos\n- 1 cebolla\n- 1/3 morrón rojo\n- 3 paquetes acelga\n- 3 cucharadas queso crema\n- queso mantecoso\n- ajo en polvo, pimentón dulce, ají molido, sal""",
        "pasos": """1. Hervir la acelga, escurrir bien y cortar.\n2. Cortar bien chiquito el morrón y la cebolla y saltear hasta que estén cocidos.\n3. Juntar la acelga con las verduras en un bol y añadir el queso crema.\n4. Mezclar los huevos con los condimentos e incorporar al bol, agregar queso mantecoso."""
    },
    {
        "titulo": "Tarta toffee",
        "ingredientes_clave": ["crema de leche", "chocolate", "dulce de leche", "masa sable"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 139 g Crema de Leche\n- 139 g Choco para derretir\n- 400 g Dulce de Leche Repostero\n- Masa sable""",
        "pasos": """1. Ganache: picar el chocolate. Calentar la crema hasta ebullición, volcar sobre el chocolate y reposar 4 min. Revolver hasta integrar.\n2. Rellenar la masa sable con dulce de leche.\n3. Volcar el ganache tibio sobre el dulce de leche. Dejar enfriar."""
    },
    {
        "titulo": "Masa para tartas (Sin Gluten)",
        "ingredientes_clave": ["premezcla sin gluten", "huevo", "leche"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 3 tazas premezcla sin gluten (o mezcla casera)\n- 1 huevo\n- 50 cc aceite\n- 1 cdita sal, 1 cdita polvo de hornear\n- Leche o agua c/n""",
        "pasos": """1. Mezclar ingredientes secos, agregar huevo y líquido de a poco hasta masa lisa.\n2. Enmantecar y espolvorear asadera.\n3. Estirar masa espolvoreando premezcla.\n4. Cocinar en fuego intermedio con relleno a gusto."""
    },
    {
        "titulo": "Tarta de Atún",
        "ingredientes_clave": ["cebolla", "huevo", "ajo", "atun", "queso crema", "tapa de tarta", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 Masa de Tarta doble\n- 2 Latas de Atún\n- 2 Cebollas grandes\n- 2 Dientes Ajo\n- 2 Huevos\n- 3 Cucharadas Queso Crema o Crema de Leche\n- 200 gr Queso cremoso\n- Condimentos a gusto""",
        "pasos": """1. Caramelizar cebolla en juliana. Hervir 1 huevo.\n2. Agregar ajo picado a la cebolla y cocinar 4 min.\n3. Agregar Atún y queso crema, condimentar. Retirar del fuego.\n4. Agregar el huevo duro picado y el huevo crudo, mezclar.\n5. Acomodar masa en fuente, esparcir relleno, poner queso cremoso y cerrar con la otra tapa.\n6. Cocinar 35 min."""
    },
    {
        "titulo": "Tarta de brócoli y espinaca con mozzarella",
        "ingredientes_clave": ["brocoli", "espinaca", "verdeo", "huevo", "queso", "queso crema", "tapa de tarta"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 brócoli mediano\n- 200 g espinaca fresca\n- 4 cebollitas de verdeo\n- 3 huevos grandes\n- 125 g mozzarella rallada\n- 100 g queso crema\n- 1 masa para tarta""",
        "pasos": """1. Precalentá el horno a 200 °C.\n2. Herví ramitos de brócoli por 5 min.\n3. Incorporá espinaca y cebollita el último minuto.\n4. Escurrí bien las verduras.\n5. Mezclá verduras, huevos, mozzarella, queso crema y sal.\n6. Forrá una tartera con la masa.\n7. Volcá el relleno.\n8. Repulgá los bordes y horneá 35-40 min."""
    },
    {
        "titulo": "Tarta de Atún con Base de Puré de Papa",
        "ingredientes_clave": ["papa", "morron", "cebolla", "tomate", "ajo", "atun", "aceituna", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 6 Papas\n- 1 Pimiento rojo\n- 1 Cebolla, 1 Tomate, 1 Diente Ajo\n- 2 Latas de Atún\n- 100 grs Aceitunas verdes\n- 4 Huevos\n- Condimentos a gusto""",
        "pasos": """1. Hervir las papas con piel.\n2. Pelar y aplastar dentro de un molde aceitado.\n3. Hornear a 180° por 10 min.\n4. Hervir 4 huevos, pelar y cortar en rodajas.\n5. Sofreír cebolla, pimiento y ajo. Agregar atún, tomate, aceitunas y condimentos.\n6. Colocar la mitad del relleno sobre la base, agregar huevos y terminar con el resto.\n7. Hornear hasta dorar."""
    },
    {
        "titulo": "Tarta básica de jamón, queso y tomate",
        "ingredientes_clave": ["tapa de tarta", "jamon", "queso", "tomate", "huevo"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 tapa de pascualina\n- jamón cocido\n- queso fresco y rallado\n- 2 tomates peritas chicos\n- 2 huevos""",
        "pasos": """1. Cortar jamón.\n2. Agregar queso en trocitos, tomate y huevos.\n3. Sumar queso rallado.\n4. Poner masa en asadera, volcar relleno y hacer repulgue.\n5. Cocinar en horno hasta dorar."""
    },
    {
        "titulo": "Tarta de coco y dulce de leche",
        "ingredientes_clave": ["huevo", "azucar", "manteca", "harina", "dulce de leche", "coco"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 400 gramos dulce de leche\n- 30 gramos manteca\n- 80 gramos coco\n- 250 gramos harina leudante\n- 3 huevos\n- 75 gramos azúcar""",
        "pasos": """1. Batir 1 huevo con azúcar. Incorporar manteca y harina leudante. Enfriar masa 20 min.\n2. Estirar masa en molde y hornear a 180 °C por 20 min.\n3. Cubrir base con dulce de leche.\n4. Mezclar coco con 2 huevos, distribuir encima y hornear hasta dorar."""
    },
    {
        "titulo": "Tarta de hojas de remolacha y salsa blanca",
        "ingredientes_clave": ["tapa de tarta", "remolacha", "zanahoria", "cebolla", "morron", "huevo", "maicena", "leche", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 masa de tarta\n- 1 atado de remolacha (las hojas)\n- 2 zanahorias, 1 cebolla, 1/2 morrón\n- 3 huevos duros\n- Salsa blanca: 500 ml leche (o agua y leche en polvo), 2 cdas maicena\n- Queso para derretir""",
        "pasos": """1. Hervir los huevos. Precocinar masa 5 min.\n2. Lavar vegetales. Picar hojas y pencas de remolacha y cocinar al vapor.\n3. Saltear cebolla, morrón y zanahoria rallada.\n4. Combinar salsa blanca y salteado.\n5. Poner huevo picado sobre la base, arriba el relleno y queso.\n6. Cocinar hasta dorar."""
    },
    {
        "titulo": "Palmeritas con tapa de tarta",
        "ingredientes_clave": ["tapa de tarta", "manteca", "azucar"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 1 paquete tapa de tarta de hojaldre\n- 50 gramos manteca\n- 3 cucharadas azúcar""",
        "pasos": """1. Ablandar manteca y batir con azúcar.\n2. Untar la mezcla en las tapas de tarta.\n3. Enrollar de cada extremo y cortar.\n4. Hornear 8-10 min de cada lado hasta dorar."""
    },
    {
        "titulo": "Tarta de Verdura con Masa Casera",
        "ingredientes_clave": ["harina", "zapallo", "zanahoria", "huevo", "acelga", "cebolla", "morron", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """Masa:\n- 250g harina 000\n- 65 cc Aceite, 100 cc agua caliente\nRelleno:\n- 1/2 zapallo, 2 zanahorias\n- 3 huevos\n- 1 paquete acelga\n- 2 Cebollas, 1 morrón\n- Queso cremoso""",
        "pasos": """1. Unir harina, aceite, sal y agua caliente. Enfriar masa.\n2. Hervir zapallo y zanahoria. Hervir huevos.\n3. Rehogar cebolla, morrón y acelga.\n4. Unir ingredientes del relleno.\n5. Estirar masa en tartera. Rellenar y tapar. Pincelar con yema y hornear 30/40 min."""
    },
    {
        "titulo": "Flan Caserito",
        "ingredientes_clave": ["leche", "huevo", "azucar"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 ml Leche\n- 4 huevos\n- 1/2 Taza azúcar\n- Esencia de vainilla\n- Azúcar para caramelo""",
        "pasos": """1. Preparar caramelo en el molde.\n2. Batir huevos, azúcar, vainilla y sal. Incorporar leche.\n3. Verter mezcla en el molde.\n4. Cocinar a baño María en horno a 170°.\n5. Enfriar y desmoldar."""
    },
    {
        "titulo": "Gelatina sabor tiramisú",
        "ingredientes_clave": ["leche", "yogurt", "gelatina", "cafe", "stevia"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 ml leche descremada\n- 300 gr yogurt natural\n- 14 g gelatina sin sabor\n- 2 cucharadas café\n- 2 cucharadas stevia""",
        "pasos": """1. Calentar leche, stevia, gelatina, 200g de yogurt y café revolviendo a fuego bajo.\n2. Pasar a vasitos y enfriar toda la noche en heladera.\n3. Coronar con el resto del yogurt y cacao."""
    },
    {
        "titulo": "Arroz con leche",
        "ingredientes_clave": ["leche", "arroz", "azucar"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 litro leche\n- 12 cucharadas colmadas arroz\n- 6 cucharadas colmadas azúcar""",
        "pasos": """1. Entibiar leche.\n2. Incorporar arroz a fuego intermedio.\n3. Colocar azúcar y mezclar hasta que esté listo el arroz."""
    },
    {
        "titulo": "Cheesecake de queso y dulce",
        "ingredientes_clave": ["galletitas", "manteca", "queso crema", "crema de leche", "huevo", "azucar", "membrillo"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """Base:\n- 300 gr galletas lincoln\n- 50 cc manteca\nCheesecake:\n- 250 gr Queso crema\n- 100 cc Crema de leche\n- 4 Huevos, 75 gr Azúcar\n- 250 gr Dulce de membrillo""",
        "pasos": """1. Triturar galletas con manteca. Cubrir molde y hornear 10 min.\n2. Batir crema, queso crema, huevos y azúcar.\n3. Ablandar membrillo con agua y colocar en el fondo de la tarta.\n4. Sumar mezcla de cheesecake y hornear a 160° por 45 min."""
    },
    {
        "titulo": "Globi, postre de la Antigua Roma",
        "ingredientes_clave": ["ricota", "harina", "miel", "semillas"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 500 g Ricota\n- 120 g Harina de trigo\n- Aceite de oliva (para freír)\n- Miel líquida\n- Semillas de sésamo o amapola""",
        "pasos": """1. Escurrir ricota y mezclar con harina formando una masa. Formar bolitas.\n2. Freír en aceite de oliva hasta dorar.\n3. Servir tibias bañadas con miel y semillas."""
    },
    {
        "titulo": "Torta Tres Leches",
        "ingredientes_clave": ["huevo", "azucar", "harina", "leche", "crema de leche", "dulce de leche"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 huevos, 60 g azúcar, 60 g harina\nPara embeber:\n- 100 g leche en polvo (o normal)\n- 100 g crema de leche\n- 250 cc leche entera\nCubierta:\n- Crema Chantilly\n- Dulce de leche""",
        "pasos": """1. Batir huevos con azúcar a punto letra. Agregar harina.\n2. Volcar en molde y hornear a 160° por 12-15 min.\n3. Mezclar las leches y crema.\n4. Pinchar el bizcochuelo y volcar el líquido. Enfriar.\n5. Cubrir con Chantilly y dulce de leche."""
    },
    {
        "titulo": "Budín de pan",
        "ingredientes_clave": ["leche", "pan", "huevo", "azucar"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 litro leche\n- 500 g pan duro\n- 5 o 6 huevos\n- 1 taza azúcar\n- Vainilla y ralladura de limón/naranja\n- Caramelo: 1.5 taza azúcar""",
        "pasos": """1. Remojar pan en leche.\n2. Preparar caramelo y bañar el molde.\n3. Desintegrar el pan remojado. Batir huevos, azúcar, esencias y mezclar con el pan.\n4. Volcar en el molde y hornear a baño María por 1 hora.\n5. Enfriar y desmoldar."""
    },
    {
        "titulo": "Crema Chantilly",
        "ingredientes_clave": ["crema de leche", "azucar"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 200 ml crema de leche (35% grasa)\n- 1 o 2 cdas azúcar impalpable\n- Vainilla""",
        "pasos": """1. Crema, varillas y bol bien fríos.\n2. Batir crema a velocidad media, agregar azúcar y vainilla.\n3. Batir hasta picos firmes."""
    },
    {
        "titulo": "Dulce de leche desde lata",
        "ingredientes_clave": ["leche condensada"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 latas leche condensada\n- Agua abundante""",
        "pasos": """1. Retirar etiquetas de las latas.\n2. Hervir sumergidas en agua por 2 o 3 horas. (No dejar que se queden sin agua).\n3. Apagar fuego y dejar enfriar en la cacerola de un día para otro."""
    },
    {
        "titulo": "Postre estilo Serenito de dulce de leche",
        "ingredientes_clave": ["leche", "azucar", "maicena", "dulce de leche"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 ml leche\n- 2 cdas azúcar\n- 2 cdas maicena\n- 4 cdas dulce de leche\n- Vainilla""",
        "pasos": """1. Separar mitad de leche y mezclar con azúcar y maicena sin grumos.\n2. Hervir la otra mitad de la leche.\n3. Unir ambas leches a fuego mínimo sin dejar de batir.\n4. Al hervir agregar dulce de leche y espesar.\n5. Servir en vasos, tapar con film al contacto y enfriar."""
    },
    {
        "titulo": "Mousse de limón casera",
        "ingredientes_clave": ["huevo", "azucar", "leche", "maicena", "limon"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 Huevos (separar claras y yemas)\n- 80 g Azúcar\n- 200 ml Leche\n- 20 g Maicena\n- Jugo y ralladura de 2 limones""",
        "pasos": """1. Mezclar yemas, maicena y un poco de leche.\n2. Calentar resto de leche con mitad del azúcar.\n3. Agregar yemas y cocinar revolviendo hasta espesar.\n4. Agregar jugo y ralladura. Enfriar.\n5. Batir claras a nieve con el resto del azúcar.\n6. Incorporar merengue a la crema con movimientos envolventes. Refrigerar."""
    },
    {
        "titulo": "Chocotorta Helada",
        "ingredientes_clave": ["queso crema", "helado", "galletitas", "leche"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 pote helado de dulce de leche\n- 200 g queso untable\n- 1 pote helado de chocolate\n- 340 g chocolinas (galletas de chocolate)\n- 100 ml leche""",
        "pasos": """1. Mezclar queso untable con helado de dulce de leche y enfriar.\n2. Armar capas: helado de chocolate, galletitas mojadas en leche, helado de chocolate. Enfriar 15 min.\n3. Agregar capa de la mezcla de dulce de leche y queso. Enfriar 15 min.\n4. Repetir capas y enfriar por 3 horas mínimo."""
    },
    {
        "titulo": "Peras al vino tinto",
        "ingredientes_clave": ["pera", "vino", "azucar"],
        "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 8 peras\n- 1 lt vino tinto\n- 10 cdas azúcar\n- 1 cdta canela""",
        "pasos": """1. Pelar peras y poner en cacerola con vino, azúcar y canela.\n2. Hervir destapado. Luego tapar y cocinar 30 min girándolas.\n3. Retirar peras y reducir la salsa a caramelo. Enfriar."""
    },
    {
        "titulo": "Postre de vainillas y limón",
        "ingredientes_clave": ["crema de leche", "leche condensada", "limon", "galletitas", "leche"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 24 vainillas\n- Leche c/n\n- 1 pote leche condensada\n- 1 pote crema\n- Jugo y ralladura de 2 limones""",
        "pasos": """1. Batir crema a medio punto, agregar leche condensada, jugo y ralladura de limón.\n2. Remojar vainillas en leche y hacer capas de vainillas y crema en una fuente.\n3. Refrigerar por tres horas."""
    },
    
    # ------------------ NUEVAS RECETAS AGREGADAS ------------------
    {
        "titulo": "Risotto con calabaza",
        "ingredientes_clave": ["calabaza", "cebolla de verdeo", "puerro", "cebolla", "arroz", "queso", "vino"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1/2 calabaza (400g)\n- 2 o más tazas de agua o caldo\n- 3-4 cebollitas de verdeo o 2 puerros\n- 1/2 cebolla\n- 1 taza arroz de risotto\n- 100 g queso\n- Sal, pimienta, nuez moscada, vino blanco""",
        "pasos": """1. Cortar la calabaza en cubos.\n2. Picar las verduras y sofreír en aceite de oliva.\n3. Agregar la calabaza al sofrito y cocinar hasta ablandar un poco.\n4. Agregar caldo o agua de a cucharones para que el arroz absorba (20-25').\n5. Agregar el arroz y saltear (momento del vino).\n6. Agregar el queso en cubos y nuez moscada para derretir."""
    },
    {
        "titulo": "Risotto de hongos",
        "ingredientes_clave": ["arroz", "cebolla de verdeo", "hongo", "queso", "vino", "manteca"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 300 g Arroz carnaroli\n- 4 unidades Cebolla de verdeo\n- 150 gramos Hongos\n- Caldo de verduras\n- Sal con curry, Pimienta, Laurel\n- Queso rallado y 1/2 copa vino blanco""",
        "pasos": """1. Dorar el arroz y el verdeo en aceite de oliva y manteca.\n2. Ir poniendo de a poco el vino.\n3. Mezclar hasta que se vea cocido el arroz y agregar todos los hongos.\n4. Poner mucho queso rallado y servir."""
    },
    {
        "titulo": "Risotto a la rúcula",
        "ingredientes_clave": ["arroz", "rucula", "caldo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 250 gr arroz\n- 200 gr rúcula\n- 1 cubito caldo de gallina\n- 500 ml agua\n- 100 gr queso rallado\n- Aceite, sal, pimienta""",
        "pasos": """1. Lavar las hojas de rúcula.\n2. Disolver el caldo en el agua hirviendo.\n3. Saltear el arroz en aceite hasta que tome color.\n4. Agregar el caldo y cocinar durante 10 minutos.\n5. Salpimentar, incorporar la rúcula y el queso. Mezclar y dejar 5 minutos más."""
    },
    {
        "titulo": "Risotto Clásico con Verduras",
        "ingredientes_clave": ["arroz", "cebolla", "zanahoria", "morron", "vino", "caldo", "champiñon", "queso", "manteca"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 250 g Arroz carnaroli\n- 1 Cebolla blanca\n- 1 Zanahoria, 1 Pimiento rojo\n- 150 ml Vino blanco seco\n- 1 litro Caldo de ave\n- 1 lata Champiñones\n- 100 g Queso parmesano, 80 g Manteca""",
        "pasos": """1. Rehogar cebolla, zanahoria y pimiento en aceite.\n2. Agregar el arroz y tostar 2 minutos.\n3. Añadir el vino blanco y dejar evaporar.\n4. Incorporar el caldo caliente en tandas.\n5. A los 15 minutos agregar los champiñones.\n6. Apagar fuego, añadir queso, manteca, sal y pimienta. Emulsionar."""
    },
    {
        "titulo": "Risotto de champiñones y espinaca",
        "ingredientes_clave": ["cebolla", "ajo", "espinaca", "champiñon", "arroz", "caldo", "queso"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 cebolla, 2 dientes ajo\n- 1 atado espinaca\n- 1 bandeja champiñones\n- 2 tazas arroz carnaroli\n- Caldo de pollo/verduras\n- Queso rallado, aceite, sal, pimienta""",
        "pasos": """1. Sofreír ajo y cebolla. Agregar champiñones.\n2. Incorporar arroz, revolver 1 minuto, sumar la espinaca.\n3. Bajar el fuego e incorporar el caldo de a cucharones (20 min).\n4. Agregar queso rallado y servir."""
    },
    {
        "titulo": "Risotto integral con verduras",
        "ingredientes_clave": ["arroz", "espinaca", "zanahoria", "zapallo", "papa", "ajo", "cebolla", "tomate", "caldo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 tacitas arroz integral\n- 1 paquete espinacas\n- 1 zanahoria, 1 rodaja zapallo, 1 papa\n- Ajo, perejil, 1 cebolla\n- 2 tomates\n- Caldo, condimentos""",
        "pasos": """1. Rehogar cebolla, ajo, perejil. Agregar zanahoria y tomate.\n2. Sumar daditos de zapallo, papa y espinaca picada.\n3. Por último el arroz y el caldo.\n4. Cocinar 25 minutos y dejar reposar antes de servir."""
    },
    {
        "titulo": "Sopa crema de verduras",
        "ingredientes_clave": ["zanahoria", "morron", "cebolla", "zapallo", "ajo", "queso crema", "choclo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 zanahoria, 1/2 pimiento, 1 cebolla\n- 1/2 zapallo, 2 dientes ajo\n- 70 gr queso crema\n- 100 gr choclo\n- 800 cc agua, sal, pimienta""",
        "pasos": """1. Asar las verduras al horno (ajo y zapallo con cáscara para sacar luego el puré).\n2. Procesar o licuar todo junto con el agua y queso crema.\n3. Calentar en olla y servir."""
    },
    {
        "titulo": "Sopa cremosa de mostaza",
        "ingredientes_clave": ["puerro", "cebolla", "ajo", "manteca", "maicena", "mostaza", "caldo", "crema de leche", "panceta"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1 puerro, 1 cebolla, 2 dientes ajo\n- 30 g manteca, 2 cdas maicena\n- 3 cdas mostaza\n- 1 litro caldo, 75 ml crema de leche\n- 200 g panceta (opcional)""",
        "pasos": """1. Sofreír cebolla y ajo en manteca.\n2. Incorporar maicena, luego el puerro y el caldo poco a poco.\n3. Hervir 15 minutos.\n4. Dorar panceta aparte.\n5. Licuar sopa con mostaza y crema. Servir con panceta."""
    },
    {
        "titulo": "Sopa paraguaya",
        "ingredientes_clave": ["harina de maiz", "leche", "cebolla", "huevo", "morron", "queso", "manteca"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 500 grs harina de maíz amarillo\n- 1 litro leche\n- 1 Kg cebollas, 1 morrón\n- 4 huevos\n- 500 grs queso cremoso\n- Manteca y condimentos""",
        "pasos": """1. Sofreír cebolla y morrón con manteca.\n2. Hervir la leche y agregar harina de maíz en forma de lluvia. Sumar el sofrito y el queso.\n3. Batir huevos y unir a la mezcla.\n4. Hornear en fuente enmantecada 45 min a 180°."""
    },
    {
        "titulo": "Sopa crema de calabaza",
        "ingredientes_clave": ["calabaza", "papa", "cebolla", "zanahoria", "ajo", "queso", "crema de leche"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 800 g Calabaza\n- 2 Papas, 1 Cebolla, 1 Zanahoria\n- Ajo en polvo, pimienta\n- Queso en hebras\n- 200 ml Crema de leche""",
        "pasos": """1. Sofreír cebolla y sellar todas las verduras.\n2. Agregar agua y caldo, cocinar.\n3. Licuar todo junto a la crema de leche.\n4. Servir y gratinar con queso por encima."""
    },
    {
        "titulo": "Sopa Crema de Verduras al Horno",
        "ingredientes_clave": ["calabaza", "zanahoria", "cebolla", "batata", "queso crema", "caldo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1/2 Calabaza, 1 Zanahoria, 1 Cebolla, 1 Batata\n- Sal, pimienta, nuez moscada\n- Queso crema\n- 500 ml Caldo""",
        "pasos": """1. Cortar verduras en cubos y asar 20 min en horno.\n2. Licuar las verduras asadas con el caldo.\n3. Llevar a cacerola unos 10 min para ajustar sabor.\n4. Servir con queso crema o rallado."""
    },
    {
        "titulo": "Sopa de Cebolla Especial",
        "ingredientes_clave": ["cebolla", "ajo", "manteca", "pan", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 1/2 kg Cebollas\n- Ajo a gusto\n- Abundante manteca\n- Rebanadas de pan tostado\n- Queso para gratinar""",
        "pasos": """1. Saltear cebolla y ajo en manteca fuego mínimo (sin sal primero).\n2. Agregar sal para que suden y cocinar 45-60 min agregando chorritos de agua.\n3. Servir y coronar con pan tostado y queso gratinado."""
    },
    {
        "titulo": "Sopa de Vegetales",
        "ingredientes_clave": ["papa", "zapallo", "zanahoria", "apio", "choclo", "cebolla", "ajo", "repollo", "puerro"],
        "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 Papas, 1/2 Zapallo, 3 Zanahorias, 3 Ramas apio\n- 2 Choclos, 3 Cebollas, 2 Dientes ajo\n- Repollo blanco, Puerro\n- Condimentos varios y agua""",
        "pasos": """1. Picar todas las verduras.\n2. Caramelizar cebollas, agregar puerro, apio y ajo.\n3. Incorporar el resto de verduras y cubrir con agua.\n4. Cocinar hasta que todo esté tierno. Decorar con semillas."""
    },
    {
        "titulo": "Sopa Crema Apio y Zapallo",
        "ingredientes_clave": ["apio", "zapallo", "choclo", "leche", "fideo", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- Paquete pequeño de Apio\n- 300gr Zapallo\n- 1 rodaja Choclo\n- 1 taza Leche, Agua\n- Fideos cabello de ángel\n- Queso mantecoso""",
        "pasos": """1. Hervir los vegetales hasta que estén tiernos.\n2. Agregar leche y fideos.\n3. Esperar que espese y servir con queso."""
    },
    {
        "titulo": "Sopa Ramen con Sobras",
        "ingredientes_clave": ["caldo", "pollo", "fideo", "huevo"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 ml Caldo de verduras y pollo\n- 50 g Pechuga de pollo cocida\n- 80 g Fideos ramen\n- 1 Huevo\n- Especias (jengibre, cúrcuma, curry)""",
        "pasos": """1. Calentar el caldo y agregar especias.\n2. Sumar los fideos ramen.\n3. Verter el huevo batido en hilo fino revolviendo suavemente.\n4. Agregar el pollo en trozos. Servir caliente."""
    },
    {
        "titulo": "Burritos rellenos con arroz de ayer",
        "ingredientes_clave": ["tapa de tarta", "cebolla", "morron", "arroz", "huevo", "pure de tomate", "mostaza", "mayonesa"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- Tapas de burritos (o tarta/empanada)\n- Arroz sobrante\n- Cebolla y morrón rehogados\n- 2 huevos batidos\n- Puré de tomate, mostaza, mayonesa""",
        "pasos": """1. Mezclar el arroz, sofrito, tomate y mostaza en sartén.\n2. Incorporar huevo y cocinar.\n3. Untar mayonesa en la masa, rellenar y cerrar.\n4. Calentar en sartén u horno."""
    },
    {
        "titulo": "Budín de pan con membrillo y pasas",
        "ingredientes_clave": ["pan", "leche", "azucar", "huevo", "membrillo", "pasa de uva"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 350 g pan duro\n- 1 litro leche, 250 g azúcar\n- 5 huevos\n- 100 g dulce de membrillo, 50 g pasas hidratadas\n- Caramelo para el molde""",
        "pasos": """1. Acaramelar molde.\n2. Hidratar pan en leche y licuar.\n3. Batir huevos e integrar.\n4. Volcar mezcla en molde, distribuir membrillo y pasas.\n5. Horno baño maría 160° por 60-75 min."""
    },
    {
        "titulo": "Sal al Malbec",
        "ingredientes_clave": ["vino", "sal"],
        "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- Resto de Vino tinto (Malbec)\n- Sal entrefina""",
        "pasos": """1. Volcar sal en el vino hasta que se embeba. Reposar.\n2. Calentar en sartén a fuego medio revolviendo hasta que se evapore el líquido.\n3. Extender sobre papel para secar bien. Guardar en frasco."""
    },
    {
        "titulo": "Masa de tarta salada de polenta",
        "ingredientes_clave": ["polenta", "harina de garbanzos", "huevo", "aceite"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 400 g Polenta cocida fría\n- 50 g Harina de garbanzos\n- Polvo de hornear\n- 1 Huevo, 30 ml Aceite""",
        "pasos": """1. Desarmar la polenta fría en un bowl.\n2. Añadir harina de garbanzos, polvo de hornear, huevo y aceite.\n3. Esparcir en tartera y hornear 180° por 20 min antes de rellenar."""
    },
    {
        "titulo": "Croquetas de Polenta Reciclada",
        "ingredientes_clave": ["polenta", "harina", "cebolla", "huevo", "leche"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": """- 250 grs polenta cocida\n- Harina integral, polvo de hornear\n- 1 huevo\n- Semillas, cebolla deshidratada, condimentos\n- Leche o soda c/n""",
        "pasos": """1. Mezclar la polenta con todos los ingredientes.\n2. Armar bolitas (agregar leche si está muy seca).\n3. Cocinar en sartén o grill."""
    },
    {
        "titulo": "Ensalada de palta",
        "ingredientes_clave": ["palta", "huevo", "tomate"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 paltas\n- 2 huevos duros\n- 1 tomate perita\n- Limón, aceite de oliva, sal y pimienta""",
        "pasos": """1. Mezclar tomate y huevo en trozos.\n2. Ahuecar paltas e integrar a la mezcla.\n3. Aderezar con limón, aceite, sal y pimienta."""
    },
    {
        "titulo": "Ensalada de Chauchas y Huevo",
        "ingredientes_clave": ["chaucha", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 500 g Chauchas\n- 5 Huevos duros\n- Aceite de oliva, vinagre, sal""",
        "pasos": """1. Hervir chauchas y pasar a agua fría para mantener color.\n2. Hervir huevos y cortar.\n3. Mezclar y aderezar a gusto."""
    },
    {
        "titulo": "Ensalada completa saludable",
        "ingredientes_clave": ["zanahoria", "repollo", "manzana", "queso crema", "limon", "tomate", "aceituna", "zucchini", "rucula", "pollo", "huevo"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- Zanahoria, repollo morado/blanco, manzana verde\n- Queso crema, jugo de limón\n- Tomate, aceitunas, zucchini, rúcula\n- Pollo desmenuzado, huevos duros""",
        "pasos": """1. Rallar y mezclar vegetales.\n2. Aderezar porciones con queso crema y limón.\n3. Servir en un gran plato integrado."""
    },
    {
        "titulo": "Ensalada de pasta con pera y nueces",
        "ingredientes_clave": ["fideo", "pera", "rucula", "nuez", "queso"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 320 gr pasta (fusilli)\n- 2 peras, 50 gr nueces, 100 gr rúcula\n- Queso rallado, aceite, sal, pimienta""",
        "pasos": """1. Hervir y colar fideos. Dejar enfriar.\n2. Mezclar rúcula, peras en trozos, nueces y fideos.\n3. Aderezar y espolvorear queso."""
    },
    {
        "titulo": "Ensalada mundialista de atún",
        "ingredientes_clave": ["papa", "zanahoria", "atun", "huevo", "mayonesa"],
        "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 papas, 2 zanahorias\n- 2 latas de atún\n- 4 huevos duros\n- 4 cucharadas mayonesa""",
        "pasos": """1. Hervir papas y zanahorias en cubos.\n2. Mezclar con atún y mayonesa.\n3. Decorar con huevo picado y enfriar."""
    },
    {
        "titulo": "Mi ensalada favorita de palta",
        "ingredientes_clave": ["tomate", "lechuga", "palta", "zapallito", "salsa de soja"],
        "celiaco": False, "vegano": True, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 4 Tomates, 1 Lechuga\n- 2 Paltas, 1 Zapallito Verde\n- Salsa de soja, aceite, sal""",
        "pasos": """1. Cortar todas las verduras crudas y lavadas.\n2. Mezclar y condimentar con aceite y salsa de soja."""
    },
    {
        "titulo": "Ensalada de Verdes y Pollo Rebozado",
        "ingredientes_clave": ["lechuga", "tomate", "mostaza", "pollo", "queso", "mani", "manzana"],
        "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- Lechuga hidropónica, tomates secos\n- Medallones de pollo rebozado\n- Queso azul, maní\n- Manzana verde, mostaza, aceite""",
        "pasos": """1. Cocinar pollo y cortar.\n2. Preparar verdes, queso, tomates y maní.\n3. Aderezar con mostaza y aceite. Sumar manzana al final."""
    },
    {
        "titulo": "Milanesas de berenjenas con ensalada",
        "ingredientes_clave": ["berenjena", "huevo", "pan rallado", "lechuga", "tomate"],
        "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 3 berenjenas\n- 3 huevos\n- Pan rallado, condimentos\n- Lechuga y tomate para acompañar""",
        "pasos": """1. Purgar berenjenas con sal y secar.\n2. Pasar por huevo condimentado y luego pan rallado.\n3. Hornear a 180° hasta dorar y servir con ensalada."""
    },
    {
        "titulo": "Ensalada de manzana con zanahoria",
        "ingredientes_clave": ["manzana", "zanahoria", "limon"],
        "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 manzanas rojas\n- 3 zanahorias\n- 1 limón, aceite""",
        "pasos": """1. Pelar y cortar en tiras finas.\n2. Exprimir limón por encima para evitar oxidación y condimentar."""
    },
    {
        "titulo": "Ensalada de Remolacha y Yogur",
        "ingredientes_clave": ["remolacha", "yogurt", "ajo", "limon"],
        "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": """- 2 Remolachas cocidas\n- 129 g Yogur natural\n- 1 diente Ajo, gotas de limón\n- Aceite, sal, pimienta""",
        "pasos": """1. Cortar remolachas en rodajas.\n2. Mezclar yogur con ajo, limón y aceite.\n3. Bañar las remolachas y enfriar antes de servir."""
    }
]

# ==========================================
# 2. CATEGORIZACIÓN SEMÁNTICA
# ==========================================
# (Sin Emojis para que los selectores CSS enganchen perfecto)
CATEGORIAS_MAP = {
    "Carnes y Proteínas": ["carne", "cerdo", "pollo", "milanesa", "chorizo", "panceta", "salchicha", "higado", "atun", "jamon"],
    "Lácteos y Huevos": ["huevo", "yogurt", "queso", "crema de leche", "leche", "queso crema", "dulce de leche", "manteca", "ricota", "leche condensada", "mayonesa"],
    "Vegetales y Legumbres": ["papa", "cebolla", "cebolla de verdeo", "verdeo", "aceituna", "ajo", "tomate", "zapallito", "zapallo", "calabaza", "zanahoria", "morron", "zucchini", "arveja", "choclo", "espinaca", "acelga", "remolacha", "garbanzo", "apio", "brocoli", "puerro", "pure de tomate", "champiñon", "hongo", "rucula", "chaucha", "repollo", "lechuga", "palta", "berenjena"],
    "Frutas y Frutos Secos": ["kiwi", "limon", "frutilla", "nuez", "manzana", "banana", "pera", "coco", "almendra", "mani", "pasa de uva"]
}

ingredientes_unicos = set()
for receta in RECETAS:
    for ing in receta["ingredientes_clave"]:
        ingredientes_unicos.add(ing)

INGREDIENTES_POR_CATEGORIA = {cat: [] for cat in CATEGORIAS_MAP.keys()}
INGREDIENTES_POR_CATEGORIA["Despensa y Otros"] = []

for ing in sorted(list(ingredientes_unicos)):
    encontrado = False
    for cat, lista_keywords in CATEGORIAS_MAP.items():
        if ing in lista_keywords:
            INGREDIENTES_POR_CATEGORIA[cat].append(ing)
            encontrado = True
            break
    if not encontrado:
        INGREDIENTES_POR_CATEGORIA["Despensa y Otros"].append(ing)

# ==========================================
# 3. LÓGICA DE BÚSQUEDA Y FILTROS
# ==========================================
def buscar_recetas(ingredientes_usuario, filtros):
    set_usuario = set(ingredientes_usuario)
    exactas = []
    casi_listas = []

    for receta in RECETAS:
        if filtros["celiaco"] and not receta.get("celiaco", False): continue
        if filtros["vegano"] and not receta.get("vegano", False): continue
        if filtros["vegetariano"] and not receta.get("vegetariano", False): continue
        if filtros["sin_coccion"] and not receta.get("sin_coccion", False): continue
        if filtros["sin_cubiertos"] and not receta.get("sin_cubiertos", False): continue
            
        set_receta = set(receta["ingredientes_clave"])
        if not set_receta.intersection(set_usuario):
            continue

        faltantes = set_receta - set_usuario
        cantidad_faltantes = len(faltantes)
        
        if cantidad_faltantes == 0:
            exactas.append(receta)
        elif cantidad_faltantes <= 2:
            receta_con_faltantes = receta.copy()
            receta_con_faltantes["ingredientes_faltantes"] = list(faltantes)
            casi_listas.append(receta_con_faltantes)

    return exactas, casi_listas

# ==========================================
# 4. CONFIGURACIÓN DE PÁGINA Y CSS
# ==========================================
st.set_page_config(page_title="¿Qué cocino hoy?", layout="centered")

st.markdown("""
<style>
/* ==============================================================
   SECCIÓN 1: ESTILOS GENERALES Y FONDO DE LA APP
   ============================================================== */
* {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

.stApp {
    background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvh2HGg8fIp_MgI0uSjKsng9aJRjUmXU9VNM6CtHZ1BlVWY4-AQ_F2rGTuhBtzdzs9ooxh2H923vh-k7abOU4unxEDSQyc1gLDEjEi18HpFi6FWz81B7XEOxw-0KNp63hYmQj60iGIu5M/s1600/Interiorrojo_Naturalezamuertaenuncua%5B1%5D.jpg");
    background-size: 150px auto; 
    background-repeat: repeat-y;
    background-position: left top, right top;
    background-attachment: fixed;
    background-color: #FDFBF5; 
}

h1, h2, h3, h4 { color: #1E3A14 !important; }
.stMarkdown p, .stMarkdown li { color: #2F3324; }

/* ==============================================================
   SECCIÓN 2: BANNERS HORIZONTALES POR CATEGORÍA CORREGIDOS
   ============================================================== */

/* 1. Banner para "Carnes y Proteínas" */
div.element-container:nth-child(5) div[data-testid="stMultiSelect"] label {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://preview.colorkit.co/color/ffa07a.png?static=true');
    background-size: cover;
    background-position: center;
    color: #FFFFFF !important;
    padding: 12px 20px;
    border-radius: 8px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
    font-size: 1.15rem;
    letter-spacing: 0.5px;
}

/* 2. Banner para "Lácteos y Huevos" */
div.element-container:nth-child(6) div[data-testid="stMultiSelect"] label {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://caseformaking.com/cdn/shop/products/Egg-Yolk-Yellow-Square_1946x.jpg?v=1653565859');
    background-size: cover;
    background-position: center;
    color: #FFFFFF !important;
    padding: 12px 20px;
    border-radius: 8px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
    font-size: 1.15rem;
    letter-spacing: 0.5px;
}

/* 3. Banner para "Vegetales y Legumbres" */
div.element-container:nth-child(7) div[data-testid="stMultiSelect"] label {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://preview.colorkit.co/color/556b2f.png?static=true');
    background-size: cover;
    background-position: center;
    color: #FFFFFF !important;
    padding: 12px 20px;
    border-radius: 8px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
    font-size: 1.15rem;
    letter-spacing: 0.5px;
}

/* 4. Banner para "Frutas y Frutos Secos" */
div.element-container:nth-child(8) div[data-testid="stMultiSelect"] label {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://i.pinimg.com/736x/d3/cb/b4/d3cbb4fec5527f09f18abd6b3ec44e14.jpg');
    background-size: cover;
    background-position: center;
    color: #FFFFFF !important;
    padding: 12px 20px;
    border-radius: 8px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
    font-size: 1.15rem;
    letter-spacing: 0.5px;
}

/* 5. Banner para "Despensa y Otros" */
div.element-container:nth-child(9) div[data-testid="stMultiSelect"] label {
    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://www.colorhexa.com/b59b7c.png');
    background-size: cover;
    background-position: center;
    color: #FFFFFF !important;
    padding: 12px 20px;
    border-radius: 8px;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.9);
    font-size: 1.15rem;
    letter-spacing: 0.5px;
}

/* ==============================================================
   SECCIÓN 3: COMPONENTES MULTISELECT Y TAGS ELEGIDOS
   ============================================================== */
div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important; 
    border: 2px solid #4F6D23 !important; 
    border-radius: 8px !important;
}
div[data-baseweb="select"] input::placeholder { color: #7A8B6E !important; }
div[data-baseweb="select"] input { color: #1E3A14 !important; }

ul[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
    border: 1px solid #4F6D23 !important;
}
li[data-baseweb="option"] {
    color: #1E3A14 !important; 
    background-color: #FFFFFF !important;
}
li[data-baseweb="option"]:hover, li[data-baseweb="option"][aria-selected="true"] {
    background-color: #99A12D !important; 
    color: #FFFFFF !important;               
}
span[data-baseweb="tag"] {
    background-color: #FBB229 !important; 
    border-radius: 6px !important;
}
span[data-baseweb="tag"] span {
    color: #1E3A14 !important;
    font-weight: bold !important;
}
span[data-baseweb="tag"] svg { fill: #1E3A14 !important; }

/* ==============================================================
   SECCIÓN 4: CHECKBOXES (FILTROS ESPECIALES)
   ============================================================== */
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {
    color: #2F3324 !important;
    font-weight: 600 !important;
}

/* Truco infalible: Modificar la variable CSS nativa de Streamlit para estos bloques */
div[data-testid="stCheckbox"] {
    --primary-color: #ffa07a !important;
}

/* Selector de ultra-alta especificidad para forzar el fondo de la cajita */
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div,
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input[aria-checked="true"] + div {
    background-color: #ffa07a !important;
    border-color: #ffa07a !important;
}

/* Asegurar que el icono (el tick) se mantenga blanco limpio */
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div svg,
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div svg path,
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input[aria-checked="true"] + div svg {
    fill: #FFFFFF !important;
    stroke: #FFFFFF !important;
    color: #FFFFFF !important;
}
/* ==============================================================
   SECCIÓN 5: BOTONES
   ============================================================== */
div.stButton > button {
    border: none !important;
    border-radius: 8px;
    font-weight: bold;
    padding: 0.6rem 1.2rem;
    transition: 0.3s;
    width: 100%;
}
div[data-testid="column"]:nth-of-type(1) div.stButton > button {
    background-color: #D22211 !important;
    color: #FFFFFF !important;
}
div[data-testid="column"]:nth-of-type(1) div.stButton > button:hover {
    background-color: #691410 !important;
}
div[data-testid="column"]:nth-of-type(2) div.stButton > button {
    background-color: #4F6D23 !important;
    color: #FFFFFF !important;
}
div[data-testid="column"]:nth-of-type(2) div.stButton > button:hover {
    background-color: #1E3A14 !important;
}

/* ==============================================================
   SECCIÓN 6: CAJAS DE RECETAS (EXPANDERS)
   ============================================================== */
[data-testid="stExpander"] summary {
    border: 2px solid #4F6D23 !important;
    border-radius: 6px !important;
    background-color: #FDFBF5 !important;
}
[data-testid="stExpander"] summary p {
    color: #1E3A14 !important;
    font-weight: bold !important;
}

/* OCULTAR LA FLECHA POR DEFECTO O EL TEXTO "arrow_down" */
[data-testid="stExpander"] summary svg,
[data-testid="stExpander"] summary div[data-testid="stIconMaterial"] {
    display: none !important;
}

div[data-testid="stExpanderDetails"] {
    background-color: #FFFFFF !important; 
    border: 2px solid #99A12D !important;
    border-top: none !important;
    border-radius: 0 0 6px 6px !important;
    padding: 1.5rem !important;
}
div[data-testid="stExpanderDetails"] * {
    color: #2F3324 !important; 
    background-color: transparent !important;
    font-family: 'Georgia', 'Times New Roman', serif !important;
    white-space: pre-wrap !important;
    line-height: 1.6 !important;
    font-size: 1.05rem !important;
}
div[data-testid="stExpanderDetails"] p strong,
div[data-testid="stExpanderDetails"] strong {
    color: #D22211 !important; 
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; 
}

/* ==============================================================
   SECCIÓN 7: AVISOS Y TITULARES DE RESULTADOS
   ============================================================== */
.titulo-exacta {
    background-color: #4F6D23;
    color: #FFFFFF !important;
    padding: 12px;
    border-radius: 8px;
    font-size: 1.4rem;
    font-weight: bold;
    text-align: center;
    border: 2px solid #1E3A14;
    margin-bottom: 10px;
}
.titulo-parcial {
    background-color: #DE770F;
    color: #FFFFFF !important;
    padding: 12px;
    border-radius: 8px;
    font-size: 1.4rem;
    font-weight: bold;
    text-align: center;
    border: 2px solid #691410;
    margin-bottom: 5px;
}
.alerta-faltantes {
    background-color: #FDFBF5;
    color: #D22211 !important;
    border-left: 5px solid #D22211;
    border-radius: 4px;
    padding: 12px;
    font-size: 1.1rem;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 5. RENDERIZADO DE LA INTERFAZ (UI)
# ==========================================

st.markdown("""
<div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
    <img src="https://cdn-icons-png.flaticon.com/512/1830/1830839.png" alt="Icono de cocina" width="60">
    <h1 style="margin: 0;">¿Qué cocino hoy?</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='font-family: \"Georgia\", serif; font-size: 1.8rem; color: #7a2d27;'>Recetas con lo que tenés a mano.</p>", unsafe_allow_html=True)
st.write("Seleccioná los ingredientes que tengas disponibles.")

# CAMPOS DE SELECCIÓN POR CATEGORÍA
ingredientes_seleccionados_totales = []

for categoria, opciones_ingredientes in INGREDIENTES_POR_CATEGORIA.items():
    if opciones_ingredientes:
        seleccion = st.multiselect(
            categoria, 
            options=opciones_ingredientes,
            placeholder="Elegí tus opciones..."
        )
        ingredientes_seleccionados_totales.extend(seleccion)

st.write("---")
st.subheader("Filtros especiales")

col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    f_celiaco = st.checkbox("Celíaco (Sin TACC)")
    f_vegano = st.checkbox("Vegano")
with col_f2:
    f_vegetariano = st.checkbox("Vegetariano")
    f_sin_coccion = st.checkbox("Sin cocción")
with col_f3:
    f_sin_cubiertos = st.checkbox("Sin cubiertos (Finger food)")

filtros_dict = {
    "celiaco": f_celiaco,
    "vegano": f_vegano,
    "vegetariano": f_vegetariano,
    "sin_coccion": f_sin_coccion,
    "sin_cubiertos": f_sin_cubiertos
}

st.write("---")
col_btn1, col_btn2 = st.columns(2)

buscar_pulsado = False
azar_pulsado = False

with col_btn1:
    if st.button("Buscar Recetas"):
        buscar_pulsado = True
with col_btn2:
    if st.button("Elegir una al azar"):
        azar_pulsado = True

# ==========================================
# 6. MOSTRAR RESULTADOS
# ==========================================
if buscar_pulsado or azar_pulsado:
    if ingredientes_seleccionados_totales:
        exactas, casi_listas = buscar_recetas(ingredientes_seleccionados_totales, filtros_dict)
        
        if azar_pulsado:
            opciones_totales = exactas + casi_listas
            if opciones_totales:
                elegida = random.choice(opciones_totales)
                exactas = [elegida] if elegida in exactas else []
                casi_listas = [elegida] if elegida in casi_listas else []
            else:
                exactas, casi_listas = [], []
        
        if exactas:
            st.success("¡Tenés todo para preparar esto!" if not azar_pulsado else "La suerte eligió esta receta ideal para vos.")
            for r in exactas:
                st.markdown(f"<div class='titulo-exacta'>{r['titulo']}</div>", unsafe_allow_html=True)
                
                with st.expander("🥘 Ver receta paso a paso 📖"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.write("") 
                
        if casi_listas:
            st.info("Te faltan hasta 2 ingredientes para estas recetas:" if not azar_pulsado else "Salió esta opción. Te falta muy poquito para hacerla:")
            for r in casi_listas:
                st.markdown(f"<div class='titulo-parcial'>{r['titulo']}</div>", unsafe_allow_html=True)
                
                faltantes_str = ", ".join(r["ingredientes_faltantes"])
                st.markdown(f"<div class='alerta-faltantes'><strong>Atención - Te falta/n:</strong> {faltantes_str}</div>", unsafe_allow_html=True)
                
                with st.expander("Ver receta"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.write("") 
                
        if not exactas and not casi_listas:
            st.warning("No encontramos recetas que coincidan con lo que elegiste y tus filtros. ¡Probá cambiando las opciones!")
            
    else:
        st.error("Por favor, seleccioná al menos un ingrediente de cualquier categoría.")
