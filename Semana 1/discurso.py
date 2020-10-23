import random

lambetazo = ['querido', 'apreciados', 'distinguidos', 'honorables', 'estimados', 'respetados']
potenciales_marranos = ['compatriotas', 'conciudadanos', 'amigos', 'coterraneos', 'copartidarios', 'electores']
condicion = ['en mi gobierno', 'con su apoyo', 'siendo elegido', 'con su ayuda', 'si me siguen', 'durante mi mandato']
compromiso = ['voy a derrotar', 'venceré', 'eliminaré', 'acabaré', 'lucharé contra', 'combatiré']
ilusion_guerrerista = ['la violencia y', 'la delincuencia y', 'la corrupción y', 'la inflación y', 
    'la pobreza y', 'el desplazamiento y']
promesa = ['trabajaré por', 'garantizaré', 'protegeré', 'velaré por', 'promoveré', 'defenderé']
beneficio_populista = ['la educación', 'el empleo', 'la seguridad', 'la paz', 'la igualdad', 'la salud']
dependiendo_votos = ['del país', 'de la ciudad', 'de la comunidad', 'de la población', 
    'para toda la gente', 'de cada colombiano']

lambetazo_select = random.choice(lambetazo)
pot_marranos_select = random.choice(potenciales_marranos)
condicion_select = random.choice(condicion)
compromiso_select = random.choice(compromiso)
ilusion_select = random.choice(ilusion_guerrerista)
promesa_select = random.choice(promesa)
beneficio_select = random.choice(beneficio_populista)
votos_select = random.choice(dependiendo_votos)

print("Discurso: " + lambetazo_select + " " + pot_marranos_select + " " + condicion_select + 
    " " + compromiso_select + " "+ ilusion_select + " " + beneficio_select + " " + votos_select + ".")