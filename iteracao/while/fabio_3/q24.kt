/*
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00.
 */

data class Survey(val salary: Float, val kids: Int)

fun main() {
    val n = input("Insira a quantidade de habitantes").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    val surveys = mutableListOf<Survey>()

    var count = 0
    while (count < n) {
        val salary = input("Insira o salário").toFloat()
        val kids = input("Insira o número de filhos").toInt()
        surveys.add(Survey(salary, kids))

        count++
    }

    val salaries = surveys.map { it.salary }.sum()
    val kidsCount = surveys.map { it.kids }.sum()
    val lessThen1000 = surveys.filter { it.salary <= 1_000F }

    println("Média de salário da população: ${salaries / surveys.size}")
    println("Média de número de filhos: ${kidsCount / surveys.size}")
    println("Percentual de pessoas com salário de até R$ 1.000,00: ${lessThen1000.size isWhatPercentOf surveys.size}%")
}

private infix fun Number.isWhatPercentOf(target: Number): Double = ((this.toDouble() * 100) / target.toDouble())

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


