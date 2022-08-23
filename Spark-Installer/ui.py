import customtkinter

from tools import version_grabber
from tools.installer import Installer


class App(customtkinter.CTk):
    WIDTH = 360
    HEIGHT = 240
    spark_versions = [""]
    hadoop_versions = [""]
    def __init__(self):
        super().__init__()


        self.spark_versions = sorted(version_grabber.getSparkVersion(), reverse=True)
        self.hadoop_versions = sorted(version_grabber.getHadoopVersion(None, self.spark_versions[0]), reverse=True)
        self.selected_spark_version = self.spark_versions[0]
        self.selected_hadoop_version = self.hadoop_versions[0]
        self.title("Spark Tool")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.maxsize(self.WIDTH, self.HEIGHT)
        self.minsize(self.WIDTH, self.HEIGHT)
        self.title = customtkinter.CTkLabel(master=self, text="Spark Tools by victoryil",
                                            text_font=("Roboto Medium", -24))
        self.title.pack(padx=20, pady=5)

        self.spark_lbl = customtkinter.CTkLabel(master=self, text="Spark version: ")
        self.spark_lbl.pack()
        self.spark_version = customtkinter.CTkOptionMenu(master=self,
                                                         values=self.spark_versions,
                                                         command=self.change_spark_version)
        self.spark_version.pack(padx=20, pady=0)

        self.hadoop_lbl = customtkinter.CTkLabel(master=self, text="Hadoop version: ")
        self.hadoop_lbl.pack()

        self.hadoop_version = customtkinter.CTkOptionMenu(master=self,
                                                          values=self.hadoop_versions,
                                                          command=self.change_hadoop_version)
        self.hadoop_version.pack(padx=20, pady=0)

        self.install_btn = customtkinter.CTkButton(master=self,
                                                   text="Install",
                                                   width=120,
                                                   height=32,
                                                   border_width=0,
                                                   corner_radius=8,
                                                   command=self.installer)
        self.install_btn.pack(padx=20, pady=20)

    def on_closing(self, event=0):
        self.destroy()

    def change_spark_version(self, vers):
        self.hadoop_versions = sorted(version_grabber.getHadoopVersion(self, vers), reverse=True)
        self.hadoop_version.configure(values=self.hadoop_versions)
        self.hadoop_version.set(self.hadoop_versions[0])
        self.selected_spark_version = vers

    def change_hadoop_version(self, vers):
        print(vers)
        self.selected_hadoop_version = vers

    def installer(self):
        from tkinter import messagebox as MessageBox
        message = f"Installing spark {self.selected_spark_version} and hadoop {self.selected_hadoop_version}"
        # print(message)
        installer = Installer
        installer.install(installer, self.selected_spark_version, self.selected_hadoop_version)
        MessageBox.showinfo("Success", message)


if __name__ == "__main__":
    app = App()
    app.mainloop()
