# Echo_server
  Projeto feito na diciplina de linguagem de programação do curso de redes de computadores no Intituto Federal de Educação, Ciência e Tecnologia do Maranhão(IFMA).

# Finalidade
  O servidor eco é uma tipo de serviço que retorna tudo o que foi enviado pelo cliente. Ele é feito através de socket que é uma interface de comunicação entre dois host na camada de aplicação. Um socket é definido pelo seu ip e a porta, esta ultima que
  pertencem a camada tranporte.

# Como Funciona
  O projeto é feito em python utilizando uma biblioteca chamada Socket.Primeiramente é necessário importar dentro do código a biblioteca Socket, depois, é necessário criar o servidor que irá receber a requisição do cliente. Para fazer isso, é necessário criar o socket, para cria-lo é necessário chamar a função socket. Esta função tem como parâmetros o tipo de protocolo utilizado para identificação de hosts(socket.AF_INTET) que nesse caso especifica o protocolo ip e o tipo de protocolo usado para o transporte que nesse caso é protocolo TCP(socket.SOCK_STREAM).
  Em seguida, é necessario inicializar o socket, para isso usamos a função bind. Essa função exige dois argumentos, o ip e a porta, ou seja, ela exige o socket. Logo após, é necessário colocar o servidor em modo escuta para ficar esperando os clientes se concectarem, para isso chamamos a função listen. Até esse momento o código só está escutando as requisições, mas não está aceitando
para esse objetivo passamos a função accept que ira pegar as requisições da escuta(listen) e aceita-las. A função accept pode receber duas váriaveis uma corresponde ao obj(os dados) e a outra ao cliente(coresponde ao socket do cliente conectado) é através do obj que o servidor eco envia de volta os dados enviados pelo cliente. 
  
  
