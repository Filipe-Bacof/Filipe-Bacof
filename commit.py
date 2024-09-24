import os
import subprocess

def git_commit(repo_path):
    try:
        os.chdir(repo_path)
        print(f"Entrou no diretório {repo_path}")
    except FileNotFoundError:
        print("Diretório não encontrado.")
        return

    subprocess.run(["git", "add", "."])
    print("Todos os arquivos foram adicionados.")

    commit_message = input("Digite a mensagem do commit: ")

    if not commit_message.strip():
        print("A mensagem de commit não pode ser vazia.")
        return

    subprocess.run(["git", "commit", "-m", commit_message])
    print(f"Commit feito com a mensagem: {commit_message}")

    subprocess.run(["git", "push"])
    print("Alterações enviadas para o repositório remoto.")

if __name__ == "__main__":
    repo_path = input("Digite o caminho do repositório Git: ")
    git_commit(repo_path)
