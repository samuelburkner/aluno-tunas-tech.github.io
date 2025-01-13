import git
import os

def initialize_repo():
    # Caminho onde o repositório será inicializado
    repo_dir = "meu_repositorio"
    
    # Verificando se o diretório já existe
    if not os.path.exists(repo_dir):
        os.mkdir(repo_dir)

    # Inicializa o repositório
    repo = git.Repo.init(repo_dir)
    print(f'Repositório inicializado em: {repo_dir}')
    return repo

def adicionar_arquivo(repo, filename):
    # Criando e escrevendo algo no arquivo
    with open(os.path.join(repo.working_tree_dir, filename), 'w') as file:
        file.write("Este é o primeiro commit do repositório.\n")

    # Adicionando o arquivo ao repositório
    repo.index.add([filename])
    print(f'Arquivo {filename} adicionado ao repositório.')

def fazer_commit(repo):
    # Realizando um commit
    repo.index.commit("Primeiro commit")
    print("Commit realizado.")

def criar_gerenciamento_remoto(repo):
    # Adiciona um repositório remoto (substitua pela URL do seu repositório)
    remote_url = "https://github.com/samuburkner/meu_repositorio.git"
    origin = repo.create_remote('origin', remote_url)

    # Empurrando para o repositório remoto
    origin.push(refspec='master:refs/heads/master')
    print("Alterações enviadas para o repositório remoto.")

if __name__ == "__main__":
    repo = initialize_repo()
    adicionar_arquivo(repo, 'README.md')
    fazer_commit(repo)
    criar_gerenciamento_remoto(repo)
