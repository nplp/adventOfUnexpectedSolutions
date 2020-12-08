import java.io.File
import java.io.InputStream

fun main(args: Array<String>) {

    val inputStream: InputStream = File("input2").inputStream()
    val lineList = mutableListOf<String>()
    inputStream.bufferedReader().useLines { lines -> lines.forEach { lineList.add(it) } }


    val nodeList = mutableListOf<Node>()
    val resultList = mutableListOf<String>()
    var amountList = mutableListOf<Int>()
    lineList.forEach {
        val split = it.split("bags contain")
        val parent = split[0].trimEnd()
        if (!split[1].contains("no other bags")) {
            val children = split[1].split(',')
            val formattedChildren = mutableListOf<Node>()
            children.forEach {
                var manipulated = it.replace(" bags", "")
                manipulated = manipulated.replace(" bag", "")
                manipulated = manipulated.replace(".", "")
                manipulated = manipulated.substring(1)
                var splitIndex = 0
                if (!manipulated[1].isDigit()) {
                    splitIndex = 1
                } else {
                    if (!manipulated[2].isDigit()) {
                        splitIndex = 2
                    } else {
                        if (!manipulated[3].isDigit()) {
                            splitIndex = 3
                        }
                    }
                }
                val amount = manipulated.substring(0, splitIndex).toInt()
                val child = manipulated.substring(splitIndex + 1)
                formattedChildren.add(Node(child, amount, emptyList()))
            }
            nodeList.add(Node(parent, 1, formattedChildren))


        } else {
            nodeList.add(Node(parent, 1, emptyList()))
        }
    }
    val notdone = true
    while (notdone) {
        val toVisit = nodeList.firstOrNull { it.visited == false && it.id != "shiny gold" } ?: break
        toVisit.visit(nodeList, resultList)
    }
    println(resultList.distinct().size)

    val newList = nodeList
    newList.forEach {
        it.visited = false
        it.canHoldShinyGold = false
    }
    nodeList.first { it.id == "shiny gold" }.visitForGold(newList,amountList,1)
    println(amountList.sumBy { it })


}

class Node(
    val id: String,
    val amount: Int,
    var children: List<Node>,
    var visited: Boolean = false,
    var canHoldShinyGold: Boolean = false,
    var multiple: Int = 1
) {
    fun addChild(child: Node) {
        children = children.plus(child)
    }

    fun visit(nodeList: List<Node>, resultList: MutableList<String>): Boolean {
        visited = true
        if (id == "shiny gold" || canHoldShinyGold) {
            return true
        } else {
            children.forEach { child ->
                nodeList.forEach {
                    if (it.id == child.id) {
                        val result = it.visit(nodeList, resultList)
                        if (result == true) {
                            canHoldShinyGold = true
                            resultList.add(id)
                            return true
                        }
                    }
                }
            }
        }
        return false
    }

    fun visitForGold(nodeList: List<Node>,amountList: MutableList<Int>, parentMultiple: Int) {
        if(visited == true) {
            return
        }
        visited = true
        children.forEach { child ->
            multiple = parentMultiple * child.amount
            amountList.add(multiple)
            nodeList.forEach {
                if(it.id == child.id) {
                    it.visitForGold(nodeList,amountList,multiple)
                }
            }
        }
    }
}

