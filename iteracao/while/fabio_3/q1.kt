fun main() {
    val n = readNumber()
    val range = if (n >= 1) 1..n else 1 downTo n
    range.forEach {
        println(it)
    }
}

fun readNumber() : Int = try {
    print("Insira um número maior que zero: ")
    readLine()!!.toInt()
} catch (e: Exception) {
    println("Entrada inválida")
    readNumber()
}