##Source: www.pdq.com/blog/powershell-text-to-speech-examples/

Add-Type -AssemblyName System.speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer

$speak.Speak("You will be adding two numbers")
Write-Host "You will be adding two numbers together"

$num1 = Read-Host -Prompt "Enter first number"
$num2 = Read-Host -Prompt "Enter second number"
$answer = [int]$num1 + [int]$num2

Write-Host("$num1 + $num2 = $answer")
$speak.Speak("$num1 + $num2 = $answer")
