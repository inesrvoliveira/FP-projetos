# Ines Oliveira     89465

#-------------------------------CELULA--------------------------------------------
# as celulas correspondem a um dicionario do tipo {'estado': v} 

# Construtor

def cria_celula(v):
    if v == 1:
        return {'estado': 1}
    elif v == 0:
        return {'estado': 0}
    elif v == -1:
        return {'estado': -1}
    else:
        raise ValueError ('cria_celula: argumento invalido.')

# Seletor 

def obter_valor(c):
    return c['estado']

# Modificador

def inverte_estado(c):
    if obter_valor(c) == 1:
        c['estado'] = 0
    elif obter_valor(c) == 0:
        c['estado'] = 1
    return c

# Reconhecedor

def eh_celula(arg):
    if isinstance(arg,(dict)):
        if len(arg) == 1:
            if obter_valor(arg) == 0 or obter_valor(arg) == 1 or obter_valor(arg) == -1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Teste
    
def celulas_iguais(c1,c2):
    if not eh_celula(c1):
        return False
    if not eh_celula(c2):
        return False
    return c1 == c2
        
# Transformador

def celula_para_str(c):
    if obter_valor(c) == -1:
        return 'x'
    else:
        return '{}'.format(obter_valor(c))

#-----------------------------COORDENADA----------------------------------------
# as coordenadas correspondem a um dicionario do tipo {'linha': l, 'coluna': c} 

# Construtor

def cria_coordenada(l,c):
    if (l==0 or l==1 or l==2) and (c==0 or c==1 or c==2):
        return {'linha': l,'coluna':c}
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos.')

# Selectores

def coordenada_linha(c):
    return c['linha']

def coordenada_coluna(c):
    return c['coluna']

# Reconhecedor

def eh_coordenada(arg):
    if isinstance(arg,(dict)):
        if len(arg) == 2:
            if (coordenada_linha(arg)==0 or coordenada_linha(arg)==1 or coordenada_linha(arg)==2) and (coordenada_coluna(arg)==0 or coordenada_coluna(arg)==1 or coordenada_coluna(arg)==2):
                return True
            else:
                return False
        else:
            return False
    else:
        return False    

# Teste

def coordenadas_iguais(c1,c2):
    if not eh_coordenada(c1):
        return False
    if not eh_coordenada(c2):
        return False
    return c1 == c2

# Transformador

def coordenada_para_str(c):
    return '({}, {})'.format(coordenada_linha(c),coordenada_coluna(c))

#--------------------------TABULEIRO--------------------------------------------
# os tabuleiros sao uma lista de listas na forma [[celula,celula,celula],[celula,celula,celula],[celula,celula]]

# Construtor

def tabuleiro_inicial():
    return [[cria_celula(-1),cria_celula(-1),cria_celula(-1)],[cria_celula(0),cria_celula(0),cria_celula(-1)],[cria_celula(0),cria_celula(-1)]]

# Reconhecedor

def eh_tabuleiro(arg):
    ctd = 0
    if isinstance(arg,list):      
        if len(arg) == 3:          
            if isinstance(arg[0],list) and isinstance(arg[1],list) and isinstance(arg[2],list):    
                if len(arg[0]) == 3 and len(arg[1]) == 3 and len(arg[2]) == 2:
                    for i in range(len(arg)):
                        for j in range(len(arg[i])):
                            if arg[i][j] == cria_celula(-1) or arg[i][j] == cria_celula(0) or arg[i][j] == cria_celula(1):
                                ctd = ctd +1           # incrementa ctd se for -1,0 ou 1
    return ctd == 8                                    # 8 pois e uma lista com 3 listas,tendo as primeiras duas, 3 elementos e a ultima 2 (3+3+2)

#----------------------FUNCAO AUXILIAR-----------------------------------

def verifica_se_eh_str_tab(s):
    ctd0 = 0            # conta quantos ( existem
    ctd1 = 0            # conta quantos ) existem
    ctd2 = 0            # conta quantos - existem
    ctd3 = 0            # conta quantos 1 existem
    ctd4 = 0            # conta quantos 0 existem
    ctd5 = 0            # conta quantas , existem
    for i in range(len(s)):
        if s[i] == '(':
            ctd0 = ctd0 + 1  
        if s[i] == ')':
            ctd1 = ctd1 + 1
        if s[i] == '-':
            ctd2 = ctd2 + 1
        if s[i] == '1':
            ctd3 = ctd3 + 1
        if s[i] == '0':
            ctd4 = ctd4 + 1 
        if s[i] == ',':
            ctd5 = ctd5 + 1 
    if ctd0 == 4 and ctd1 == 4:                          # verifica se os () sao ambos apenas 4
        if ctd5 == 7:                                    # verifica se as , sao 7
            if ctd2<=ctd3:                               # verifica se os - sao menores ou iguais aos 1
                if (ctd4+(ctd3-ctd2)+ctd2) == 8:         # se a soma de 0 1 e - e 8
                    return True                          # se isto tudo se verificar podemos considerar que e um tabuleiro
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
#--------------------------------------------------------------------------------------

# Construtor

def str_para_tabuleiro(s):
    if not verifica_se_eh_str_tab(s) :  # funcao aux que verifica e um tabuleiro na forma tuplo de tuplos
        raise ValueError ('str_para_tabuleiro: argumento invalido.')
    lista = []                         # lista para guardar as celulas
    s_novo = eval(s)
    for i in range(len(s_novo)):      
        for j in range(len(s_novo[i])):    # percorre o tabuleiro na forma tuplo de tuplos
            if s_novo[i][j] == -1:     
                lista.append(cria_celula(-1)) 
            elif s_novo[i][j] == 0:    
                lista.append(cria_celula(0))
            elif s_novo[i][j] == 1:    
                lista.append(cria_celula(1))    
    
    return [[lista[0],lista[1],lista[2]],[lista[3],lista[4],lista[5]],[lista[6],lista[7]]]

# Seletores
  
def tabuleiro_dimensao(t):
    return len(t)

def tabuleiro_celula(t,coor):
    return t[coordenada_linha(coor)][coordenada_coluna(coor)]

# Modificadores

def tabuleiro_substitui_celula(t,cel,coor):
    if not (eh_tabuleiro(t) and eh_celula(cel) and eh_coordenada(coor)):
        raise ValueError ('tabuleiro_substitui_celula: argumentos invalidos.')
    else:
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = cel
        return t

def tabuleiro_inverte_estado(t,coor):
    if not (eh_coordenada(coor) and eh_tabuleiro(t)):
        raise ValueError ('tabuleiro_inverte_estado: argumentos invalidos.')
    t[coordenada_linha(coor)][coordenada_coluna(coor)] = inverte_estado(t[coordenada_linha(coor)][coordenada_coluna(coor)]) 
    return t

# Teste

def tabuleiros_iguais(t1,t2):
    if not (eh_tabuleiro(t1) and eh_tabuleiro(t2)):
        return False
    return t1 == t2 
        

# Transformador

def tabuleiro_para_str(t):
    str0 = '+-------+\n|...{2}...|\n|..{1}.{5}..|\n|.{0}.{4}.{7}.|\n|..{3}.{6}..|\n+-------+'
    lista = []      # lista para guardar  os x's , 0's e 1's
    for i in range(tabuleiro_dimensao(t)):      
        for j in range(tabuleiro_dimensao(t[i])):  
            if t[i][j] == cria_celula(-1):     
                lista.append('x')
            elif t[i][j] == cria_celula(0):    
                lista.append('0')
            elif t[i][j] == cria_celula(1):    
                lista.append('1')
    return str0.format(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5],lista[6],lista[7])

#--------------------------operações de alto nivel associadas ao tipo tabuleiro---------------------------------

def porta_x(t,p):
    if (not eh_tabuleiro(t)) or (p!='E' and p!='D'):
        raise ValueError ('porta_x: argumentos invalidos.')
    if p == 'E':
        for i in range(tabuleiro_dimensao(t[1])):       
            t = tabuleiro_inverte_estado(t,cria_coordenada(1,i))
    else:
        for i in range(tabuleiro_dimensao(t[2])):
            t = tabuleiro_inverte_estado(t,cria_coordenada(i,1))
        t = tabuleiro_inverte_estado(t,cria_coordenada(2,0))    # muda o primeiro elemento da 3 lista (pois esta lista so tem 2 elementos, por isso o elemento que precisamos de mudar tem indice 0)
    return t
    
#------------------------------------------------------------------------------------------------------------------    
        
def porta_z(t,p):
    if (not eh_tabuleiro(t)) or (p!='E' and p!='D'):
        raise ValueError ('porta_z: argumentos invalidos.')
    if p == 'E':           
        for i in range(tabuleiro_dimensao(t[0])):
            t = tabuleiro_inverte_estado(t,cria_coordenada(0,i))        
    else:
        for i in range(2):
            t = tabuleiro_inverte_estado(t,cria_coordenada(i,2))
        t = tabuleiro_inverte_estado(t,cria_coordenada(2,1))        
    return t      
#----------------------------------------------------------------------------------------------------    
    
def porta_h(t,p):
    if (not eh_tabuleiro(t)) or (p!='E' and p!='D'):
        raise ValueError ('porta_h: argumentos invalidos.')
    if p == 'E':   
        t = [t[1],t[0],t[2]]
    else:
        t0_novo = [t[0][0],t[0][2],t[0][1]] 
        t1_novo = [t[1][0],t[1][2],t[1][1]] 
        t2_novo = [t[2][1],t[2][0]] 
        t = [t0_novo,t1_novo,t2_novo]
    return t
#------------------------------------------------------------------------------------------------

def hello_quantum(cc):
    X = 'X'
    Z = 'Z'
    H = 'H'
    E = 'E'
    D = 'D'
    i = 0                                 # variavel para guardar o indice de ':'
    jog = 0                               # numero de jogadas
    tab_inicial = tabuleiro_inicial()     # tabuleiro inicial que o jogador vai alterar
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:')
    while i < len(cc):
        if cc[i] == ':':                  # procura o indice do caracter ':'
            break
        i = i + 1
    tab_final = str_para_tabuleiro(cc[0:i])     # tabuleiro objetivo resultante da particao da string dada no caracter ':'
    print(tabuleiro_para_str(tab_final))
    print('Comecando com o tabuleiro que se segue:')
    print(tabuleiro_para_str(tab_inicial))
    while(jog<int(cc[i+1])):                       
        p = input('Escolha uma porta para aplicar (X, Z ou H): ')
        l = input('Escolha um qubit para analisar (E ou D): ')
        if p == X:
            tab_inicial = porta_x(tab_inicial,l)
        elif p == Z:
            tab_inicial = porta_z(tab_inicial,l) 
        elif p == H:
            tab_inicial = porta_h(tab_inicial,l) 
        print(tabuleiro_para_str(tab_inicial))
        jog = jog + 1
        if tabuleiros_iguais(tab_inicial,tab_final):
            break
        
    if tabuleiros_iguais(tab_inicial,tab_final):
        print('Parabens, conseguiu converter o tabuleiro em {} jogadas!'.format(jog))
        return True
    else:
        return False