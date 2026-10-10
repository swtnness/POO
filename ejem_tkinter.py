
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
        self.title("Multiplicar")
        self.geometry("300x150")
        
        self.configure(fg_color="#F5BBD3")

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
            command=self.mostrar_mensaje,
            fg_color="#F48FB1",
            hover_color="#EC407A",
            text_color="#661136",
            corner_radius=15
        )
        self.btn.pack(pady=10)

    # Método que se ejecuta al presionar el botón
    def mostrar_mensaje(self):
        self.lbl.configure(text="Hello, world!")


# Crear el objeto e iniciar la aplicación
if __name__ == "__main__":
    app = AppHello()
    app.mainloop()
