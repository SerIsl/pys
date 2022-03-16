Function range(x , y)
Dim arr(), i
Redim arr(y-1-x)

For i = 0 to y-1-x
arr(i) = x
x = x + 1
Next
range = arr
End Function

Dim s 


For Each x in range (0, 15)
s = s + " " + CStr(x)


Next

'MsgBox s
TopTable = "3,00 kW.2,50 kW.1,70 kW.0,90 kW"
Oven = "2,20 kW.1,40 kW"

Function WattTopla2 (x, y)
    Dim  a, result, c, d

    result = 0


    
    a = Split(x, vbCr)
    'MsgBox UBound(a)
    b = Split(y, vbCr)
    ReDim e(Ubound(a)+Ubound(b)+1)

        'MsgBox Ubound(a)


    For Each i in range(0, Ubound(b)+Ubound(a)+2)
        If i < UBound(a)+1 Then
            e(i) = a(i)
        Else
            e(i) = b(i-UBound(a)-1) 
        End If

    Next
    'For Each q in a
    '    MsgBox q
    'Next

    For Each ab in e
        c = Split(ab, " ")
        'MsgBox c(1)
        If InStr(1, c(0), "x", 1) > 0 Then
            
            d = Split(c(0), "x",-1, 1)
            result = result + CInt(d(0))*CInt(d(1)) 
        Else
            result = result + CInt(c(0))
        End If
    'MsgBox c(0)
    Next

  WattTopla2 = result & " W"

End Function

Function WattTopla1 (x)
    Dim  a, result, c, d

    result = 0


    
    a = Split(x, vbCr)
    'MsgBox UBound(a)

    For Each ab in a
        c = Split(ab, " ")
        'MsgBox c(1)
        If InStr(1, c(0), "x", 1) > 0 Then
            
            d = Split(c(0), "x",-1, 1)
            result = result + CInt(d(0))*CInt(d(1)) 
        Else
            result = result + CInt(c(0))
        End If
    'MsgBox c(0)
    Next

  WattTopla1 = result & " W"

End Function

Function kWattTopla2 (x, y, z)
    Dim  a, result, c, d, e()

    result = 0

    a = Split(x, ".")
    'MsgBox UBound(a)
    b = Split(y, ".")
    'MsgBox UBound(b)

    If z = 1 Then

        ReDim e(Ubound(a)+Ubound(b))

        'MsgBox Ubound(a)


        For Each i in range(0, Ubound(b)+Ubound(a)+1)
            If i < UBound(a)+1 Then
                e(i) = a(i)
            Else
                e(i) = b(i-UBound(a)-1) 
            End If

        Next

        'For Each q in e

        '    MsgBox q
        'Next

        For Each ab in e
            c = Split(ab, " ")
            'MsgBox c(1)
            If InStr(1, c(0), "x", 1) > 0 Then
                
                d = Split(c(0), "x",-1, 1)
                result = result + CInt(d(0))*CDbl(d(1)) 
            Else
                result = result + CDbl(c(0))
            End If
        'MsgBox c(0)
        Next

    Else
        ReDim e(Ubound(a)+Ubound(b)+1)

        'MsgBox Ubound(a)


        For Each i in range(0, Ubound(b)+Ubound(a)+2)
            If i < UBound(a)+1 Then
            e(i) = a(i)
            Else
            e(i) = b(i-UBound(a)-1) 
            End If

        Next

        'For Each q in e

        '    MsgBox q
        'Next

        For Each ab in e
            c = Split(ab, " ")
            'MsgBox c(1)
            If InStr(1, c(0), "x", 1) > 0 Then
                
                d = Split(c(0), "x",-1, 1)
                result = result + CInt(d(0))*CDbl(d(1)) 
            Else
                result = result + CDbl(c(0))
            End If
        'MsgBox c(0)
        Next
    
    End If
    MsgBox result & " W"

End Function

'call kWattTopla2(TopTable, Oven, 1)
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


days_30 = Array("02", "04", "06", "09", "11")
days_31 = Array("01", "03", "05", "07", "08", "10", "12")

week = 41
today = DateValue("01-01-2021")
monthofyear = 0

weekofyear = DatePart("ww", today,2)
val = True

While val
    If week = weekofyear Then

        monthofyear = DatePart("m", today,2)
        val = False
    Else
        today = DateAdd("d",30,today)
        weekofyear = DatePart("ww", today,2)
    End If


Wend



MsgBox 