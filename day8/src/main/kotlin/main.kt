import java.io.File
import java.io.InputStream

fun main(args: Array<String>) {
    val inputStream: InputStream = File("input").inputStream()
    val lineList = mutableListOf<String>()
    inputStream.bufferedReader().useLines { lines -> lines.forEach { lineList.add(it) } }
    val accList = mutableListOf<Int>()

    var index = 0
    val instructionsList = mutableListOf<Instruction>()
    lineList.forEach {
        instructionsList.add(Instruction(index, it.split(" ")[0], it.split(" ")[1].toInt()))
        index++
    }
    instructionsList[0].run(instructionsList, accList)
    println(accList.sum())
    var notFinished = true
    var changeIndex = -1
    while(notFinished) {
        accList.clear()
        instructionsList.clear()
        index = 0
        lineList.forEach {
            instructionsList.add(Instruction(index, it.split(" ")[0], it.split(" ")[1].toInt()))
            index++
        }
        val toChange = instructionsList.first { it.index > changeIndex && it.mode != "acc" }
        if(toChange.mode == "nop") {
            toChange.mode = "jmp"
        } else {
            toChange.mode = "nop"
        }
        changeIndex = toChange.index
        instructionsList[toChange.index] = toChange
        instructionsList[0].run(instructionsList, accList)

        if(instructionsList[instructionsList.size-1].visited) {
            notFinished = false
        }
    }
    println(accList.sum())
}

class Instruction(
    val index: Int,
    var mode: String,
    val value: Int,
    var visited: Boolean = false
) {

    fun run(instructionsList: List<Instruction>, accList: MutableList<Int>) {
        if (visited) {
            return
        }
        visited = true
        if (mode == "nop") {
            if(index + 1 >= instructionsList.size) {
                return
            }
            instructionsList[index + 1].run(instructionsList, accList)
        } else if (mode == "jmp") {
            if(index + value >= instructionsList.size) {
                return
            }
            instructionsList[index + value].run(instructionsList, accList)
        } else if (mode == "acc") {
            accList.add(value)
            if(index + 1 >= instructionsList.size) {
                return
            }
            instructionsList[index + 1].run(instructionsList, accList)
        }

    }
}