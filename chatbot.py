import nltk
from nltk.chat.util import Chat, reflections

# Definición de los patrones de entrada y respuestas
patrones = [
    [
        r"hola|buenos dias|buenas tardes|buenas noches",
        ["¡Hola! ¿Como te llamas?",]
    ],
    [
        r"mi nombre es (.*)|me llamo (.*)",
        ["Hola %1, ¿cómo puedo ayudarte?",]  
    ],
    [
        r"¿Cómo estás?",  # Si el usuario pregunta "¿Cómo estás?"
        ["Estoy bien, gracias. ¿Y tú?",]  # El chatbot responde que está bien y pregunta cómo está el usuario
    ],
    [
        r"Me siento en peligro|Necesito ayuda",
        ["Recuerda llamar a las líneas de emergencia si es una urgencia: 911"]
    ],
    [
        r"Quiero platicar con alguien",
        ["Claro! Aquí estoy para escucharte. ¿Sobre qué quieres hablar?"]
    ]
    [
        r"bye|chao|adios|diu|hasta luego|Hasta Luego",
        ["¡Hasta luego! Si necesitas algo más, no dudes en preguntar.",]
    ],
    [
        r"(|)",
        ["Lo siento, no puedo procesar tu mensaje :("]
    ]
]

def chatbot():
    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?")
    chat = Chat(patrones, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
