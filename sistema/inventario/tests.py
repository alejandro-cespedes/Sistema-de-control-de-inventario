from django.test import TestCase
from django.contrib.auth import get_user_model

class UsuarioModelTest(TestCase):

    # Configuración de datos de prueba que se utilizarán en las pruebas
    @classmethod
    def setUpTestData(cls):
        # Crea un usuario administrador para realizar las pruebas
        cls.admin = get_user_model().objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@example.com',
            first_name='Admin',
            last_name='',
            nivel=1
        )

        # Crea un usuario regular para realizar las pruebas
        cls.user = get_user_model().objects.create_user(
            username='user',
            password='user123',
            email='user@example.com',
            first_name='User',
            last_name='',
            nivel=2
        )

    # Prueba para el método "numeroRegistrados"
    def test_numeroRegistrados(self):
        # Obtiene la cantidad total de usuarios en la base de datos
        count = get_user_model().objects.all().count()
        # Compara el resultado del método con la cantidad real de usuarios
        self.assertEqual(count, get_user_model().numeroRegistrados())

    # Prueba para el método "numeroUsuarios" con el tipo "administrador"
    def test_numeroUsuarios_administrador(self):
        # Obtiene la cantidad de usuarios administradores en la base de datos
        count = get_user_model().objects.filter(is_superuser=True).count()
        # Compara el resultado del método con la cantidad real de usuarios administradores
        self.assertEqual(count, get_user_model().numeroUsuarios('administrador'))

    # Prueba para el método "numeroUsuarios" con el tipo "usuario"
    def test_numeroUsuarios_usuario(self):
        # Obtiene la cantidad de usuarios regulares en la base de datos
        count = get_user_model().objects.filter(is_superuser=False).count()
        # Compara el resultado del método con la cantidad real de usuarios regulares
        self.assertEqual(count, get_user_model().numeroUsuarios('usuario'))
