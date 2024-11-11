# Importaciones necesarias de Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    """
    Gestor personalizado para el modelo de Usuario.
    Proporciona métodos auxiliares para crear usuarios y superusuarios.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y guarda un nuevo usuario con el email y contraseña dados.

        Args:
            email (str): El email del usuario.
            password (str, opcional): La contraseña del usuario. Por defecto es None.
            **extra_fields: Campos adicionales para el usuario.

        Returns:
            User: Una instancia del modelo de Usuario creado.

        Raises:
            ValueError: Si no se proporciona un email.
        """
        if not email:
            raise ValueError('Debe ingresar una dirección de correo')

        # Normaliza el email (convierte el dominio a minúsculas)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)  # Establece la contraseña de forma segura
        user.save(using=self._db)  # Guarda el usuario en la base de datos
        return user

    def create_superuser(self, email, password):
        """
        Crea y guarda un nuevo superusuario con el email y contraseña dados.

        Args:
            email (str): El email del superusuario.
            password (str): La contraseña del superusuario.

        Returns:
            User: Una instancia del modelo de Usuario (superusuario) creado.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado que utiliza email en lugar de nombre de usuario.

    Este modelo extiende las capacidades del modelo de usuario predeterminado de Django,
    permitiendo la autenticación por email y añadiendo campos adicionales.
    """

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='Correo electrónico',
        help_text='Dirección de correo electrónico del usuario'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nombre',
        help_text='Nombre del usuario'
    )
    apellido_paterno = models.CharField(
        max_length=100,
        verbose_name='Apellido paterno',
        help_text='Apellido paterno del usuario'
    )
    apellido_materno = models.CharField(
        max_length=100,
        verbose_name='Apellido materno',
        help_text='Apellido materno del usuario'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Activo',
        help_text='Designa si este usuario debe ser tratado como activo.'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Es staff',
        help_text='Designa si el usuario puede iniciar sesión en el sitio de administración.'
    )
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name='Fecha de registro',
        help_text='Fecha y hora en que el usuario se registró'
    )

    objects = UserManager()  # Asigna el gestor personalizado

    USERNAME_FIELD = 'email'  # Usa el email como campo de identificación para el inicio de sesión
    REQUIRED_FIELDS = []  # El email ya es requerido por ser el USERNAME_FIELD

    class Meta:
        app_label = 'core'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        """
        Representación en cadena del usuario.

        Returns:
            str: El email del usuario.
        """
        return self.email

    def get_full_name(self):
        """
        Obtiene el nombre completo del usuario.

        Returns:
            str: El nombre completo del usuario (nombre y apellidos).
        """
        return f"{self.name} {self.apellido_paterno} {self.apellido_materno}"

    def get_short_name(self):
        """
        Obtiene el nombre corto del usuario.

        Returns:
            str: El nombre del usuario.
        """
        return self.name