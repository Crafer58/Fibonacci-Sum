from tkinter import *

root = Tk();
root.title("Fibonacci Sum");
root.geometry("400x400");

user_input = Entry(root)
series = Label(root, text = "Fibonacci Series: ")
label_sum = Label(root, text = "Sum: ");



def Fibonacci():
    number1 = 0
    number2 = 1
    sum = 0
    num = user_input.get()
    i = 1
    total_sum = 0
    
    while(i <= int(num)):
        series["text"] += str(sum) + " "
        i = i + 1
        number1 = number2
        number2 = sum
        sum = number1 + number2 
        
        total_sum = total_sum + sum

    label_sum["text"] = str(total_sum)
   
     



btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci);

btn.pack()
series.pack()
label_sum.pack()
user_input.pack()


root.mainloop()

