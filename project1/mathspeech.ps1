##Source: www.pdq.com/blog/powershell-text-to-speech-examples/
## www.tutorialspoint.com/how-to-get-the-variable-date-type-in-powershell
Add-Type -AssemblyName System.speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer

$speak.Speak("You will be adding two numbers")
Write-Host "You will be adding two numbers together"

$num1 = Read-Host -Prompt "Enter first number (integer)"

try{$int1 = [int]$num1}
catch {throw "This is not an integer"}
if($int1.GetType().Name -eq "Int32") {
    $num2 = Read-Host -Prompt "Enter second number (integer)"
    try{$int2 = [int]$num2}
    catch {throw "This is not an integer"}
    if($int2.GetType().Name -eq "Int32"){
        $answer = $int1 + $int2

        Write-Host("$num1 + $num2 = $answer")
        $speak.Speak("$num1 + $num2 = $answer")
    }
}

