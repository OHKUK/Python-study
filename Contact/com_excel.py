import win32com.client


#파일 작성
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Add()
# ws = wb.Worksheets("Sheet1")
# ws.Cells(1, 1).Value = "hello world"
# wb.SaveAs('D:\\test\\Python-study\\Contact\\test.xlsx')
# excel.Quit()

#파일 읽기
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# wb = excel.Workbooks.Open('D:\\test\\Python-study\\Contact\\input.xlsx')
# ws = wb.ActiveSheet
# print(ws.Cells(1,1).Value)
# excel.Quit()


#셀에 컬러 넣기
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('D:\\test\\Python-study\\Contact\\input.xlsx')
ws = wb.ActiveSheet

ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10