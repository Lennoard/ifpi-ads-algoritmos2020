// Leia LimiteSuperior e LimiteInferior e escreva todos os
// números ímpares entre os limites lidos.

fun main() {
    val start = readInt("Insira o limite inferior")
    val end = readInt("Insira o limite superior")

    if (end < start) for (i in end until start) {
        printOddNumber(i)
    } else for (i in start until end) {
        printOddNumber(i)
    }
}

private fun readInt(message: String): Int = print("$message ").run {
    readLine()!!.toInt()
}

private fun printOddNumber(i: Int) {
    if (i % 2 == 1) {
        println(i)
    }
}