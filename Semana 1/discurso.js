let x = "Hola gente de MinTIC 2022"
console.log(x)

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

lambetazo_select = lambetazo[Math.floor(Math.random()*(lambetazo.length))]
pot_marranos_select = potenciales_marranos[Math.floor(Math.random()*(potenciales_marranos.length))]
condicion_select = condicion[Math.floor(Math.random()*(condicion.length))]
compromiso_select = compromiso[Math.floor(Math.random()*(compromiso.length))]
ilusion_select = ilusion_guerrerista[Math.floor(Math.random()*(ilusion_guerrerista.length))]
promesa_select = promesa[Math.floor(Math.random()*(promesa.length))]
beneficio_select = beneficio_populista[Math.floor(Math.random()*(beneficio_populista.length))]
votos_select = dependiendo_votos[Math.floor(Math.random()*(dependiendo_votos.length))]

console.log("Discurso: " + lambetazo_select + " " + pot_marranos_select + " " + condicion_select + 
    " " + compromiso_select + " "+ ilusion_select + " " + beneficio_select + " " + votos_select + ".")