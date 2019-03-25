# Para importar a árvore de decisões do scikit-learn:
from sklearn import tree
clf = tree.DecisionTreeClassifier()

# Vamos agora criar dados para treinar nossa árvore de decisões:
# [fazenda, sol, mar, vento]
# fazenda = 0 => não há fontes de biomassa; fazenda = 1 => há fonte
# sol = 0 => baixa luminosidade; sol = 1 => SOBRAL
# mar = 0 => não tem água perto; mar = 1 => tem água perto
# vento = 0 => não venta; vento = 1 => venta

solar = 0
eolica = 1
maremotriz = 2
biomassa = 3

dados = [ [0, 1, 0, 1], [0, 1, 0, 0], [1, 1, 0, 0], [1, 1, 0, 1],
        [0, 0, 1, 1], [0, 1, 1, 1],
        [0, 0, 1, 0],[0, 1, 1, 0],[1, 0, 1, 0],[1, 1, 1, 0],[0, 0, 1, 1],[0, 1, 1, 1],[1, 0, 1, 1],[1, 1, 1, 1],
        [1, 0, 0, 0],[1, 1, 0, 0],[1, 0, 1, 0],[1, 1, 1, 0],[1, 0, 0, 1],[1, 1, 0, 1],[1, 0, 1, 1],[1, 1, 1, 1] ]

tipo = [solar, solar, solar, solar, eolica, eolica,
        maremotriz, maremotriz, maremotriz, maremotriz, maremotriz, maremotriz, maremotriz, maremotriz,
        biomassa, biomassa, biomassa, biomassa, biomassa, biomassa, biomassa, biomassa]


clf = clf.fit(dados, tipo)
print("=================== BEM-VINDO(A) ===================")
print("PARA AS PERGUNTAS ABAIXO, DIGITE APENAS SIM OU NÃO.")
print("Sobre a cidade a ser analisada: ")
fazenda = input("Há fazendas por perto? ")
if fazenda.lower() == 'sim':
    fazenda = 1
elif fazenda.lower() == 'não':
    fazenda = 0
elif fazenda.lower() == 'nao':
    fazenda = 0

sol = input("Há bastante Sol? ")
if sol.lower() == 'sim':
    sol = 1
elif sol.lower() == 'não':
    sol = 0
elif sol.lower() == 'nao':
    sol = 0

mar = input("Há um mar lá perto? ")
if mar.lower() == 'sim':
    mar = 1
elif mar.lower() == 'não':
    mar = 0
elif mar.lower() == 'nao':
    mar = 0

vento = input("Venta muito? ")
if vento.lower() == 'sim':
    vento = 1
elif vento.lower() == 'não':
    vento = 0
elif vento.lower() == 'nao':
    vento = 0

resultado = clf.predict([[fazenda, sol, mar, vento]])

print("========== O RESULTADO DA ANÁLISE FOI: ==========")

if resultado == 0:
    print("É melhor usar energia solar, você deve estar em Sobral!")
elif resultado == 1:
    print("Use energia eólica, mas mantenha longe da galera!")
elif resultado == 2:
    print("Aproveite as ondas e use energia maremotriz!")
elif resultado == 3:
    print("Use todos os restos das fazendas e faça biomassa!")