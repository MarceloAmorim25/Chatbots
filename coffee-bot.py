def cafe_bot():
  print("Seja bem-vindo!")
  size = tamanho_cafe()
  cafe_tipo = tipo_de_cafe()
  print('Então foi um café {}, {}!'.format(size,cafe_tipo))
  nome = input('Poderia me dizer seu nome?')
  print('Obrigado, {}! Seu café já estará pronto.'.format(nome))
  
  
def tamanho_cafe():
  resposta = input('Qual o tamanho do café? \n[a] pequeno \n[b] médio \n[c] grande \n>')
  
  if resposta == 'a': 
    return 'pequeno'
  elif resposta == 'b':
    return 'médio'
  elif resposta == 'c':
    return 'grande'
  else: 
    printar()
    return tamanho_cafe()

def printar():
    print('Me desculpe, não entendi seu pedido =( Poderia repetir?')

def tipo_de_cafe():
    resposta = input('Qual o tipo do café? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')    
    if resposta == 'a': 
      return 'brewed coffee'
    elif resposta == 'b':
      return 'mocha'
    elif resposta == 'c':
      return pedido_latte()
    else: 
      printar()
      return tipo_de_cafe()

def pedido_latte():
      resposta = input('Qual o tipo de leite para o seu latte? \n[a] 2% milk \n[b] Desnatado \n[c] Leite de soja\n>')
      if resposta == 'a': 
        return 'latte'
      elif resposta == 'b':
        return 'desnatado'
      elif resposta == 'c':
        return 'leite de soja'
      else: 
        printar()
        return tipo_de_cafe()
    


cafe_bot()
