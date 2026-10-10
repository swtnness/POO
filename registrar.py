import customtkinter as ctk

# Configure the graphical environment
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


# Define the class
class RegistrationListApp(ctk.CTk):

    # Constructor
    def __init__(self):
        super().__init__()  # Create the graphical window
        # Set the window title
        self.title("User Registration")
        # Set the window dimensions
        self.geometry("400x450")
        # Set the window background to soft pink
        self.configure(fg_color="#FFF0F5")
        # Disable window resizing
        self.resizable(False, False)
        # APPLICATION STATE (OOP)
        # LIST TO STORE DATA
        self.data_list = []  # Create an empty list
        # Call the method to build the interface elements
        self.create_widgets()

    # Helper method responsible for creating and positioning components
    def create_widgets(self):

        # Main window heading
        self.title_label = ctk.CTkLabel(
            self,
            text="Data Manager",
            font=("Arial", 20, "bold"),
            text_color="#B56591"
        )
        self.title_label.pack(pady=(15, 5))
        # Container to align the text field and button
        self.input_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.input_frame.pack(
            pady=10,
            padx=20,
            fill="x"
        )
        # Text field for entering new data
        self.data_entry = ctk.CTkEntry(
            self.input_frame,
            width=200,
            placeholder_text="Enter your name",
            fg_color="#FFFFFF",
            border_color="#EFA3C8",
            text_color="#444444",
            placeholder_text_color="#B58CA4"
        )
        self.data_entry.pack(
            side="left",
            padx=(0, 10)
        )
        # Register button
        self.register_button = ctk.CTkButton(
            self.input_frame,
            text="Register",
            width=100,
            fg_color="#EFA3C8",
            hover_color="#D989B5",
            text_color="#FFFFFF",
            command=self.register_data
        )
        self.register_button.pack(side="left")
        # Scrollable container
        self.scroll_list = ctk.CTkScrollableFrame(
            self,
            label_text="Items Saved in the List",
            fg_color="#F8C8DC",
            label_fg_color="#EFA3C8",
            label_text_color="#FFFFFF"
        )
        self.scroll_list.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(10, 5)
        )
        # Label to display the total number of registered items
        self.counter_label = ctk.CTkLabel(
            self,
            text="Total Records: 0",
            font=("Arial", 12, "italic"),
            text_color="#B56591"
        )
        self.counter_label.pack(pady=10)

    # Method to register new data
    def register_data(self):
        # Get the entered text
        data = self.data_entry.get().strip()
        # Check if the text field is not empty
        if data:
            # Add the data to the list
            self.data_list.append(data)
            # Display the registered data
            data_label = ctk.CTkLabel(
                self.scroll_list,
                text=data,
                text_color="#B56591",
                fg_color="#FFF0F5",
                corner_radius=8
            )
            data_label.pack(
                pady=5,
                padx=10,
                fill="x"
            )
            # Update the total number of registered items
            self.counter_label.configure(
                text=f"Total Records: {len(self.data_list)}"
            )
            # Clear the text field
            self.data_entry.delete(0, "end")


# Run the application only when this file is executed directly
if __name__ == "__main__":
    app = RegistrationListApp()
    app.mainloop()