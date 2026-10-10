
import customtkinter as ctk

# Configuración de apariencia
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# Definir la clase
class AppHello(ctk.CTk):

    # Constructor
    def __init__(self):
        super().__init__()

        # Configurar ventana
        self.title("Hello World with CustomTkinter")
        self.geometry("300x150")

        # Texto en la ventana
        self.lbl = ctk.CTkLabel(
            self,
            text="Hello...",
            font=("Arial", 24, "bold")
        )
        self.lbl.pack(pady=20)

        # Botón para mostrar el mensaje
        self.btn = ctk.CTkButton(
            self,
            text="Mostrar",
            command=self.mostrar_mensaje
        )
        self.btn.pack(pady=10)

    # Método que se ejecuta al presionar el botón
    def mostrar_mensaje(self):
        self.lbl.configure(text="Hello, world!")


# Crear el objeto e iniciar la aplicación
if __name__ == "__main__":
    app = AppHello()
    app.mainloop()
