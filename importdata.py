import xlrd
from app import db
from app.models import User

def read_excel():
    workbook = xlrd.open_workbook(r'./users.xlsx')
    sheet1 = workbook.sheet_by_index(0)
    cols = sheet1.col_values(0)
    for i in range(1, sheet1.nrows):
        user = User(name=sheet1.cell(i, 0).value,
                    stu_number=str(int(sheet1.cell(i, 1).value)),
                    password=str(int(sheet1.cell(i, 2).value)))
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    read_excel()