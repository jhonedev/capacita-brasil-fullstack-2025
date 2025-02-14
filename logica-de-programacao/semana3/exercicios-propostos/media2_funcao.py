A = float(input())
B = float(input())
C = float(input())

def mediaPonderada(nota1, nota2, nota3, p1, p2, p3):
    media = (nota1 * p1 + nota2 * p2 + nota3 * p3 ) / (p1 + p2 + p3)
    return media

med = mediaPonderada(A, B, C, 2, 3, 5)
print(f"MEDIA = {med:.1f}")