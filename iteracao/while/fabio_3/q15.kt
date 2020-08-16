// Leia N, calcule e escreva os N primeiros
// termos de seqüência (1, 3, 6, 10, 15,...).

fun main() {
    val n = input("Insira um número").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    val triangularNumbers = mutableListOf<Int>()
    var count = 1
    while (true) {
        if (count.isTriangular) {
            triangularNumbers.add(count)
        }
        if (triangularNumbers.size >= n) break
        count++
    }

    println(triangularNumbers.joinToString())
}

private val Int.isTriangular : Boolean get() {
    if (this < 0) return false

    var sum = 0
    var n = 1
    while (sum <= this) {
        sum += n
        if (sum == this) return true
        n++
    }
    return false
}


private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


