from django.core.management.base import BaseCommand, CommandError
from ILMP_app.models import Mascotas

class Command(BaseCommand):
    help = 'Añadir mascota'

    def add_arguments(selft, parse):
        parse.add_argument('namePet', help="Nombre de la mascota")
    
    def handle(self, *args, **options):
        name=options["namePet"]
        Mascotas.objects.create(namePet=name)
        self.stdout.write('Mascota añadida')