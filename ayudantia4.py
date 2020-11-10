
import tkinter as tk 
import parser

window = tk.Tk()

window.title("Calculadora")

display = tk.Entry(window)
display.grid(row=1, columnspan= 4, sticky= tk.W +tk.E)

i=0

def get_number(n):
	global i
	display.insert(i,n)
	i+=1

def get_operation(operador):
	global i
	largo_operador = len(operador)
	display.insert(i,operador)
	i+=largo_operador

def clear_display():
	display.delete(0,tk.END)

def eliminar():
	display_state = display.get()
	if len(display_state):
		display_new_state = display_state[:-1]
		clear_display()
		display.insert(0, display_new_state)

	else:
		clear_display()
		display.insert(0,'Error')

def calcular():
	display_state = display.get()
	try:
		expresion_matematica = parser.expr(display_state).compile()
		resultado = eval(expresion_matematica)
		clear_display()
		display.insert(0,resultado)

	except Exception:
		clear_display()
		display.insert(0,'Error')

#cambiar el signo
def signo():
	display_state = display.get()
	if len(display_state):
		if(display_state[0] == '-'):
			display_new_state = display_state[1:len(display_state)]
		else:
			display_new_state = "-"+ display_state
		clear_display()
		display.insert(0,display_new_state)
	else:
		clear_display()
		display.insert(0,'Error')

#fila 1
tk.Button(window, text= "AC", width= 4, height=2, command= lambda: clear_display()).grid(row=2, column=0,  sticky= tk.W +tk.E)
tk.Button(window, text= "+/-", width= 4, height=2, command= lambda: signo()).grid(row=2, column=1,  sticky= tk.W +tk.E)
tk.Button(window, text= "%", width= 4, height=2, command= lambda:get_operation('%')).grid(row=2, column=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "/", width= 4, height=2, command= lambda:get_operation('/')).grid(row=2, column=3,  sticky= tk.W +tk.E)

#fila2
tk.Button(window, text= "1", width= 4, height=2, command= lambda:get_number(1)).grid(row=3, column=0,  sticky= tk.W +tk.E)
tk.Button(window, text= "2", width= 4, height=2, command= lambda:get_number(2)).grid(row=3, column=1,  sticky= tk.W +tk.E)
tk.Button(window, text= "3", width= 4, height=2, command= lambda:get_number(3)).grid(row=3, column=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "x", width= 4, height=2, command= lambda:get_operation('*')).grid(row=3, column=3,  sticky= tk.W +tk.E)

#fila3
tk.Button(window, text= "4", width= 4, height=2, command= lambda:get_number(4)).grid(row=4, column=0,  sticky= tk.W +tk.E)
tk.Button(window, text= "5", width= 4, height=2, command= lambda:get_number(5)).grid(row=4, column=1,  sticky= tk.W +tk.E)
tk.Button(window, text= "6", width= 4, height=2, command= lambda:get_number(6)).grid(row=4, column=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "-", width= 4, height=2, command= lambda:get_operation('-')).grid(row=4, column=3,  sticky= tk.W +tk.E)

#fila4
tk.Button(window, text= "7", width= 4, height=2, command= lambda:get_number(7)).grid(row=5, column=0,  sticky= tk.W +tk.E)
tk.Button(window, text= "8", width= 4, height=2, command= lambda:get_number(8)).grid(row=5, column=1,  sticky= tk.W +tk.E)
tk.Button(window, text= "9", width= 4, height=2, command= lambda:get_number(9)).grid(row=5, column=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "+", width= 4, height=2, command= lambda:get_operation('+')).grid(row=5, column=3,  sticky= tk.W +tk.E)

#fila5
tk.Button(window, text= "0", width= 4, height=2, command= lambda:get_number(0)).grid(row=6, columnspan=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "←", width= 4, height=2, command= lambda: eliminar()).grid(row=6, column=2,  sticky= tk.W +tk.E)
tk.Button(window, text= "=", width= 4, height=2, command= lambda: calcular()).grid(row=6, column=3,  sticky= tk.W +tk.E)
window.mainloop()