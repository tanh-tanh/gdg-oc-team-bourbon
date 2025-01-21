# -*- coding: utf-8 -*-
"""ML_notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F8-fqogKz5EFd5zbE79iVt6JJ2avKLST
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("hosammhmdali/heart-disease-dataset")

#loading libs and data
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os
csv_path = os.path.join(path, "Dataset Heart Disease.csv")

hd_training = pd.read_csv(csv_path)

#xoa cot unname va xem 3 thong tin dau tien
#voi cac cot not avaible thi ta se xoa cac hang do tuc axis=0
hd_training = hd_training.dropna(axis=0)
hd_training = hd_training.drop('Unnamed: 0',axis=1)
hd_training.head(3)
hd_training.columns

"""**Mục tiêu**: dựa vào các tiêu chí như độ tuổi, giới tính,v.v, để train và dự đoán xem bệnh nhân có bị heart attack không"""

#khoi tao bo test X la input con y la output cho thuat toan
y = hd_training.target
hd_training_notg = hd_training.drop('target',axis=1)
X = hd_training_notg
# mo ta tong quat ve dau vao
X.describe()

"""**Tạo bộ test**"""

#nhap test vao
out_path = os.path.join(path, "cleveland1.csv")
hd_test=pd.read_csv(out_path)
hd_test = hd_test.dropna(axis=0)
hd_test.columns

"""**note:** chúng ta có thể thấy cột thông tin 2 bên chưa tương xứng nên ta cần phải thay thế"""

hd_test.rename(columns={'resting bp s': 'resting bps'}, inplace=True)
hd_test.columns

y_test = hd_test.target
hd_test = hd_test.drop('target',axis=1)
X_test = hd_test

"""**Phần 1:** thuật toán Decision Tree Regressor"""

# Chon model ML
hd_model_dtr = DecisionTreeRegressor(random_state=8)
# ket hop model voi data duoc cap
hd_model_dtr.fit(X, y)

print("Do chinh xac cua Decision Tree Regressor la: ")
hd_model_dtr.score(X_test,y_test)

"""**Phần 2:** thuật toán Random Forest Classifier"""

hd_model_RF = RandomForestClassifier(random_state=8)
# ket hop model voi data duoc cap
hd_model_RF.fit(X, y)

print("Do chinh xac cua Random Forest Classifier la: ")
hd_model_RF.score(X_test,y_test)

"""**Kết Luận** :

Qua 2 thuật toán trên ta thấy thuật toán Random Forest Classifier tốt hơn nên ta sẽ sử dụng thuật toán này để ứng dụng vào

**Bây giờ ta sẽ nhận thông tin từ người dùng và dự đoán**
"""

columns = ['age', 'sex', 'chest pain type', 'resting bps', 'cholesterol', 'fasting blood sugar', 'resting ecg', 'max heart rate', 'exercise angina', 'oldpeak', 'ST slope']
row = [-1]*11

import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Giả sử bạn đã load/xây dựng mô hình Random Forest này ở đâu đó:
# from joblib import load
# hd_model_RF = load("path_to_your_model.joblib")

# Ở ví dụ này, ta tạo biến hd_model_RF tạm để code không bị lỗi,
# bạn cần thay thế bằng mô hình thật của mình:
class MockModel:
    def predict(self, df):
        # Code giả sử dựa vào cột age (df["age"]) để đoán,
        # chỉ mang tính ví dụ, bạn thay bằng logic/mô hình thật
        return [1 if df["age"][0] >= 50 else 0]

hd_model_RF = MockModel()

# Các cột tương ứng với model của bạn:
columns = [
    "age",       # 0
    "sex",       # 1
    "cp",        # 2
    "trtbps",    # 3 (nhịp tim trên giây khi nghỉ ngơi - bạn đặt tên cột phù hợp)
    "chol",      # 4
    "fbs",       # 5
    "thalachh",  # 6 (nhịp tim trên giây lớn nhất)
    "exng",      # 7 (exercise angina)
    "unknown8",  # 8 (có thể là cột không dùng, tuỳ vào dataset)
    "oldpeak",   # 9
    "slp"        # 10 (stslope)
]


def validate_and_predict():
    """Hàm lấy dữ liệu từ các Entry, kiểm tra tính hợp lệ, 
       tạo DataFrame và gọi mô hình dự đoán."""
    try:
        # Lấy dữ liệu từ các entry
        age_val = int(entry_age.get())
        sex_val = int(entry_sex.get())
        cp_val = int(entry_cp.get())
        trtbps_val = int(entry_trtbps.get())
        chol_val = int(entry_chol.get())
        fbs_val = int(entry_fbs.get())
        thalachh_val = int(entry_thalachh.get())
        exng_val = int(entry_exng.get())
        oldpeak_val = float(entry_oldpeak.get())
        slp_val = float(entry_slp.get())

        # Kiểm tra tính hợp lệ (có thể thay đổi tuỳ ý theo logic bạn muốn)
        # Tuổi (giả sử 28 < age < 77 theo yêu cầu)
        if not (28 < age_val < 77):
            messagebox.showerror("Lỗi", "Tuổi không hợp lệ (yêu cầu 28 < tuổi < 77).")
            return

        # Giới tính (0 hoặc 1)
        if sex_val not in [0, 1]:
            messagebox.showerror("Lỗi", "Giới tính không hợp lệ (0 là nam, 1 là nữ).")
            return

        # Mức độ đau ngực (cp) từ 1 đến 4
        if not (1 <= cp_val <= 4):
            messagebox.showerror("Lỗi", "Mức độ đau ngực phải từ 1 đến 4.")
            return

        # nhịp tim trên giây khi nghỉ ngơi (giả sử 0 <= trtbps <= 200)
        if not (0 <= trtbps_val <= 200):
            messagebox.showerror("Cảnh báo", "Nhịp tim nghỉ ngơi bất thường. Vui lòng kiểm tra lại.")
            return

        # cholesterol (0 <= chol <= 603)
        if not (0 <= chol_val <= 603):
            messagebox.showerror("Cảnh báo", "Cholesterol vượt quá giới hạn. Vui lòng kiểm tra lại.")
            return

        # fasting blood sugar (0 hoặc 1)
        if fbs_val not in [0, 1]:
            messagebox.showerror("Cảnh báo", "Giá trị fasting blood sugar không hợp lệ (0 hoặc 1).")
            return

        # nhịp tim trên giây lớn nhất (0 <= thalachh <= 202)
        if not (0 <= thalachh_val <= 202):
            messagebox.showerror("Cảnh báo", "Nhịp tim lớn nhất bất thường. Vui lòng kiểm tra lại.")
            return

        # exercise angina (0 hoặc 1)
        if exng_val not in [0, 1]:
            messagebox.showerror("Cảnh báo", "Giá trị exercise angina không hợp lệ (0 hoặc 1).")
            return

        # oldpeak (-2.6 <= oldpeak <= 6.2)
        if not (-2.6 <= oldpeak_val <= 6.2):
            messagebox.showerror("Cảnh báo", "oldpeak vượt quá giới hạn. Vui lòng kiểm tra lại.")
            return

        # stslope (1 <= slp <= 3)
        if not (1 <= slp_val <= 3):
            messagebox.showerror("Cảnh báo", "Giá trị stslope không hợp lệ (1-3).")
            return

        # Tập hợp dữ liệu vào list (chú ý cột 8 ta tạm cho = 0 nếu không dùng)
        row = [
            age_val,        # [0]
            sex_val,        # [1]
            cp_val,         # [2]
            trtbps_val,     # [3]
            chol_val,       # [4]
            fbs_val,        # [5]
            thalachh_val,   # [6]
            exng_val,       # [7]
            0,              # [8] (nếu bạn không sử dụng cột này thì đặt mặc định)
            oldpeak_val,    # [9]
            slp_val         # [10]
        ]

        # Tạo DataFrame
        df = pd.DataFrame([row], columns=columns)

        # Gọi mô hình để dự đoán
        prediction = hd_model_RF.predict(df)
        
        # Xử lý kết quả
        if prediction[0] == 1:
            messagebox.showinfo("Kết quả", "Bạn có khả năng bị đau tim.")
        else:
            messagebox.showinfo("Kết quả", "Bạn không có khả năng bị đau tim.")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng kiểm tra lại: chỉ được nhập số hợp lệ.")


# Tạo cửa sổ chính
window = tk.Tk()
window.title("Dự đoán nguy cơ đau tim")

# Tạo các Label và Entry cho mỗi trường thông tin
label_age = tk.Label(window, text="Tuổi (28 < tuổi < 77):")
label_age.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_age = tk.Entry(window)
entry_age.grid(row=0, column=1, padx=5, pady=5)

label_sex = tk.Label(window, text="Giới tính (0 nam, 1 nữ):")
label_sex.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sex = tk.Entry(window)
entry_sex.grid(row=1, column=1, padx=5, pady=5)

label_cp = tk.Label(window, text="Mức độ đau ngực (1-4):")
label_cp.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_cp = tk.Entry(window)
entry_cp.grid(row=2, column=1, padx=5, pady=5)

label_trtbps = tk.Label(window, text="Nhịp tim nghỉ ngơi (0-200):")
label_trtbps.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_trtbps = tk.Entry(window)
entry_trtbps.grid(row=3, column=1, padx=5, pady=5)

label_chol = tk.Label(window, text="Giá trị cholesterol (0-603):")
label_chol.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_chol = tk.Entry(window)
entry_chol.grid(row=4, column=1, padx=5, pady=5)

label_fbs = tk.Label(window, text="Fasting Blood Sugar (0 hoặc 1):")
label_fbs.grid(row=5, column=0, padx=5, pady=5, sticky="e")
entry_fbs = tk.Entry(window)
entry_fbs.grid(row=5, column=1, padx=5, pady=5)

label_thalachh = tk.Label(window, text="Nhịp tim lớn nhất (0-202):")
label_thalachh.grid(row=6, column=0, padx=5, pady=5, sticky="e")
entry_thalachh = tk.Entry(window)
entry_thalachh.grid(row=6, column=1, padx=5, pady=5)

label_exng = tk.Label(window, text="Exercise Angina (0 hoặc 1):")
label_exng.grid(row=7, column=0, padx=5, pady=5, sticky="e")
entry_exng = tk.Entry(window)
entry_exng.grid(row=7, column=1, padx=5, pady=5)

label_oldpeak = tk.Label(window, text="Oldpeak (-2.6 đến 6.2):")
label_oldpeak.grid(row=8, column=0, padx=5, pady=5, sticky="e")
entry_oldpeak = tk.Entry(window)
entry_oldpeak.grid(row=8, column=1, padx=5, pady=5)

label_slp = tk.Label(window, text="ST Slope (1-3):")
label_slp.grid(row=9, column=0, padx=5, pady=5, sticky="e")
entry_slp = tk.Entry(window)
entry_slp.grid(row=9, column=1, padx=5, pady=5)

# Tạo nút "Dự đoán"
btn_predict = tk.Button(window, text="Dự đoán", command=validate_and_predict)
btn_predict.grid(row=10, column=0, columnspan=2, pady=10)

# Chạy vòng lặp giao diện
window.mainloop()
