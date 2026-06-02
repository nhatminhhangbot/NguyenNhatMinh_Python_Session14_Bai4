"""
1. Hàm phụ trợ calculate_average(student)
- Tên hàm: calculate_average
- Input: dictionary student chứa thông tin 1 sinh viên
- Output: Điểm trung bình (số thực)
2. Hàm display_grades(records)
- Tên hàm: display_grades
- Input: List records chứa các dictionary sinh viên
- Output: None (Chỉ in bảng điểm ra màn hình)
3. Hàm update_student_score(records)
- Tên hàm: update_student_score
- Input: List records chứa các dictionary sinh viên
- Output: None (Cập nhật trực tiếp vào list records)
4. Hàm generate_report(records)
- Tên hàm: generate_report
- Input: List records chứa các dictionary sinh viên
- Output: None (Chỉ in báo cáo ra màn hình)
5. Hàm find_valedictorian(records)
- Tên hàm: find_valedictorian
- Input: List records chứa các dictionary sinh viên
- Output: None (Chỉ in vinh danh ra màn hình)
"""

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def display_grades(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start = 1):
        avg_score = calculate_average(student)

        if avg_score >= 8.0:
            rank = "Giỏi"
        elif avg_score >= 6.5:
            rank = "Khá"
        elif avg_score >= 5.0:
            rank = "Trung bình"
        else:
            rank = "Yếu"

        print(f"{index}. [{student['student_id']}] {student['name']:<12} | "
              f"Toán: {student['math']:3.1f} | "
              f"Lý: {student['physics']:3.1f} | "
              f"Hóa: {student['chemistry']:3.1f} | "
              f"ĐTB: {avg_score:.2f} - {rank}")
    print("---------------------------")

def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()

    target_student = None
    for student in records:
        if student["student_id"] == student_id:
            target_student = student
            break

    if not target_student:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
    
    subjects = {"1": "math", "2": "physics", "3": "chemistry"}
    names = {"math": "Toán", "physics": "Lý", "chemistry": "Hóa"}

    while True:
        choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ").strip()
        if choice in subjects:
            selected_subject = subjects[choice]
            break
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 3!")

    while True:
        score_input = input("Nhập điểm mới: ").strip()
        if score_input and score_input.count('.') <= 1 and score_input.replace('.', '', 1).isdigit():
            new_score = float(score_input)

            if 0 <= new_score <= 10:
                break
            else:
                print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        else:
            print("Điểm số không hợp lệ. Vui lòng nhập vào một số!")
    
    target_student[selected_subject] = new_score
    print(f">> Đã cập nhật điểm {names[selected_subject]} của sinh viên '{target_student["name"]}' thành {new_score:.1f}.")

def generate_report(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    pass_count = 0
    fail_count = 0

    for student in records:
        avg_score = calculate_average(student)
        if avg_score >= 5.0:
            pass_count += 1
        else:
            fail_count += 1
    
    pass_percentage = (pass_count / len(records)) * 100
    fail_percentage = (fail_count / len(records)) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {len(records)}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_percentage:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_percentage:.2f}%)")
    print("----------------------")

def find_valedictorian(records):
    if len(records) == 0:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    
    valedictorian = records[0]
    max_avg = calculate_average(valedictorian)

    for student in records[1:]:
        current_avg = calculate_average(student)
        if current_avg > max_avg:
            max_avg = current_avg
            valedictorian = student

    print("\n--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {valedictorian["name"]} (Mã: {valedictorian["student_id"]})")
    print(f" Điểm Trung Bình: {max_avg:.2f}")
    print(" Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")
        
    choice = input("Chọn chức năng (1-5): ").strip()
        
    if choice == "1":
        display_grades(student_records)
    elif choice == "2":
        update_student_score(student_records)
    elif choice == "3":
        generate_report(student_records)
    elif choice == "4":
        find_valedictorian(student_records)
    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5!")