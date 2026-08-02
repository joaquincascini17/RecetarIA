import streamlit as st
import random

# ==========================================
# 1. BASE DE DATOS DE RECETAS
# ==========================================
RECETAS = [
    # --- TUS RECETAS ORIGINALES ACTUALIZADAS CON "tipo" ---
    {
        "titulo": "Pastel de Papa con Aceitunas",
        "ingredientes_clave": ["carne", "papa", "aceituna", "cebolla", "huevo"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 500 gramos carne\n- 4 papas grandes\n- 1 puñado aceitunas\n- 1 cebolla chica colorada\n- 1 cebolla chica común\n- 2 huevos duros\n- A gusto condimentos",
        "pasos": "1. Cocinar carne con cebollas.\n2. Hervir papas y hacer puré.\n3. En un molde armar capa de puré, carne con huevo y aceitunas, y capa de puré.\n4. Gratinar al horno."
    },
    {
        "titulo": "Guiso de Carne y Papa",
        "ingredientes_clave": ["ajo", "cebolla", "carne", "papa", "tomate"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 3 dientes ajo\n- 1 cebolla\n- 500 grs carne\n- 2 papas\n- 1 lata de tomate",
        "pasos": "1. Picar y rehogar ajo y cebolla.\n2. Sellar carne.\n3. Agregar tomate, papas en cubos y agua.\n4. Cocinar hasta reducir."
    },
    {
        "titulo": "Milanesa de Cerdo",
        "ingredientes_clave": ["cerdo", "huevo", "ajo", "pan rallado"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 1,5 kg carne de cerdo\n- 6 huevos\n- Ajo, pan rallado, perejil",
        "pasos": "1. Pasar la carne por huevo con ajo y perejil, luego por pan rallado.\n2. Freír en aceite caliente."
    },
    {
        "titulo": "Tortilla de Papa Fit",
        "ingredientes_clave": ["papa", "huevo"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 4 Papas\n- 5 Huevos\n- Condimentos",
        "pasos": "1. Hervir papas en cubos.\n2. Batir huevos y mezclar con papas.\n3. Cocinar vuelta y vuelta en sartén aceitada."
    },
    {
        "titulo": "Helado Cremoso de Frutas",
        "ingredientes_clave": ["kiwi", "yogurt"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": "- Kiwis\n- Yogurt natural\n- Edulcorante",
        "pasos": "1. Pelar frutas.\n2. Mixear con yogurt y edulcorante.\n3. Congelar."
    },
    {
        "titulo": "Zapallitos Rellenos",
        "ingredientes_clave": ["zapallito", "zanahoria", "cebolla", "morron", "ajo", "carne", "huevo", "queso"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 6 zapallitos\n- Zanahoria, cebollas, morrón, ajo\n- 1/2 kg carne picada\n- Huevo, queso cremoso",
        "pasos": "1. Hervir zapallitos y ahuecar.\n2. Saltear verduras y carne.\n3. Rellenar, coronar con queso y hornear."
    },
    {
        "titulo": "Tarta de Zucchini con Base de Papa Dorada",
        "ingredientes_clave": ["papa", "zucchini", "huevo", "queso", "cebolla", "morron"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 2 papas\n- 3 zucchinis\n- 5 huevos\n- Queso, cebolla, morrón",
        "pasos": "1. Armar base con rodajas de papa al horno.\n2. Rellenar con vegetales rehogados y huevo.\n3. Gratinar con queso."
    },
    {
        "titulo": "Salteado de Pollo y Puerros con Arroz",
        "ingredientes_clave": ["arroz", "pollo", "puerro", "verdeo", "ajo", "morron", "vino", "crema de leche"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Arroz\n- Pollo, puerro, verdeo, ajo, morrón\n- Vino blanco, crema de leche",
        "pasos": "1. Hervir arroz.\n2. Saltear pollo y vegetales.\n3. Desglasar con vino, agregar crema y servir."
    },
    {
        "titulo": "Tarta Invertida de Banana",
        "ingredientes_clave": ["huevo", "azucar", "banana", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 2 huevos\n- Azúcar, bananas\n- Harina, aceite, esencia vainilla",
        "pasos": "1. Acaramelar molde y poner bananas.\n2. Batir líquidos y sumar harina.\n3. Hornear y desmoldar en caliente."
    },
    {
        "titulo": "Cheesecake de queso y dulce",
        "ingredientes_clave": ["galletitas", "manteca", "queso crema", "crema de leche", "huevo", "azucar", "membrillo"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Galletas, manteca\n- Queso crema, crema, huevos, membrillo",
        "pasos": "1. Armar base de galleta y manteca.\n2. Ablandar membrillo y poner en el fondo.\n3. Verter mezcla de quesos y hornear a 160° por 45 min."
    },
    {
        "titulo": "Chocotorta Helada",
        "ingredientes_clave": ["queso crema", "helado", "galletitas", "leche"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": "- Helado dulce de leche y chocolate\n- Queso crema, galletas de chocolate, leche",
        "pasos": "1. Mezclar queso crema con helado de DDL.\n2. Intercalar capas de helado, galletas mojadas y mezcla de DDL.\n3. Congelar."
    },
    
    # --- NUEVAS RECETAS AGREGADAS ---
    {
        "titulo": "Galletas de naranja",
        "ingredientes_clave": ["huevo", "azucar", "harina", "aceite", "naranja"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 1 huevo\n- 100 gr azúcar\n- 300 gr harina leudante\n- 3 cdas aceite\n- Ralladura y jugo de naranja",
        "pasos": "1. Batir huevo con azúcar, aceite y naranja.\n2. Incorporar harina y enfriar 10 min.\n3. Armar bolitas, aplastar y hornear 10-15 min a 180°."
    },
    {
        "titulo": "Galletas de Avena y coco sin Harina",
        "ingredientes_clave": ["avena", "coco", "huevo", "stevia", "aceite", "leche", "semillas"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 1 taza avena, 1 taza coco\n- 1 huevo, edulcorante\n- 5 cdas aceite, 1/2 taza leche\n- Mix semillas",
        "pasos": "1. Mezclar líquidos y edulcorante.\n2. Agregar avena, coco y semillas.\n3. Armar galletas y hornear 15-20 min a 180°."
    },
    {
        "titulo": "Galletas de avena con chips",
        "ingredientes_clave": ["avena", "harina", "azucar", "aceite", "huevo", "chocolate"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 115 g avena\n- 50 g harina, 75 g azúcar\n- 50 ml aceite, 1 huevo\n- Chips de chocolate",
        "pasos": "1. Batir huevo y azúcar. Incorporar secos y aceite.\n2. Enfriar 30 min.\n3. Armar bolitas y hornear a 170°."
    },
    {
        "titulo": "Galletas cerealitas caseras",
        "ingredientes_clave": ["semillas", "harina", "avena", "aceite"],
        "tipo": "Salado", "celiaco": False, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 150 gr mix semillas\n- 3 tazas harina integral\n- 1 taza avena\n- Aceite oliva, sal, polvo hornear",
        "pasos": "1. Hidratar semillas.\n2. Mezclar con harina, avena, aceite y sal.\n3. Estirar fino, cortar y hornear 20 min."
    },
    {
        "titulo": "Galletas Bolas de Chocolate y Chips",
        "ingredientes_clave": ["manteca", "azucar", "huevo", "harina", "chocolate"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 100 grs manteca\n- Azúcar blanca y negra\n- Huevo, harina, chips de chocolate",
        "pasos": "1. Unir todo. Hacer bolas de 30 grs.\n2. Congelar y hornear 15 min a 180°."
    },
    {
        "titulo": "Cookies NYC",
        "ingredientes_clave": ["harina", "manteca", "azucar", "huevo", "chocolate"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Harina, bicarbonato\n- Manteca, azúcar, 2 huevos\n- 200 gr chocolate o chips",
        "pasos": "1. Cremar manteca y azúcar. Agregar huevos.\n2. Incorporar secos y chips.\n3. Congelar bolas 30 min y hornear 9-11 min a 190°."
    },
    {
        "titulo": "Galletas al limón",
        "ingredientes_clave": ["azucar", "limon", "aceite", "huevo", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 100 g azúcar, limón\n- 100 ml aceite, 1 huevo\n- 200 g harina, polvo hornear",
        "pasos": "1. Unir azúcar y ralladura. Sumar jugo, aceite y huevo.\n2. Agregar harina, hacer un chorizo y congelar 40 min.\n3. Cortar y hornear."
    },
    {
        "titulo": "Galletas de Queso Sin TACC",
        "ingredientes_clave": ["queso", "premezcla", "aceite", "manteca"],
        "tipo": "Salado", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 100 g queso fresco en cubos\n- Premezcla c/n\n- Aceite o manteca, sal",
        "pasos": "1. Mezclar queso, materia grasa y sal. Sumar premezcla.\n2. Enfriar, estirar y cortar.\n3. Hornear 10-15 min a 180°."
    },
    {
        "titulo": "Galletas marineras",
        "ingredientes_clave": ["harina", "levadura", "aceite"],
        "tipo": "Salado", "celiaco": False, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 300 grs harina\n- Sal, levadura, agua tibia\n- 50 cc aceite, vinagre",
        "pasos": "1. Mezclar todo y amasar.\n2. Hacer bollos, estirar finos sobre harina de maíz.\n3. Hornear fuerte hasta dorar."
    },
    {
        "titulo": "Galletas Proteicas de soja",
        "ingredientes_clave": ["harina de soja", "harina", "stevia", "aceite"],
        "tipo": "Dulce", "celiaco": False, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Harina de soja, harina integral\n- Edulcorante, aceite, agua",
        "pasos": "1. Amasar todos los ingredientes.\n2. Dar forma y hornear hasta que hagan piso."
    },
    {
        "titulo": "Pepas saludables de avena",
        "ingredientes_clave": ["avena", "harina de coco", "stevia", "chia", "limon", "mermelada"],
        "tipo": "Dulce", "celiaco": True, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 1 tz avena, 1 tz harina de coco\n- Stevia, chia, ralladura de limón, agua\n- Mermelada",
        "pasos": "1. Integrar masa y formar pepas.\n2. Rellenar el centro con mermelada.\n3. Hornear 35-40 min."
    },
    {
        "titulo": "Galletas caseras clásicas",
        "ingredientes_clave": ["manteca", "azucar", "huevo", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- 100 g manteca\n- ½ taza azúcar\n- 1 huevo, harina c/n",
        "pasos": "1. Cremar manteca y azúcar. Sumar huevo.\n2. Integrar harina, hacer bolitas y aplastar.\n3. Hornear 10-12 min a 180°."
    },
    {
        "titulo": "Galletas de jengibre",
        "ingredientes_clave": ["harina", "azucar", "manteca", "huevo", "leche", "limon"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Harina, azúcar, manteca, huevo, leche\n- Jengibre, canela, nuez moscada\n- Glaseado: limón, clara, azúcar impalpable",
        "pasos": "1. Mezclar húmedos y secos. Unir todo.\n2. Estirar, cortar y hornear 10 min a 180°.\n3. Decorar con el glaseado."
    },
    {
        "titulo": "Cookies de chocolate amargo",
        "ingredientes_clave": ["mani", "azucar", "huevo", "leche", "avena", "almendra", "coco", "chocolate"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Pasta de maní, azúcar, huevo, leche\n- Avena, harina de almendras, coco\n- Chocolate amargo picado",
        "pasos": "1. Batir pasta de maní con azúcar y húmedos.\n2. Mezclar secos y chocolate, unir todo.\n3. Enfriar, formar esferas y hornear a 160° por 15 min."
    },
    {
        "titulo": "Cheesecake Oreo",
        "ingredientes_clave": ["galletitas", "manteca", "azucar", "queso crema", "crema de leche", "leche"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": "- Oreos, manteca\n- Queso crema, crema de leche, leche en polvo\n- Gelatina sin sabor",
        "pasos": "1. Base de Oreos y manteca (enfriar).\n2. Batir quesos, cremas y endulzante.\n3. Sumar gelatina hidratada, mezclar y rellenar. Heladera 6 hs."
    },
    {
        "titulo": "Torta de chocolate humeda",
        "ingredientes_clave": ["huevo", "azucar", "aceite", "leche", "harina", "cacao", "chocolate", "manteca"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Huevo, azúcar, aceite, leche\n- Harina, cacao, chocolate picado\n- Buttercream: manteca, azúcar impalpable, cacao",
        "pasos": "1. Batir líquidos y sumar secos tamizados.\n2. Hornear a 170° por 35 min.\n3. Cubrir con buttercream batido."
    },
    {
        "titulo": "Torta Matera con Crema Pastelera",
        "ingredientes_clave": ["huevo", "azucar", "maicena", "leche", "aceite", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Pastelera: huevo, azúcar, maicena, leche\n- Bizcocho: huevos, azúcar, aceite, leche, harina leudante",
        "pasos": "1. Hacer pastelera al fuego y enfriar.\n2. Batir bizcochuelo a punto letra y sumar secos.\n3. Volcar en molde, decorar enrejado con pastelera y hornear 40 min."
    },
    {
        "titulo": "Torta de Nuez",
        "ingredientes_clave": ["huevo", "azucar", "nuez", "dulce de leche", "crema de leche"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 4 huevos, azúcar\n- 300 gr nueces\n- Dulce de leche, crema chantilly",
        "pasos": "1. Batir yemas y claras por separado. Mezclar envolvente con nueces trituradas.\n2. Hornear 30 min a 170°.\n3. Decorar con DDL y crema."
    },
    {
        "titulo": "Torta Húngara",
        "ingredientes_clave": ["harina", "azucar", "huevo", "manteca", "leche", "coco"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina, azúcar, huevos, levadura, leche\n- Manteca, coco rallado",
        "pasos": "1. Armar masa leudada con manteca.\n2. Estirar, rellenar con manteca, azúcar y coco, enrollar.\n3. Leudar y hornear 35 min."
    },
    {
        "titulo": "Torta de manzana a la sartén (Apta diabéticos)",
        "ingredientes_clave": ["almendra", "huevo", "manzana", "stevia", "aceite", "leche"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina de almendras, polvo hornear\n- Huevo, leche, aceite, edulcorante\n- Manzana",
        "pasos": "1. Rallar manzana e integrar con la masa.\n2. Volcar en sartén, decorar con láminas de manzana.\n3. Cocinar vuelta y vuelta."
    },
    {
        "titulo": "Torta rápida Sin TACC",
        "ingredientes_clave": ["huevo", "leche", "aceite", "premezcla", "dulce de leche"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 4 huevos, 200 cc leche, aceite\n- Premezcla sin TACC\n- Relleno: DDL o pasta de maní",
        "pasos": "1. Batir líquidos e integrar premezcla.\n2. Hornear 50 min a 160°.\n3. Rellenar y decorar."
    },
    {
        "titulo": "Torta de mermelada en taza",
        "ingredientes_clave": ["harina", "azucar", "huevo", "leche", "aceite", "mermelada"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina leudante, azúcar, huevo\n- Leche, aceite\n- Mermelada",
        "pasos": "1. Batir líquidos y secos en la taza.\n2. Sumar mermelada y mezclar apenas.\n3. Microondas por 3 min aprox."
    },
    {
        "titulo": "Torta Tres Leches (Versión Rápida)",
        "ingredientes_clave": ["huevo", "azucar", "harina", "leche", "crema de leche", "dulce de leche"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Bizcochuelo clásico (huevo, azúcar, harina)\n- Líquido: Leche en polvo, crema, leche entera\n- Chantilly, DDL",
        "pasos": "1. Hornear bizcochuelo.\n2. Pinchar y bañar con mezcla de leches.\n3. Decorar con crema y DDL."
    },
    {
        "titulo": "Brigadeiro para cubierta de tortas",
        "ingredientes_clave": ["leche condensada", "cacao", "crema de leche", "manteca", "chocolate"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 1 lata leche condensada\n- 70 grs cacao, 100 cc crema\n- 75 grs manteca, chips chocolate",
        "pasos": "1. Poner todo en cacerola.\n2. Hervir a fuego bajo y enfriar."
    },
    {
        "titulo": "Torta de Chocolate en Flip/Sartén",
        "ingredientes_clave": ["huevo", "azucar", "aceite", "cacao", "leche", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Huevo, azúcar, aceite, leche\n- Cacao amargo, harina leudante",
        "pasos": "1. Mezclar todo.\n2. Volcar en flip/sartén enmantecada.\n3. Cocinar 15 min de cada lado."
    },
    {
        "titulo": "Torta negra o cara sucia",
        "ingredientes_clave": ["harina", "azucar", "leche", "levadura", "manteca"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina, azúcar, levadura, leche, agua\n- Manteca, Azúcar negra",
        "pasos": "1. Armar masa con levadura. Agregar manteca y amasar.\n2. Leudar y estirar.\n3. Cubrir con azúcar negra y hornear 15 min a 200°."
    },
    {
        "titulo": "Torta Brownie con Merengue",
        "ingredientes_clave": ["huevo", "azucar", "chocolate", "manteca", "harina", "nuez", "dulce de leche"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Huevos, azúcar, chocolate cobertura, manteca\n- Harina, nueces\n- DDL y Merengue suizo",
        "pasos": "1. Unir manteca y choco derretidos a los huevos.\n2. Sumar secos y hornear a 180° por 30 min.\n3. Cubrir con DDL y merengue batido a baño maría."
    },
    {
        "titulo": "Torta Rusa",
        "ingredientes_clave": ["harina", "azucar", "grasa", "levadura", "manteca"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina, azúcar, sal, grasa, levadura\n- Dulce de caramelo (agua, azúcar, harina)\n- Cubierta arenada (manteca, harina, azúcar)",
        "pasos": "1. Armar masa y estirar en molde.\n2. Rellenar con el dulce espeso de caramelo.\n3. Cubrir con el arenado y hornear."
    },
    {
        "titulo": "Torta Capri Sin TACC",
        "ingredientes_clave": ["manteca", "azucar", "huevo", "limon", "almendra"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Manteca, azúcar, huevos, limón\n- Harina de almendras, fécula de maíz",
        "pasos": "1. Batir yemas con manteca. Sumar secos y limón.\n2. Incorporar claras a nieve.\n3. Hornear 40 min a 170°."
    },
    {
        "titulo": "Torta de Yogur y Mermelada",
        "ingredientes_clave": ["huevo", "limon", "azucar", "aceite", "yogurt", "mermelada", "harina"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Huevos, azúcar, aceite, yogur\n- Harina leudante, mermelada, limón",
        "pasos": "1. Batir húmedos e integrar harina.\n2. Volcar la mitad en molde, vetear con mermelada, cubrir con el resto.\n3. Hornear 25 min."
    },
    {
        "titulo": "Torta Kuchen Alemana",
        "ingredientes_clave": ["harina", "manteca", "azucar", "huevo", "queso", "yogurt", "frutos rojos"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Base: Harina, manteca, azúcar, huevo\n- Relleno: Queso crema, yogur (o quark), huevo, azúcar, maicena\n- Frutos rojos",
        "pasos": "1. Estirar base en molde.\n2. Mezclar relleno suavemente y volcar. Hundir frutos rojos.\n3. Hornear 40 min a 170°. Enfriar bien en heladera."
    },
    {
        "titulo": "Torta Vasca (Cheesecake Cremoso)",
        "ingredientes_clave": ["queso", "huevo", "azucar", "harina", "crema de leche"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 800 g Queso blanco\n- Huevos, azúcar, 30 g harina\n- Crema de leche",
        "pasos": "1. Batir todo junto.\n2. Volcar en molde forrado en papel manteca.\n3. Hornear a 220° por 35 min hasta tostar. Enfriar 4 hs."
    },
    {
        "titulo": "Crumble de manzana sin tacc",
        "ingredientes_clave": ["premezcla", "azucar", "manteca", "huevo", "manzana"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Premezcla, azúcar, manteca pomada, huevo\n- Manzanas, canela\n- Arenado para cubrir",
        "pasos": "1. Armar masa base y estirar en placa.\n2. Cocinar manzanas en sartén con azúcar y canela.\n3. Cubrir con manzanas y arenado. Hornear 40 min a 180°."
    },
    {
        "titulo": "Crumble de manzana con avena",
        "ingredientes_clave": ["manzana", "avena", "azucar", "huevo", "manteca"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Manzanas verdes\n- Avena, azúcar, huevo, manteca\n- Canela, nueces",
        "pasos": "1. Acomodar manzanas en placa y pre-hornear.\n2. Mezclar avena, azúcar, huevo y volcar encima.\n3. Agregar manteca y hornear hasta dorar."
    },
    {
        "titulo": "Tartamisú",
        "ingredientes_clave": ["galletitas", "manteca", "queso crema", "crema de leche", "azucar", "cafe", "cacao"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": True, "sin_cubiertos": False,
        "texto_ingredientes": "- Base: Chocolinas, manteca\n- Crema: Queso crema, crema, azúcar\n- Relleno: Vainillas, café, cacao",
        "pasos": "1. Base de galletas trituradas. Enfriar.\n2. Batir quesos y crema a punto firme.\n3. Armar capas de crema, vainillas remojadas en café y crema. Espolvorear cacao."
    },
    {
        "titulo": "Cookies Tiramisú",
        "ingredientes_clave": ["manteca", "azucar", "huevo", "harina", "cacao", "queso crema", "crema de leche", "cafe"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Masa: Manteca, azúcar, huevo, harina, cacao, café\n- Topping: Queso crema, crema, azúcar impalpable",
        "pasos": "1. Armar masa de cookies y congelar en bolitas.\n2. Hornear 8 min a 180° y enfriar.\n3. Decorar con la crema batida en espiral y cacao."
    },
    {
        "titulo": "Tiramisú fit en microondas",
        "ingredientes_clave": ["huevo", "leche", "queso crema", "cafe", "cacao", "avena"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Masa: Huevo, leche en polvo, polvo hornear\n- Relleno: Queso crema, edulcorante, café, cacao",
        "pasos": "1. Hacer panquecito en microondas.\n2. Cortar, mojar en café y apilar con la crema.\n3. Decorar con cacao."
    },
    {
        "titulo": "Tiramisú con Avena y Banana",
        "ingredientes_clave": ["banana", "avena", "cafe", "leche", "stevia", "queso crema", "cacao"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Bananas, avena, café, leche\n- Queso crema o yogur griego, cacao",
        "pasos": "1. Mezclar puré de banana con secos y café.\n2. Hornear base 35 min.\n3. Enfriar y cubrir con queso crema y cacao."
    },
    {
        "titulo": "Budín fácil de banana",
        "ingredientes_clave": ["huevo", "harina", "aceite", "azucar", "banana"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 1 huevo, 2 bananas\n- Harina leudante, aceite, azúcar",
        "pasos": "1. Mixear líquidos y bananas.\n2. Integrar harina sin batir en exceso.\n3. Hornear 40 min."
    },
    {
        "titulo": "Budín de banana sin TACC",
        "ingredientes_clave": ["banana", "azucar", "huevo", "aceite", "yogurt", "nuez", "maicena"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Bananas maduras, azúcar, huevos, aceite\n- Yogur natural, fécula de maíz (maicena)\n- Nueces",
        "pasos": "1. Batir huevos, yogur y aceite. Sumar banana pisada.\n2. Integrar fécula tamizada y nueces.\n3. Hornear 50 min a 170°."
    },
    {
        "titulo": "Budín de mandarina",
        "ingredientes_clave": ["mandarina", "harina", "azucar", "aceite", "yogurt", "huevo"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Mandarinas (sin semillas)\n- Harina leudante, azúcar, aceite, yogur, huevos",
        "pasos": "1. Licuar gajos de mandarina y ralladura con aceite y yogur.\n2. Batir huevos y azúcar. Unir todo con harina.\n3. Hornear a 170°."
    },
    {
        "titulo": "Quinoa carrot cake muffins",
        "ingredientes_clave": ["quinoa", "huevo", "zanahoria", "pasa de uva", "nuez"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Quinoa cocida, huevos, zanahoria rallada\n- Edulcorante, especias (canela, etc.)\n- Pasas, nueces, polvo de hornear",
        "pasos": "1. Mixear quinoa, huevos y especias.\n2. Sumar zanahoria, nueces y pasas.\n3. Hornear en pirotines 30 min a 170°."
    },
    {
        "titulo": "Muffins de avena y moras en Air Fryer",
        "ingredientes_clave": ["huevo", "azucar", "aceite", "leche", "avena", "mermelada"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Huevos, azúcar, aceite, leche\n- Avena, mermelada de moras",
        "pasos": "1. Mezclar líquidos y agregar avena.\n2. Llenar moldes a la mitad, poner mermelada y cubrir.\n3. Freidora de aire 160° por 22 min."
    },
    {
        "titulo": "Ñoquis 100% integrales de papa",
        "ingredientes_clave": ["papa", "harina", "huevo"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- 1 kilo papas\n- 400 gr harina integral\n- 2 huevos",
        "pasos": "1. Hacer puré y dejar enfriar MUY bien.\n2. Unir con huevos y harina necesaria.\n3. Cortar y hervir hasta que floten."
    },
    {
        "titulo": "Ñoquis de papa con salsa bolognesa",
        "ingredientes_clave": ["papa", "huevo", "harina", "queso", "cebolla", "zanahoria", "morron", "carne"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Masa: papa, huevo, harina, queso\n- Salsa: carne vacuna, tomate, cebolla, zanahoria",
        "pasos": "1. Hervir salsa de estofado lento.\n2. Armar masa de ñoquis con puré frío.\n3. Hervir y salsear."
    },
    {
        "titulo": "Tortas Fritas clásicas",
        "ingredientes_clave": ["harina", "grasa"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Harina común\n- Grasa vacuna, sal, agua tibia",
        "pasos": "1. Mezclar harina y grasa derretida con salmuera.\n2. Amasar y estirar discos con agujero en medio.\n3. Freír en grasa o aceite."
    },
    {
        "titulo": "Buñuelos de Calabaza (Buñols)",
        "ingredientes_clave": ["calabaza", "harina", "azucar", "levadura"],
        "tipo": "Dulce", "celiaco": False, "vegano": True, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Puré de calabaza, agua tibia\n- Harina, levadura fresca, azúcar",
        "pasos": "1. Integrar todo y leudar 40 min.\n2. Freír bolitas en aceite caliente.\n3. Espolvorear con azúcar."
    },
    {
        "titulo": "Pastafrola rústica de membrillo",
        "ingredientes_clave": ["harina", "azucar", "huevo", "manteca", "leche", "membrillo"],
        "tipo": "Dulce", "celiaco": False, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina leudante, azúcar, huevos, manteca\n- Leche, membrillo",
        "pasos": "1. Arenar secos con manteca y líquidos.\n2. Forrar tartera, rellenar y hacer tiras.\n3. Hornear 25 min."
    },
    {
        "titulo": "Pastafrola con Masa de Harina de Arroz (Sin TACC)",
        "ingredientes_clave": ["harina", "maicena", "azucar", "huevo", "manteca", "membrillo", "dulce de leche"],
        "tipo": "Dulce", "celiaco": True, "vegano": False, "vegetariano": True, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Harina de arroz, maicena\n- Azúcar, huevo, manteca\n- Dulce de membrillo o DDL",
        "pasos": "1. Unir sin amasar y enfriar masa 1 hr.\n2. Estirar, rellenar y enrejar.\n3. Hornear 30 min."
    },
    {
        "titulo": "Empanadas de carne cortada a cuchillo",
        "ingredientes_clave": ["carne", "cebolla", "verdeo", "manteca", "huevo", "harina", "grasa"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Carne, cebolla blanca y de verdeo\n- Manteca, huevos duros\n- Masa: harina, grasa, salmuera",
        "pasos": "1. Rehogar cebollas y sellar carne. Enfriar guiso 1 día.\n2. Armar masa con grasa y estirar tapas.\n3. Rellenar, repulgar y hornear."
    },
    {
        "titulo": "Empanadas Greco-Árabes de Berenjena",
        "ingredientes_clave": ["pure de tomate", "tapa de tarta", "aceite", "ajo", "zanahoria", "morron", "cebolla", "berenjena", "carne", "leche", "harina", "manteca"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Berenjena, carne picada, cebolla, zanahoria\n- Especias (baharat), salsa tomate\n- Bechamel (manteca, leche, harina), tapas empanadas",
        "pasos": "1. Saltear vegetales y carne. Enfriar.\n2. Hacer bechamel.\n3. Rellenar empanadas con la mezcla y hornear."
    },
    {
        "titulo": "Empanadas de pollo, crema y champiñones",
        "ingredientes_clave": ["tapa de tarta", "pollo", "champiñon", "crema de leche", "cebolla", "verdeo", "vino", "limon"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": True,
        "texto_ingredientes": "- Pechugas, champiñones, crema\n- Cebollas, vino blanco, tapas de empanadas",
        "pasos": "1. Cocinar y desmenuzar pollo.\n2. Rehogar cebollas y champis, desglasar con vino, sumar crema.\n3. Enfriar relleno, armar y hornear."
    },
    {
        "titulo": "Sorrentinos con Masa de Zapallo",
        "ingredientes_clave": ["harina", "huevo", "aceite", "zapallo", "espinaca", "ricota", "cebolla", "morron", "queso", "carne", "zanahoria", "tomate"],
        "tipo": "Salado", "celiaco": False, "vegano": False, "vegetariano": False, "sin_coccion": False, "sin_cubiertos": False,
        "texto_ingredientes": "- Masa: Harina, huevos, puré de zapallo\n- Relleno: Espinaca, ricota, vegetales\n- Salsa: Bolognesa de carne",
        "pasos": "1. Hacer masa firme con puré de zapallo seco.\n2. Rellenar sorrentinos con ricota y espinaca.\n3. Hervir y servir con bolognesa."
    }
]

# ==========================================
# 2. CATEGORIZACIÓN SEMÁNTICA
# ==========================================
CATEGORIAS_MAP = {
    "Carnes y Proteínas": ["carne", "cerdo", "pollo", "milanesa", "chorizo", "panceta", "salchicha", "higado", "atun", "jamon", "bondiola", "matambre"],
    "Lácteos y Huevos": ["huevo", "yogurt", "queso", "crema de leche", "leche", "queso crema", "dulce de leche", "manteca", "ricota", "leche condensada", "mayonesa", "margarina", "grasa"],
    "Vegetales y Legumbres": ["papa", "cebolla", "cebolla de verdeo", "verdeo", "aceituna", "ajo", "tomate", "zapallito", "zapallo", "calabaza", "zanahoria", "morron", "zucchini", "arveja", "choclo", "espinaca", "acelga", "remolacha", "garbanzo", "apio", "brocoli", "puerro", "pure de tomate", "champiñon", "hongo", "rucula", "chaucha", "repollo", "lechuga", "palta", "berenjena"],
    "Frutas y Frutos Secos": ["kiwi", "limon", "frutilla", "nuez", "manzana", "banana", "pera", "coco", "almendra", "mani", "pasa de uva", "naranja", "mandarina", "frutos rojos"]
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
def buscar_recetas(ingredientes_usuario, filtros, tipo_sabor):
    set_usuario = set(ingredientes_usuario)
    exactas = []
    casi_listas = []

    for receta in RECETAS:
        # Filtro de tipo (Dulce/Salado)
        if tipo_sabor != "Todas":
            tipo_receta = receta.get("tipo", "Ambos")
            if tipo_receta != tipo_sabor and tipo_receta != "Ambos":
                continue

        # Filtros de dieta y método
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
/* SECCIÓN 1: ESTILOS GENERALES Y FONDO DE LA APP */
* { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; }
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

/* SECCIÓN 2: BANNERS HORIZONTALES POR CATEGORÍA CORREGIDOS */
div.element-container:nth-child(5) div[data-testid="stMultiSelect"] label { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://preview.colorkit.co/color/ffa07a.png?static=true'); background-size: cover; background-position: center; color: #FFFFFF !important; padding: 12px 20px; border-radius: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); font-size: 1.15rem; letter-spacing: 0.5px; }
div.element-container:nth-child(6) div[data-testid="stMultiSelect"] label { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://caseformaking.com/cdn/shop/products/Egg-Yolk-Yellow-Square_1946x.jpg?v=1653565859'); background-size: cover; background-position: center; color: #FFFFFF !important; padding: 12px 20px; border-radius: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); font-size: 1.15rem; letter-spacing: 0.5px; }
div.element-container:nth-child(7) div[data-testid="stMultiSelect"] label { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://preview.colorkit.co/color/556b2f.png?static=true'); background-size: cover; background-position: center; color: #FFFFFF !important; padding: 12px 20px; border-radius: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); font-size: 1.15rem; letter-spacing: 0.5px; }
div.element-container:nth-child(8) div[data-testid="stMultiSelect"] label { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://i.pinimg.com/736x/d3/cb/b4/d3cbb4fec5527f09f18abd6b3ec44e14.jpg'); background-size: cover; background-position: center; color: #FFFFFF !important; padding: 12px 20px; border-radius: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); font-size: 1.15rem; letter-spacing: 0.5px; }
div.element-container:nth-child(9) div[data-testid="stMultiSelect"] label { background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://www.colorhexa.com/b59b7c.png'); background-size: cover; background-position: center; color: #FFFFFF !important; padding: 12px 20px; border-radius: 8px; text-shadow: 1px 1px 4px rgba(0,0,0,0.9); font-size: 1.15rem; letter-spacing: 0.5px; }

/* SECCIÓN 3: COMPONENTES MULTISELECT Y TAGS ELEGIDOS */
div[data-baseweb="select"] > div { background-color: #FFFFFF !important; border: 2px solid #4F6D23 !important; border-radius: 8px !important; }
div[data-baseweb="select"] input::placeholder { color: #7A8B6E !important; }
div[data-baseweb="select"] input { color: #1E3A14 !important; }
ul[data-baseweb="menu"] { background-color: #FFFFFF !important; border: 1px solid #4F6D23 !important; }
li[data-baseweb="option"] { color: #1E3A14 !important; background-color: #FFFFFF !important; }
li[data-baseweb="option"]:hover, li[data-baseweb="option"][aria-selected="true"] { background-color: #99A12D !important; color: #FFFFFF !important; }
span[data-baseweb="tag"] { background-color: #FBB229 !important; border-radius: 6px !important; }
span[data-baseweb="tag"] span { color: #1E3A14 !important; font-weight: bold !important; }
span[data-baseweb="tag"] svg { fill: #1E3A14 !important; }

/* SECCIÓN 4: CHECKBOXES Y RADIO BUTTONS (FILTROS) */
div[data-testid="stCheckbox"] label, div[data-testid="stCheckbox"] label p { color: #2F3324 !important; font-weight: 600 !important; }
div[data-testid="stCheckbox"] { --primary-color: #ffa07a !important; }
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div, div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input[aria-checked="true"] + div { background-color: #ffa07a !important; border-color: #ffa07a !important; }
div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div svg, div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input:checked + div svg path, div[data-testid="stCheckbox"] label[data-baseweb="checkbox"] input[aria-checked="true"] + div svg { fill: #FFFFFF !important; stroke: #FFFFFF !important; color: #FFFFFF !important; }

/* Radio Buttons para Dulce/Salado */
div.row-widget.stRadio > div { background-color: #FDFBF5; padding: 10px 15px; border-radius: 8px; border: 2px solid #4F6D23; }
div.row-widget.stRadio > div { --primary-color: #ffa07a !important; } 

/* SECCIÓN 5: BOTONES */
div.stButton > button { border: none !important; border-radius: 8px; font-weight: bold; padding: 0.6rem 1.2rem; transition: 0.3s; width: 100%; }
div[data-testid="column"]:nth-of-type(1) div.stButton > button { background-color: #D22211 !important; color: #FFFFFF !important; }
div[data-testid="column"]:nth-of-type(1) div.stButton > button:hover { background-color: #691410 !important; }
div[data-testid="column"]:nth-of-type(2) div.stButton > button { background-color: #4F6D23 !important; color: #FFFFFF !important; }
div[data-testid="column"]:nth-of-type(2) div.stButton > button:hover { background-color: #1E3A14 !important; }

/* SECCIÓN 6: CAJAS DE RECETAS (EXPANDERS) */
[data-testid="stExpander"] summary { border: 2px solid #4F6D23 !important; border-radius: 6px !important; background-color: #FDFBF5 !important; }
[data-testid="stExpander"] summary, [data-testid="stExpander"] summary div, [data-testid="stExpander"] summary span { font-size: 0px !important; color: transparent !important; }
[data-testid="stExpander"] summary p { font-size: 1.15rem !important; color: #1E3A14 !important; font-weight: bold !important; margin: 0 !important; padding: 5px 0 !important; }
[data-testid="stExpander"] summary svg, [data-testid="stExpander"] summary [data-testid="stIconMaterial"], [data-testid="stExpander"] summary .material-symbols-rounded { display: none !important; }
div[data-testid="stExpanderDetails"] { background-color: #FFFFFF !important; border: 2px solid #99A12D !important; border-top: none !important; border-radius: 0 0 6px 6px !important; padding: 1.5rem !important; }
div[data-testid="stExpanderDetails"] * { color: #2F3324 !important; background-color: transparent !important; font-family: 'Georgia', 'Times New Roman', serif !important; white-space: pre-wrap !important; line-height: 1.6 !important; font-size: 1.05rem !important; }
div[data-testid="stExpanderDetails"] p strong, div[data-testid="stExpanderDetails"] strong { color: #D22211 !important; font-size: 1.1rem !important; text-transform: uppercase !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; }

/* SECCIÓN 7: AVISOS Y TITULARES */
.titulo-exacta { background-color: #4F6D23; color: #FFFFFF !important; padding: 12px; border-radius: 8px; font-size: 1.4rem; font-weight: bold; text-align: center; border: 2px solid #1E3A14; margin-bottom: 10px; }
.titulo-parcial { background-color: #DE770F; color: #FFFFFF !important; padding: 12px; border-radius: 8px; font-size: 1.4rem; font-weight: bold; text-align: center; border: 2px solid #691410; margin-bottom: 5px; }
.alerta-faltantes { background-color: #FDFBF5; color: #D22211 !important; border-left: 5px solid #D22211; border-radius: 4px; padding: 12px; font-size: 1.1rem; margin-bottom: 15px; }
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

# SECCIÓN DE FILTROS 
tipo_sabor = st.radio("Sabor buscado", ["Todas", "Dulce", "Salado"], horizontal=True)

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
    "celiaco": f_celiaco, "vegano": f_vegano, "vegetariano": f_vegetariano, 
    "sin_coccion": f_sin_coccion, "sin_cubiertos": f_sin_cubiertos
}

st.write("---")
col_btn1, col_btn2 = st.columns(2)

buscar_pulsado = False
azar_pulsado = False

with col_btn1:
    if st.button("Buscar Recetas"): buscar_pulsado = True
with col_btn2:
    if st.button("Elegir una al azar"): azar_pulsado = True

# ==========================================
# 6. MOSTRAR RESULTADOS
# ==========================================
if buscar_pulsado or azar_pulsado:
    if ingredientes_seleccionados_totales:
        exactas, casi_listas = buscar_recetas(ingredientes_seleccionados_totales, filtros_dict, tipo_sabor)
        
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
                
                with st.expander("🥘 Ver receta paso a paso 📖"):
                    st.markdown("**Ingredientes:**")
                    st.text(r["texto_ingredientes"])
                    st.markdown("**Paso a paso:**")
                    st.text(r["pasos"])
                st.write("") 
                
        if not exactas and not casi_listas:
            st.warning("No encontramos recetas que coincidan con lo que elegiste y tus filtros. ¡Probá cambiando las opciones!")
            
    else:
        st.error("Por favor, seleccioná al menos un ingrediente de cualquier categoría.")
