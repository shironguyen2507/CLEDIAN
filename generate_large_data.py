import pandas as pd
import random
import os

# Cấu hình số lượng dữ liệu muốn tạo
NUM_SAMPLES = 10000  # Mỗi loại sẽ tạo 10000 dòng (dư ra so với yêu cầu 10000)

# Đường dẫn lưu file
RAW_DIR = "datasets/raw"
if not os.path.exists(RAW_DIR):
    os.makedirs(RAW_DIR)

# --- THƯ VIỆN DỮ LIỆU MẪU (VIETNAMESE) ---

BANKS = ["VCB", "Techcombank", "BIDV", "VietinBank", "ACB", "MBBank", "Sacombank", "VPBank", "TPBank", "SHB", "DongA Bank", "Eximbank", "SeABank", "HDBank", "MSB", "OCB", "VIB", "ABBank", "SCB", "Nam A Bank", "PVcomBank", "Kienlongbank", "Saigonbank", "Bac A Bank", "LienVietPostBank", "GPBank", "OceanBank", "BaoViet Bank", "CIMB Vietnam", "Public Bank Vietnam", "Woori Bank Vietnam", "Standard Chartered Vietnam", "HSBC Vietnam", "Shinhan Bank Vietnam", "Citibank Vietnam"]
SCORES = ["10.000.000", "50.000.000", "100.000.000", "200.000.000", "SH 150i", "Mercedes", "Iphone 14 Pro", "Macbook Pro M2", "Samsung Galaxy S23", "Xe Air Blade", "Xe Vision", "Ipad Pro", "Apple Watch Series 8", "Voucher Shopee 1.000.000 VND", "Voucher Lazada 2.000.000 VND", "Voucher Tiki 500.000 VND", "Tai nghe AirPods Pro", "Smart TV Samsung 55 inch", "Xe máy Honda Lead", "Laptop Dell XPS 13", "Voucher Grab 300.000 VND", "Voucher Now 200.000 VND", "Voucher Foody 150.000 VND", "Voucher Be 100.000 VND", "Voucher Gojek 250.000 VND", "Voucher VNPay 400.000 VND",]
LINKS_SCAM = [".xyz", ".top", ".club", ".vip", ".cc", ".info", ".online", "-verify.com", "-bank.net", "-secure.org"]
LINKS_SAFE = [".com.vn", ".vn", ".com", ".org", ".gov.vn"]
NAMES = ["Tuấn", "Hưng", "Lan", "Mai", "Đức", "Thắng", "Huyền", "Ngọc", "Minh", "Hà", "Phương", "Anh", "Quang", "Trang", "Khánh", "Vy", "Long", "Diệp", "Sơn", "Linh", "Thảo", "Nhi", "Bảo", "Trâm", "Hiếu", "Quỳnh", "Thanh", "Duyên", "Phát", "Tâm", "Hà", "My", "Hoàng", "Thương", "Phúc", "My", "Ngân", "Tuyết", "Việt", "Bình", "Chi", "Thủy", "Quốc", "Hạnh", "Phước", "Luân", "Diệu", "Kiệt", "Trung", "Yến", "Đại", "Phan", "Quý", "Hải", "Lộc", "Cường", "Dũng", "Thịnh", "Vân", "Tú", "Hòa", "Như", "Phương", "Sang", "Tùng", "Vỹ", "Khôi", "Trí", "Đan", "Linh", "Huy", "Thảo", "Quân", "Vinh", "Nguyên", "Tín", "Duy", "Hải", "Phương", "Thành", "Nghĩa", "Bích", "Lan", "Trâm", "Hương", "Giang", "Diễm", "Uyên", "Châu", "Phú", "Khang", "Đăng", "Vũ", "Tài", "Lâm", "Công", "Thiện", "Nhật", "Trường", "Đức", "Quang", "Vương", "Thái", "Hùng", "Phước", "Tấn", "Sỹ", "Đạt", "Lý", "Toàn", "Khánh", "Dạ", "Nguyệt", "Thanh", "Tường", "Bảo", "Trinh", "Diệu", "Hải", "Yến", "Nhã", "Quỳnh", "Thảo", "Vy", "Phương", "Anh", "Hà", "My", "Trâm", "Chi", "Thủy", "Ngân", "Ly", "Trúc", "Hạnh", "Duyên", "Thùy", "Trang", "Nhung", "Phương", "Oanh", "Hương", "Quỳnh", "Linh", "Diệp", "Mai", "Vân", "Hà", "Anh"]
JOBS = ["TikTok", "Shopee", "Lazada", "Tiki", "YouTube", "Facebook", "Grab", "Now", "Be", "Gojek", "VNPay", "Viettel", "Mobifone", "Vinaphone", "Zalo", "VNG", "Foody", "Ahamove", "Baemin", "Lalamove", "Giao Hang Nhanh", "Giao Hang Tiet Kiem", "DHL", "FedEx", "UPS", "Viettel Post", "Ninja Van", "J&T Express", "Best Express", "GHN Express", "AloShip", "Boxme", "Sendo", "Citus", "Voso", "Postmart", "Lixi", "Viettel Money", "MoMo", "ZaloPay", "AirPay", "VNDirect", "SSI", "HSC", "VPS", "TCBS", "FPTS", "MB Securities", "ACB Securities", "Vietcombank Securities", "Techcom Securities"]

# --- HÀM SINH TIN NHẮN LỪA ĐẢO (SCAM) ---
def generate_scam_sms():
    templates = [
        "Chúc mừng thuê bao quý khách đã trúng thưởng {prize}. Truy cập {link} để nhận thưởng ngay.",
        "Tài khoản {bank} của bạn bị tạm khóa. Vui lòng đăng nhập tại {link} để xác thực.",
        "Phát hiện giao dịch bất thường tại tài khoản {bank} số tiền {money} VND. ủy giao dịch tại {link}.",
        "TUYỂN DỤNG {job}: Việc nhẹ lương cao, thu nhập 500k-1tr/ngày. IB Zalo 09{phone}.",
        "Bộ Công An triệu tập ông/bà liên quan đến đường dây đưa tiền. Khai báo ngay tại app VNeID gia mao: {link}.",
        "Vay tiền nhanh không cần thẩm định, giải ngân 15 phút. Lãi suất 0%. Đăng ký: {link}.",
        "Shop xả kho nghi bán, Iphone 15 Pro Max giá chỉ 2 triệu. Đặt ngay tại {link}.",
        "Lệnh bắt tạm giam đã được gửi đến bạn. Vui lòng hợp tác điều tra tại {link}.",
        "Em là sinh viên cần tiền đóng học, nhận được khách kinh doanh. Xem anh em tại {link}.",
        "Chuyển tiền gấp cho tôi, tôi đang có việc gấp làm, mai tôi trả. STK {bank} 1903{phone}.",
        "Vui lòng truy cập {link} để biết thêm chi tiết.",
        "Bạn đã thắng lớn trong chương trình khuyến mãi của {bank}, nhận ngay {prize} tại {link}.",
        "Cảnh báo bảo mật: Tài khoản {bank} của bạn có dấu hiệu bị xâm nhập. Xác thực ngay tại {link}.",
        "Đăng ký vay tiền nhanh trong ngày, duyệt hồ sơ 100%. Truy cập {link} để biết thêm chi tiết.",
        "Bạn có một gói quà tặng từ {job}, nhận ngay tại {link}.",
        "Hệ thống phát hiện giao dịch lạ, vui lòng xác minh tài khoản {bank} của bạn tại {link} để tránh bị khóa.",
        "Chúc mừng bạn đã trúng thưởng {prize} từ chương trình khuyến mãi của chúng tôi. Nhấn vào {link} để nhận giải thưởng.",
        "Cảnh báo: Tài khoản ngân hàng {bank} của bạn có hoạt động bất thường. Vui lòng đăng nhập tại {link} để kiểm tra.",
        "Bạn đã được chọn để nhận khoản vay nhanh với lãi suất thấp. Đăng ký ngay tại {link}.",
        "Thông báo: Bạn có một gói quà tặng từ {job}. Nhận ngay tại {link}.",
        "Hệ thống của chúng tôi phát hiện giao dịch đáng ngờ trên tài khoản {bank} của bạn. Vui lòng xác minh tại {link} để tránh bị khóa.",
        "Chúc mừng bạn đã trúng thưởng {prize}. Vui lòng truy cập {link} để nhận giải thưởng.",
        "Cảnh báo bảo mật: Tài khoản {bank} của bạn có dấu hiệu bị xâm nhập. Xác thực ngay tại {link} để bảo vệ tài khoản của bạn.",
        "Đăng ký vay tiền nhanh trong ngày, duyệt hồ sơ 100%. Truy cập {link} để biết thêm chi tiết và nhận khoản vay.",
        "Bạn có một gói quà tặng từ {job}, nhận ngay tại {link}. Đừng bỏ lỡ cơ hội này!",
        "Hệ thống phát hiện giao dịch lạ, vui lòng xác minh tài khoản {bank} của bạn tại {link} để tránh bị khóa và bảo vệ tài sản của bạn.",
        "Chúc mừng bạn đã trúng thưởng {prize} từ chương trình khuyến mãi của chúng tôi. Nhấn vào {link} để nhận giải thưởng ngay hôm nay.",
        "Cảnh báo: Tài khoản ngân hàng {bank} của bạn có hoạt động bất thường. Vui lòng đăng nhập tại {link} để kiểm tra và bảo vệ tài khoản của bạn.",
        "Bạn đã được chọn để nhận khoản vay nhanh với lãi suất thấp. Đăng ký ngay tại {link} để được hỗ trợ nhanh chóng.",
        "Thông báo: Bạn có một gói quà tặng từ {job}. Nhận ngay tại {link} trước khi hết hạn.",
        "Hệ thống của chúng tôi phát hiện giao dịch đáng ngờ trên tài khoản {bank} của bạn. Vui lòng xác minh tại {link} để tránh bị khóa và bảo vệ tài sản của bạn.",
    ]
    
    data = []
    for _ in range(NUM_SAMPLES):
        tpl = random.choice(templates)
        msg = tpl.format(
            prize=random.choice(SCORES),
            link="http://" + random.choice(["vcb", "tcb", "support", "nhanthuong", "vaynhanh", "verify", "secure"]) + str(random.randint(10,99)) + random.choice(LINKS_SCAM),
            bank=random.choice(BANKS),
            money=f"{random.randint(1, 50)}00.000",
            job=random.choice(JOBS),
            phone=str(random.randint(10000000, 99999999))
        )
        data.append([msg, "sms_scam", "2024-05-22"])
    
    return pd.DataFrame(data, columns=["text", "source", "timestamp"])

# --- HÀM SINH TIN NHẮN AN TOÀN (SAFE) ---
def generate_safe_sms():
    templates = [
        "Mã OTP của bạn là {otp}. Vui lòng không chia sẻ mã này cho bất kỳ ai.",
        "{bank}: Số dư tài khoản thay đổi -{money} VND. ội dung: Thanh toán tiền điện.",
        "{bank}: Quý khách vừa nhận được {money} VND từ {name}. Số dư mới: {money}0 VND.",
        "Đơn hàng {job} của bạn đang được giao. Shipper sẽ gọi trước khi đến.",
        "Chúc mừng sinh nhật {name}! Chúc bạn tuổi mới nhiều niềm vui và thành công.",
        "Lịch thi môn Công nghệ phần mềm vào lúc 13h30 tại phòng A{room}.",
        "Hôm nay trời đẹp quá, đi cà phê không {name} ơi?",
        "Tối nay họp nhóm lúc 8h nhé mọi người, nhớ mang laptop.",
        "Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi. Chúc quý khách một ngày tốt lành.",
        "Bác sĩ hẹn tai khám vào thứ {day} tuần sau lúc 9 giờ sáng.",
        "Mã OTP của bạn là {otp}. Vui lòng giữ bí mật mã này để bảo vệ tài khoản của bạn.",
        "{bank}: Giao dịch rút tiền {money} VND thành công. Số dư hiện tại: {money}0 VND.",
        "{bank}: Bạn vừa nhận được {money} VND từ {name}. Số dư mới: {money}0 VND.",
        "Đơn hàng từ {job} đã được xác nhận và sẽ được giao trong vòng 2-3 ngày làm việc.",
        "Chúc mừng {name} đã hoàn thành khóa học trực tuyến về lập trình Python!",
        "Lịch hẹn với bác sĩ vào thứ {day} lúc 10 giờ sáng tại phòng khám số 5.",
        "Cuộc họp nhóm sẽ diễn ra vào lúc 14h tại phòng họp B{room}. Vui lòng đến đúng giờ.",
        "Chúc mừng bạn đã nhận được phần thưởng từ chương trình khuyến mãi {job}!",
        "Nhắc nhở: Bạn có cuộc hẹn với khách hàng vào thứ {day} lúc 15 giờ chiều.",
        "Mã OTP của bạn là {otp}. Vui lòng không chia sẻ mã này với bất kỳ ai để bảo vệ tài khoản của bạn.",
        "{bank}: Giao dịch chuyển khoản {money} VND thành công. Số dư hiện tại: {money}0 VND.",
        "{bank}: Bạn vừa nhận được {money} VND từ {name}. Số dư mới: {money}0 VND.",
        "Đơn hàng từ {job} đã được giao thành công. Cảm ơn bạn đã mua sắm tại cửa hàng chúng tôi!",
        "Chúc mừng {name} đã hoàn thành khóa học trực tuyến về kỹ năng mềm!",
        "Lịch hẹn với bác sĩ vào thứ {day} lúc 11 giờ sáng tại phòng khám số 3.",
        "Cuộc họp nhóm sẽ diễn ra vào lúc 10h tại phòng họp C{room}. Vui lòng đến đúng giờ.",
    ]
    
    data = []
    for _ in range(NUM_SAMPLES):
        tpl = random.choice(templates)
        msg = tpl.format(
            otp=random.randint(100000, 999999),
            bank=random.choice(BANKS),
            money=f"{random.randint(1, 50)}00.000",
            name=random.choice(NAMES),
            job=random.choice(JOBS),
            room=random.randint(100, 500),
            day=random.randint(2, 7)
        )
        data.append([msg, "sms_safe", "2024-05-22"])
    
    return pd.DataFrame(data, columns=["text", "source", "timestamp"])

# --- HÀM SINH URL ĐỘC HẠI ---
def generate_phishing_urls():
    prefixes = ["vietcombank", "techcombank", "mbbank", "shopee-tuyendung", "vay-tien", "nhan-thuong", "he-thong-bao-mat", "xac-thuc-tai-khoan"]
    suffixes = ["-vip", "-online", "-secure", "-vn", "-update", "-login", "-check"]
    tlds = [".xyz", ".top", ".club", ".info", ".net", ".cc", ".online"]
    
    urls = []
    for _ in range(NUM_SAMPLES):
        domain = random.choice(prefixes) + random.choice(suffixes) + str(random.randint(1, 999)) + random.choice(tlds)
        url = f"http://{domain}"
        urls.append(url)
    
    return urls

# --- CHẠY CHƯƠNG TRÌNH ---
def main():
    print("⏳ Đang sinh dữ liệu giả lập (>10000 mẫu mỗi loại)...")
    
    # 1. Tạo SMS Scam
    df_scam = generate_scam_sms()
    df_scam.to_csv(f"{RAW_DIR}/manual_scam.csv", index=False)
    print(f"✅ Đã tạo {len(df_scam)} tin nhắn lừa đảo tại {RAW_DIR}/manual_scam.csv")
    
    # 2. Tạo SMS Safe
    df_safe = generate_safe_sms()
    df_safe.to_csv(f"{RAW_DIR}/manual_safe.csv", index=False)
    print(f"✅ Đã tạo {len(df_safe)} tin nhắn an toàn tại {RAW_DIR}/manual_safe.csv")
    
    # 3. Tạo URL Phishing
    urls = generate_phishing_urls()
    with open(f"{RAW_DIR}/manual_urls.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")
    print(f"✅ Đã tạo {len(urls)} đường link độc hại tại {RAW_DIR}/manual_urls.txt")

    print("\n🎉 HOÀN TẤT! Folder datasets đã đầy ắp dữ liệu.")

if __name__ == "__main__":
    main()