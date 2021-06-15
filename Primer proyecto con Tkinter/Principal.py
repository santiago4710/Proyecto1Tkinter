from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


raiz = Tk()

#Windows settings
raiz.geometry("500x500")
raiz.title("First project with Tkinter")
raiz.resizable(0,0)



# Pantallas para cada menu

def home():
	# encabezado
	principal_label.config(fg="white",bg="black", font=("Italy",25),padx=220,pady=20)
	principal_label.grid(row=0, column=0)


	
	products_table.grid(row=1, column=0, columnspan=2)
	products_table.config(yscrollcommand=scroolbar_text.set)

	# listar los productos cuando los completemos

	'''for productos in products:
		if len(productos) == 3:
			productos.append("added") # solo se muestran los nuvos campos de la lista y no repiten
			Label(products_box, text=productos[0]).grid()
			Label(products_box, text=productos[1]).grid()
			Label(products_box, text=productos[2]).grid()
			Label(products_box, text="-------------------------------------------").grid()
			Label(products_box, text="\n").grid()'''


	for productos in products:
		if len(productos) == 3:
			productos.append("added") # solo se muestran los nuevos campos de la lista y no repiten
			products_table.insert('',0,text=productos[0],values=(productos[1]))

	# Ocultar pantallas 
	
	agregar_label.grid_remove()
	acerca_label.grid_remove()
	agregar_frame.grid_remove()

	return True


def add():	

	agregar_frame.grid(row=1)
	
	agregar_label.config(fg="white",bg="black", font=("Italy",25),padx=120,pady=20)
	agregar_label.grid(row=0, column=0, columnspan=12)

	#Campos del formulario

	add_name_label.grid(row=1, column=0, padx=5, pady=5,sticky=W)
	add_name_entry.grid(row=1, column=1, padx=5, pady=5,sticky=W)

	add_price_label.grid(row=2, column=0, padx=5, pady=5,sticky=W)
	add_price_entry.grid(row=2, column=1, padx=5, pady=5,sticky=W)

	add_description_label.grid(row=3, column=0, padx=5, pady=5,sticky=NW)
	add_description_entry.grid(row=3, column=1, padx=5, pady=5,sticky=W)
	add_description_entry.config(width=30, height=5, font=("Italy",12), padx=15, pady=15, yscrollcommand=scroolbar_text.set)

	scroolbar_text.grid(column=2,row=3, sticky="nsew")

	boton.grid(row=4,column=1,sticky=N)



	# Ocultar pantallas 
	principal_label.grid_remove()
	acerca_label.grid_remove()
	products_box.grid_remove()
	products_table.grid_remove()
	infoLabel.grid_remove()



	return True



def add_products():
	#para obtener los datos al apretar al boton guardar
	products.append([
		name_data.get(),
		price_data.get(),
		add_description_entry.get("1.0", "end-1c")]) # ponemos asi para que nos retorne Text

	# introducimos los productos dentro de la bbdd
	miconexion = sqlite3.connect("Productos")
	elcursor = miconexion.cursor()
	elcursor.execute("INSERT INTO Productos_Tienda VALUES(NULL,'" + name_data.get() + "','" + price_data.get() + "','" + add_description_entry.get("1.0", END) + "')")
	miconexion.commit()
	messagebox.showinfo("Producto", "Se ha registrado correactamente el producto en la bbdd")



	name_data.set("")
	price_data.set("")
	add_description_entry.delete("1.0", END) #standar para un Text

	print(products)

	home()



def info():

	acerca_label.config(fg="white",bg="black", font=("Italy",25),padx=160,pady=20)
	acerca_label.grid(row=0, column=0)

	infoLabel.grid(row=1)

	# Ocultar pantallas 
	principal_label.grid_remove()
	agregar_label.grid_remove()
	agregar_frame.grid_remove()
	products_box.grid_remove()
	products_table.grid_remove()




	return True

# creacion de la bbdd
def basedatos():

	conexion = sqlite3.connect("Productos")

	cursor = conexion.cursor()

	try:
		cursor.execute('''
			CREATE TABLE Productos_Tienda(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_PRODUCTO VARCHAR(70),
			PRECIO VARCHAR(10),
			DESCRIPCION VARCHAR(150))''')

		mensaje = messagebox.showinfo("BASE DE DATOS", "Se ha creado con exito la base de datos")

	except:
		mensaje2 = messagebox.showwarning("BASE DE DATOS", "Ya se encuentra existente la base de datos")

# campos de cada campo de pantallas
principal_label = Label(raiz, text="Inicio")
agregar_label = Label(raiz, text="Agregar productos")
acerca_label = Label(raiz, text="Acerca de mi")




#variables
products = []
name_data = StringVar()
price_data = StringVar()

# campos para formulario
agregar_frame = Frame(raiz)

# Nombre producto
add_name_label = Label(agregar_frame,text='Nombre del producto:')
add_name_entry = Entry(agregar_frame,textvariable= name_data)


# Precio del producto
add_price_label = Label(agregar_frame,text='Precio del producto:')
add_price_entry = Entry(agregar_frame,textvariable= price_data)

# descripcion del producto
add_description_label = Label(agregar_frame, text="Descripcion:")
add_description_entry = Text(agregar_frame)
scroolbar_text = Scrollbar(agregar_frame,command=add_description_entry.yview)

boton= Button(agregar_frame,text="Guardar producto", command=add_products)
boton= Button(agregar_frame,text="Guardar producto", command=add_products)


infoLabel = Label(raiz,text='Esto es un primer proyecto de tkinter por Santiago Fajardo')

# campos en inicio
home_label = Label(raiz, text="")
products_box = Frame(raiz,width=250)
products_box.grid(row=1)

# tabla para el inicio
Label(products_box).grid(row=0)
products_table = ttk.Treeview(height=12, columns=2)



	# creamos la columna
products_table.heading("#0",text="Producto",anchor=W)
products_table.heading("#1",text="Precio",anchor=W)





# Cargar pantalla inicio
home()

#Menu 
menu = Menu(raiz)
menu.add_command(label = "Inicio", command=home)
menu.add_command(label = "conectar bbdd", command=basedatos)
menu.add_command(label = "Añadir productos", command=add)
menu.add_command(label = "Acerca de", command=info)
menu.add_command(label = "Salir", command = raiz.quit) 


#Introducir el menu dentro de la raiz
raiz.config(menu=menu)



raiz.mainloop()