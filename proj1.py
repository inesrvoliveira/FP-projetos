# Ines Oliveira     89465

# A funcao verifica se o argumento dado corresponde a um tabuleiro, se for retorna True e em caso contrario retorna False
#------------------------------------------------------------------------------------
def eh_tabuleiro(t):
    ctd=0
    if isinstance(t,tuple):           # verifica se t e tuplo ( retorna True e em caso contrario retorna False )  
        if len(t) == 3:          
            if isinstance(t[0],tuple) and isinstance(t[1],tuple) and isinstance(t[2],tuple):    # verifica se os 3 elementos sao tuplos
                if len(t[0]) == 3 and len(t[1]) == 3 and len(t[2]) == 2:
                    for i in range(len(t)):
                        for j in range(len(t[i])):
                            if t[i][j] == -1 or t[i][j] == 0 or t[i][j] == 1:      # verifica se cada elemento dos tuplos "dentro" de t corresponde a -1, 0 ou 1
                                ctd = ctd +1                                       # sempre que cada elemento carresponder a esses valores incrementa a variavel ctd
    return ctd == 8                                                               # sao 8 valores (3+3+2), sendo que se o ctd for igual a 8, podemos confirmar que t e um tabuleiro

# A funcao recebe um tabuleiro e devolve uma cadeia de caracteres que o representa, ou seja, devolve a sua representacao “para os nossos olhos”
#-------------------------------------------------------------------------------------------

def tabuleiro_str(ta):
    str0 = '+-------+\n|...{2}...|\n|..{1}.{5}..|\n|.{0}.{4}.{7}.|\n|..{3}.{6}..|\n+-------+'
    lista = []      # lista para guardar  os x's , 0's e 1's
    if not eh_tabuleiro(ta):
        raise ValueError ('tabuleiro_str: argumento invalido')
    for i in range(len(ta)):      #percorre as linhas da matriz ta
        for j in range(len(ta[i])):  #percorre as colunas da matriz ta
            if ta[i][j] == -1:     #se no tuplo na linha 1 e na coluna j o valor for -1 , coloca-se na lista um x
                lista.append('x')
            elif ta[i][j] == 0:    #se no tuplo na linha 1 e na coluna j o valor for 0 , coloca-se na lista um 0
                lista.append('0')
            elif ta[i][j] == 1:    #se no tuplo na linha 1 e na coluna j o valor for 1 , coloca-se na lista um 1
                lista.append('1')
    return str0.format(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7]) # segundo a ordem que esta na str0 coloca-se cada elemento da lista

# A funcao verifica se os dois argumentos sao tabuleiros e se forem, se sao iguais returnando True caso sejam e False em caso contrario
#--------------------------------------------------------------------------------------------------

def tabuleiros_iguais(ta1,ta2):
    if not eh_tabuleiro(ta1):
        raise ValueError ('tabuleiros_iguais: um dos argumentos nao e tabuleiro')
    if not eh_tabuleiro(ta2):
        raise ValueError ('tabuleiros_iguais: um dos argumentos nao e tabuleiro')
    return ta1 == ta2

# A funcao recebe um tabuleiro e um caracter (“E” ou “D”) e devolve um novo tabuleiro resultante de aplicar a porta X ao qubit esquerdo ou direito, conforme o caracter seja “E” ou “D”
#----------------------------------------------------------------------------------------------------

def porta_x(ta,s):
    if not eh_tabuleiro(ta): # verifica se ta e um tabuleiro, retorna erro se nao for
        raise ValueError ('porta_x: um dos argumentos e invalido')
    if (s!='E' and s!='D'): # verifica se a s e 'E' ou 'D', retorna erro se nao for
        raise ValueError ('porta_x: um dos argumentos e invalido')
    if s == 'E':
        nova_list=[] # nova lista que vai ser o novo tuplo do meio do tabuleiro
        ta_novo = [ta[0],ta[2]]        
        for i in range(len(ta[1])): # percorre o tuplo do meio do tabuleiro
            if ta[1][i] == 0:     # se o valor nao posicao i for 0, substitui por 1 na nova_list
                nova_list.append(1)
            elif ta[1][i] == 1:   # se o valor nao posicao i for 1, substitui por 0 na nova_list
                nova_list.append(0)
            elif ta[1][i] == -1:  # se o valor nao posicao i for 0, substitui por 1  na nova_list
                nova_list.append(-1) 
        nova_list = tuple(nova_list) # transforma a lista nova_list num tuplo
        ta_novo.insert(1,nova_list) # insere no meio da lista ta_novo a nova_lista (que e agora um tuplo)
        ta_novo = tuple(ta_novo) # transforma a lista ta_novo num tuplo
        return ta_novo
    
    elif s == 'D':
        nova_list2=[[ta[0][0],ta[0][2]],[ta[1][0],ta[1][2]],[ta[2][1]]] # nova lista que vai substuir o tuplo
        for i in range(2): # percorre os elementos de indice 1 dos primeiros 2 tuplos 
            if ta[i][1] == 0:
                nova_list2[i].insert(1,1) # se o valor for 0, insere 1 na lista de indice i da nova_list2
            elif ta[i][1] == 1:
                nova_list2[i].insert(1,0) # se o valor for 1, insere 0 na lista de indice i da nova_list2
            elif ta[i][1] == -1:
                nova_list2[i].insert(1,-1) # se o valor for -1, insere -1 na lista de indice i da nova_list2
        if ta[2][0] == 0:      # se o elemento de indice 0 do ultimo tuplo de ta e 0, insere 1 na lista de indice 2 da nova_list2
            nova_list2[2].insert(0,1)
        elif ta[2][0] == 1:    # se o elemento de indice 0 do ultimo tuplo de ta e 1, insere 0 na lista de indice 2 da nova_list2
            nova_list2[2].insert(0,0)
        elif ta[2][0] == -1:   # se o elemento de indice 0 do ultimo tuplo de ta e -1, insere -1 na lista de indice 2 da nova_list2
            nova_list2[2].insert(0,-1)
        return (tuple(nova_list2[0]),tuple(nova_list2[1]),tuple(nova_list2[2])) # retorna um tuplo com 3 tuplos ( de cada lista dentro de nova_list2 que forem "transformadas" em tuplos)
 
# A funcao recebe um tabuleiro e um caracter e devolve um novo tabuleiro resultante de aplicar a porta Z ao qubit da esquerda ou da direita, conforme o caracter seja “E” ou “D
#------------------------------------------------------------------------------------------------------------------ 
    
def porta_z(ta,s):    
    if not eh_tabuleiro(ta):
        raise ValueError ('porta_z: um dos argumentos e invalido')
    if (s!='E' and s!='D'):
        raise ValueError ('porta_z: um dos argumentos e invalido')
    if s == 'E':    # executa exatamente as mesmas funcionalidades que a funcao em cima mas aqui o tuplo que vai ser alterado e o de indice 0
        nova_list=[]
        ta_novo = [ta[1],ta[2]]        
        for i in range(len(ta[0])): # percorre o tuplo de indice 0 de ta
            if ta[0][i] == 0:     
                nova_list.append(1)
            elif ta[0][i] == 1:   
                nova_list.append(0)
            elif ta[0][i] == -1:  
                nova_list.append(-1) 
        nova_list = tuple(nova_list)
        ta_novo.insert(0,nova_list)
        ta_novo = tuple(ta_novo) 
        return ta_novo    
    
    elif s == 'D': # executa exatamente as mesmas funcionalidades que a funcao em cima mas aqui o valor a ser substituido e o de indice 2 dos dois primeiros tuplos e de indice 1 do ultimo tuplo de ta
        nova_list2=[[ta[0][0],ta[0][1]],[ta[1][0],ta[1][1]],[ta[2][0]]]
        for i in range(2):    # percorre os elementos de indice 2 dos 2 primeiros tuplos de ta
            if ta[i][2] == 0:
                nova_list2[i].insert(2,1)
            elif ta[i][2] == 1:
                nova_list2[i].insert(2,0)
            elif ta[i][2] == -1:
                nova_list2[i].insert(2,-1)
        if ta[2][1] == 0:
            nova_list2[2].insert(1,1)
        elif ta[2][1] == 1:
            nova_list2[2].insert(1,0)
        elif ta[2][1] == -1:
            nova_list2[2].insert(1,-1)
        return (tuple(nova_list2[0]),tuple(nova_list2[1]),tuple(nova_list2[2]))    


# A funcao recebe um tabuleiro e um caracter e devolve um novo tabuleiro resultante de aplicar a porta H ao qubit da esquerda ou da direita, conforme o caracter seja “E” ou “D”
#--------------------------------------------------------------------------------------------------------

def porta_h(ta,s): 
    if not eh_tabuleiro(ta):
        raise ValueError ('porta_h: um dos argumentos e invalido')
    if (s!='E' and s!='D'):
        raise ValueError ('porta_h: um dos argumentos e invalido') 
    if s == 'E':   
        ta_novo = [ta[2]] # criamos uma nova lista com o tuplo de indice 2 de ta
        ta_novo.insert(0,ta[0]) # inserimos o tuplo de indice 0 de ta a frente do tuplo anterior ( no indice 0)
        ta_novo.insert(0,ta[1]) # inserimos o tuplo de indice 1 de ta a frente do tuplo anterior ( no indice 0)
        return tuple(ta_novo) # retornamos a lista ta_novo transformada num tuplo
    
    if s == 'D':
        ta0_novo = [ta[0][0],ta[0][2],ta[0][1]] # lista com os elementos do 1 tuplo de ta, mas ordem diferente trocando o 2 com o 3
        ta1_novo = [ta[1][0],ta[1][2],ta[1][1]] # lista com os elementos do 2 tuplo de ta, mas ordem diferente trocando o 2 com o 3
        ta2_novo = [ta[2][1],ta[2][0]] # lista com os elementos do 3 tuplo de ta, mas ordem diferente trocando o 1 com o 2
        return (tuple(ta0_novo),tuple(ta1_novo),tuple(ta2_novo)) # retorna um tuplo de todas as listas ( "transformadas" em tuplos ) juntas por ordem de ta
    
#-------------------------------------FIM---------------------------------------------------------------------------
        
    
    