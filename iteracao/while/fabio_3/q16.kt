// Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
//(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.

fun main() {
    val n = input("Insira um número").toInt().also {
        require(it >= 2) { "Deve ser maior que 2" }
    }

    var n1 = 1
    var n2 = 0

    for (i in 0 until n) {
        n1 += n2
        n2 = n1 - n2
        println(n1)
    }
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


