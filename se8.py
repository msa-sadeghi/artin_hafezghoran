# ── توابع محاسباتی ──────────────────────────────
def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b
def divide(a, b):
    if b == 0:
        return "خطا: تقسیم بر صفر!"
    return a / b
def power(a, b):      return a ** b
def modulo(a, b):     return a % b

# ── نمایش منو ──────────────────────────────────
def show_menu():
    print("\n" + "="*30)
    print("   ماشین حساب علمی")
    print("="*30)
    print("1. جمع       (+)")
    print("2. تفریق     (-)")
    print("3. ضرب       (×)")
    print("4. تقسیم     (÷)")
    print("5. توان      (^)")
    print("6. باقیمانده (%)")
    print("0. خروج")
    print("="*30)

# ── گرفتن عدد از کاربر ────────────────────────
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("لطفاً عدد وارد کنید")

# ── اجرای عملیات ───────────────────────────────
def calculate(choice, a, b):
    operations = {
        '1': ('جمع',        add),
        '2': ('تفریق',      subtract),
        '3': ('ضرب',        multiply),
        '4': ('تقسیم',      divide),
        '5': ('توان',       power),
        '6': ('باقیمانده', modulo),
    }
    if choice in operations:
        name, func = operations[choice]
        result = func(a, b)
        print(f"\n نتیجه {name}: {result}")
    else:
        print("انتخاب نامعتبر!")

# ── حلقه اصلی برنامه ──────────────────────────
def main():
    print("به ماشین حساب علمی خوش آمدید!")
    while True:
        show_menu()
        choice = input("انتخاب شما: ")
        if choice == '0':
            print("خداحافظ! ")
            break
        a = get_number("عدد اول: ")
        b = get_number("عدد دوم: ")
        calculate(choice, a, b)

main()
