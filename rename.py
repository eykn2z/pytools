import os

import tkinter
from tkinter import ttk,messagebox,filedialog
from pprint import pprint

# todo:初期値を入れる、カーソルが入ってるようにする、エンターでbtn_clickにいく

num=None
window_title="ファイル名を変更する"

class NumWindow(tkinter.Canvas):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        # ウィジェット
        option={"padx":10,"pady":5}
        self.num_label=ttk.Label(self,text="初期値")
        self.num_label.grid(row=0,column=0,**option)
        self.num_box=ttk.Entry(self,width=8)
        self.num_box.grid(row=0,column=1,**option)
        self.btn=ttk.Button(self,text="実行",command=self.btn_click)
        self.btn.grid(row=0,column=2,**option)

    def btn_click(self):
        global num
        if self.num_box.get() is '':
            messagebox.showinfo(window_title,"入力してください")
            return
        num=self.num_box.get()
        num=num if type(num)==int else int(num)
        self.quit()
        return
        
def file_dialog(initDir=os.path.abspath(os.path.dirname(__file__))):
    files = filedialog.askopenfilenames(initialdir = initDir)
    if type(files) is not tuple:
        messagebox.showinfo(window_title,"ファイルを選択してください")
        return False
    return files

def get_new_names(files,num=0):
    file_types=[os.path.splitext(f)[1] for f in files]
    new_names=["{}{}".format(n,t) for n,t in enumerate(file_types,num)]
    return new_names

def change_names(files,new_names):
    file_dirs=[os.path.dirname(f) for f in files]
    new_files=["{}/{}".format(dir,name) for dir,name in zip(file_dirs,new_names)]
    res = messagebox.askyesno(window_title, "名前変更してよいですか？")
    if res is False:
        return
    for file,new_file,dir in zip(files,new_files,file_dirs):
        os.rename(file,new_file)
    messagebox.showinfo(window_title, "変換が終わりました")
    return new_files

def main(debug=False):
    root=tkinter.Tk()
    root.title("ファイル名を変更する")
    root.resizable(False, False)

    if debug:
        return
    
    # 1. select files
    root.withdraw()
    files=file_dialog(r"C:\Users\akane\GoogleDrive\PDF\キタミ式IT応用情報")
    
    # 2. set initial number
    if files is False:
        return
    print(files)
    print("ファイルが選択されました")

    root.deiconify()
    NumWindow(root).mainloop()
    print(num)
    print("初期値が設定されました")

    if num is None:
        return

    # 3. change file name
    root.withdraw()
    new_names=get_new_names(files,num)
    new_filepath_list=change_names(files,new_names)
    print(new_filepath_list)    
    return True


if __name__=="__main__":
    main()