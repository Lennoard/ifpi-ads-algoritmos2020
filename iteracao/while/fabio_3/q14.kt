import kotlin.math.pow
import kotlin.math.sqrt

// Leia N, calcule e escreva o maior quadrado menor ou igual a N.
// Por exemplo, se N for igual a 38, o maior quadrado menor
// que 38 é 36 (quadrado de 6).

fun main() {
    val n = input("Insira um número").toDouble().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    println("O maior quadrado menor ou igual a $n é ${n.nearestSquare}")
}

private val Double.nearestSquare : Int get() {
    var nearest = 0
    var count = 1
    while (true) {
        val power = count.toDouble().pow(2)
        if (power > this) break

        nearest = power.toInt()
        count++
    }
    return nearest
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


