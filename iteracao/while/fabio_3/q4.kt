fun main() {
    var start = readInt("Insira o A₀")
    val end = readInt("Insira o limite")
    val r = readInt("Insira a razão")

    require(start in 1..end) { "Limite ou A₀ inválido" }

    while (start <= end) {
        println(start)
        start *= r
    }
}

private fun readInt(message: String): Int = print("$message ").run {
    readLine()!!.toInt()
}


