import streamlit as st

# 1. DICCIONARIO DE SINÓNIMOS
SINONIMOS = {
    "huevos": "huevo",
    "yogur": "yogurt",
    "yoghurt": "yogurt",
    "papas": "papa",
    "cebollas": "cebolla",
    "tomates": "tomate",
    "morrones": "morron",
    "pimiento": "morron",
    "pimientos": "morron",
    "aji": "morron",
    "ají": "morron",
    "ajies": "morron",
    "limones": "limon",
    "quesos": "queso",
    "zapallitos": "zapallito",
    "calabaza": "zapallo",
    "zapallos": "zapallo",
    "carnes": "carne",
    "lenteja": "lentejas",
    "arroses": "arroz",
    "ajos": "ajo",
    "galletita": "galletitas",
    "puerros": "puerro",
    "verdeos": "verdeo",
    "crema": "crema de leche",
    "suprema": "pollo",
    "supremas": "pollo",
    "pata": "pollo",
    "patas": "pollo",
    "muslo": "pollo",
    "muslos": "pollo",
    "fideos": "fideo",
    "spaghetti": "fideo",
    "moñito": "fideo",
    "moñitos": "fideo",
    "hígado": "higado",
    "milanesas": "milanesa",
    "salchichas": "salchicha",
    "arvejas": "arveja"
}

# 2. BASE DE DATOS CON LAS RECETAS COMPLETAS (Sin perejil en claves)
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
    }
]

# 3. LÓGICA DE BÚSQUEDA (Actualizada para hasta 2 faltantes)
def buscar_recetas(ingredientes_usuario):
    lista_cruda = [i.strip().lower() for i in ingredientes_usuario.split(",")]
    
    lista_normalizada = []
    for ing in lista_cruda:
        ing_corregido = SINONIMOS.get(ing, ing)
        lista_normalizada.append(ing_corregido)
        
    set_usuario = set(lista_normalizada)
    
    exactas = []
    casi_listas = []

    for receta in RECETAS:
        set_receta = set(receta["ingredientes_clave"])
        
        faltantes = set_receta - set_usuario
        cantidad_faltantes = len(faltantes)
        
        if cantidad_faltantes == 0:
            exactas.append(receta)
        elif cantidad_faltantes <= 2:
            # Si le faltan 1 o 2 ingredientes, los guardamos juntos
            receta_con_faltantes = receta.copy()
            receta_con_faltantes["ingredientes_faltantes"] = list(faltantes)
            casi_listas.append(receta_con_faltantes)

    return exactas, casi_listas

# 4. INTERFAZ DE USUARIO
st.set_page_config(page_title="¿Qué cocino hoy?", page_icon="🍳")

st.title("🍳 ¿Qué cocino hoy?")
st.write("Escribí los ingredientes que tenés a mano.")

ingredientes_input = st.text_input(
    "Tus ingredientes (separados por coma):", 
    placeholder="ej: papa, huevo, fideo, milanesa"
)

if st.button("Buscar Recetas"):
    if ingredientes_input:
        exactas, casi_listas = buscar_recetas(ingredientes_input)
        
        if exactas:
            st.success("¡Tenés todo para preparar esto! 🍽️")
            for r in exactas:
                st.subheader(r["titulo"])
                
                with st.expander("📖 Ver receta completa"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.divider()
        else:
            if not casi_listas:
                st.error("No encontramos nada exacto con esos ingredientes.")
        
        if casi_listas:
            st.info("Te faltan unos ingredientes para estas recetas: 🛒")
            for r in casi_listas:
                st.subheader(r["titulo"])
                faltantes_str = ", ".join(r["ingredientes_faltantes"])
                st.warning(f"**Te falta/n:** {faltantes_str}")
                
                with st.expander("📖 Ver receta completa"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.divider()
                
        if not exactas and not casi_listas:
            st.warning("No hay coincidencias cercanas. ¡Probá agregando más ingredientes!")
            
    else:
        st.error("Por favor, ingresá al menos un ingrediente.")
