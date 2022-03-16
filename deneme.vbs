Sub anla
Dim x

x = 0

Value = 9

While x < 5

If Value < 1000 And Value >99 Then

Value = "0" & Value

ElseIf Value < 100 And Value > 9 Then
Value = "00" & Value

ElseIf Value < 10 Then
Value = "000" & Value
End If

MsgBox(Value)

Value = CInt(Value) - 1

x = x + 1

Wend

End Sub

anla()