import streamlit as st

# 1. BASE DE DATOS CON LAS RECETAS COMPLETAS
RECETAS = [
    {
        "titulo": "Pastel de Papa con Aceitunas",
        "ingredientes_clave": ["carne", "papa", "aceituna", "cebolla", "huevo"],
        "texto_ingredientes": """- 500 gramos carne
- 4 papas grandes
- 1 puñado aceitunas
- 1 cebolla chica colorada
- 1 cebolla chica común
- 2 huevos duros
- A gusto condimentos""",
        "pasos": """1. En una sartén cocinamos la carne cortada en trocitos con las cebollas con condimentos a gusto!
2. Hervimos las papas cortadas en cubos, las pisamos cuando ya están listas y le ponemos un chorrito de aceite y sal!
3. En un molde ponemos el puré, tapando toda la parte de abajo. Luego la carne ya cocida con huevo duro cortado en trocitos y las aceitunas cortadas. Y por último, arriba ponemos otra capa de puré!
4. Le podemos poner aceitunas o queso rallado arriba! La llevamos al horno a temperatura media hasta que esté calentito!"""
    },
    {
        "titulo": "Guiso de Carne y Papa",
        "ingredientes_clave": ["ajo", "cebolla", "carne", "papa", "tomate"],
        "texto_ingredientes": """- 3 dientes ajo
- 1 cebolla grande
- 500 grs carne (roast beef)
- 2 papas
- 1 lata de tomate cubeteado
- Condimentos varios""",
        "pasos": """1. Poner un chorrito de aceite en una cacerola, picar los ajos, agregar.
2. Picar la cebolla.
3. Cortar la carne en láminas finas, agregar hasta dorar la cebolla y que cambie de color la carne.
4. Agregar los condimentos.
5. Pelar, cortar la papa en trocitos pequeños.
6. Agregar la lata de tomate cubeteado y 2 latas de agua.
7. Agregar las papas, cocinar a fuego medio semitapado hasta que estén las papas y reduzca."""
    },
    {
        "titulo": "Milanesa de Cerdo",
        "ingredientes_clave": ["cerdo", "huevo", "ajo", "pan rallado"],
        "texto_ingredientes": """- 1,5 kg carne o nalga de cerdo
- 6 huevos
- 4 dientes ajo
- 600 grs pan rallado
- Perejil
- Aceite para freír""",
        "pasos": """1. Pedirle al carnicero que te corte en bifes finitos para hacer milanesas. Salar la carne. Pasar huevo mezclado con el ajo y perejil bien picaditos. Después por pan rallado, apretar bien el pan sobre la carne.
2. Calentar el aceite en una sartén y freír. Cuando estén doraditas las sacas y las vas amontonando sobre papel de cocina para escurrir."""
    },
    {
        "titulo": "Tortilla de Papa Fit",
        "ingredientes_clave": ["papa", "huevo"],
        "texto_ingredientes": """- 4 Papas Grandes
- 5 Huevos
- c/n Aceite, Pimienta, Pimentón, Orégano, Ají Molido Picante, Ajo en Polvo, Polvo de Cebollas""",
        "pasos": """1. Pelamos, lavamos y cortamos en cubos no muy grandes las papas y ponemos a hervir en abundante agua.
2. Una vez cocidas las pasamos a una fuente.
3. En un bowl ponemos los huevos junto con los condimentos y batimos muy bien.
4. Ponemos las papas dentro del bowl con los huevos.
5. Calentamos aceite en la tortillera. Añadimos la mezcla y dejamos cocinar. Le damos la vuelta.
6. Desmoldamos en un plato."""
    },
    {
        "titulo": "Helado Cremoso de Frutas",
        "ingredientes_clave": ["kiwi", "yogurt"],
        "texto_ingredientes": """- 10 kiwis chicos (o cualquier fruta)
- 1 pote de yogurt natural
- C/n edulcorante líquido""",
        "pasos": """1. Pelar y cortar todos los kiwis en el bowl. Agregar el yogurt y el edulcorante.
2. Mixear hasta que quede uniforme, sin grumos.
3. Pasar a un recipiente o bolsitas.
4. Dejar congelar unas horas (o toda la noche)."""
    },
    {
        "titulo": "Bocaditos de Arroz",
        "ingredientes_clave": ["arroz", "harina", "huevo"],
        "texto_ingredientes": """- 1 ración de arroz
- 1 cucharadita grande de perejil
- 1-2 cucharadas harina leudante
- Sal a gusto
- 2 huevos""",
        "pasos": """1. En un bol ponemos el arroz con los huevos y mezclamos.
2. Luego ponemos el perejil con la sal.
3. Agregamos la harina y mezclamos.
4. Le hacemos forma con la mano o cuchara y las ponemos en una placa enmantecada. Lo llevamos al horno hasta que queden listos."""
    },
    {
        "titulo": "Zapallitos Rellenos",
        "ingredientes_clave": ["zapallito", "zanahoria", "cebolla", "morron", "ajo", "carne", "caldo", "huevo", "queso"],
        "texto_ingredientes": """- 6 zapallitos verdes medianos
- 1 zanahoria, 2 cebollas, 1 morrón, 1 ajo
- 1/2 kg carne picada
- 1 cubo caldo de verduras
- 1 huevo
- 200 g queso cremoso en cubitos
- Chorrito vino tinto o blanco""",
        "pasos": """1. Hervir los zapallitos en agua con sal hasta que ablanden. Enfriar y ahuecar.
2. En una olla calentar aceite y dorar la carne picada, agregar las verduras picadas.
3. Sumar condimentos, caldo y un chorrito de vino. Cocinar hasta integrar.
4. Rellenar cada zapallito hasta la mitad, agregar un cubito de queso, terminar de rellenar y coronar con más queso.
5. Acomodar en bandeja, verter huevo batido por encima y llevar al horno por 25 minutos."""
    },
    {
        "titulo": "Revuelto de papa, sofrito y huevo",
        "ingredientes_clave": ["papa", "cebolla", "zanahoria", "morron", "ajo", "huevo"],
        "texto_ingredientes": """- 3 papas medianas
- 1 cebolla, 1 zanahoria, 1/2 morrón, 2 dientes ajo
- 3 huevos
- c/n sal, pimienta, nuez moscada, cúrcuma, cayena, perejil""",
        "pasos": """1. Picar bien fino cebolla, morrón y ajo. Cortar la papa y zanahoria en cubos chiquitos.
2. Calentar aceite y rehogar todas las verduras juntas hasta que las papas estén casi hechas.
3. Agregar los huevos y condimentos y cocinar revolviendo hasta que cuajen."""
    },
    {
        "titulo": "Tarta de Zucchini con Base de Papa Dorada",
        "ingredientes_clave": ["papa", "zucchini", "huevo", "queso", "cebolla", "morron"],
        "texto_ingredientes": """- 2 papas
- 3 zucchinis
- 5 huevos M
- 1 trozo queso cremoso
- 1 cebolla chica, 1/3 morrón
- c/n pimienta, sal, nuez moscada""",
        "pasos": """1. Cortar la papa en rodajas finas. Aceitar la tartera, disponer las rodajas encimadas y hornear a fuego fuerte.
2. Cortar el zucchini, salar y masajear. Picar cebolla y morrón y agregar.
3. Sumar huevos y condimentos.
4. Verter el relleno sobre las papas a medio hacer. A media cocción agregar queso por encima y gratinar."""
    },
    {
        "titulo": "Tortilla en freidora de aire",
        "ingredientes_clave": ["papa", "cebolla de verdeo", "cebolla", "morron", "jamon", "huevo", "queso"],
        "texto_ingredientes": """- 3 papas medianas
- 2 cdas cebolla de verdeo, 1 cda cebolla común, 1 cda morrón
- 2 fetas jamón cocido
- 5 huevos
- 2 cdas queso rallado""",
        "pasos": """1. Pelar y cortar las papas muy chiquitas. Picar verduras.
2. Poner en el molde de freidora con aceite en spray. Cocinar a 180° por 18 min revolviendo.
3. A mitad de cocción sumar el jamón picado.
4. Mezclar huevos con queso y sal. Incorporar las verduras listas y dejar reposar 5 min.
5. Cocinar en molde rociado a 175° por 17 minutos."""
    },
    {
        "titulo": "Papas Rellenas Deliciosas",
        "ingredientes_clave": ["papa", "pollo", "zanahoria", "cebolla", "morron", "ajo", "huevo", "queso"],
        "texto_ingredientes": """- 6 papas medianas
- 2 pata muslo
- 2 zanahorias, 4 cebollas, 1/2 morrón, 2 ajos
- 3 huevos (2 duros, 1 crudo)
- 300 g queso cremoso""",
        "pasos": """1. Hervir las papas con piel. Hervir el pollo.
2. Hervir 2 huevos.
3. Trozar el pollo cocido. Saltear verduras picadas y mezclar con el pollo y huevos duros picados.
4. Ahuecar las papas (ya blandas).
5. Rellenar las papas con la mezcla. Meter al horno, coronar con queso y rociar con el huevo crudo.
6. Cocinar hasta dorar."""
    },
    {
        "titulo": "Pan de Carne con Verduras Horneadas",
        "ingredientes_clave": ["carne", "huevo", "zanahoria"],
        "texto_ingredientes": """- 500 gr carne picada
- 2 huevos
- 1 cda Provenzal, Orégano, Sal, Mostaza
- 1 Zanahoria (y más verduras a gusto)""",
        "pasos": """1. Hierve los huevos.
2. Mezcla la carne con provenzal, orégano, sal y mostaza. Distribuye plano, pon los huevos en el medio y enrolla.
3. Pon la carne en una asadera enaceitada.
4. Corta verduras en daditos, condimenta y pon en otra asadera.
5. Cocinar carne y verduras en horno a 180 grados por 40 minutos."""
    },
    {
        "titulo": "Albóndigas en Salsa de Zapallo Calabaza y Arroz",
        "ingredientes_clave": ["carne", "ajo", "morron", "cebolla", "galletitas", "leche", "maicena", "zapallo", "caldo", "arroz"],
        "texto_ingredientes": """- 800 g Carne picada
- 1 diente Ajo
- 1/4 unidad Morrón colorado
- 1/2 unidad Cebolla
- 50 g Restos de galletitas de agua
- 50 ml Leche
- 2 cucharadas Maicena
- 300 g Zapallo calabaza asado
- 1 litro Caldo
- Arroz blanco""",
        "pasos": """1. Pica ajo, morrón y cebolla. Mezcla con la carne picada en un bol.
2. Añade galletitas, leche, sal, pimienta y maicena. Mezcla bien y forma bolitas.
3. Licúa el zapallo asado con el caldo hasta obtener una salsa cremosa.
4. Vierte la salsa en una cacerola y lleva a ebullición.
5. Agrega las albóndigas, cocina hasta que hierva, baja el fuego y deja media hora hasta que la salsa reduzca."""
    },
    {
        "titulo": "Salteado de Pollo y Puerros con Arroz",
        "ingredientes_clave": ["arroz", "pollo", "puerro", "verdeo", "ajo", "morron", "vino", "crema de leche"],
        "texto_ingredientes": """- 4 jarritos de arroz
- 2 mitades pechugas pollo
- 3 varas de puerro
- 3 varas de verdeo
- 3 dientes ajo
- 1 pimiento rojo
- 1/2 vaso vino blanco
- 3 cucharadas de crema de leche""",
        "pasos": """1. Hervir el arroz y reservar.
2. Picar el pollo en cubos y dorar en wok. Retirar.
3. Picar pimiento, ajos, puerro, verdeo y cocinar en el wok.
4. Pasados 15 min unir verduras con el pollo, agregar vino blanco y reducir.
5. Agregar crema de leche y servir sobre el arroz."""
    },
    {
        "titulo": "Arroz Blanco Perfecto",
        "ingredientes_clave": ["arroz", "ajo"],
        "texto_ingredientes": """- 2 tazas arroz
- 2 1/2 tazas agua
- 1 ajo entero o picado""",
        "pasos": """1. Colocar el arroz y el agua en una cacerola.
2. Agregar aceite, sal y el ajo. Mezclar.
3. Tapar y fuego medio/bajo por 10 minutos.
4. Cuando el agua se consuma, bajar a mínimo, tapar con una bolsa limpia haciendo honguito, apagar el fuego y dejar 5 minutos más."""
    },
    {
        "titulo": "Carne al Wok con Arroz Blanco",
        "ingredientes_clave": ["carne", "cebolla", "morron", "ajo", "arroz", "salsa de soja", "vino"],
        "texto_ingredientes": """- 800 grs nalga o cuadrada
- 2 cebollas grandes
- 1 morrón mediano
- 3 dientes ajo
- 4 tacitas de arroz
- Salsa de soja, sal, pimienta, jengibre molido
- 100 ml vino blanco""",
        "pasos": """1. Filetear la carne y sellar en wok. Retirar.
2. Rehogar cebolla y morrón. Cuando transparenta, agregar ajos y vino.
3. Evaporar el alcohol e incorporar la carne. Condimentar a gusto.
4. Hervir el arroz y servir junto con la carne."""
    },
    {
        "titulo": "Pollo al curry con arroz blanco",
        "ingredientes_clave": ["arroz", "pollo", "crema de leche", "cebolla", "curry"],
        "texto_ingredientes": """- 2 tazas arroz
- 2 supremas de pollo
- 250 ml crema
- 1 cebolla
- a gusto Sal, pimienta, curry en polvo""",
        "pasos": """1. Hervir el arroz blanco, reservar.
2. Picar la cebolla y sofreírla en una olla hasta transparentar.
3. Agregar el pollo cubeteado y dorar.
4. Agregar condimentos y la crema."""
    },
    {
        "titulo": "Arroz blanco con Pollo frito",
        "ingredientes_clave": ["arroz", "ajo", "pollo", "morron"],
        "texto_ingredientes": """- 1 taza Arroz largo fino
- 2 1/2 tazas Agua
- Hoja laurel y un diente ajo
- Sal fina
- Para Freír: Aceite girasol
- 4 Pata de pollo
- Sal, pimienta, pimentón, perejil fresco
- 1 pedazo Morrón rojo""",
        "pasos": """1. En una ollita poner agua, hoja de laurel y ajo. Cuando rompa el hervor agregar el arroz.
2. Echar sal a gusto y revolver, cocinar unos minutos. Colocar la tapa y bajar el fuego.
3. Sacar el ajo y laurel. Arroz listo.
4. Para el pollo: En un wok poner aceite con pimentón, el morrón y perejil.
5. Condimentar las patas de pollo con sal y pimienta. Freír en pequeñas cantidades en aceite caliente."""
    },
    {
        "titulo": "Pollo a la Cazadora con Arroz Blanco",
        "ingredientes_clave": ["pollo", "cebolla", "zanahoria", "verdeo", "puerro", "morron", "ajo", "tomate", "pure de tomate", "arroz"],
        "texto_ingredientes": """- 3 Patas y Muslos
- 3 cebollas medianas
- 2 Zanahorias medianas
- 1 cebolla de Verdeo
- 1 Puerro
- 1/2 Morrón Colorado
- 2 Dientes Ajo
- 1 Tomate
- 1 Puré de Tomate
- Arroz""",
        "pasos": """1. Picar todas las verduras. Limpiar las patas y muslos sacando la piel.
2. En una olla profunda colocar aceite y dorar las presas de pollo. Retirar y reservar.
3. En la misma olla poner los vegetales duros (cebolla, zanahoria, morrón, verdeo, puerro). Cuando transparenta agregar ajos y tomate.
4. Salpimentar, agregar puré de tomate y cocinar 15 minutos.
5. Agregar las presas de pollo y cocinar a fuego medio 35-40 min.
6. Hervir el arroz con sal y aceite (o caldo). Servir el pollo sobre el arroz."""
    },
    {
        "titulo": "Hígado con arroz blanco",
        "ingredientes_clave": ["higado", "caldo", "cebolla", "morron", "arroz"],
        "texto_ingredientes": """- 3 bifes de hígado
- 1 caldo
- 1 cebolla
- 1/4 de ají morrón
- 1/4 de taza de arroz""",
        "pasos": """1. Cortamos los bifes al medio, los colocamos en el fondo de una cacerola junto con las verduras picadas y el caldo a fuego lento, unos 25 a 30 minutos.
2. Se hará una salsita espesa. Aparte cocinamos el arroz en abundante agua por 15 minutos.
3. Servimos todo junto."""
    },
    {
        "titulo": "Milanesas con Fideos, Queso y Salsa Blanca",
        "ingredientes_clave": ["milanesa", "fideo", "salsa blanca", "leche", "queso"],
        "texto_ingredientes": """- 6 U. Milanesas (carne o pollo)
- 1/2 Paquete Spaghetti
- 1 Sobre Polvo para Salsa Blanca
- 600 ml. Leche
- 1 Sobre Ajinomoto sabor Verdura
- Queso Cremoso
- Orégano, Nuez Moscada, Ají Molido Picante, Aceite, Pimienta""",
        "pasos": """1. Pincelar una placa para horno con aceite y colocar las milanesas.
2. En una olla mezclar el polvo de salsa blanca, la leche, saborizante, pimienta y nuez moscada. Revolvemos al fuego hasta que espese.
3. Hervir agua y cocinar los fideos. Al mismo tiempo cocinar las milanesas al horno.
4. Colar los fideos y mezclarlos con la salsa blanca.
5. Dar vuelta las milanesas doradas, colocarles encima fideos con salsa, fetas de queso cremoso, orégano y ají molido. Gratinar en el horno.
6. Emplatar."""
    },
    {
        "titulo": "Guiso de Fideos Moñito",
        "ingredientes_clave": ["carne", "chorizo", "panceta", "salchicha", "morron", "cebolla", "zanahoria", "verdeo", "apio", "ajo", "zapallo", "fideo", "arveja", "pure de tomate", "caldo"],
        "texto_ingredientes": """- 1 kg roast beef cortado en trocitos
- 2 chorizos, 200 g panceta, 2 salchichas parrilleras
- 1/2 ají verde, 1 cebolla grande, 1/2 ají rojo
- 1 zanahoria, 1 penca de verdeo, 1 penca de apio, 2 dientes ajo
- 1 rodaja calabacita
- 500 g fideos moñito, 1 lata de arvejas
- 500 g puré de tomate, caldo, condimentos""",
        "pasos": """1. Rehogar panceta. Retirar y dorar chorizos y salchichas. Retirar.
2. Dorar la carne en tandas y retirar.
3. Picar las verduras y ablandarlas en la misma sartén 10 min.
4. Pasar todo a una olla grande (carne, verduras, embutidos). Incorporar puré de tomate, caldo, agua y condimentos.
5. Cocinar semitapado 1.5 hs.
6. Agregar fideos y cocinar. Al final sumar las arvejas, apagar el fuego y dejar asentar."""
    },
    {
        "titulo": "Fideos con salsa",
        "ingredientes_clave": ["pure de tomate", "cebolla", "morron", "carne", "fideo"],
        "texto_ingredientes": """- 500 g Puré de tomate
- 1 cebolla
- 1/2 morrón rojo, 1/2 morrón verde
- Condimentos y sal a gusto
- 600 g Carne picada
- 1 paquete fideos (a gusto)""",
        "pasos": """1. Cortar la cebolla y los morrones en cubitos, rehogarlos en aceite.
2. Agregar la carne picada y condimentar.
3. Cuando la carne esté cocinada, incorporar el puré de tomate.
4. En una olla hervir agua y cocinar los fideos a gusto.
5. Colar los fideos, servir y agregar la salsa."""
    },
    {
        "titulo": "Tarta souflee de choclo",
        "ingredientes_clave": ["choclo", "huevo", "crema de leche", "queso", "tapa de tarta"],
        "texto_ingredientes": """- 2 latas de maíz cremoso amarillo
- 5 huevos
- 1 pote chico de crema
- 2 sobres queso rallado
- 5 fetas de queso de barra cortado en tiritas
- 1 sobre masa de tarta""",
        "pasos": """1. En un bol poner 2 latas de choclo 5 huevos y un pote de crema. Mixar todo quedará una crema
2. Agregaremos el queso rallado y 5 fetas de queso de barra cortado en tiritas mezclar todo
3. Enmantecar y forrar un molde de tarta con una de las hojas de masa volcar el relleno y tapar con la otra hoja de masa apretando los bordes para cerrar bien
4. Recortar los excedentes de la masa y llevar a horno hasta dorar."""
    },
    {
        "titulo": "Tarta de Manzana invertida",
        "ingredientes_clave": ["azucar", "manzana", "huevo", "leche", "harina"],
        "texto_ingredientes": """Caramelo:
- 3/4 taza Azúcar
- 2 manzanas grandes
Mezcla:
- 2 huevos
- 1 taza azúcar
- 1/2 taza aceite
- 1 taza leche
- 1 cucharadita Esencia de vainilla
- Ralladura de 1 limón
- 3 tazas harina leudante""",
        "pasos": """1. Enmantecar y enharinar el molde, poner azúcar, poner las manzanas y reservar. En un bol mezclar los huevos con el azúcar.
2. Agregar el aceite, mezclar, luego integrar la leche, esencia, ralladura.
3. Agregar la harina tamizada, mezclar. Agregar la mezcla al molde.
4. Cocinar en horno a 180° por 45 minutos aproximadamente.
5. Desmoldar en caliente para que no se pegue el caramelo."""
    },
    {
        "titulo": "Tarta salada de remolacha y queso cottage",
        "ingredientes_clave": ["almendra", "manteca", "huevo", "cebolla", "ajo", "remolacha", "queso crema", "queso"],
        "texto_ingredientes": """Masa:
- 150 g almendras molidas
- 30 g ghee casero o manteca
- 1 huevo
Relleno:
- 1 cda aceite de oliva
- 1 cebolla mediana
- 2 dientes ajo
- 3 huevos
- 3 (o 4) remolachas ya cocidas
- 3 cdas soperas colmadas de queso cottage
- 1 feta queso protein (aprox. 70 gramos)""",
        "pasos": """1. Mezclar ingredientes de la masa. Extender sobre asadera. Pinchar con tenedor. Llevar a horno medio 15 a 20 minutos.
2. Sofreír la cebolla y ajos. Picar las remolachas y agregarlas.
3. Batir los huevos con el cottage. Condimentar. Agregar el rehogado y mezclar. Agregar queso.
4. Agregar el relleno a la base y llevar nuevamente al horno, hasta dorar."""
    },
    {
        "titulo": "Tarta Invertida de Banana",
        "ingredientes_clave": ["huevo", "azucar", "banana", "harina"],
        "texto_ingredientes": """- 2 huevos
- 1/2 taza Azúcar
- 2 bananas
- 1/2 taza aceite
- 1 cucharadita Esencia de vainilla
- 1/2 taza Harina leudante
Caramelo:
- 1/2 taza Azúcar""",
        "pasos": """1. Caramelo: hacer el caramelo en sartén. Poner en fuente y arriba rodajas de banana.
2. Mezclar huevos y azúcar. Incorporar aceite y esencia.
3. Incorporar harina tamizada. (Si queda denso agregar leche).
4. Poner mezcla en molde y hornear a baño maría 120° por 55 minutos (o horno convencional).
5. Desmoldar en caliente."""
    },
    {
        "titulo": "Tarta de cebolla con masa de garbanzos",
        "ingredientes_clave": ["garbanzo", "harina", "cebolla", "huevo", "queso", "leche"],
        "texto_ingredientes": """Masa:
- 1 lata de garbanzos (o 200 grs cocidos)
- 3 cds aceite
- 4 cds aproximadamente harina
Relleno:
- 3 cebebollas
- 3 huevos
- 100 grs queso rallado
- 200 grs queso cremoso o mozzarella
- 4 cdas harina
- 100 cc leche""",
        "pasos": """1. Masa: mixear garbanzos con aceite y condimentos. Incorporar harina hasta formar masa.
2. Cortar cebolla en Juliana y rehogar.
3. En bol mezclar huevos, leche, harina. Agregar cebolla y quesos.
4. Forrar molde con la masa, volcar relleno y espolvorear queso. Cocinar en horno fuerte."""
    },
    {
        "titulo": "Relleno tarta de acelga",
        "ingredientes_clave": ["acelga", "morron", "cebolla", "queso crema", "huevo", "queso"],
        "texto_ingredientes": """- 3 huevos
- 1 cebolla
- 1/3 morrón rojo
- 3 paquetes acelga
- 3 cucharadas queso crema
- queso mantecoso
- ajo en polvo, pimentón dulce, ají molido, sal""",
        "pasos": """1. Hervir la acelga, escurrir bien y cortar.
2. Cortar bien chiquito el morrón y la cebolla y saltear hasta que estén cocidos.
3. Juntar la acelga con las verduras en un bol y añadir el queso crema.
4. Mezclar los huevos con los condimentos e incorporar al bol, agregar queso mantecoso."""
    },
    {
        "titulo": "Tarta toffee",
        "ingredientes_clave": ["crema de leche", "chocolate", "dulce de leche", "masa sable"],
        "texto_ingredientes": """- 139 g Crema de Leche
- 139 g Choco para derretir
- 400 g Dulce de Leche Repostero
- Masa sable""",
        "pasos": """1. Ganache: picar el chocolate. Calentar la crema hasta ebullición, volcar sobre el chocolate y reposar 4 min. Revolver hasta integrar.
2. Rellenar la masa sable con dulce de leche.
3. Volcar el ganache tibio sobre el dulce de leche. Dejar enfriar."""
    },
    {
        "titulo": "Masa para tartas (Sin Gluten)",
        "ingredientes_clave": ["premezcla sin gluten", "huevo", "leche"],
        "texto_ingredientes": """- 3 tazas premezcla sin gluten (o mezcla casera)
- 1 huevo
- 50 cc aceite
- 1 cdita sal, 1 cdita polvo de hornear
- Leche o agua c/n""",
        "pasos": """1. Mezclar ingredientes secos, agregar huevo y líquido de a poco hasta masa lisa.
2. Enmantecar y espolvorear asadera.
3. Estirar masa espolvoreando premezcla.
4. Cocinar en fuego intermedio con relleno a gusto."""
    },
    {
        "titulo": "Tarta de Atún",
        "ingredientes_clave": ["cebolla", "huevo", "ajo", "atun", "queso crema", "tapa de tarta", "queso"],
        "texto_ingredientes": """- 1 Masa de Tarta doble
- 2 Latas de Atún
- 2 Cebollas grandes
- 2 Dientes Ajo
- 2 Huevos
- 3 Cucharadas Queso Crema o Crema de Leche
- 200 gr Queso cremoso
- Condimentos a gusto""",
        "pasos": """1. Caramelizar cebolla en juliana. Hervir 1 huevo.
2. Agregar ajo picado a la cebolla y cocinar 4 min.
3. Agregar Atún y queso crema, condimentar. Retirar del fuego.
4. Agregar el huevo duro picado y el huevo crudo, mezclar.
5. Acomodar masa en fuente, esparcir relleno, poner queso cremoso y cerrar con la otra tapa.
6. Cocinar 35 min."""
    },
    {
        "titulo": "Tarta de brócoli y espinaca con mozzarella",
        "ingredientes_clave": ["brocoli", "espinaca", "verdeo", "huevo", "queso", "queso crema", "tapa de tarta"],
        "texto_ingredientes": """- 1 brócoli mediano
- 200 g espinaca fresca
- 4 cebollitas de verdeo
- 3 huevos grandes
- 125 g mozzarella rallada
- 100 g queso crema
- 1 masa para tarta""",
        "pasos": """1. Precalentá el horno a 200 °C.
2. Herví ramitos de brócoli por 5 min.
3. Incorporá espinaca y cebollita el último minuto.
4. Escurrí bien las verduras.
5. Mezclá verduras, huevos, mozzarella, queso crema y sal.
6. Forrá una tartera con la masa.
7. Volcá el relleno.
8. Repulgá los bordes y horneá 35-40 min."""
    },
    {
        "titulo": "Tarta de Atún con Base de Puré de Papa",
        "ingredientes_clave": ["papa", "morron", "cebolla", "tomate", "ajo", "atun", "aceituna", "huevo"],
        "texto_ingredientes": """- 6 Papas
- 1 Pimiento rojo
- 1 Cebolla, 1 Tomate, 1 Diente Ajo
- 2 Latas de Atún
- 100 grs Aceitunas verdes
- 4 Huevos
- Condimentos a gusto""",
        "pasos": """1. Hervir las papas con piel.
2. Pelar y aplastar dentro de un molde aceitado.
3. Hornear a 180° por 10 min.
4. Hervir 4 huevos, pelar y cortar en rodajas.
5. Sofreír cebolla, pimiento y ajo. Agregar atún, tomate, aceitunas y condimentos.
6. Colocar la mitad del relleno sobre la base, agregar huevos y terminar con el resto.
7. Hornear hasta dorar."""
    },
    {
        "titulo": "Tarta básica de jamón, queso y tomate",
        "ingredientes_clave": ["tapa de tarta", "jamon", "queso", "tomate", "huevo"],
        "texto_ingredientes": """- 1 tapa de pascualina
- jamón cocido
- queso fresco y rallado
- 2 tomates peritas chicos
- 2 huevos""",
        "pasos": """1. Cortar jamón.
2. Agregar queso en trocitos, tomate y huevos.
3. Sumar queso rallado.
4. Poner masa en asadera, volcar relleno y hacer repulgue.
5. Cocinar en horno hasta dorar."""
    },
    {
        "titulo": "Tarta de coco y dulce de leche",
        "ingredientes_clave": ["huevo", "azucar", "manteca", "harina", "dulce de leche", "coco"],
        "texto_ingredientes": """- 400 gramos dulce de leche
- 30 gramos manteca
- 80 gramos coco
- 250 gramos harina leudante
- 3 huevos
- 75 gramos azúcar""",
        "pasos": """1. Batir 1 huevo con azúcar. Incorporar manteca y harina leudante. Enfriar masa 20 min.
2. Estirar masa en molde y hornear a 180 °C por 20 min.
3. Cubrir base con dulce de leche.
4. Mezclar coco con 2 huevos, distribuir encima y hornear hasta dorar."""
    },
    {
        "titulo": "Tarta de hojas de remolacha y salsa blanca",
        "ingredientes_clave": ["tapa de tarta", "remolacha", "zanahoria", "cebolla", "morron", "huevo", "maicena", "leche", "queso"],
        "texto_ingredientes": """- 1 masa de tarta
- 1 atado de remolacha (las hojas)
- 2 zanahorias, 1 cebolla, 1/2 morrón
- 3 huevos duros
- Salsa blanca: 500 ml leche (o agua y leche en polvo), 2 cdas maicena
- Queso para derretir""",
        "pasos": """1. Hervir los huevos. Precocinar masa 5 min.
2. Lavar vegetales. Picar hojas y pencas de remolacha y cocinar al vapor.
3. Saltear cebolla, morrón y zanahoria rallada.
4. Combinar salsa blanca y salteado.
5. Poner huevo picado sobre la base, arriba el relleno y queso.
6. Cocinar hasta dorar."""
    },
    {
        "titulo": "Palmeritas con tapa de tarta",
        "ingredientes_clave": ["tapa de tarta", "manteca", "azucar"],
        "texto_ingredientes": """- 1 paquete tapa de tarta de hojaldre
- 50 gramos manteca
- 3 cucharadas azúcar""",
        "pasos": """1. Ablandar manteca y batir con azúcar.
2. Untar la mezcla en las tapas de tarta.
3. Enrollar de cada extremo y cortar.
4. Hornear 8-10 min de cada lado hasta dorar."""
    },
    {
        "titulo": "Tarta de Verdura con Masa Casera",
        "ingredientes_clave": ["harina", "zapallo", "zanahoria", "huevo", "acelga", "cebolla", "morron", "queso"],
        "texto_ingredientes": """Masa:
- 250g harina 000
- 65 cc Aceite, 100 cc agua caliente
Relleno:
- 1/2 zapallo, 2 zanahorias
- 3 huevos
- 1 paquete acelga
- 2 Cebollas, 1 morrón
- Queso cremoso""",
        "pasos": """1. Unir harina, aceite, sal y agua caliente. Enfriar masa.
2. Hervir zapallo y zanahoria. Hervir huevos.
3. Rehogar cebolla, morrón y acelga.
4. Unir ingredientes del relleno.
5. Estirar masa en tartera. Rellenar y tapar. Pincelar con yema y hornear 30/40 min."""
    },
    {
        "titulo": "Flan Caserito",
        "ingredientes_clave": ["leche", "huevo", "azucar"],
        "texto_ingredientes": """- 500 ml Leche
- 4 huevos
- 1/2 Taza azúcar
- Esencia de vainilla
- Azúcar para caramelo""",
        "pasos": """1. Preparar caramelo en el molde.
2. Batir huevos, azúcar, vainilla y sal. Incorporar leche.
3. Verter mezcla en el molde.
4. Cocinar a baño María en horno a 170°.
5. Enfriar y desmoldar."""
    },
    {
        "titulo": "Gelatina sabor tiramisú",
        "ingredientes_clave": ["leche", "yogurt", "gelatina", "cafe", "stevia"],
        "texto_ingredientes": """- 500 ml leche descremada
- 300 gr yogurt natural
- 14 g gelatina sin sabor
- 2 cucharadas café
- 2 cucharadas stevia""",
        "pasos": """1. Calentar leche, stevia, gelatina, 200g de yogurt y café revolviendo a fuego bajo.
2. Pasar a vasitos y enfriar toda la noche en heladera.
3. Coronar con el resto del yogurt y cacao."""
    },
    {
        "titulo": "Arroz con leche",
        "ingredientes_clave": ["leche", "arroz", "azucar"],
        "texto_ingredientes": """- 1 litro leche
- 12 cucharadas colmadas arroz
- 6 cucharadas colmadas azúcar""",
        "pasos": """1. Entibiar leche.
2. Incorporar arroz a fuego intermedio.
3. Colocar azúcar y mezclar hasta que esté listo el arroz."""
    },
    {
        "titulo": "Cheesecake de queso y dulce",
        "ingredientes_clave": ["galletitas", "manteca", "queso crema", "crema de leche", "huevo", "azucar", "membrillo"],
        "texto_ingredientes": """Base:
- 300 gr galletas lincoln
- 50 cc manteca
Cheesecake:
- 250 gr Queso crema
- 100 cc Crema de leche
- 4 Huevos, 75 gr Azúcar
- 250 gr Dulce de membrillo""",
        "pasos": """1. Triturar galletas con manteca. Cubrir molde y hornear 10 min.
2. Batir crema, queso crema, huevos y azúcar.
3. Ablandar membrillo con agua y colocar en el fondo de la tarta.
4. Sumar mezcla de cheesecake y hornear a 160° por 45 min."""
    },
    {
        "titulo": "Globi, postre de la Antigua Roma",
        "ingredientes_clave": ["ricota", "harina", "miel", "semillas"],
        "texto_ingredientes": """- 500 g Ricota
- 120 g Harina de trigo
- Aceite de oliva (para freír)
- Miel líquida
- Semillas de sésamo o amapola""",
        "pasos": """1. Escurrir ricota y mezclar con harina formando una masa. Formar bolitas.
2. Freír en aceite de oliva hasta dorar.
3. Servir tibias bañadas con miel y semillas."""
    },
    {
        "titulo": "Torta Tres Leches",
        "ingredientes_clave": ["huevo", "azucar", "harina", "leche", "crema de leche", "dulce de leche"],
        "texto_ingredientes": """- 2 huevos, 60 g azúcar, 60 g harina
Para embeber:
- 100 g leche en polvo (o normal)
- 100 g crema de leche
- 250 cc leche entera
Cubierta:
- Crema Chantilly
- Dulce de leche""",
        "pasos": """1. Batir huevos con azúcar a punto letra. Agregar harina.
2. Volcar en molde y hornear a 160° por 12-15 min.
3. Mezclar las leches y crema.
4. Pinchar el bizcochuelo y volcar el líquido. Enfriar.
5. Cubrir con Chantilly y dulce de leche."""
    },
    {
        "titulo": "Budín de pan",
        "ingredientes_clave": ["leche", "pan", "huevo", "azucar"],
        "texto_ingredientes": """- 1 litro leche
- 500 g pan duro
- 5 o 6 huevos
- 1 taza azúcar
- Vainilla y ralladura de limón/naranja
- Caramelo: 1.5 taza azúcar""",
        "pasos": """1. Remojar pan en leche.
2. Preparar caramelo y bañar el molde.
3. Desintegrar el pan remojado. Batir huevos, azúcar, esencias y mezclar con el pan.
4. Volcar en el molde y hornear a baño María por 1 hora.
5. Enfriar y desmoldar."""
    },
    {
        "titulo": "Crema Chantilly",
        "ingredientes_clave": ["crema de leche", "azucar"],
        "texto_ingredientes": """- 200 ml crema de leche (35% grasa)
- 1 o 2 cdas azúcar impalpable
- Vainilla""",
        "pasos": """1. Crema, varillas y bol bien fríos.
2. Batir crema a velocidad media, agregar azúcar y vainilla.
3. Batir hasta picos firmes."""
    },
    {
        "titulo": "Dulce de leche desde lata",
        "ingredientes_clave": ["leche condensada"],
        "texto_ingredientes": """- 2 latas leche condensada
- Agua abundante""",
        "pasos": """1. Retirar etiquetas de las latas.
2. Hervir sumergidas en agua por 2 o 3 horas. (No dejar que se queden sin agua).
3. Apagar fuego y dejar enfriar en la cacerola de un día para otro."""
    },
    {
        "titulo": "Postre estilo Serenito de dulce de leche",
        "ingredientes_clave": ["leche", "azucar", "maicena", "dulce de leche"],
        "texto_ingredientes": """- 500 ml leche
- 2 cdas azúcar
- 2 cdas maicena
- 4 cdas dulce de leche
- Vainilla""",
        "pasos": """1. Separar mitad de leche y mezclar con azúcar y maicena sin grumos.
2. Hervir la otra mitad de la leche.
3. Unir ambas leches a fuego mínimo sin dejar de batir.
4. Al hervir agregar dulce de leche y espesar.
5. Servir en vasos, tapar con film al contacto y enfriar."""
    },
    {
        "titulo": "Mousse de limón casera",
        "ingredientes_clave": ["huevo", "azucar", "leche", "maicena", "limon"],
        "texto_ingredientes": """- 3 Huevos (separar claras y yemas)
- 80 g Azúcar
- 200 ml Leche
- 20 g Maicena
- Jugo y ralladura de 2 limones""",
        "pasos": """1. Mezclar yemas, maicena y un poco de leche.
2. Calentar resto de leche con mitad del azúcar.
3. Agregar yemas y cocinar revolviendo hasta espesar.
4. Agregar jugo y ralladura. Enfriar.
5. Batir claras a nieve con el resto del azúcar.
6. Incorporar merengue a la crema con movimientos envolventes. Refrigerar."""
    },
    {
        "titulo": "Chocotorta Helada",
        "ingredientes_clave": ["queso crema", "helado", "galletitas", "leche"],
        "texto_ingredientes": """- 1 pote helado de dulce de leche
- 200 g queso untable
- 1 pote helado de chocolate
- 340 g chocolinas (galletas de chocolate)
- 100 ml leche""",
        "pasos": """1. Mezclar queso untable con helado de dulce de leche y enfriar.
2. Armar capas: helado de chocolate, galletitas mojadas en leche, helado de chocolate. Enfriar 15 min.
3. Agregar capa de la mezcla de dulce de leche y queso. Enfriar 15 min.
4. Repetir capas y enfriar por 3 horas mínimo."""
    },
    {
        "titulo": "Peras al vino tinto",
        "ingredientes_clave": ["pera", "vino", "azucar"],
        "texto_ingredientes": """- 8 peras
- 1 lt vino tinto
- 10 cdas azúcar
- 1 cdta canela""",
        "pasos": """1. Pelar peras y poner en cacerola con vino, azúcar y canela.
2. Hervir destapado. Luego tapar y cocinar 30 min girándolas.
3. Retirar peras y reducir la salsa a caramelo. Enfriar."""
    },
    {
        "titulo": "Postre de vainillas y limón",
        "ingredientes_clave": ["crema de leche", "leche condensada", "limon", "galletitas", "leche"],
        "texto_ingredientes": """- 24 vainillas
- Leche c/n
- 1 pote leche condensada
- 1 pote crema
- Jugo y ralladura de 2 limones""",
        "pasos": """1. Batir crema a medio punto, agregar leche condensada, jugo y ralladura de limón.
2. Remojar vainillas en leche y hacer capas de vainillas y crema en una fuente.
3. Refrigerar por tres horas."""
    }
]

# 2. SISTEMA DE CATEGORIZACIÓN SEMÁNTICA (Automático)
CATEGORIAS_MAP = {
    "🥩 Carnes y Proteínas": ["carne", "cerdo", "pollo", "milanesa", "chorizo", "panceta", "salchicha", "higado", "atun", "jamon"],
    "🧀 Lácteos y Huevos": ["huevo", "yogurt", "queso", "crema de leche", "leche", "queso crema", "dulce de leche", "manteca", "ricota", "leche condensada"],
    "🥦 Vegetales y Legumbres": ["papa", "cebolla", "aceituna", "ajo", "tomate", "zapallito", "zapallo", "zanahoria", "morron", "zucchini", "verdeo", "arveja", "choclo", "espinaca", "acelga", "remolacha", "garbanzo", "apio", "brocoli", "puerro", "pure de tomate"],
    "🍎 Frutas y Frutos Secos": ["kiwi", "limon", "frutilla", "nuez", "manzana", "banana", "pera", "coco", "almendra"]
}

# Extraemos los ingredientes únicos de la base de recetas
ingredientes_unicos = set()
for receta in RECETAS:
    for ing in receta["ingredientes_clave"]:
        ingredientes_unicos.add(ing)

# Armamos un diccionario agrupando por las categorías semánticas
INGREDIENTES_POR_CATEGORIA = {cat: [] for cat in CATEGORIAS_MAP.keys()}
INGREDIENTES_POR_CATEGORIA["🌾 Despensa y Otros"] = [] # Todo lo que no encaja va acá

for ing in sorted(list(ingredientes_unicos)):
    encontrado = False
    for cat, lista_keywords in CATEGORIAS_MAP.items():
        if ing in lista_keywords:
            INGREDIENTES_POR_CATEGORIA[cat].append(ing)
            encontrado = True
            break
    if not encontrado:
        INGREDIENTES_POR_CATEGORIA["🌾 Despensa y Otros"].append(ing)

# 3. LÓGICA DE BÚSQUEDA
def buscar_recetas(ingredientes_usuario):
    set_usuario = set(ingredientes_usuario)
    exactas = []
    casi_listas = []

    for receta in RECETAS:
        set_receta = set(receta["ingredientes_clave"])
        
        # Filtro estricto: al menos un ingrediente coincidente
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

# 4. INTERFAZ DE USUARIO Y DISEÑO GRÁFICO (CSS)
st.set_page_config(page_title="¿Qué cocino hoy?", page_icon="🍳")

# BLOQUE CSS COMPLETO
st.markdown("""
<style>
.stApp {
    background-color: #FDFBF5;
}

h1, h2, h3 {
    color: #1E3A14 !important;
}

.stMarkdown p, .stMarkdown li {
    color: #2F3324;
}

/* ESTILOS PARA LOS MULTISELECT CATEGORIZADOS */
div[data-testid="stMultiSelect"] label {
    color: #1E3A14 !important;
    font-size: 1.1rem;
    font-weight: bold;
    margin-top: 10px; /* Para separar un poco los campos */
}

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important; 
    border: 2px solid #4F6D23 !important; 
    border-radius: 8px !important;
}

div[data-baseweb="select"] input::placeholder {
    color: #7A8B6E !important;
}

div[data-baseweb="select"] input {
    color: #1E3A14 !important;
}

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

span[data-baseweb="tag"] svg {
    fill: #1E3A14 !important;
}

/* ESTILOS BOTÓN BÚSQUEDA */
div.stButton > button:first-child {
    background-color: #D22211 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px;
    font-weight: bold;
    padding: 0.6rem 1.2rem;
    transition: 0.3s;
    margin-top: 20px;
}

div.stButton > button:first-child:hover {
    background-color: #691410 !important;
    color: #FFFFFF !important;
}

/* BOTÓN DESPLEGABLE DE RECETAS */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary * {
    color: #1E3A14 !important; /* <--- Fuerza el verde oscuro en las letras y la flechita */
    font-weight: bold !important;
    background-color: #FDFBF5 !important; /* <--- Fondo crema */
}

[data-testid="stExpander"] summary {
    border: 2px solid #4F6D23 !important;
    border-radius: 6px !important;
}

/* CAJA DE TEXTO RECETAS Y PASOS */
div[data-testid="stExpanderDetails"] {
    background-color: #FFFFFF !important; 
    border: 2px solid #99A12D !important;
    border-top: none !important;
    border-radius: 0 0 6px 6px !important;
    padding: 1.5rem !important;
}

div[data-testid="stExpanderDetails"],
div[data-testid="stExpanderDetails"] * {
    color: #2F3324 !important; 
    background-color: transparent !important;
    font-family: "Helvetica", "Arial", sans-serif !important;
    white-space: pre-wrap !important;
}

div[data-testid="stExpanderDetails"] p strong,
div[data-testid="stExpanderDetails"] strong {
    color: #D22211 !important; 
    font-size: 1.1rem !important;
    text-transform: uppercase !important;
}

/* ESTILOS TÍTULOS Y AVISOS DE FALTANTES */
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


st.title("🍳 ¿Qué cocino hoy?")
st.write("Seleccioná los ingredientes separándolos por su categoría. (Asumimos que tenés sal, aceite, condimentos y agua).")

# CAMPOS DE SELECCIÓN POR CATEGORÍA
ingredientes_seleccionados_totales = []

for categoria, opciones_ingredientes in INGREDIENTES_POR_CATEGORIA.items():
    if opciones_ingredientes: # Solo mostramos la categoría si hay ingredientes adentro
        seleccion = st.multiselect(
            categoria, 
            options=opciones_ingredientes,
            placeholder=f"Elegí tus {categoria.split(' ')[1].lower()}..."
        )
        # Sumamos todo a una sola lista unificada para que el buscador haga lo suyo
        ingredientes_seleccionados_totales.extend(seleccion)

if st.button("Buscar Recetas"):
    if ingredientes_seleccionados_totales:
        exactas, casi_listas = buscar_recetas(ingredientes_seleccionados_totales)
        
        if exactas:
            st.success("¡Tenés todo para preparar esto! 🍽️")
            for r in exactas:
                st.markdown(f"<div class='titulo-exacta'>{r['titulo']}</div>", unsafe_allow_html=True)
                
                with st.expander("Ver receta"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.write("") 
                
        if casi_listas:
            st.info("Te faltan hasta 2 ingredientes para estas recetas: 🛒")
            for r in casi_listas:
                st.markdown(f"<div class='titulo-parcial'>{r['titulo']}</div>", unsafe_allow_html=True)
                
                faltantes_str = ", ".join(r["ingredientes_faltantes"])
                st.markdown(f"<div class='alerta-faltantes'>🛒 <strong>Te falta/n:</strong> {faltantes_str}</div>", unsafe_allow_html=True)
                
                with st.expander("Ver receta"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.write("") 
                
        if not exactas and not casi_listas:
            st.warning("No encontramos recetas que coincidan con lo que elegiste. ¡Probá seleccionando algo más!")
            
    else:
        st.error("Por favor, seleccioná al menos un ingrediente de cualquier categoría.")
