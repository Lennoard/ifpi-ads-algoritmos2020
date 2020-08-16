// Leia N e uma lista de N números e escreva o maior número da lista.

fun main() {
    val n = input("Insira um número").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    var greatest = 0
    repeat(n) {
        readLine()?.toInt()?.let { line ->
            if (line > greatest) {
                greatest = line
            }
        }
    }

    println("O maior número é: $greatest")
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


