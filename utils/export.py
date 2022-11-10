import xlwt
from datetime import datetime
from django.http import HttpResponse

MDATA = datetime.now().strftime('%Y-%m-%d')




def export_xlsx2(model, filename, queryset, columns):
    
    response = HttpResponse(content_type='applications/ms.excel')
    response['Content-Disposition'] = 'attachment: filename"%s"'% filename
    #response['Content-Disposition'] = 'attachment; filename="form.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("formulario dados")
    
    row_num = 0
    
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    for col_num in range(len(columns)):
        ws.write(row_num,col_num, columns[col_num], font_style)
        
    default_style = xlwt.XFStyle()
    
    rows = queryset
    for row, rowdata in enumerate(rows):
        row_num += 1
        for col, val in enumerate(rowdata):
            ws.write(row_num, col, val, default_style)
            
    wb.save(response)
    return response


def export_xlsx(filename_final, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"'% filename_final

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Iniciais','CNS','CPF','Data Inicio','Unidade','Sexo','Cor','Data Nascimento','Tipo',
               'Endereco','Numero','Complemento','Cep','Responsavel','Tipo','Data Inicio','Situacao']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = queryset
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)    
    wb.save(response)    
    return response
    