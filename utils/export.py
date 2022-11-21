import xlwt
from datetime import datetime
from django.http import HttpResponse


MDATA = datetime.now().strftime('%Y-%m-%d')

def substituir(values):
    arr = [('iniciais','Iniciais'),('cns','CNS'),('cpf', 'CPF'),('dtinicio', 'Data Inicio'),('unidade__nome', 'Unidade'),('sexo', 'Sexo'),
           ('cor','Cor'),('dnasc','Data Nascimento'),('log', 'Logradouro'),('end', 'Endereço'),('numero', 'Numero'),('complemento', 'Complemento'),
           ('cep','Cep'),('responsavel','Responsavel'),('tipo', 'Tipo de Acumulo'),('situacao', 'Situação'),('orgaos', 'Orgãos'),]

    for er,subs in arr:
        #texto = texto.replace(er,subs)
        values = [i.replace(er, subs) for i in values]
    return values



def export_xlsx(filename_final, queryset,values):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="%s"'% filename_final

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') 
    

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    
    columns = substituir(values)
    rows = queryset
    row_num = 0
    
    

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    
    font_style = xlwt.XFStyle()
    
    
    for row in rows:
        row_num += 1  
        row = list(row)
        
        
        for col_num in range(len(row)):
            
            #converte datetime em string
            if columns[col_num] == 'Data Nascimento' or columns[col_num] == 'Data Inicio':
                row[col_num] = row[col_num].strftime('%d/%m/%Y')
            
                
            ws.write(row_num, col_num, row[col_num], font_style)
                     
                    
    wb.save(response) 
    return response
    