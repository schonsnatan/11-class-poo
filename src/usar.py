from interface.classes.csv_class import CsvProcessor

arquivo_csv = './exemplo.csv'
filtro = 'estado'
atributo = 'PR'

file1 = CsvProcessor(arquivo_csv)
file1.carregar_csv()
print(file1.filtrar_por(['estado','preco'],['PR',238.68]))