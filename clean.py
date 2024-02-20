import pandas as pd
import re


# Hàm để trích xuất thương hiệu từ tên sản phẩm
def extract_brand(product_name):
    for brand in brands:
        if re.search(r"\b{}\b".format(brand), product_name, flags=re.IGNORECASE):
            return brand
    return None


def get_platform(link):
    if isinstance(link, str):
        platform = link[8:14]  # Lấy phần từ vị trí 6 đến 11 trong chuỗi link
        if "Shopee" in platform:
            return "Shopee"
    return "Don't Use"


def extract_brand_samsung_phone(product_name):
    max_match = None
    max_length = 0
    for samsung_product in samsung_products:
        if re.search(
            r"\b{}\b".format(samsung_product), product_name, flags=re.IGNORECASE
        ):
            if len(samsung_product) > max_length:
                max_match = samsung_product
                max_length = len(samsung_product)
    return max_match




# data Samsung

samsung_products = [
    "Samsung Galaxy S",
    "Samsung Galaxy S II",
    "Samsung Galaxy S III",
    "Samsung Galaxy S4",
    "Samsung Galaxy S5",
    "Samsung Galaxy S6",
    "Samsung Galaxy S6 Edge",
    "Samsung Galaxy S6 Edge+",
    "Samsung Galaxy S7",
    "Samsung Galaxy S7 Edge",
    "Samsung Galaxy S8",
    "Samsung Galaxy S8+",
    "Samsung Galaxy S9",
    "Samsung Galaxy S9+",
    "Samsung Galaxy S10e",
    "Samsung Galaxy S10",
    "Samsung Galaxy S10+",
    "Samsung Galaxy S20",
    "Samsung Galaxy S20+",
    "Samsung Galaxy S20 Ultra",
    "Samsung Galaxy S21",
    "Samsung Galaxy S21+",
    "Samsung Galaxy S21 Ultra",
    "Samsung Galaxy S22",
    "Samsung Galaxy S22+",
    "Samsung Galaxy S22 Ultra",
    "Samsung Galaxy S23",
    "Samsung Galaxy S23 Plus",
    "Samsung Galaxy S23 Ultra",
    "Samsung Galaxy A",
    "Samsung Galaxy A3",
    "Samsung Galaxy A5",
    "Samsung Galaxy A7",
    "Samsung Galaxy A3",
    "Samsung Galaxy A5",
    "Samsung Galaxy A7",
    "Samsung Galaxy A3",
    "Samsung Galaxy A5",
    "Samsung Galaxy A8",
    "Samsung Galaxy A3",
    "Samsung Galaxy A5",
    "Samsung Galaxy A7",
    "Samsung Galaxy A8",
    "Samsung Galaxy A8+",
    "Samsung Galaxy A6",
    "Samsung Galaxy A7",
    "Samsung Galaxy A9",
    "Samsung Galaxy A10",
    "Samsung Galaxy A20",
    "Samsung Galaxy A30",
    "Samsung Galaxy A40",
    "Samsung Galaxy A50",
    "Samsung Galaxy A60",
    "Samsung Galaxy A70",
    "Samsung Galaxy A80",
    "Samsung Galaxy A90 5G",
    "Samsung Galaxy A01",
    "Samsung Galaxy A11",
    "Samsung Galaxy A21",
    "Samsung Galaxy A31",
    "Samsung Galaxy A41",
    "Samsung Galaxy A51",
    "Samsung Galaxy A71",
    "Samsung Galaxy A81",
    "Samsung Galaxy A91",
    "Samsung Galaxy A02",
    "Samsung Galaxy A12",
    "Samsung Galaxy A32",
    "Samsung Galaxy A42",
    "Samsung Galaxy A52",
    "Samsung Galaxy A72",
    "Samsung Galaxy A03",
    "Samsung Galaxy A13",
    "Samsung Galaxy A23",
    "Samsung Galaxy A33",
    "Samsung Galaxy A53",
    "Samsung Galaxy A73",
    "Samsung Galaxy A04",
    "Samsung Galaxy A14",
    "Samsung Galaxy A24",
    "Samsung Galaxy A34",
    "Samsung Galaxy A54",
    "Samsung Galaxy A74",
    "Samsung Galaxy Z Fold",
    "Samsung Galaxy Z Flip",
    "Samsung Galaxy Z Fold 2",
    "Samsung Galaxy Z Flip 5G",
    "Samsung Galaxy Z Fold 3",
    "Samsung Galaxy Z Flip 3",
    "Samsung Galaxy Z Fold 4",
    "Samsung Galaxy Z Flip 4",
    "Samsung Galaxy Z Fold 5",
    "Samsung Galaxy Z Flip 5",
    "Samsung Galaxy J",
    "Samsung Galaxy J1",
    "Samsung Galaxy J2",
    "Samsung Galaxy J3",
    "Samsung Galaxy J5",
    "Samsung Galaxy J7",
    "Samsung Galaxy J Max",
    "Samsung Galaxy J Pro",
    "Samsung Galaxy J Prime",
    "Samsung Galaxy J7 Prime",
    "Samsung Galaxy J2 Pro",
    "Samsung Galaxy J3 Pro",
    "Samsung Galaxy J5 Pro",
    "Samsung Galaxy J7 Pro",
    "Samsung Galaxy J4",
    "Samsung Galaxy J6",
    "Samsung Galaxy J8",
    "Samsung Galaxy J4 Plus",
    "Samsung Galaxy J6 Plus",
    "Samsung Galaxy J8 Plus",
    "Samsung Galaxy Note",
    "Samsung Galaxy Note II",
    "Samsung Galaxy Note 3",
    "Samsung Galaxy Note 4",
    "Samsung Galaxy Note 5",
    "Samsung Galaxy Note 7",
    "Samsung Galaxy Note 8",
    "Samsung Galaxy Note 9",
    "Samsung Galaxy Note 10",
    "Samsung Galaxy Note 20",
    "Samsung Galaxy Note 20 Ultra",
    "Samsung Galazy Z Flip5",
    "Samsung Galaxy M14",
    "Samsung Galazy Z Flip5",
]
# Tạo danh sách các thương hiệu
brands = [
    "Apple",
    "Xiaomi",
    "Samsung",
    "Oppo",
    "Realme",
    "Vertu",
    "Asus",
    "Redmi",
    "Lg",
    "Infinix",
    "Sony",
    "Google",
    "Vsmart",
    "Vivo",
    "Kudixiong",
    "Itel",
    "Poco",
    "Tecno",
    "Nokia",
]

brand_country_dict = {
    "Apple": "Hoa Kỳ",
    "Xiaomi": "Trung Quốc",
    "Samsung": "Hàn Quốc",
    "Oppo": "Trung Quốc",
    "Realme": "Trung Quốc",
    "Vertu": "Anh Quốc",
    "Asus": "Đài Loan",
    "Redmi": "Trung Quốc",
    "Lg": "Hàn Quốc",
    "Infinix": "Trung Quốc",
    "Sony": "Nhật Bản",
    "Google": "Hoa Kỳ",
    "Vsmart": "Việt Nam",
    "Vivo": "Trung Quốc",
    "Xsmart": "Việt Nam",
    "Kudixiong": "Trung Quốc",
    "Xiaomi Youpin": "Trung Quốc",
    "Itel": "Trung Quốc",
    "Poco": "Trung Quốc",
    "Tecno": "Trung Quốc",
    "Nokia": "Phần Lan"
}
# Đọc dữ liệu từ sheet thứ hai trong tệp Excel
df = pd.read_excel("Data Mau.xlsx", sheet_name="Dữ liệu")

df.columns = df.columns.str.title()

# Lấy danh sách các cột cần giữ
columns_to_keep = [
    "Tên Sản Phẩm",
    "Doanh Thu",
    "Ngành Hàng",
    "Thương Hiệu",
    "Link Shop",
    "Ngày Bắt Đầu Bán",
    "Tổng Doanh Số",
    "Tổng Số Đã Bán",
]

# Chọn chỉ các cột cần giữ
df = df[columns_to_keep]

# loc nganh hang
df = df.loc[df["Ngành Hàng"] == "Điện Thoại & Máy Tính Bảng"]

# Áp dụng việc viết hoa chữ đầu tiên và sau dấu cách cho toàn bộ dữ liệu
df = df.applymap(lambda x: x.title() if isinstance(x, str) else x)


# Thêm dữ liệu vào cột "Thương hiệu" dựa trên các giá trị trong cột "Tên Sản Phẩm"
df["Thương Hiệu"] = df["Tên Sản Phẩm"].apply(lambda x: extract_brand(str(x)))

df['Sản Phẩm Samsung'] = df['Tên Sản Phẩm'].apply(extract_brand_samsung_phone)

df.loc[df["Thương Hiệu"] != "Samsung", "Sản Phẩm Samsung"] = "Don't Use"

# Thêm cột mới 
df["Sàn"] = df["Link Shop"].apply(get_platform)

df[["Năm", "Tháng"]] = df["Ngày Bắt Đầu Bán"].str.split("-", expand=True)

df["Quốc Gia"] = df["Thương Hiệu"].map(brand_country_dict)

# Xóa các dòng có giá trị cột "Thương Hiệu" là NaN hoặc rỗng
df = df.dropna(subset=["Thương Hiệu","Sản Phẩm Samsung", "Link Shop","Quốc Gia"])

df["Link Shop"] = df["Link Shop"].str.lower()

# Lưu dữ liệu đã xử lý ra tệp CSV mới
df.to_csv("du_lieu_da_xu_ly.csv", index=False)
