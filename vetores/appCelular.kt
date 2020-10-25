import java.text.NumberFormat
import java.util.*
import kotlin.system.exitProcess

fun main() {
    printMenu()
}

fun printMenu() {
    val selectedPhoneMenu = if (selectedPhoneIndex >= 0) {
        "5  - Editar celular"
    } else {
        ""
    }

    val menu = """
        
        
        <<<<<<<<<<<<      App Celular      >>>>>>>>>>
        
        1  - Cadastrar novo celular
        2  - Remover celular
        3  - Listar celulares
        4  - Buscar celulares
        $selectedPhoneMenu
        =============================================
        0 - Sair
        
        Insira a opção:
    """.trimIndent()

    try {
        checkOption(input(menu).toInt())
    } catch (e: Exception) {
        showError("Erro: ${e.message}")
    }
}

@Throws(IllegalArgumentException::class)
fun checkOption(option: Int) = when (option) {
    0 -> exitProcess(0)
    1 -> insertPhone()
    2 -> removePhone()
    3 -> listPhones()
    4 -> searchPhones()
    5 -> editPhone()

    else -> throw IllegalArgumentException("Opção inválida")
}

fun insertPhone() = try {
    val phone = mutableMapOf<String, Any>(
            "nome"          to input("Nome:"),
            "marca"         to input("Marca:"),
            "tela"          to input("Tela (polegadas):").replaceChar(',', '.').toFloat(),
            "valor"         to input("Valor em reais:").replaceChar(',', '.').toFloat(),
            "cam_frontal"   to input("Câmera frontal (Sim/Não):")
    )
    phones.add(phone)
    showSuccess("Celular adicionado")
} catch (e: Exception) {
    System.err.println("Não foi possível cadastrar o celular, verifique os parâmetros")
    printMenu()
}

fun removePhone() {
    if (selectedPhone == null) {
        System.err.println("Nenhum celular Selecionado, use a opçao de busca ou lista para selecionar um celular")
    } else {
        phones.removeAt(selectedPhoneIndex)
        showSuccess()
    }
}

fun listPhones() = println("Lista de celulares:").also {
    phones.forEach { phone ->
        prettyPrintPhone(phone)
    }
}

fun searchPhones() {
    val query = input("Insira o termo de pesquisa:").toLowerCase()
    val matchingPhones = phones.filter {
        val nameMatches = it.getOrDefault("nome", "").toString().toLowerCase().contains(query)
        val manufactureMatches = it.getOrDefault("marca", "").toString().toLowerCase().contains(query)

        nameMatches or manufactureMatches
    }

    if (matchingPhones.isEmpty()) {
        showError("Nenhum celular corresponde ao termo de pesquisa")
    } else {
        selectPhone(matchingPhones)
    }
}

fun prettyPrintPhone(phone: Map<String, Any>) {
    println("\n\n[${phone["nome"]}]")
    println("Marca: ${phone["marca"]}")
    println("Tela: ${phone["tela"]} polegadas")
    println("Valor: ${(phone["valor"] as Float).toBRL()}")
    println("Câmera frontal?: ${phone["cam_frontal"]}")
}

fun selectPhone(phoneList: List<MutableMap<String, Any>>) {
    if (phoneList.isEmpty()) {
        showError("Nenhum celular cadastrado")
        return
    }

    phoneList.forEachIndexed { index, phone ->
        val name = phone["nome"]
        val manufacturer = if (phone["marca"].toString().isBlank()) "(Marca desconhecida)" else phone["marca"]
        println("${index + 1} - $manufacturer $name")
    }

    val option = runCatching { input("Selecione o celular: ").toInt() }.getOrDefault(0) - 1
    if (option in phoneList.indices) {
        val selectedPhone = phoneList[option]
        selectedPhoneIndex = phones.indexOf(selectedPhone)
        showSuccess("${selectedPhone["nome"]} selecionado")
    } else {
        showError("Opção inválida (opções válidas: ${phoneList.indices})")
    }
}

fun editPhone() {
    if (selectedPhone == null) {
        showError("Nenhum celular selecionado")
        return
    }

    selectedPhone?.apply {
        set("nome", input("Nome:"))
        set("marca", input("Marca:"))
        set("tela", input("Tela (polegadas):").replaceChar(',', '.').toFloat())
        set("valor", input("Valor em reais:").replaceChar(',', '.').toFloat())
        set("cam_frontal", input("Câmera frontal (Sim/Não):"))
    }

    phones[selectedPhoneIndex] = selectedPhone!!

    showSuccess("Celular atualizado")
}

fun showSuccess(message: String = "Operação realizada com sucesso") = println(message).also {
    input("Pressione uma tecla para continuar...")
    printMenu()
}

fun showError(message: String) = System.err.println(message).also {
    input("Pressione uma tecla para continuar...")
    printMenu()
}

fun input(message: String): String = print("$message ").run {
    readLine()!!
}

// ==================================================================================================

fun String.replaceChar(old: Char, new: Char): String = StringBuilder().let {
    for (c in this) {
        it.append(if (c == old) new else c)
    }
    it.toString()
}

fun Number.toBRL() : String {
    val locale = Locale("pt", "BR")
    return NumberFormat.getCurrencyInstance(locale).apply {
        minimumFractionDigits = 2
    }.format(this)
}

// ==================================================================================================

val phones = mutableListOf<MutableMap<String, Any>>()
var selectedPhoneIndex = -1
val selectedPhone: MutableMap<String, Any>? get() = phones.getOrNull(selectedPhoneIndex)
