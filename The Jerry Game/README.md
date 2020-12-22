-Para un correcto funcionamiento se recomienda abrir la carpeta "The_Jerry_Games" 
 dentro de su editor de texto.

-El juego se encuentra disponible en el archivo "main.py".

-Mantener las carpetas de los sprites en la carpeta "The_Jerry_Games".

-En caso de guardar los archivos en otra ubicacion (fuera de la carpeta contenedora)
 debera editar las siguientes rutas en el archivo "main.py":
	
	83. self.background
	89. self.jerry_Character
	94. self.enemy_Character_1
	100. linea 100 self.enemy_Character_2
	106. linea 106 self.enemy_Character_3

-Tambien debera editar la siguiente ruta en el archivo "clases.py":
	
	134. self.sheet
	163. self.sheet

-Para utilizar solamente el teclado:
	
	-Desconectar el Arduino.
	-Abrir el Archivo "main.py".
	-Dirigirse a la linea 34 y comentar "self.initialize()" con un "#".
	-Dirigirse a la linea 141 y comentar desde [linea 141:linea 150] con """
 
-Si usted detecta algun bug porfavor comunicarlo.
