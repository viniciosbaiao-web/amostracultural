def calcular_media():
    print("=== Calculadora de Média Escolar ===")
    
    try:
        # Solicita as notas ao usuário
        nota1 = float(input("Digite a primeira nota (0 a 10): "))
        nota2 = float(input("Digite a segunda nota (0 a 10): "))
        
        # Verifica se as notas estão dentro do intervalo válido
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("Erro: As notas devem estar entre 0 e 10.")
            return

        # Calcula a média simples
        media = (nota1 + nota2) / 2
        print(f"\nSua média final foi: {media:.1f}")

        # Verifica a situação do aluno
        if media >= 7.0:
            print("Situação: APROVADO! Parabéns.")
        elif media >= 5.0:
            print("Situação: RECUPERAÇÃO.")
        else:
            print("Situação: REPROVADO.")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (use ponto para decimais).")

if __name__ == "__main__":
    calcular_media()

