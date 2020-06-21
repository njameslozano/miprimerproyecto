from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    lista_enfermedades = [  "Asma", "Enfermedad renal crónica bajo tratamiento con diálisis",
                            "Enfermedad pulmonar crónica", "Diabetes", "Trastornos de la hemoglobina",
                            "Personas inmunodeprimidas", "Enfermedad hepática", 
                            "Persona de 65 años de edad o más", "Afecciones cardíacas graves",
                            "Obesidad grave" ]
    lista_sintomas =    [ "Fiebre","Tos seca","Cansancio","Molestias y dolores","Dolor de garganta",
                            "Diarrea","Conjuntivitis","Dolor de cabeza",
                            "Dificultad para respirar o sensación de falta de aire",
                            "Dolor o presión en el pecho","Incapacidad para hablar o moverse" ] 
    context = { "enfermedades" : lista_enfermedades,
                "sintomas" : lista_sintomas,
                "numero_de_enfermedades" : len(lista_enfermedades), 
                "numero_de_sintomas" : len(lista_sintomas) }

    return render(request, "index.html", context )



def contacto(request):
    return HttpResponse("Mi email es njames@alumnos.uai.cl")