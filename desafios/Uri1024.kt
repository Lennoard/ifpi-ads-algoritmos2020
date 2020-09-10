import java.util.*

/*
Solicitaram para que você construisse um programa simples de criptografia.
Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las.
O processo é muito simples. São feitas três passadas em tod o texto.

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas
3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar
caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e
última passada, tod e qualquer caractere a partir da metade em diante (truncada) devem ser
deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá p
roduzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz
“3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

##Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104),
indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.

##Saída
Para cada entrada, deve-se apresentar a mensagem criptografada.
 */

fun main() {
    val scanner = Scanner(System.`in`)
    var index = 0
    var lines = 0
    val inputs = mutableListOf<String>()

    while (scanner.hasNext()) {
        if (index == 0) {
            lines = scanner.nextInt()
            index++
            scanner.nextLine()
        } else {
            inputs.add(scanner.nextLine())
            index++
        }
        if (index > lines) break
    }

    inputs.forEach {
        println(it.primeiraPassada().segundaPassada().terceiraPassada())
    }
}

fun String.primeiraPassada(): String {
    val sb = StringBuilder()
    forEach {
        sb.append(if (it.islower or it.isUpper) it rotateBy 3 else it)
    }

    return sb.toString()
}

fun String.segundaPassada(): String {
    return this.reversed()
}

fun String.terceiraPassada(): String {
    if (length <= 1) return this
    val sb = StringBuilder()
    val firstHalf = substring(0 until length / 2)
    val secondHalf = substring(length / 2 until length)

    sb.append(firstHalf)
    secondHalf.forEach {
        sb.append(it - 1)
    }
    return sb.toString()
}

infix fun Char.rotateBy(n: Int): Char {
    if (n >= 0) return this + n
    return this - n
}

fun String.reversed(): String {
    if (length <= 0) return this

    val sb = StringBuilder()
    for (i in lastIndex downTo 0) {
        sb.append(this[i])
    }

    return sb.toString()
}

val Char.isUpper get() = this.toInt() in 65..90
val Char.islower get() = this.toInt() in 97..122