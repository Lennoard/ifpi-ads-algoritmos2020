import java.io.File
import java.util.*

const val WORDS_TXT = "C:\\words.txt"

fun main() {
    val menu = """
        =========     WordPlay    =========
        1 - Palavras com mais de 20 letras
        2 - Palaras sem "e"
        3 - Palavras sem letras selecionadas
        4 - Palavras contendo somente letras selecionadas
        5 - Palavras contendo todas as letras de uma sequência
        6 - Palavras em ordem alfabética
        0 - Sair
        
        Digite uma opção:
    """.trimIndent()

    var option = runCatching {
        input(menu).toInt()
    } .getOrDefault(-1)

    while (option != 0) {
        when (option) {
            1 -> showWordsWithMoreThan20Letters()
            2 -> showWordsWithOutE()
            3 -> showWordsWithoutParticularLetters()
            4 -> showWordsContainingOnly()
            5 -> showWordsContainingAll()
            6 -> showAbecedarianWords()
            else -> println("\n\nOPÇÃO INVÁLIDA")
        }
        option = runCatching {
            input("\n\n$menu").toInt()
        }.getOrDefault(-1)
    }

}

fun showWordsWithMoreThan20Letters() {
    println("\n[PALAVRAS COM MAIS 20 LETRAS]\n")
    forEachWord { word ->
        if (word.length > 20) {
            println(word)
        }
    }
}

fun showWordsWithOutE() {
    println("\n[PALAVRAS SEM A LETRA 'E']\n")
    var eCount = 0
    var totalCount =0
    forEachWord { word ->
        if (word.hasNoE) {
            println(word)
            eCount++
        }
        totalCount++
    }

    val percentage = eCount isWhatPercentOf totalCount
    println("\nPORCENTAGEM DE PALAVRAS SEM 'E': $percentage%")
}

fun showWordsWithoutParticularLetters() {
    val chars = mutableListOf<Char>()

    readSequence().forEach { input ->
        if (input.length > 0) { //isNotEmpty()
            chars.add(input[0])
        }
    }

    var avoidsCount = 0
    forEachWord { word ->
        if (word.avoids(chars)) {
            avoidsCount++
        }
    }

    println("\n[QUANTIDADE DE PALAVRAS SEM '${chars.joinToString()}': $avoidsCount")
}

fun showWordsContainingOnly() {
    val chars = mutableListOf<Char>()

    readSequence().forEach { input ->
        if (input.length > 0) { //isNotEmpty()
            chars.add(input[0])
        }
    }

    println("\nPALAVRAS CONTENDO SOMENTE '$chars':\n")
    forEachWord {
        if (it.usesOnly(chars)) {
            println(it)
        }
    }
}

fun showWordsContainingAll() {
    val chars = mutableListOf<Char>()

    readSequence().forEach { input ->
        if (input.length > 0) { //isNotEmpty()
            chars.add(input[0])
        }
    }

    println("\nPALAVRAS CONTENDO TODAS AS LETRAS DE '$chars':\n")
    forEachWord {
        if (it.usesAll(chars)) {
            println(it)
        }
    }
}

fun showAbecedarianWords() {
    println("\nPALAVRAS EM ORDEM ALFABÉTICA:\n")
    forEachWord {
        if (it.isAbecedarian()) {
            println(it)
        }
    }
}

private val String.hasNoE: Boolean get() = avoids(listOf('e'))

fun String.avoids(that: List<Char>): Boolean {
    for (thisChar in this) {
        for (thatChar in that) {
            if (thisChar == thatChar) return false
        }
    }
    return true
}

fun String.usesOnly(that: List<Char>): Boolean {
    for (thisChar in this) {
        if (!that.contains(thisChar)) {
            return false
        }
    }
    return true
}

fun String.usesAll(chars: List<Char>): Boolean {
    for (c in chars) {
        if (!contains(c)) {
            return false
        }
    }
    return true
}

fun String.isAbecedarian(): Boolean {
    var prev = first()
    for (c in this) {
        if (c < prev) return false
        prev = c
    }
    return true
}

fun readSequence(): List<String> {
    val scanner = Scanner(System.`in`)
    var index = 0
    var lines = 0
    val inputs = mutableListOf<String>()

    println("\nINSIRA A QUANTIDADE DE ENTRADAS")
    while (scanner.hasNext()) {
        if (index == 0) {
            println("\nAGORA INSIRA AS ENTRADAS")
            lines = scanner.nextInt()
            index++
            scanner.nextLine()
        } else {
            inputs.add(scanner.nextLine())
            index++
        }
        if (index > lines) break
    }

    return inputs
}

fun forEachWord(action: (String) -> Unit) = runCatching {
    File(WORDS_TXT).readLines()
}.getOrElse {
    println("Falha ao ler o arquivo words.txt")
    null
}?.let { words ->
    words.forEach {
        action(it)
    }
}

infix fun Number.isWhatPercentOf(other: Number): Double {
    return (this.toDouble() / other.toDouble()) * 100
}

fun input(message: String): String = print("$message ").run {
    readLine()!!
}