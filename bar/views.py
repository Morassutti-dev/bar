from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from bar.models import Comanda,ItemComanda,Produto
from bar.forms import AdicionarItemForm, EditarComandaForm 
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def criar_comanda(request):
    comanda = Comanda.objects.create(usuario=request.user)
    return redirect('detalhes_comanda', comanda_id=comanda.id)

@login_required
def detalhes_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    return render(request, 'comanda_detalhes.html', {'comanda': comanda})


def detalhes_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    itens = comanda.itens.all()  # Pegando os itens da comanda

    # Calculando o total corretamente
    total = sum(item.quantidade * item.produto.preco for item in itens)

    return render(request, 'detalhes_comanda.html', {'comanda': comanda, 'itens': itens, 'total': total})

def adicionar_item(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    produtos = Produto.objects.all()

    if request.method == "POST":
        form = AdicionarItemForm(request.POST)
        if form.is_valid():
            produto = form.cleaned_data['produto']
            quantidade = form.cleaned_data['quantidade']

            # Verificação de estoque (usando o campo 'quantidade')
            if produto.quantidade < quantidade:
                messages.error(request, f"Estoque insuficiente para {produto.nome}. Disponível: {produto.quantidade}")
                return redirect("adicionar_item", comanda_id=comanda.id)

            # Criando ou atualizando o item na comanda
            item, created = ItemComanda.objects.get_or_create(
                comanda=comanda, produto=produto,
                defaults={"quantidade": quantidade}
            )
            if not created:
                item.quantidade += quantidade
                if item.quantidade < 0:
                    messages.error(request, "A quantidade não pode ser negativa.")
                    return redirect("adicionar_item", comanda_id=comanda.id)
                item.save()

            messages.success(request, f"{quantidade}x {produto.nome} adicionado(s) à comanda.")
            return redirect("detalhes_comanda", comanda_id=comanda.id)
    else:
        form = AdicionarItemForm()

    return render(request, "adicionar_item.html", {"comanda": comanda, "form": form, "produtos": produtos})




def listar_comandas(request):
    # Busca todas as comandas no banco de dados
    comandas = Comanda.objects.all()
    
    # Passa as comandas para o template
    return render(request, "listar_comandas.html", {"comandas": comandas})


def editar_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    
    if request.method == "POST":
        form = EditarComandaForm(request.POST, instance=comanda)
        if form.is_valid():
            form.save()
            messages.success(request, "Comanda atualizada com sucesso!")
            return redirect('listar_comandas')
    else:
        form = EditarComandaForm(instance=comanda)
    
    return render(request, 'editar_comanda.html', {'form': form, 'comanda': comanda})

def excluir_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id)
    comanda.delete()
    messages.success(request, "Comanda excluída com sucesso!")
    return redirect('listar_comandas')


def excluir_item(request, item_id):
    item = get_object_or_404(ItemComanda, id=item_id)
    comanda_id = item.comanda.id  # Guarda o ID da comanda para redirecionar depois
    item.delete()
    messages.success(request, "Item excluído com sucesso!")
    return redirect('detalhes_comanda', comanda_id=comanda_id)

