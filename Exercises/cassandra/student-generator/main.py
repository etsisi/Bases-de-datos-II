import argparse
import csv
import random

from faker import Faker


fake = Faker(['es_ES', 'en_US', 'it_IT'])
carreras = [
    'Psicología Canina',
    'Artes del Café',
    'Turismo Espacial',
    'Biología Marina',
    'Cocina Molecular',
    'Diseño de Moda Intergaláctica',
    'Historia del Universo Paralelo',
    'Música para Plantas',
    'Filosofía Cuántica',
    'Teoría Práctica'
    ]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Students generator')
    parser.add_argument('n', type=int, help='How many students')
    parser.add_argument('output', type=str, help='Output file path')
    args = parser.parse_args()

    with open(args.output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nombre', 'edad', 'carrera'])

        for identifier in range(args.n):
            nombre = fake.name()
            edad = fake.random_int(min=18, max=30)
            carrera = random.choice(carreras)
            writer.writerow([identifier, nombre, edad, carrera])