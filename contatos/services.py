from .models import Contato

class ContatoService:
    @staticmethod
    def cadastrar(nome, telefone, email):
        contato = Contato(nome=nome, telefone=telefone, email=email)
        contato.save()
        return contato

    @staticmethod
    def listar():
        return Contato.objects.all()