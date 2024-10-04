import uuid

import click
from app import db
from app.models import Author, Book
from datetime import date

def seed_data():
    # clear existing data
    db.drop_all()
    db.create_all()

    # author data
    author1 = Author(id=str(uuid.uuid4()),
                     name="Tere Liye",
                     bio="Penulis dan akuntan berkebangsaan Indonesia",
                     birth_date=date(1979,5,21))
    author2 = Author(id=str(uuid.uuid4()),
                     name="Pramoedya Ananta Toer",
                     bio="Salah satu sastrawan Indonesia yang paling berpengaruh. Karya-karyanya seringkali mengangkat tema sosial dan politik.",
                     birth_date=date(1925,11,6))
    author3 = Author(id=str(uuid.uuid4()),
                     name="Andrea Hiranata",
                     bio="Novelis indonesia yang berasal dari Pulau belitung.",
                     birth_date=date(1966,10,24))

    db.session.add_all([author1,
                        author2,
                        author3,
                        ])
    db.session.commit()

    # book data
    book1 = Book(id=str(uuid.uuid4()),
                 title="Hafalan Sholat Delisa",
                 description="Hafalan Sholat Delisa",
                 published_date=date(2005,1,1),
                 author_id=author1.id)
    book2 = Book(id=str(uuid.uuid4()),
                 title="Moga Bunda Disayang Allah",
                 description="Moga Bunda Disayang Allah",
                 published_date=date(2006,1,1),
                 author_id=author1.id)
    book3 = Book(id=str(uuid.uuid4()),
                 title="Manusia Bumi",
                 description="Manusia Bumi",
                 published_date=date(1980,1,1),
                 author_id=author2.id)
    book4 = Book(id=str(uuid.uuid4()),
                 title="Anak Semua Bangsa",
                 description="Anak Semua Bangsa",
                 published_date=date(1981,1,1),
                 author_id=author2.id)
    book5 = Book(id=str(uuid.uuid4()),
                 title="Laskar Pelangi",
                 description="FLaskar Pelangi",
                 published_date=date(2005,1,1),
                 author_id=author3.id)
    book6 = Book(id=str(uuid.uuid4()),
                 title="Sang Pemimpi",
                 description="Sang Pemimpi",
                 published_date=date(2006,1,1),
                 author_id=author3.id)

    db.session.add_all([book1,
                        book2,
                        book3,
                        book4,
                        book5,
                        book6
                        ])

    db.session.commit()

@click.command('seed_data')
def seed():
    """Seed the database with initial data."""
    seed_data()
    click.echo('Seed data done!')