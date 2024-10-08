import tkinter as tk
from tkinter import messagebox
from math import sqrt

# Hàm để giải phương trình bậc 2
def giaiphuongtrinh():
    try:
        # Lấy giá trị từ các ô nhập liệu
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        
        # Giải phương trình
        delta = b**2 - 4*a*c
        
        if delta < 0:
            kq = "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            kq = f"Phương trình có nghiệm kép: x = {x:.2f}"
        else:
            x1 = (-b + sqrt(delta)) / (2*a)
            x2 = (-b - sqrt(delta)) / (2*a)
            kq = f"Phương trình có 2 nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}"
        
        kq_pt.config(text=kq)
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

# Hàm thoát chương trình
def exit_program():
    if messagebox.askyesno("Thoát", "Bạn có muốn thoát không?"):
        root.quit()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải Phương Trình Bậc 2")

# Tạo menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Tạo LabelFrame để nhập các giá trị a, b, c
frame_input = tk.LabelFrame(root, text="Nhập các hệ số", padx=10, pady=10)
frame_input.pack(side=tk.LEFT, padx=10, pady=10)

# Label và Entry cho hệ số a
so_a = tk.Label(frame_input, text="Hệ số a:")
so_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_input)
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Label và Entry cho hệ số b
so_b = tk.Label(frame_input, text="Hệ số b:")
so_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_input)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Label và Entry cho hệ số c
so_c = tk.Label(frame_input, text="Hệ số c:")
so_c.grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame_input)
entry_c.grid(row=2, column=1, padx=5, pady=5)

# Tạo LabelFrame để hiển thị nút giải và kết quả
frame_result = tk.LabelFrame(root, text="Kết quả", padx=10, pady=10)
frame_result.pack(side=tk.RIGHT, padx=10, pady=10)

# Nút giải phương trình
kq_pt = tk.Button(frame_result, text="Giải", command=giaiphuongtrinh)
kq_pt.grid(row=0, column=0, padx=5, pady=5)

# Label để hiển thị kết quả
kq_pt = tk.Label(frame_result, text="Kết quả sẽ hiển thị tại đây")
kq_pt.grid(row=0, column=1, padx=5, pady=5)

# Chạy chương trình
root.mainloop()
