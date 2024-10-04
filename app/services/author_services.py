from app.repositories.author_repository import AuthorRepository
from app.models import Author

class AuthorService:
    @staticmethod
    def get_all_authors():
        return AuthorRepository.get_all()

    @staticmethod
    def get_author_by_id(author_id):
        return AuthorRepository.get_by_id(author_id)

    @staticmethod
    def create_author(data):
        new_author = Author(**data)
        AuthorRepository.save(new_author)
        return new_author

    @staticmethod
    def update_author(author, data):
        # author = Author.query.get_or_404(author_id)
        for key, value in data.items():
            setattr(author, key, value)
        AuthorRepository.save(author)

    @staticmethod
    def delete_author(author):
        AuthorRepository.delete(author)

