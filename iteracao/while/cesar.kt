import java.text.Normalizer
import kotlin.math.abs

fun main() {
    val word = input("Insira a palavra:").unaccent().trim()
    val rotateRange = input("Insira o alcance da rotação:").toInt()

    println(word rotateBy rotateRange)
}

private infix fun String.rotateBy(range: Int): String {
    val sb = StringBuilder()

    forEach { c ->
        if (!c.isLetter()) {
            sb.append(c)
        } else {
            val positive = range >= 0
            val isInBounds = if (positive) c.toInt() + range <= 'z'.toInt() else c.toInt() - abs(range) >= 'a'.toInt()

            if (isInBounds) {
                sb.append(if (positive) {
                    c rotateBy range
                } else {
                    c rotateBy(range * -1)
                })
            } else {
                var tempChar = c
                var rotateCount = 0

                while (true)  {
                    if (rotateCount == abs(range)) break
                    println(tempChar)
                    if (positive) {
                        if (tempChar == 'z') {
                            tempChar = 'a'
                        }
                        tempChar = tempChar rotateBy 1
                        rotateCount++
                    } else {
                        if (tempChar == 'a') {
                            tempChar = 'z'
                        }
                        tempChar = tempChar rotateBy -1
                        rotateCount++
                    }
                }
                sb.append(tempChar)
            }
        }
    }

    return sb.toString()
}

private fun input(message: String): String = print("$message ").run {
    readLine()!!
}

private fun String.unaccent(): String {
    val temp = Normalizer.normalize(this, Normalizer.Form.NFD)
    return Regex("\\p{InCombiningDiacriticalMarks}+").replace(temp, "")
}

private infix fun Char.rotateBy(count: Int): Char = when {
    count >= 0 -> {
        if (isUpperCase()) {
            (this.toLowerCase() + count).toUpperCase()
        }
        this + count
    }
    isUpperCase() -> {
        (this.toLowerCase() - count).toUpperCase()
    }
    else -> this - count
}
