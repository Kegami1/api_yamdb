from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category, Genre, Title, Review, Comment, User
from django.shortcuts import get_object_or_404


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


def check_not_empty_base(class_type):
    if class_type.objects.exists():
        print(f'data in {class_type} already loaded...exiting.')
        print(ALREDY_LOADED_ERROR_MESSAGE)
    else:
        print(f'Loading data {class_type}')
    return


class Command(BaseCommand):
    help = "Loads data from .csv files"

    def handle(self, *args, **options):

        check_not_empty_base(Genre)
        for row in DictReader(open('static/data/genre.csv')):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            genre.save()

        check_not_empty_base(Category)
        for row in DictReader(open('static/data/category.csv')):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            category.save()

        check_not_empty_base(Title)
        for row in DictReader(open('static/data/titles.csv')):
            for row_genre_title in DictReader(
                open('static/data/genre_title.csv')
            ):
                if row_genre_title['title_id'] == row['id']:
                    genre_id = row_genre_title['genre_id']
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=get_object_or_404(Category, id=row['category']),
                genre=get_object_or_404(Genre, id=genre_id)
            )
            title.save()

        check_not_empty_base(Review)
        for row in DictReader(open('static/data/review.csv')):
            review = Review(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author=get_object_or_404(User, id=row['author']),
                score=row['score'],
                pub_date=row['pub_date'],
            )
            review.save()

        check_not_empty_base(Comment)
        for row in DictReader(open('static/data/comments.csv')):
            comment = Comment(
                id=row['id'],
                review=get_object_or_404(Review, id=row['review_id']),
                text=row['text'],
                author=get_object_or_404(User, id=row['author']),

                pub_date=row['pub_date'],
            )
            comment.save()