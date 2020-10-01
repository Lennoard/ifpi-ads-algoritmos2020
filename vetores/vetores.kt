import kotlin.system.exitProcess

val list = mutableListOf<Int>()

fun main() {
    val menu = """
        ==============================================
        1  - Inserir valores
        2  - Inserir em posição
        ==============================================
        3  - Mostrar valor posição
        4  - Mostrar todos os valores
        5  - Mostrar valores ímpares
        6  - Mostrar valores pares
        7  - Mostrar valores primos
        8  - Mostrar valores positivos
        9  - Mostrar valores negativos
        10 - Mostrar valores zerados
        ==============================================
        11 - Remover do início
        12 - Remover do fim
        13 - Remover da posição específica
        14 - Remover tudo
        ==============================================
        15 - Média dos valores
        16 - Ocorrências de um determinado valor
        ==============================================
        0 - Sair
        
        
        Opção:
    """.trimIndent()

    runCatching {
        while (true) {
            checkOption(input(menu).toInt())
        }
    }.getOrElse {
        System.err.println(it.message)
    }
}

fun checkOption(option: Int) = when (option) {
    0 -> exitProcess(0)
    1 -> insert()
    2 -> insert(input("Posição onde inserir:").toInt())
    3 -> getItem()
    4 -> showItems()
    5 -> showItems { it % 2 == 1 }
    6 -> showItems { it % 2 == 0 }
    7 -> showItems { it.isPrime() }
    8 -> showItems { it >= 0 }
    9 -> showItems { it < 0 }
    10 -> showItems { it == 0 }
    11 -> remove(0)
    12 -> remove(list.lastIndex)
    13 -> remove(input("Posição para remover :").toInt())
    14 -> list.clear().also { showSuccess() }
    15 -> showAverage()
    16 -> countOccurrences()

    else -> throw IllegalArgumentException("Opção inválida")
}

fun insert(position: Int = -1) {
    fun askAndAdd(pos: Int) = input("Valor:").toInt().let {
        list.add(pos, it)
    }

    if (position == -1) {
        val amount = input("Quantos valores desejar inserir?").toInt()

        repeat(amount) {
            askAndAdd(list.size)
        }
    } else {
        checkIndex(position)
        askAndAdd(position)
    }

    showSuccess()
}

fun remove(position: Int = -1) {
    checkIndex(position)
    list.removeAt(position)
    showSuccess()
}

fun getItem() = println(list.getOrNull(input("Posição:").toInt())).also {
    showSuccess()
}

fun showItems(selector: ((Int) -> Boolean)? = null) {
    if (selector != null) {
        list.forEach {
            if (selector(it)) {
                println(it)
            }
        }
    } else list.forEach {
        println(it)
    }

    showSuccess()
}

fun showAverage() {
    var sum = 0
    list.forEach { sum += it }

    println("Média de números na lista: ${sum / list.size}")
    showSuccess()
}

fun countOccurrences() {
    val n = input("Número:").toInt()
    var count = 0
    list.forEach {
        if (it == n) {
            count++
        }
    }

    println(count)
    showSuccess()
}

fun Int.isPrime(): Boolean {
    for (i in 2..this / 2) {
        if (this % i == 0) {
            return false
        }
    }
    return true
}

fun showSuccess() = println("Operação realizada com sucesso").also {
    input("Pressione <enter> para continuar...")
}

fun checkIndex(position: Int) {
    if (position !in 0..list.lastIndex) {
        throw IllegalArgumentException("Posição maior ou menor que a própria lista")
    }
}

fun input(message: String): String = print("$message ").run {
    readLine()!!
}