import pygame as pg
import constantes
import pygame_textinput as pg_textinput
import PySimpleGUI as sg

pg.font.init()
fontP = pg.font.get_default_font()
fontE = pg.font.match_font('Verdana',0,1)
fontT = pg.font.SysFont('Times New Roman',30,0,0)
fontI = pg.font.SysFont(fontP,45)
fontMenor = pg.font.SysFont(fontP,25)
fonteTextoE = pg.font.SysFont(fontE,30)
#fontTimes = pg.font.SysFont(fontT,30)
#ret = pg.Rect(200,40,200,80)
pg.mixer.init()
pg.mixer.Sound('somAcerto.wav')
pg.mixer.Sound('somFase.wav')
somAcerto = pg.mixer.Sound('somAcerto.wav')
somFase = pg.mixer.Sound('somFase.wav')
screen = pg.display.set_mode((0,0))
clock = pg.time.Clock()
sg.theme('Dark Grey 13')
pos = pg.image.load('fogos.png').convert()
pg.display.set_caption('Investigation')
                        #############   CAIXAS DE TEXTOS #############
manager = pg_textinput.TextInputManager(validator=lambda input: len(input) <= 55)
textinput = pg_textinput.TextInputVisualizer(manager=manager, font_object=fontT)
#pg.key.set_repeat(500, 50) # press every 50 ms after waiting 200 ms
textinput.cursor_blink_interval = 300 # blinking interval in ms
textinput.antialias = True

"""
#pg.key.set_repeat(200, 25)
esperando = True
while esperando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            esperando = False
        if event.type == pg.KEYUP:
            esperando = False
"""

#x = 1280
#y = 720
greenMark = pg.image.load('greenMark.png').convert_alpha()
greenMark = pg.transform.scale((greenMark),(120,120))
greenMark2 = pg.transform.scale((greenMark),(180,180))
class GameState():
    def __init__(self):
        self.state = 'intro'

   
    def intro(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
        
            if event.type == pg.KEYUP:
                self.state = 'nivel1t1'
        
        telaInicio = pg.image.load('inicio.png').convert()
        screen.blit(telaInicio,(0,0))
        pg.display.flip()

    def nivel1t1(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he has black hair and brown eyes':
                pg.mixer.Sound.play(somAcerto)
                screen.blit(greenMark,(700,100))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'nivel1t2'
                
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he has black hair and brown eyes':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')

                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('Sempre formule frases no presente e com todas letras min??sculas\n *Aten????o para as regras: No ingl??s, quando falamos da condi????o que um sujeito se encontra, utilizamos o verbo To Be, que quando usado para se referir a terceira pessoa do singular(ele,ela/he, she) ele(o verbo) sofre altera????o, geralmente sofre adi????o de S, veja exemplos:\n Cleiton joga futebol todos os dias // Cleiton plays soccer everyday\n M??rcia tem dois cachorros// Marcia has two dogs\n Gloss??rio de poss??veis op????es: black - preto, brown - marrom/castanho, blue - azul, hair - cabelo, eyes = olhos',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('i1_jogo_720p.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('Descreva a cor do cabelo e dos olhos ',32,constantes.cBlue)
        screen.blit(comecoCabelo,(400,100))
                
        pg.display.flip()
        pg.display.update()

    def nivel1t2(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he is thin and average height':
                pg.mixer.Sound.play(somAcerto)
                screen.blit(greenMark,(700,100))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'nivel1t3'
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he is thin and average height':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')

                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('Para esta quest??o em espec??fico diga exatamente a estrutura corporal(gordo/magro) e(and) a altura\n formula????o: ele ?? |. . .|  e |. . .|\nGloss??rio de poss??veis op????es: Tall = alto, short = baixo, average height = estatura(altura) m??dia\n thin = magro, fat = gordo',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('i1_jogo_720p.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('O suspeito ?? magro ou gordo? alto ou baixo?',32,constantes.cBlue)
        screen.blit(comecoCabelo,(400,100))
                
        pg.display.flip()
        pg.display.update()
    def nivel1t3(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he wears red and purple jacket with shorts jeans' or event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he wears purple and red jacket with shorts jeans':
                pg.mixer.Sound.play(somFase)
                screen.blit(greenMark2,(1365/2,720/2))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'nivel2t1'
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he wears red and purple jacket with shorts jeans':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')
                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('A formula????o da frase ??: Ele veste |.... | com  |. . .|\n Gloss??rio de possiveis op????es: wear = veste, white t-shirt = camisa branca, red jacket and white = casaco vermelho e branco, purple shorts = shorts roxo',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('i1_jogo_720p.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('Descreva as roupas do suspeito, primeiro a superior logo em seguida a inferior ',32,constantes.cBlue)
        screen.blit(comecoCabelo,(250,100))
                
        pg.display.flip()

    def nivel2t1(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he is bald and he has blue eyes' or event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he has no hair and he has blue eyes' :
                pg.mixer.Sound.play(somAcerto)
                screen.blit(greenMark,(700,100))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'nivel2t2'
                
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he is bald and he has blue eyes'or event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he has no hair and he has blue eyes':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')

                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('Formula????o da resposta: ele ?? |...| // ele n??o possui |...| e possui |....| olhos\nPara este indiv??duo voc?? pode dizer se ele n??o possui cabelos ou se ?? careca, no ingles s??o coisas \'diferentes\'\n Gloss??rio de poss??veis op????es: Have no = n??o tem/n??o possui, bald = careca ',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('suspeito2.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('Descreva o cabelo e a cor dos olhos do suspeito ',32,constantes.cBlue)
        screen.blit(comecoCabelo,(400,100))
                
        pg.display.flip()
        pg.display.update()

    def nivel2t2(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he is fat and tall':
                pg.mixer.Sound.play(somAcerto)
                screen.blit(greenMark,(700,100))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'nivel2t3'
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he is fat and tall':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')

                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('Formula????o da resposta: ele ?? (gordo ou magro) e (alto ou baixo)',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('suspeito2.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('Descreva se ele ?? gordo/magro e alto/baixo',32,constantes.cBlue)
        screen.blit(comecoCabelo,(400,100))
                
        pg.display.flip()
        #pg.display.update()
   
    def nivel2t3(self):
        #cria retangulo pra animar lampada com colis??o
        rect = pg.Rect(*screen.get_rect().bottomleft, 200, 10).inflate(290, 490)
        point = pg.mouse.get_pos()
        collide = rect.collidepoint(point)
        #pg.draw.rect(screen, (255,20,200), rect)
        
        events = pg.event.get()     ########## DISPARA EVENTOS ###########
        for event in events:
            if event.type == pg.QUIT:
                exit()
                                    ########## Le eventos ###########
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he does not wears a shirt and he wears a green shorts' or event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he only wears a green shorts':
                pg.mixer.Sound.play(somFase)
                screen.blit(greenMark2,(1365/2,720/2))
                pg.display.flip()
                pg.time.delay(100)
                self.state = 'pos'
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value != 'he does not wears a shirt and he wears a green shorts' or event.type == pg.KEYDOWN and event.key == pg.K_RETURN and textinput.value == 'he only wears a green shorts':
                sg.popup('Voc?? digitou errado, confira as dicas e tente novamente')
                                     ########## DISPARA DICAS ###########
            if event.type == pg.MOUSEBUTTONDOWN and collide:
             sg.popup('Aqui vai uma coisa nova :)\n voc?? pode dizer se ele n??o est?? usando camisa e est?? usando um shorts, ou voc?? pode optar por dizer que ele somente/apenas veste um shorts\n Note que para negar uma a????o voc?? precisar?? de um verbo auxiliar, que conhecemos por Do ou Does\n o Do ?? geralmente atribu??do a primeira pessoa do singular, enquanto que o Does ?? atribu??do para a terceira\n ou seja se quiser dizer que ele nao veste uma camisa ter?? que usar he does not (nega????o)\n Gloss??rio poss??veis op????es: Do/ do not, does/ does not\n only = apenas/somente/s??\n formula????o da resposta: ele n??o usa uma camisa e usa shorts verdes // ele somente usa um shorts verdes',title=('Dicas'))
                                    ########## ELEMENTO PRINCIPAL FASE1 ###########
        criminoso = pg.image.load('suspeito2.png').convert()
        screen.blit(criminoso,(0,0))
                                    ########## LAMPADA ###########
        lampada = pg.image.load('lampadaO.png').convert_alpha()
        lampada = pg.transform.scale((lampada),(156,160))
        screen.blit(lampada,(200,500))
        #pg.display.flip()
                                    ########## REPRODUZ INPUT TEXT ###########
        textinput.update(events)
        # Blit its surface onto the screen
        screen.blit(textinput.surface, (400, 135))
        pg.display.flip()
                                    ########## LEGENDA SOB LAMP ###########
        dicaLamp = fontMenor.render('Clique na l??mpada e aguarde dicas',1,(0,0,0),None)
        screen.blit(dicaLamp,(140,500))
        #pg.display.flip()
        
                                    ########## INSTRUCAO DOQ FAZER ###########
        comecoCabelo = fonteTextoE.render('Descreva as roupas do indiv??duo ',32,constantes.cBlue)
        screen.blit(comecoCabelo,(400,100))
                
        pg.display.flip()
  
    def pos(self):
        events = pg.event.get()
        pg.mixer.Sound.play(somFase)
        for event in events:
            if event.type == pg.QUIT:
                exit()
        pg.time.delay(100)
        screen.blit(pos,(70,0))
        pg.display.flip()

    def controlador(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'nivel1t1':
            self.nivel1t1()
        if self.state == 'nivel1t2':
            self.nivel1t2()
        if self.state == 'nivel1t3':
            self.nivel1t3()
        if self.state == 'nivel2t1':
            self.nivel2t1()
        if self.state == 'nivel2t2':
            self.nivel2t2()
        if self.state == 'nivel2t3':
            self.nivel2t3()
        if self.state == 'pos':
            self.pos()
        
        

pg.init()
game_state = GameState()
Clock = pg.time.Clock()
while True:
    game_state.controlador()
    clock.tick(30)
