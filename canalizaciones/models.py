from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    TIPOS_CANALIZACION = [
        ('beca', 'Beca'),
        ('asesoria', 'Asesoría'),
        ('psicologia', 'Atención Psicológica'),
    ]
    alumno = models.CharField(max_length=100)  # Cambiado a CharField
    tipo = models.CharField(max_length=20, choices=TIPOS_CANALIZACION)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} - {self.tipo}"
