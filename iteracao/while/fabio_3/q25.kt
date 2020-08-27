/*
Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco;
Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleição.
 */

fun main() {
    val n = input("Insira a quantidade de eleitores").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    val votes = mutableListOf<Int>()

    var count = 0
    while (count < n) {
        val partialWinner = votes.filter { it in 1..3 }.mostCommonElement()

        val vote = input("Insira o seu voto (1, 2, 3, 9 para nulo ou 0 para em branco)").toInt()

        if (vote == 0) {
            partialWinner?.let {
                println("Seu voto em branco irá para o candidato $partialWinner")
                votes.add(partialWinner)
            }
        }
        votes.add(vote)
        count++
    }

    println("Candidato 1: ${votes.filter { it == 1 }.size} votos")
    println("Candidato 2: ${votes.filter { it == 2 }.size} votos")
    println("Candidato 3: ${votes.filter { it == 3 }.size} votos")
    println("Votos nulos: ${votes.filter { it == 9 }.size} votos")
    println("Votos em branco: ${votes.filter { it == 0 }.size} votos")
    println("Vencedor: ${votes.mostCommonElement()}")
}

private fun <T> List<T>.mostCommonElement(): T? {
    return groupBy { 
        it
    }.mapValues {
        it.value.size
    }.maxBy {
        it.value
    }?.key
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


