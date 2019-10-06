import gspread
from datetime import datetime

# Подключение Google drive
from oauth2client.service_account import ServiceAccountCredentials

try:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Затраты').worksheet('Октябрь')
except:
    print("No internet, can't load Google Spreadsheet")

# ----------
COMMENT_COL = sheet.find("Комментарий").col
SUM_COL = sheet.find("Сумма").col
DELTA_COL = sheet.find("Разница").col
REST_COL = sheet.find("Остаток евро").col
# --------

def get_number_of_rows() -> int:
    return sheet.get_all_values().__len__()

def write_in_sheet(message: list):
    if str(message[0]) == 'Потратил':
        message[1] = '-' + message[1]
    elif str(message[0]) == 'Получил':
        message[1] = '+' + message[1]
    # cell_list = sheet.range('A1' + 'F' + get_number_of_rows())
    # sheet.update_cells(cell_list, )
    __row_number__ = get_number_of_rows()+1
    row =[f'=D{__row_number__-1}', str(message[1]), datetime.now().strftime("%d.%m.%Y"),
          f'=A{__row_number__}+B{__row_number__}', str(message[3])]
    sheet.append_row(row, value_input_option='USER_ENTERED')
    # sheet.insert_row(row, get_number_of_rows() + 1)
    print('wrote in spreadsheet')


def get_spent_value() -> int:
    return sheet.cell(3,8).value


def get_cells_values()->list:
    return sheet.get_all_values()
# def get_user_row(user_id: int) -> int:
#     return sheet.find(str(user_id)).row


# def get_user_state(user_id: int, file: sheet) -> str:
#     return file.sheet1.cell(get_user_row(user_id, file), STATE_COL, ).value
#
#
# def get_user_language(user_id: int, file: sheet) -> str:
#     return file.sheet1.cell(get_user_row(user_id, file), LANGUAGE_COL, ).value
#
#
# def get_user_game_state(user_id: int, file: sheet) -> str:
#     return file.sheet1.cell(get_user_row(user_id, file), GAME_COL, ).value
