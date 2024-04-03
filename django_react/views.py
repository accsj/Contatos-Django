from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contato
from .serializers import ContatoSerializer
from rest_framework import status


@api_view(['POST'])
def cadastrar(request):
    if request.method == 'POST':
        serializer = ContatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Contato cadastrado com sucesso!', 'contato': serializer.data}, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET'])
def listar(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def deletar(request, contato_id):
    try:
        contato = Contato.objects.get(pk=contato_id)
    except Contato.DoesNotExist:
        return Response({'mensagem': 'Contato não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        contato.delete()
        return Response({'mensagem': 'Contato excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def alterar(request, contato_id):
    try:
        contato = Contato.objects.get(pk=contato_id)
    except Contato.DoesNotExist:
        return Response({'mensagem': 'Contato não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ContatoSerializer(contato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensagem': 'Nome do contato atualizado com sucesso!', 'contato': serializer.data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
