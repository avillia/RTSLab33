from openpyxl import Workbook

import math


def fermat_factor(N, sheet):
    if N % 2 != 1:
        raise ValueError
    else:
        a = math.ceil(N ** 0.5)
        b2 = a ** 2 - N

        iteration = 1
        sheet['A1'] = f"Iteration {iteration}"
        sheet['B1'] = f"a = {a}"
        sheet['C1'] = f"b2 = {b2}"

        while int(b2 ** 0.5) != b2 ** 0.5:
            a += 1
            b2 = a ** 2 - N

            iteration += 1
            sheet[f'A{iteration}'] = f"Iteration {iteration}"
            sheet[f'B{iteration}'] = f"a = {a}"
            sheet[f'C{iteration}'] = f"b2 = {b2}"

        p, q = int(a - b2 ** 0.5), int(a + b2 ** 0.5)

        sheet[f'A{iteration+2}'] = f"Final result is:"
        sheet[f'B{iteration+2}'] = f"p = {p}"
        sheet[f'C{iteration+2}'] = f"q = {q}"


if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    fermat_factor(591, sheet=ws)
    wb.save("Lab31.xlsx")
