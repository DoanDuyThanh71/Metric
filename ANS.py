import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("du_lieu_da_xu_ly.csv")

# Nhóm dữ liệu theo cột "Thương Hiệu" và tính tổng số đã bán và doanh số cho mỗi nhóm
thong_ke = df.groupby("Thương Hiệu").agg({"Tổng Số Đã Bán": "sum", "Tổng Doanh Số": "sum"})

# Hiển thị bảng thống kê
print(thong_ke)

# Lưu dữ liệu vào tệp Excel

chuoi = "Phân loại doanh số và doanh thu theo từng thương hiệu:"
cau_df = pd.DataFrame([chuoi], columns=['Cau 1'])
cau_df.to_csv("cau1.csv", index=False)
thong_ke.to_csv("cau1.csv",mode ='a', index=False)
# ----------------------------------------------------------------
# Cau 2
# Nhóm dữ liệu theo cột "Quốc Gia" và tính tổng số đã bán cho mỗi quốc gia
thong_ke_quoc_gia = df.groupby("Quốc Gia")["Tổng Số Đã Bán"].sum().reset_index()

# Sắp xếp dữ liệu theo tổng số đã bán giảm dần
thong_ke_quoc_gia = thong_ke_quoc_gia.sort_values(by="Tổng Số Đã Bán", ascending=False)

# Lấy quốc gia có tổng số đã bán cao nhất
quoc_gia_ban_chay_nhat = thong_ke_quoc_gia.iloc[0]

# In bảng thống kê
print("Bảng thống kê số điện thoại đã bán theo từng quốc gia:")
print(thong_ke_quoc_gia)

# In kết quả quốc gia bán chạy nhất
print("\nQuốc gia bán chạy nhất:")
print(quoc_gia_ban_chay_nhat)

# Lưu dữ liệu vào tệp Excel
thong_ke_quoc_gia.to_csv("cau2.csv", index=False)
chuoi = "Quốc gia bán chạy nhất:"
cau_df = pd.DataFrame([chuoi], columns=['Cau 2'])
cau_df.to_csv("cau2.csv", index=False)
thong_ke_quoc_gia.to_csv("cau2.csv",mode ='a', index=False)

# ----------------------------------------------------------------
# Cau 3
# Nhóm dữ liệu theo cột "Quốc Gia" và tính tổng Doanh Số cho mỗi quốc gia
sales_by_country = df.groupby("Quốc Gia")["Tổng Doanh Số"].sum().reset_index()

# Sắp xếp dữ liệu theo tổng Doanh Số giảm dần
sales_by_country = sales_by_country.sort_values(by="Tổng Doanh Số", ascending=False)

# Lấy quốc gia có tổng Doanh Số cao nhất
top_selling_country = sales_by_country.iloc[0]["Quốc Gia"]

# In ra bảng thống kê
print("Bảng thống kê số điện thoại đã bán theo từng quốc gia:")
print(sales_by_country)

# In ra quốc gia có tổng Doanh Số cao nhất
print("\nQuốc gia có tổng doanh số tốt nhât là:", top_selling_country)

# Lưu dữ liệu vào tệp Excel
chuoi = "Quốc gia có tổng doanh số tốt nhât là:"
cau_df = pd.DataFrame([chuoi], columns=['Cau 3'])
cau_df.to_csv("cau3.csv", index=False)
sales_by_country.to_csv("cau3.csv",mode ='a', index=False)

# ----------------------------------------------------------------
# Cau 4
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("du_lieu_da_xu_ly.csv")
# Lọc dữ liệu chỉ chứa thông tin của Samsung trên sàn Shopee
samsung_shopee_df = df[(df["Thương Hiệu"] == "Samsung") & (df["Sàn"] == "Shopee")]

# Tính tổng doanh số và tổng số đã bán của Samsung Galaxy S23 trên sàn Shopee
s23_sales = samsung_shopee_df[samsung_shopee_df["Tên Sản Phẩm"].str.contains("Samsung Galaxy S23")].agg({"Tổng Số Đã Bán": "sum", "Doanh Thu": "sum"})

# Tính tổng doanh số và tổng số đã bán của các điện thoại Samsung khác trên sàn Shopee
other_samsung_sales = samsung_shopee_df[~samsung_shopee_df["Tên Sản Phẩm"].str.contains("Samsung Galaxy S23")].agg({"Tổng Số Đã Bán": "sum", "Doanh Thu": "sum"})

# Tính tỷ lệ của Samsung Galaxy S23 so với tổng số các điện thoại Samsung khác trên sàn Shopee
s23_sales_ratio = s23_sales / other_samsung_sales

# In ra kết quả
print("Tỷ lệ về doanh số và số đã bán của Samsung Galaxy S23 so với các điện thoại khác của Samsung trên sàn Shopee:")
print(s23_sales_ratio)

chuoi = "Tỷ lệ về doanh số và số đã bán của Samsung Galaxy S23 so với các điện thoại khác của Samsung trên sàn Shopee"

cau4_df = pd.DataFrame([chuoi],columns=['Cau 4'])

cau4_df.to_csv("cau4.csv", index=False)

s23_sales_ratio.to_csv("cau4.csv", mode='a', header=False)
# Tạo hai khung biểu đồ
fig, (ax1, ax2) = plt.subplots(1,2)

# Vẽ biểu đồ doanh số
bars1 = ax1.bar(["Samsung Galaxy S23", "Other Samsung Phones"], [s23_sales["Tổng Số Đã Bán"], other_samsung_sales["Tổng Số Đã Bán"]])
ax1.set_title('Số lượng sản phẩm bán ra')

# Hiển thị dữ liệu trên đầu cột cho biểu đồ doanh số
for bar in bars1:
    yval = bar.get_height()
    ax1.annotate(f"{yval}", xy=(bar.get_x() + bar.get_width() / 2, yval), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom')

# Vẽ biểu đồ doanh thu
bars2 = ax2.bar(["Samsung Galaxy S23", "Other Samsung Phones"], [s23_sales["Doanh Thu"], other_samsung_sales["Doanh Thu"]])
ax2.set_title('Doanh thu')

# Hiển thị dữ liệu trên đầu cột cho biểu đồ doanh thu
for bar in bars2:
    yval = bar.get_height()
    ax2.annotate(f"{yval}", xy=(bar.get_x() + bar.get_width() / 2, yval), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom')

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
