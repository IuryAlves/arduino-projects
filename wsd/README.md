<h1> WSD </h1>

<h3> Web-Serial-Display </h3>

projeto que pega o dado passado em um input de um formulário web e mostra em um display 16x2 através de um arduino

<h4>  Material </h4>

- Arduino uno ( outros modelos devem funcionar)
- jumpers (fios)
- potenciometro 10k
- display lcd 16x2  
- protoboard
- cabo usb a-b ( cabo de impressora)


<h4>  linguagens utilizadas </h4>

- python
- c/c++
- html5 (linguagem de marcação)

<h4>  Requerimentos </h4>

<h5>  bibliotecas python </h5>
- Flask
- pySerial

<h5>  outros </h5>
-Arduino IDE


<h4>  Instalação </h4>

Se voce tem o pip(python install package) instalado em seu computador, voce pode instalar as dependencias assim:

<code> sudo pip install flask </code> <br>
<code> sudo pip install pySerial </code>

Caso contrário, abaixe elas aqui: 
http://flask.pocoo.org/ <br>
http://sourceforge.net/projects/pyserial/files/

<b> este mini tutorial não cobrirá a instalação e configuração das dependencias! </b>

<h4> Esquema na arduino </h4>

<h5> a posição dos fios que devem ser ligados na arduino e no display
estão na imagem abaixo </h5>

<img src="display-esquema .png">


Ligue o cabo usb na arduino e em seu computador, na IDE da arduino veja em qual porta serial se encontra a arduino.
No programa em python a porta está definida como: <code> /dev/ttyACM2 </code> se for diferente faça os devidos ajustes no arquivo <b>web.py</b>


<h4> Execução </h4>

Compile e passe o programa <code> web_serial_display.ino</code> para  a arduino

No termimal execute o arquivo <b> web.py</b> <code> python web.py </code>
<b> obs </b> o arduino precisa estar conectado na porta usb.
Abra o seu navegador no endereço <code> http://127.0.0.1:5000 </code> e divirta-se! =) 

<b> É provavel que ainda tenha erros, se voce quiser enviar sugestões, alertar sobre erros e problemas você pode abrir uma nova issue ou me enviar um e-mail em: iuryalves20@gmail.com




