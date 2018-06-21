#include <Excel.au3>


Local $oExcel = _Excel_Open()
Local $oWorkbook1 = _Excel_BookOpen($oExcel, "E:\Draft\DataToComment.xlsx")
Local $oRange = $oWorkbook1.ActiveSheet.Range("A4:J7")
_Excel_RangeCopyPaste($oWorkbook1.ActiveSheet, $oRange)

_Excel_Close($oExcel)


;~ $oExcel = ObjCreate("Excel.Application")
;~ $oExcel.Visible = 1
;~ $oExcel.WorkBooks.Open ("E:\Draft\DataToComment.xlsx") ;opens the Excel file I want
;~ $oExcel.Application.ActiveSheet.Range("A1:J7").Select ;selects the first set of data I want
;~ $oExcel.Application.Selection.Copy  ;

;MsgBox(0,"Excel popup","COPIED")