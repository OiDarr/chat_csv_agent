import threading

import tkinter
import tkinter.scrolledtext

from agent import get_csv_agent_response


class GraphicalInterface:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.window, text="Чат с агентом:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.window)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')

        self.msg_label = tkinter.Label(self.window, text="Сообщение:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.window, height=3)
        self.input_area.pack(padx=20, pady=5)
        self.input_area.bind("<Return>", self.user_request)

        self.send_button = tkinter.Button(self.window, text="Отправить", command=self.user_request)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.stop)
        self.window.mainloop()

    def user_request(self, event=None):
        message = self.input_area.get('1.0', 'end')
        self.write(message=message, sender="Вы")
        threading.Thread(target=self.agent_response, args=(message,)).start()
        self.input_area.delete('1.0', 'end')
        return "break"

    def agent_response(self, prompt):
        answer = f'{get_csv_agent_response(prompt)}\n'
        self.write(message=answer, sender="Агент")

    def write(self, message, sender):
        self.text_area.config(state='normal')
        self.text_area.insert('end', f"{sender}: {message}")
        self.text_area.yview('end')
        self.text_area.config(state='disabled')

    def stop(self):
        self.window.destroy()
        exit(0)


if __name__ == '__main__':
    gui = GraphicalInterface()
