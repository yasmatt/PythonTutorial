from data_generator.generator import generate_romdom_dataset
from xls.xls import read_xls,read_sheet,filter_by_month,create_xls_from_csv,crate_col_mapper

if '__main__' == __name__:
    excel_file_name = 'data.xlsx'
    sheet_name = "売上実績"
    # generate_romdom_dataset('data.csv', num_rows=100)
    # create_xls_from_csv(sheet_name,'data.csv', 'data.xlsx')
    wb = read_xls(excel_file_name)
    ws = read_sheet(wb,sheet_name)
    m = crate_col_mapper(ws)
    filter_by_month(ws,'日付',m)

    print(m)
    # pivot('data.xlsx')
