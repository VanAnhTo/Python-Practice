#include <Excel.au3>


Local $oExcel = _Excel_Open()
Local $oWorkbook1 = _Excel_BookOpen($oExcel, "E:\Draft\DataToComment.xlsx")
Local $oRange = $oWorkbook1.ActiveSheet.Range("A4:J7")
_Excel_RangeCopyPaste($oWorkbook1.ActiveSheet, $oRange)

