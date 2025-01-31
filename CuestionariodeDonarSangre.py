# Preguntas

def ask_questions():
    questions = [
        '1. ¿Ha leído los folletos informativos que le hemos dado? ¿Los ha entendido?',
        '2. ¿Ha donado sangre, plaquetas o plasma en los últimos tres (3) meses?',
        '3. ¿Se siente bien para donar sangre hoy?',
        '4. ¿Está o ha estado embarazada en los últimos seis (6) meses?',
        '5. ¿Está tomando o ha tomado en los últimos dos (2) días algún medicamento que contenga aspirina?',
        '6. ¿Ha tenido fiebre acompañada de dolor de cabeza y malestar general?',
        '7. ¿Ha tomado alguno de los medicamentos que aparece en el folleto?',
        '8. ¿Ha recibido alguna vacuna?',
        '9. ¿Ha estado en contacto con una persona que tenía una enfermedad contagiosa?',
        '10. ¿Ha tenido algún piercing o perforación corporal en los últimos tres (3) meses?',
        '11. ¿Ha tenido contacto con la sangre de otra persona?',
        '12. ¿Ha convivido o mantenido contacto íntimo con alguien que tuviese hepatitis o fuera portador del virus de la hepatitis?',
        '13. ¿Ha viajado fuera de Puerto Rico o los Estados Unidos en los últimos tres (3) meses?',
        '14. ¿Ha tenido una prueba positiva para el Virus de la Inmunodeficiencia Humana (VIH) o Virus del SIDA?',
        '15. ¿Ha tenido alguna prueba positiva para hepatitis (B o C)?',
        '16. ¿Se ha inyectado drogas (heroína, esteroide, etc.) alguna vez en su vida?',
        '17. ¿Ha aceptado alguna vez dinero, drogas u otro tipo de pago a cambio de tener relaciones sexuales?',
        '18. ¿Ha tenido relaciones sexuales con más de una persona?',
        '19. ¿Ha tenido relaciones sexuales con una persona que haya salido positivo(a) en una prueba de virus del SIDA (VIH)?',
        '20. ¿Ha tenido alguna enfermedad de transmisión sexual (sifilis, gonorrea, etc.)?',
        '21. ¿Ha leído los folletos informativos que le hemos dao? ¿Los ha entendido?',
        '22. ¿Ha sido rechazado como donante anteriormente?',
        '23. ¿Ha recibido transfusión de sangre o médula ósea?',
        '24. ¿Ha tenido diabetes?',
        '25. ¿Tiene alguna duda o pregunta?'

    ]

# Diccionario para almacenar respuestas

    answers = {}

    for question in questions:
        while True:
            response = input(f'{question} sí/no: ').strip().lower()
            if response in ['sí', 'si', 'no']:
                answers[question] = response
                break
            else:
                print('Por favor responda con "sí" o "no".')

    return answers

# Correr función y recolectar respuestas

user_answers = ask_questions()

# Print respuestas

print('\nRepuestas de los usuarios:')
for question, answer in user_answers.items():
    print(f'{question}: {answer}')
    
    
    
        
