Dim G30_30, G20_20, G20_13, G30_30kW, result, a, b,c()
G30_30 = Array(276, 247, 218, 182, 124, 65, 160, 102)
G30_30kW = Array("3,80","3,40","3,00", "2,50", "1,70", "0,90", "2,20", "1,40")
G20_20 = Array(0.362, 0.324, 0.275, 0.234, 0.168, 0.085, 0.218, 0.140)
G20_13 = Array(0.345, 0.309, 0.273, 0.227, 0.155, 0.082, 0.200, 0.127)


Function range(x , y)
Dim arr(), i
Redim arr(y-1-x)

For i = 0 to y-1-x
arr(i) = x
x = x + 1
Next
range = arr
End Function

Function LenA(x)   
        LenA = UBound(x)+1
End Function



'MsgBox result


Function goster(dizi)
    For Each i in dizi

        MsgBox i
 
    Next
End Function


    Function wattHesapla(x)
    gelen1 = "2,50 kw.1,70 kw.0,90 kw"
    gelen2 = "2,20 kw.1,40 kw"


        Dim dizi1, dizi2, TotalDizi, tmpD

        Select Case x
            case 0 
                TotalDizi = Split(gelen1, ".")
                wattHesapla = TotalDizi
            case 1
                dizi1 = Split(gelen1, ".") 
                dizi2 = Split(gelen2, ".")
                ReDim TotalDizi(LenA(dizi1)+LenA(dizi2)-2)

                For Each i in range(0, LenA(TotalDizi))
                    If  i < LenA(dizi1) Then
                        TotalDizi(i) = dizi1(i)
                    Else
                        TotalDizi(i) = dizi2(i-lenA(dizi1))
                    End If
                Next
                wattHesapla = TotalDizi
            case 2 
                dizi1 = Split(gelen1, ".") 
                dizi2 = Split(gelen2, ".")
                ReDim TotalDizi(LenA(dizi1)+LenA(dizi2)-1)

                For Each i in range(0, LenA(TotalDizi))
                    If  i < LenA(dizi1) Then
                        TotalDizi(i) = dizi1(i)
                    Else
                        TotalDizi(i) = dizi2(i-lenA(dizi1))
                    End If
                Next
                wattHesapla = TotalDizi

        End Select 

    End Function    



Function gasCons(x)
Dim c, result, GasType
Dim G30_30, G20_20, G20_13, G30_30kW, a, b
G30_30 = Array(276, 247, 218, 182, 124, 65, 160, 102)
G30_30kW = Array("3,80","3,40","3,00", "2,50", "1,70", "0,90", "2,20", "1,40")
G20_20 = Array(0.362, 0.324, 0.275, 0.234, 0.168, 0.085, 0.218, 0.140)
G20_13 = Array(0.345, 0.309, 0.273, 0.227, 0.155, 0.082, 0.200, 0.127)
result = 0
a = wattHesapla(x)
'gasdeneme = "G30 - 30 mbar"
'gasdeneme2 = "G20 - 20 mbar"
gasdeneme3 = "G20 - 13 mbar"
If Len(gasdeneme3)>0 Then
    GasType = gasdeneme3
ElseIf Len(gasdeneme2)>0 Then
GasType = gasdeneme2
Else
GasType = gasdeneme
End If
'GasType = "G30 - 30 mbar"
'GasType2 = "G20 - 20 mbar"
'goster(a)

Select Case GasType
    case "G30 - 30 mbar"
        For Each ab in range(0, LenA(a))
            c=Split(a(ab), " ")
            If InStr(1, c(0), "x", 1) > 0 Then
                arr = Split(c(0), "x",-1, 1)
                MsgBox arr(1)
                For Each ac in range(0, LenA(G30_30kW))
                    If arr(1) = G30_30kW(ac) Then
                        result = result + CInt(arr(0))*G30_30(ac)
                        'MsgBox result
                    End If
                Next
            End If
            For Each ax in range(0, LenA(G30_30kW))
                If c(0) = G30_30kW(ax) Then
                    result = result + G30_30(ax)
                End If
            Next
        Next
    
    case "G20 - 20 mbar"
        For Each ab in range(0, LenA(a))
            c=Split(a(ab), " ")
            If InStr(1, c(0), "x", 1) > 0 Then
                arr = Split(c(0), "x",-1, 1)
                'MsgBox arr(1)
                For Each ac in range(0, LenA(G30_30kW))
                    If arr(1) = G30_30kW(ac) Then
                        result = result + CInt(arr(0))*G20_20(ac)
                    End If
                Next
            End If
            For Each ax in range(0, LenA(G30_30kW))
                If c(0) = G30_30kW(ax) Then
                    result = result + G20_20(ax)
                End If
            Next
        Next
    
    case "G20 - 13 mbar"
        For Each ab in range(0, LenA(a))
            c=Split(a(ab), " ")
            If InStr(1, c(0), "x", 1) > 0 Then
                arr = Split(c(0), "x",-1, 1)
                'MsgBox arr(1)
                For Each ac in range(0, LenA(G30_30kW))
                    If arr(1) = G30_30kW(ac) Then
                        result = result + CInt(arr(0))*G20_13(ac)
                    End If
                Next
            End If
            For Each ax in range(0, LenA(G30_30kW))
                If c(0) = G30_30kW(ax) Then
                    result = result + G20_13(ax)
                End If
            Next
        Next
End Select

gasCons = result

End Function

MsgBox gasCons(0)