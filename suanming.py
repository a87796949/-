import requests
import tkinter
import tkinter.font as myFont

app_key = "be064d64b45ee1ffbf7a70e04f9f74da"
url = "http://v.juhe.cn/dream/query?"

def a():
    params = {
        "key" : app_key,
        "q" : input_entry.get()
    }
    response = requests.get(url, params=params).json()
    if response["result"]:
        response_result = response["result"]
        output_str = ""
        for dream in response_result:
            output_str +="梦见[ {} ]\n梦境解析: \n   {}\n\n".format(dream["title"], dream["des"])
    else:
        output_str = response["reason"]

    dram_keyword_text.delete(0.0, "end")
    dram_keyword_text.insert("insert", output_str)



root = tkinter.Tk()
root.title("周公解梦")
root.geometry("450x500")

entry_font = myFont.Font(size=15, family="华文楷体", weight="bold")
entry_font1 = myFont.Font(size=17, family="楷体")
entry_font2 = myFont.Font(size=12, family="华文楷体")

dram_keyword_lab = tkinter.Label(root,text="梦见", justify="center", font=entry_font, bg="DarkGoldenrod")
dram_keyword_lab.place(x=50, y=20)

input_entry = tkinter.Entry(root, justify="center", font=entry_font1, bg="SkyBlue", width=14)
input_entry.place(x=98, y=20)


input_button = tkinter.Button(root, text="开始解梦", justify="center", font=entry_font2, bg="SkyBlue", width=9,
                              command=a)
input_button.place(x=250, y=18)

dram_keyword_text = tkinter.Text(root,font=entry_font2, width=53, height=53)

dram_keyword_text.place(x=5 ,y=55)

root.mainloop()