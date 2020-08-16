// Leia um número N, some todos os números inteiros entre
// 1 e N e escreva o resultado obtido.

fun main() {
    val n = input("Insira um número").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    var sum = 0
    (1..n).forEach { sum += it }

    println("Soma dos números inteiros: $sum")

}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


