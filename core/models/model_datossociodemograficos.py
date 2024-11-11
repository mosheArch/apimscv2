from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class DatosSociodemograficos(models.Model):
    """
    Modelo para almacenar datos sociodemográficos de los usuarios.
    """

    ESTADO_CIVIL_CHOICES = [
        ('', 'Estado civil'),
        (1, 'Casada'),
        (2, 'Unión libre'),
        (3, 'Soltera'),
        (4, 'Viuda')
    ]

    ESCOLARIDAD_CHOICES = [
        ('', 'Escolaridad'),
        (1, 'Primaria'),
        (2, 'Secundaria'),
        (3, 'Bachillerato'),
        (4, 'Licenciatura'),
        (5, 'Posgrado')
    ]

    OCUPACION_CHOICES = [
        ('', 'Ocupación'),
        (1, 'Ama de casa'),
        (2, 'Empleada'),
        (3, 'Estudiante'),
        (4, 'Desempleada')
    ]

    STATUS_ECONOMICO_CHOICES = [
        ('', 'Estatus económico'),
        (1, 'Baja baja'),
        (2, 'Baja alta'),
        (3, 'Media baja'),
        (4, 'Media alta')
    ]

    SI_NO_CHOICES = [
        ('', 'Seleccione'),
        (1, 'Sí'),
        (2, 'No')
    ]

    PARIDAD_CHOICES = [
        ('', 'Paridad'),
        (1, 'Primigesta'),
        (2, 'Multigesta')
    ]

    TIPO_ANESTESIA_CHOICES = [
        ('', 'Tipos de anestesia'),
        (1, 'Anestesia inhalatoria'),
        (2, 'Anestesia general'),
        (0, 'Otra')
    ]

    TIPO_PARTO_CHOICES = [
        ('', 'Tipos de parto'),
        (1, 'Vaginal'),
        (2, 'Cesárea')
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='datos_sociodemograficos'
    )
    edad = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(12), MaxValueValidator(100)]
    )
    estado_civil = models.PositiveSmallIntegerField(
        choices=ESTADO_CIVIL_CHOICES,
        default='',
    )
    escolaridad = models.PositiveSmallIntegerField(
        choices=ESCOLARIDAD_CHOICES,
        default='',
    )
    ocupacion = models.PositiveSmallIntegerField(
        choices=OCUPACION_CHOICES,
        default='',
    )
    status_economico = models.PositiveSmallIntegerField(
        choices=STATUS_ECONOMICO_CHOICES,
        default='',
    )
    ingreso_mensual = models.PositiveIntegerField()
    embarazo_deseado = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    embarazo_planeado = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    parto_termino = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    paridad = models.PositiveSmallIntegerField(
        choices=PARIDAD_CHOICES,
        default='',
    )
    numero_de_hijos = models.PositiveSmallIntegerField()
    lactancia = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    tiempo_de_lactancia = models.PositiveSmallIntegerField()
    enfermedad_del_neonato = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    tipo_de_enfermedad_neonato = models.CharField(max_length=100, blank=True)
    anestesia = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    tipo_de_anestesia = models.PositiveSmallIntegerField(
        choices=TIPO_ANESTESIA_CHOICES,
        default='',
    )
    tipo_de_parto = models.PositiveSmallIntegerField(
        choices=TIPO_PARTO_CHOICES,
        default='',
    )
    edad_del_bebe = models.PositiveSmallIntegerField()
    lugar_de_atencion = models.CharField(max_length=100)
    apoyo_de_familia = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    apoyo_de_pareja = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    abortos = models.PositiveSmallIntegerField(
        choices=SI_NO_CHOICES,
        default='',
    )
    numero_de_abortos = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Datos de {self.user.name}"

    class Meta:
        verbose_name = "Datos Sociodemográficos"
        verbose_name_plural = "Datos Sociodemográficos"


class ResultadoPrediccion(models.Model):
    """
    Modelo para almacenar los resultados de las predicciones.
    """
    resultado = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Predicción para {self.user.name}"

    class Meta:
        verbose_name = "Resultado de Predicción"
        verbose_name_plural = "Resultados de Predicción"