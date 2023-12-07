https://github.com/Rat0n02/Fresadora_cnc.git

Introducción: 
una fresadora CNC es una herramienta fundamental en la fabricación moderna. Esta máquina utiliza programación para esculpir, cortar y dar forma a materiales que e este caso nos centramos en la fabricación de diseños de placas CNC.
Al operar con un software especializado, la fresadora CNC puede producir piezas con una precisión increíble, replicando diseños complejos de manera eficiente. Esta tecnología ha revolucionado la industria de la manufactura lo que beneficia a los sectores diversos como la ingeniería y la producción de prototipos.


Justificación: 
la fabricación de este proyecto se hizo con la finalidad de ahorrar tiempo y dinero en la creación de placas CNC, además de que se evita usar sustancias alta mente contaminantes para la creación de las placas.

Objetivo general
Diseñar y fabricar una maquina fresadora CNC enfocada en placas pcb que gracias al movimientos de 3 tornillos sin fin se mueva en lo ejes x, y, z permitiéndole trazar la ruta que el diseño de la placa le pide.

Marco teórico:
 La implementación de una máquina fresadora CNC parala fabricación de PCB, ha sido un tema de estudio de investigación para profesionales en el área de la electricidad y la electrónica, así como también lo ha sido para la industria y algunos centros educativos. Los desarrollos en la implementación de este tipo de prototipos se han dado en diversos campos trayendo consigo grandes avances. Tales el caso de la implementación del CNC en prototipos de máquinas como tornos, fresadoras, cortadoras, etc., con movimientos en sus tres ejes (X, Y, Z) por medio de control numérico computarizado. Los ejes de estas máquinas son movidos por medio de tornillos accionados por servomotores o motores paso a paso. Las señales procedentes del controlador de la maquina son amplificadas por unas unidades, de modo que sean lo suficientemente potentes y adecuadamente programadas para operar los motores.
 
Funcionamiento del CNC 
El sistema de la maquina CNC se divide en tres componentes:
1.software: hace el diseño de PCB mediante un programa de diseño automatizado capaz de generar archivos en formato GRBL. La interfaz del usuario se creo para poder abrir la aplicación que genera el código G que en este caso es Inkscape.
2- hardware electrónico: conformada por los dispositivos electrónicos como es el Arduino uno, la raspberry pi, cnc shield, motores y los drivers DRV8825.
3-Estructura mecánica: corresponde a la estructura que esta formada por los ejes y el motor de fresado. La estructura tiene tres ejes de posicionamiento, tres motores paso a paso encargados de cada movimiento de los ejes y la máquina encargada del fresado. 

INSTRUCCIONES :
Descripción del proceso de funcionamiento 
Dentro de este funcionamiento podemos encontrar nuestra interfaz la cual nos ayudara a indicar que este encendido nuestro programa y podemos arrancarlo cuando se necesite, ten en cuenta que cuando se utiliza esta interfaz no podrás utilizarla cuando tengas las ventanas abiertas (aplicaciones seleccionadas) ya que no te dejara continuar después.
Interfaz:
![image](https://github.com/Rat0n02/Fresadora_cnc/assets/146589981/64f1455f-354e-4bca-afa8-0dc94042def0)

 
Aplicación de Inkscape:
![image](https://github.com/Rat0n02/Fresadora_cnc/assets/146589981/4eae4de2-cbe3-463f-bf77-7684438368f5)

 
Aplicación de g-code universal:
![image](https://github.com/Rat0n02/Fresadora_cnc/assets/146589981/28d51ac6-a0fb-448b-9575-ac240911e3f9)

 
Esta interfaz está conectada a una controladora llamada Raspberry pi 4 la cual nos ayudará a proyectar y correrla de la manera adecuada esta tiene la capacidad de alimentarse desde 3v a 5v máx.
Nuestra controladora estará conectada con un puerto serial directamente a un Arduino por medio de USB. En el Arduino se encontrará previamente conectada una Shield la cual nos controla los motores nema 17 con una alimentación de 12v -10Amp.
El usuario iniciara descargando las aplicaciones correspondientes para que conseguir su objetivo , para esto estarán las aplicaciones de Inkscape el cual nos ayudara a vectorizar y crear nuestro código g a partir de una imagen previamente seleccionana.Una vez teniendo lo anterior dentro de Inkscape configuraremos los parámetros correspondientes a nuestra máquina , como lo es el tamaño de la placa a detallar y la profundidad de nuestro eje z, después de eso generaremos nuestro código G el cual después abriremos en nuestra aplicación de G-code Universal el cual se encarga de leer nuestro código  tal y como lo arroja desde Inkscape.
La funcionalidad de nuestra app G-code Universal es mandar la señal y/o orientación que corresponde a nuestros motores para seguir el patrón que se indicó desde el código generado.

![image](https://github.com/Rat0n02/Fresadora_cnc/assets/146589981/c5b69394-10b9-43db-9129-82bebc570624)

COMO FUNCIONA LA APLICACIONES:
VIDEO QUE PUEDE SER DE  TU AYUDA 
https://www.youtube.com/watch?v=Eou1AIwa6bI&pp=ygUeY29tbyB1c2FyIGlua3NjYXBlICBQQVJBIEdDT0RF 
generar codigo con las medidascorrespondientes 
![image](https://github.com/Rat0n02/Fresadora_cnc/assets/146589981/49b7ece9-f7b0-4de3-9317-8815148556c9)



