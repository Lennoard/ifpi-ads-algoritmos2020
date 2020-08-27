/*
Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário.
 */

fun main() {
    val n = input("Insira a quantidade de funcionários").toInt().also {
        require(it >= 0) { "Deve ser maior que 0" }
    }

    var count = 0
    while (count < n) {
        val id = input("Insira o ID").toInt()
        val hours = input("Insira o número de horas trabalhadas").toInt()
        val dependents = input("Insira a quantidade de dependentes").toInt()

        val salary = (hours * 12.0) + (dependents * 40)
        val inss = 8.5 percentOf salary
        val ir = 5 percentOf salary
        val net = salary - (inss + ir)

        println("Foi descontado R$$inss de INSS, R$$ir de IR")
        println("Salário líquido: R$$net")
        count++
    }
}

private infix fun Number.percentOf(target: Number): Double = ((this.toDouble() * target.toDouble()) / 100)

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}


