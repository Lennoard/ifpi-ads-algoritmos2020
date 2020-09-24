fun main() {
    val arraySize = print("QUANTOS NÚMEROS PRETENDE DIGITAR? ").run { readLine()!! }.toInt()
    val array = IntArray(arraySize)

    println("\nDigite o número e aperte ENTER em seguida $arraySize vezes")
    repeat(arraySize) { index ->
        array[index] = readLine()!!.toInt()
    }

    with (array) {
        println(this.toList())
        countEvenAndOdd(this)
        countPositiveAndNegative(this)

        with (doublePositives()) {
            println("\n\n${this.toList()}")

            countEvenAndOdd(this)
            countPositiveAndNegative(this)

            var sum = 0.0
            forEach { sum += it }

            println("Média: ${sum / size}")
        }
    }

}

fun countEvenAndOdd(array: IntArray) {
    var evens = 0
    var odds = 0

    array.forEach {
        if (it % 2 == 0) evens++ else odds++
    }

    println("Números pares: $evens")
    println("Números ímpares: $odds")
}

fun countPositiveAndNegative(array: IntArray) {
    var positives = 0
    var negatives = 0

    array.forEach {
        if (it >= 0 ) positives++ else negatives++
    }

    println("Números positivos: $positives")
    println("Números negativos: $negatives")
}

fun IntArray.doublePositives(): IntArray {
    val array = IntArray(size)
    repeat(size) { index ->
        if (this[index] >= 0) {
            array[index] = this[index] * 2
        } else {
            array[index] = this[index] / 2
        }
    }

    return array
}