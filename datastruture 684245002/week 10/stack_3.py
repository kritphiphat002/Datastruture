stack = []
pairs = { ')':'(' ,']':'[', '}':'{' }
opens = set(pairs.values())

expr = input("Enter expression with brackets: ")
valid = True

# ===== ตรวจสอบวงเล็บ =====
for ch in expr:
    if ch in opens:
        stack.append(ch)
        print("push :", ch, "stack =", stack)

    elif ch in pairs:
        if not stack:
            print("Error : stack empty but found closing bracket", ch)
            valid = False
            break

        top = stack.pop()
        print("pop :", top ,"for closing", ch ,"stack =", stack)

        if top != pairs[ch]:
            print("Error: bracket not match ->", top, "vs", ch)
            valid = False
            break

if valid and stack:
    print("Error : still ", stack)
    valid = False


# ===== คำนวณ =====
if valid:
    print("\n--- Calculate Step by Step ---")

    values = []
    operators = []

    def apply_op():
        b = values.pop()
        a = values.pop()
        op = operators.pop()

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b

        print("Calculate :", a, op, b, "=", result)
        values.append(result)

    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    i = 0
    while i < len(expr):
        ch = expr[i]

        # ===== รองรับเลขติดลบ =====
        if ch.isdigit() or (ch == '-' and
           (i == 0 or expr[i-1] in "(+-*/")):

            num = ch
            i += 1
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1

            values.append(int(num))
            print("Push number :", num)
            continue

        elif ch == '(':
            operators.append(ch)

        elif ch == ')':
            while operators and operators[-1] != '(':
                apply_op()
            operators.pop()

        elif ch in "+-*/":
            while (operators and
                   precedence(operators[-1]) >= precedence(ch)):
                apply_op()
            operators.append(ch)

        i += 1

    while operators:
        apply_op()

    print("Final Result :", values[0])


# ===== สรุป =====
if valid:
    print("result : valid")
else:
    print("result : invalid")