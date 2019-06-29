from nltk.chat.util import Chat

pares = [
 
    [ 
        r"oi|olá|ola|bom dia|boa tarde|boa noite|ta bom|tudo bem|ok|vamos em frente|ok beleza|ok, beleza|pode ser", 
        ["FomeBot: Você sabe que tipo de restaurante está procurando?"]
    ],

    [ 
        r"((nordestina|baiana|nordestino|restaurante nordestino|restaurante baiano|baiano|restaurante de comida nordestina|de comida nordestina|de comida baiana|comida nordestina|comida baiana|vatapá|vatapa|mocotó|mocoto|dende|acaraje|acarajé)|(.*) (nordestina|baiana|nordestino|restaurante nordestino|restaurante baiano|baiano|restaurante de comida nordestina|de comida nordestina|de comida baiana|comida nordestina|comida baiana|vatapá|vatapa|mocotó|mocoto|dende|acaraje|acarajé))", 
        ["FomeBot: Para comida com gostinho do nordeste sugiro o Iaiá Bistrô.\nO menu é típico do nordeste como pato no tucupi e vatapá,\ncom charmoso deque, do almoço ao happy hour e jantar.\nEle fica na Rua Chavantes de 636, bairro Assunção\nPreço médio de 120,00 por pessoa.\n\nAberto de:\nterça à sexta 19:00 - 23:00\nsábado 12:00 - 15:00, 19:00 - 23:00\ndomingo: 12:00-15:30\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
		

    [ 
        r"((francês|francesa|restaurante francês|restaurante frances|frances|restaurante de comida francesa|de comida francesa|comida francesa)|(.*) (francês|francesa|restaurante francês|restaurante frances|frances|restaurante de comida francesa|de comida francesa|comida francesa))", 
        ["FomeBot: Se você quiser se sentir em um filme francês eu sugiro o Le Bateau Ivre.\n Esse restaurante tem pratos clássicos, champanhe, flores e arte e se localiza na Rua Tito Lívio Zambecari número 805, bairro Mont'Serrat\nAberto de terça à sábado 20:00 - 00:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((vegetariano|vegetariana|restaurante vegetariano|restaurante de comida vegetariana|comida vegetariana|sem carne)|(.*) (vegetariana|vegetariano|restaurante vegetariano|restaurante de comida vegetariana|comida vegetariana|sem carne))", 
        ["FomeBot: Uma ótima sugestão é o restaurante Prato Verde.\nEle é um buffet vegetariano super aconchegante com vista para um jardim,\nserve opções de comida saudável há muitos anos.\n\nLocalizado na Rua Santa Terezinha, 42, bairro Bom Fim\nAberto de:\nsegunda à sexta 11:00 - 14:30\nsábado e domingo 11:00 - 15:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((vegano|vegana|restaurante vegano|restaurate de comida vegana|comida vegana)|(.*) (vegano|vegana|restaurante vegano|restaurate de comida vegana|comida vegana))", 
        ["FomeBot: Ótima escolha! Sugiro o restaurante Bonobo, é um dos meus favoritos.\nEle é um restaurante vegano, ecológico e aconchegante,\ncom espaço cultural e decoração rústica.\n\nLocalizado na R. Castro Alves, 101 - Independência\nAberto de quarta à domingo 12:00 - 14:30\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((alemão|alemã|alemao|restaurante alemão|restaurante alemao|restaurante de comida alemã|comida alemã|de comida alemã|chopp|chope)|(.*) (alemão|alema|alemao|restaurante alemão|restaurante alemao|restaurante de comida alemã|comida alemã|de comida alemã|chopp|chope))", 
        ["FomeBot: Kühl! O Ratskeller é um restaurante alemão tradicional e aconchegante,\ncom serviço de bufê que inclui salsicha, pato e truta.\nLocalizado na Av. Pará, 1324 - São Geraldo\nAberto de:\nterça à sexta 11:30 - 14:00, 19:00-23:30\nsábado 11:30 - 14:30, 19:00 - 23:30\ndomingo: 11:30 - 15:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((japonês|japones|japonesa|restaurante japonês|restaurante japones|restaurante de comida japonesa|comida japonesa|de comida japonesa|sushi)|(.*) (japonês|japonesa|japones|restaurante japonês|restaurante japones|restaurante de comida japonesa|comida japonesa|de comida japonesa|sushi))", 
        ["FomeBot: Pra aproveitar o melhor da culinária niponica sugiro o Sushi by Cleber.\nO restaurante é moderno e original\n serve pratos asiáticos inovadores e contemporâneos.\n\nLocalizado na Rua Desembargador Espiridião de Lima Medeiros, 317 - Três Figueiras\n Aberto todos os dias das 18:30 - 23:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((frutos do mar|de frutos do mar|restaurante de frutos do mar)|(.*) (frutos do mar|de frutos do mar|restaurante de frutos do mar))", 
        ["FomeBot:Sugiro o Candido's Frutos do mar.\nEspecializado em frutos do mar, oferece pratos clássicos e bebidas,\nem salão tradicional com aquário.\n\nLocalizado na Av. Pará, 1281 - Navegantes\nAberto de terça à sexta das 11:30-14:00 e sábado 11:30 - 14:30, 19:00 - 23:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((asiático|asiática|chinês|indiano|asiatico|asiatica|chines|restaurante chinês|restaurante chines|restaurante indiano|restaurante de comida asiática|restaurante asiático|de comida asiática|comida asiática)|(.*)(asiático|asiática|chinês|indiano|asiatico|asiatica|chines|restaurante chinês|restaurante chines|restaurante indiano|restaurante de comida asiática|restaurante asiático|de comida asiática|comida asiática))", 
        ["FomeBot: O Restaurante Galangal é uma ótima opção.\nGastronomia tailandesa sofisticada e chamativa\nem ambiente convidativo e envolvente de temas asiáticos marcantes.\nFaixa de preço de R$56 - R$99.\n\nLocalizado na Rua Dona Laura, 196 - Rio Branco.\nAberto de segunda à sexta 19:00 - 23:30 e sábado 12:00 - 16:00, 19:00 - 23:30\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
    
    [ 
        r"((churrascaria|churrasco)|(.*) (churrascaria|churrasco))", 
        ["FomeBot: Que tal a Currascaria Porto Alegre?\nRestaurante casual que serve churrasco e pratos do cotidiano,\nem buffet variado com opções regionais e sobremesas.\nPreços a partir de 19,90.\n\nLocalizado na  Av. São Pedro, 934 - São Geraldo.\nAberto de:\nterça à sexta das 11:30 - 14:00\nsábado 11:30 - 15:00, 18:00 - 22:00\ndomingo 11:00 - 15:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
    
    [ 
        r"((pizzaria|pizza)|(.*) (pizzaria|pizza))", 
        ["FomeBot: Considere a Nono Ludovico.\nUma grande e tranquila pizzaria com sabores e opções tradicionais,\nalém de um salão para festas e reuniões.\n\nLocalizado na Av. Lavras, 328 - Petrópolis.\nAberto todos os dias das 19:00 - 23:30\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
    
    [ 
        r"((italiano|italiana|restaurante italiano|de comida italiana|comida italiana|restaurante de comida italiana)|(.*) (italiano|italiana|restaurante italiano|de comida italiana|comida italiana|restaurante de comida italiana))", 
        ["FomeBot: Sugiro o restaurante Peppo Cucina.\nCom cantina à luz de velas e obras de arte.\nPreço médio de 140,00 por pessoa.\n\nLocalizado na R. Dona Laura, 161 - Rio Branco.\nAberto de:\nsegunda à quinta das 11:30 - 14:30, 18:00 - 00:00,\nsexta 11:30 - 14:30, 18:00 - 01:00\nsábado 11:30 - 16:00, 18:00 - 01:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
    
    [ 
        r"((australiano|australiana|restaurante australiano|de comida australiana|comida autraliana|restaurante de comida australiana)|(.*) (australiano|australiana|restaurante australiano|de comida australiana|comida autraliana|restaurante de comida australiana))", 
        ["FomeBot: Sugiro o restaurante Hooro - Australian Pub.\nBar e cozinha australiana.\nCom temperos sul-americanos, buffet livre no almoço e hambúrguer à noite.\n\nLocalizado na R. Fernandes Vieira, 466 - Bom Fim.\nAberto de:\nterça à quinta das 11:30 - 14:30, 18:00 - 00:00,\nsexta 18:00 - 00:00,\nsábado 11:30 - 14h:30, 18:00 - 00:00,\ndomingo 11:30-15:00, 18:00-23:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"((buffet livre|bifê livre|bife livre|bufê livre|bufe livre)|(.*) (buffet livre|bifê livre|bife livre|bufê livre|bufe livre))", 
        ["FomeBot: Sugiro o restaurante Via Napoli.\nGastronomia do dia a dia no buffet caseiro apurado,\nservido em ambiente casual e impessoal de rotatividade.\n\nLocalizado na R. Barão do Triunfo, 732 - Azenha.\nAberto de segunda à sábado das 11:00 - 15:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],
    
    [ 
        r"((mexicano|mexicana|restaurante mexicano|de comida mexicana|restaurante de comida mexicana|comida mexicana)|(.*) (mexicano|mexicana|restaurante mexicano|de comida mexicana|restaurante de comida mexicana|comida mexicana))", 
        ["FomeBot: Sugiro o restaurante Guacamole Cocina Mexicana.\nCom pratos típicos e músicas tocadas por um grupo de mariachis.\nPreço médio de 80,00 por pessoa.\n\nLocalizado na R. Des. Augusto Loureiro Lima, 165 - Petrópolis.\nAberto de domingo à quinta das 18:00 - 00:30, sexta e sábado das 18:00 - 00:00\n\nGostaria de uma sugestão de outro tipo de restaurante?"]
    ],

    [ 
        r"achei caro|é caro|muito caro|não gostei do preço|preço salgado|nossa que caro, achei muito caro", 
        ["FomeBot: Que pena :( \nQuem sabe posso lhe sugerir um outro restaurante?"]
    ],
	
    [ 
        r"sim|sim, obrigada|sim, obrigado|sim obrigada|sim obrigado", 
        ["FomeBot: Que tipo de restaurante você procura?"]
    ],

    [ 
        r"não sei|nao sei|nao|não|não, obrigada|não, obrigado|não obrigada|não obrigado|nao obrigado|nao obrigada|não obrigado|não obrigada", 
        ["FomeBot: Se já estiver satisfeito, foi um prazer ajudar você :)\n\nse não...\nHmm...Que tipo de comida você está com vontade de comer?"]
    ],

    [ 
        r" |(.*)", 
        ["FomeBot: desculpe, não entendi, pode repetir?"]
    ]

,]    

def chatty():
    print("FomeBot: Olá, eu sou o FomeBot, vou tentar te ajudar a encontrar a melhor opção de restaurante em Porto Alegre para matar a sua fome!")
    chat = Chat(pares)
    chat.converse()
if __name__ == "__main__":
    chatty()
        
