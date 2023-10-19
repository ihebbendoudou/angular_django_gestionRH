from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Client
from .models import Compte
from .serialiers import ClientSerializer,CompteSerializer

@api_view(['GET', 'POST'])
def client_list(request, format=None):
    if request.method=='GET':
        client = Client.objects.all().order_by('nom')
        serializer = ClientSerializer(client,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method== 'POST':
          serializer =ClientSerializer(data=request.data)
          if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
          else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT','DELETE'])
def client_detail(request,id,format=None):
    try:
       client= Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=ClientSerializer(client)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=ClientSerializer(client,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        #/*************************/
@api_view(['GET', 'POST'])
def compte_listPerClient(request,id, format=None):
    client=Compte.objects.filter(code_cli__id=id)
    serializer = CompteSerializer(client,many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def compte_per_code_cpt(request,id, format=None):
    compte=Compte.objects.filter(code_cpt=id)
    serializer = CompteSerializer(compte,many=True)
    return Response(serializer.data)


 


@api_view(['GET', 'POST'])
def compte_list(request, format=None):
    if request.method=='GET':
        compte = Compte.objects.all()
        serializer = CompteSerializer(compte,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method== 'POST':
          serializer =CompteSerializer(data=request.data)
          if serializer.is_valid():
             serializer.save()
             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
          else:
            return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT','DELETE'])
def compte_detail(request,id,format=None):
    try:
       compte= Compte.objects.get(pk=id)
    except Compte.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=CompteSerializer(compte)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        serializer=CompteSerializer(compte,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=='DELETE':
        compte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















 #################################################################
@api_view(['GET', 'PUT'])
def compte_retrait(request,id, format=None):
    compte=Compte.objects.filter(code_cli__code_cli=id)
    serializer=CompteSerializer(compte,data=request.data)
    for e in serializer.data:
        if e.solde>500:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        else:
            for a in compte:
                a.solde=a.solde-e.solde
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

#################################################################
@api_view(['GET', 'put'])
def compte_verser(request,id, format=None):
    compte=Compte.objects.filter(code_cpt=id)
    serializer = CompteSerializer(compte,many=True)
    return Response(serializer.data)

###############Compte##############
