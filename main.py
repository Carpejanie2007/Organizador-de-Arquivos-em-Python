import os
import random 

lista_extensoes = ["jpg", "txt", "pdf", "docx", "mp4"]
lista_arquivos = ["arquivo_1", "arquivo_2", "arquivo_3", "arquivo_4", "arquivo_5", "arquivo_6", "arquivo_7", "arquivo_8", "arquivo_9", "arquivo_10" ]
lista_arquivos_nova = []

def sortear_Arquivos():
    for arquivos in lista_arquivos:
        arquivo_escolhido = random.choice(lista_arquivos)
        extensao_escolhida = random.choice(lista_extensoes)
        arquivos = arquivo_escolhido + "." + extensao_escolhida
        if arquivos not in lista_arquivos_nova:
            lista_arquivos_nova.append(arquivos)
        else:
            print(f"{arquivos} Ja existe! Apague o existente para continuar!")
    print(lista_arquivos_nova)

def criar_Folder(lista_extensoes):
    for extensoes in lista_extensoes:
        os.makedirs(f"Arquivos/{extensoes}", exist_ok=True)


def criando_arquivos(lista_arquivos_nova):
    for arquivos in lista_arquivos_nova:
        arquivos_criados = open(f"Arquivos/{arquivos}", "w")
        arquivos_criados.close()


def organizar_arquivos():
    arquivos_criados = os.listdir("Arquivos")
    for arquivos in arquivos_criados:
        if ".jpg" in arquivos:
            if os.path.exists(f"Arquivos/jpg/{arquivos}"):
                os.remove(f"Arquivos/jpg/{arquivos}")
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/jpg/{arquivos}")
            else:
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/jpg/{arquivos}")
        elif ".docx" in arquivos:
            if os.path.exists(f"Arquivos/docx/{arquivos}"):
                os.remove(f"Arquivos/docx/{arquivos}")
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/docx/{arquivos}")
            else:
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/docx/{arquivos}")
        elif ".mp4" in arquivos:
            if os.path.exists(f"Arquivos/mp4/{arquivos}"):
                os.remove(f"Arquivos/mp4/{arquivos}")
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/mp4/{arquivos}")
            else:
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/mp4/{arquivos}")
        elif ".pdf" in arquivos:
            if os.path.exists(f"Arquivos/pdf/{arquivos}"):
                os.remove(f"Arquivos/pdf/{arquivos}")
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/pdf/{arquivos}")
            else:
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/pdf/{arquivos}")
        elif ".txt" in arquivos:
            if os.path.exists(f"Arquivos/txt/{arquivos}"):
                os.remove(f"Arquivos/txt/{arquivos}")
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/txt/{arquivos}")
            else:
                os.rename(f"Arquivos/{arquivos}", f"Arquivos/txt/{arquivos}")


sortear_Arquivos()
criar_Folder(lista_extensoes)
criando_arquivos(lista_arquivos_nova)
organizar_arquivos()


