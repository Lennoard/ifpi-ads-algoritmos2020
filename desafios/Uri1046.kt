fun main() {
    val input = readLine()!!.split(" ").map {
        it.toInt()
    }
    val startTime = input.first()
    val endTime = input.last()

    val timeSpan = getTimeSpan(startTime, endTime)
    println("O JOGO DUROU $timeSpan HORA(S)")
}

fun getTimeSpan(startTime: Int, endTime: Int): Int {
    return when {
        startTime > endTime -> (24 - startTime) + endTime
        endTime > startTime -> endTime - startTime
        else -> 24
    }
}