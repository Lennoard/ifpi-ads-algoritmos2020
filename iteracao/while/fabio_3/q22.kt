/*
Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
numero de identificação e o peso do boi mais magro e do boi mais gordo.
 */

data class Card(val id: Int, val name: String, val weight: Float)

fun main() {
    val n = input("Insira a quantidade de fichas").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    var count = 0
    val cards = mutableListOf<Card>()

    while (count < n) {
        val id = input("Insira o ID").toInt()
        val name = input("Insira o nome")
        val weight = input("Insira o peso").toFloat()

        cards.add(Card(id, name, weight))
        count++
    }

    val skinniest = cards.minBy {
        it.weight
    }

    val fattest = cards.maxBy {
        it.weight
    }

    println("Boi mais magro: $skinniest")
    println("Boi mais gordo: $fattest")
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


