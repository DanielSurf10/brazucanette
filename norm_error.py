errors = {
    "SPC_INSTEAD_TAB": "Espaços no início da linha",
    "TAB_INSTEAD_SPC": "Encontrado tab quando esperando espaço",
    "CONSECUTIVE_SPC": "Dois ou mais espaços consecutivos",
    "CONSECUTIVE_WS": "Dois ou mais espaços em branco consecutivos",
    "SPC_BFR_OPERATOR": "Faltando espaço antes do operador",
    "SPC_AFTER_OPERATOR": "Faltando espaço após o operador",
    "NO_SPC_BFR_OPR": "Espaço extra antes do operador",
    "NO_SPC_AFR_OPR": "Espaço extra após o operador",
    "SPC_AFTER_PAR": "Faltando espaço após o parêntese (chave/colchete)",
    "SPC_BFR_PAR": "Faltando espaço antes do parêntese (chave/colchete)",
    "NO_SPC_AFR_PAR": "Espaço extra após o parêntese (chave/colchete)",
    "NO_SPC_BFR_PAR": "Espaço extra antes do parêntese (chave/colchete)",
    "SPC_AFTER_POINTER": "Espaço após o ponteiro",
    "SPC_LINE_START": "Espaço/tabulação inesperada no início da linha",
    "SPC_BFR_POINTER": "Espaçamento inadequado antes do ponteiro",
    "SPACE_BEFORE_FUNC": "Espaço antes do nome da função",
    "TOO_MANY_TABS_FUNC": "Tabulações extras antes do nome da função",
    "TOO_MANY_TABS_TD": "Tabulações extras antes do nome typedef",
    "MISSING_TAB_FUNC": "Tabulação em falta antes do nome da função",
    "MISSING_TAB_VAR": "Tabulação em falta antes do nome da variável",
    "TOO_MANY_TAB_VAR": "Tabulação extra antes do nome da variável",
    "LINE_TOO_LONG": "Linha muito longa",
    "EXP_PARENTHESIS": "Parêntese esperado",
    "MISSING_IDENTIFIER": "Qualificador de tipo ou identificador em falta nos argumentos da função",
    "FORBIDDEN_CHAR_NAME": "Identificadores definidos pelo usuário devem conter apenas caracteres minúsculos, dígitos ou ''",
    "TOO_FEW_TAB": "Tabulações em falta para o nível de recuo",
    "TOO_MANY_TAB": "Tabulações extras para o nível de recuo",
    "TOO_MANY_WS": "Espaços em branco extras para o nível de recuo",
    "SPACE_REPLACE_TAB": "Espaço encontrado quando se esperava uma tabulação",
    "TAB_REPLACE_SPACE": "Tabulação encontrada quando se esperava um espaço",
    "TOO_MANY_LINES": "Função com mais de 25 linhas",
    "SPACE_EMPTY_LINE": "Espaço em linha vazia",
    "SPC_BEFORE_NL": "Espaço antes da quebra de linha",
    "TOO_MANY_INSTR": "Muitas instruções em uma única linha",
    "PREPROC_NO_SPACE": "Faltando espaço após diretiva de pré-processador",
    "PREPROC_UKN_STATEMENT": "Declaração de pré-processador não reconhecida",
    "PREPROC_START_LINE": "Declaração de pré-processador não no início da linha",
    "PREPROC_CONSTANT": "Declaração de pré-processador deve conter apenas definições constantes",
    "PREPROC_EXPECTED_EOL": "Fim de linha esperado após declaração de pré-processador",
    "PREPROC_BAD_IF": "Declaração de pré-processador 'if' sem 'endif'",
    "PREPROC_BAD_ELIF": "Declaração de pré-processador 'elif' sem 'if' ou 'elif'",
    "PREPROC_BAD_IFDEF": "Declaração de pré-processador 'ifdef' sem 'endif'",
    "PREPROC_BAD_IFNDEF": "Declaração de pré-processador 'ifndef' sem 'endif'",
    "PREPROC_BAD_ELSE": "Declaração de pré-processador 'else' sem 'if' ou 'elif'",
    "PREPROC_BAD_ENDIF": "Declaração de pré-processador 'endif' sem 'if', 'elif' ou 'else'",
    "PREPROC_BAD_INDENT": "Indentação incorreta na declaração de pré-processador",
    "PREPROC_MULTLINE": "Declaração de pré-processador multilinha é proibida",
    "PREPOC_ONLY_GLOBAL": "Declarações de pré-processador só são permitidas no escopo global",
    "USER_DEFINED_TYPEDEF": "Typedef definido pelo usuário deve começar com 't_'",
    "STRUCT_TYPE_NAMING": "Nome da estrutura deve começar com 's_'",
    "ENUM_TYPE_NAMING": "Nome do enum deve começar com 'e_'",
    "UNION_TYPE_NAMING": "Nome da união deve começar com 'u_'",
    "GLOBAL_VAR_NAMING": "Variável global deve começar com 'g_'",
    "GLOBAL_VAR_DETECTED": "Variável global presente no arquivo. Certifique-se de que seja uma escolha razoável.",
    "EOL_OPERATOR": "Operador lógico no final da linha",
    "EMPTY_LINE_FUNCTION": "Linha vazia na função",
    "EMPTY_LINE_FILE_START": "Linha vazia no início do arquivo",
    "EMPTY_LINE_FUNCTION": "Linha vazia na função",
    "EMPTY_LINE_EOF": "Linha vazia no final do arquivo",
    "WRONG_SCOPE_VAR": "Variável declarada no escopo incorreto",
    "IMPLICIT_VAR_TYPE": "Tipo em falta na declaração de variável",
    "VAR_DECL_START_FUNC": "Declaração de variável não no início da função",
    "TOO_MANY_VARS_FUNC": "Muitas declarações de variáveis em uma função",
    "TOO_MANY_FUNCS": "Muitas funções no arquivo",
    "BRACE_SHOULD_EOL": "Quebra de linha esperada após a chave",
    "CONSECUTIVE_NEWLINES": "Quebras de linha consecutivas",
    "NEWLINE_PRECEDES_FUNC": "Funções devem ser separadas por uma quebra de linha",
    "NL_AFTER_VAR_DECL": "Declarações de variáveis devem ser seguidas por uma quebra de linha",
    "NL_AFTER_PREPROC": "Declaração de pré-processador deve ser seguida por uma quebra de linha",
    "MULT_ASSIGN_LINE": "Múltiplas atribuições em uma única linha",
    "MULT_DECL_LINE": "Múltiplas declarações em uma única linha",
    "DECL_ASSIGN_LINE": "Declaração e atribuição em uma única linha",
    "FORBIDDEN_CS": "Estrutura de controle proibida",
    "SPACE_AFTER_KW": "Faltando espaço após a palavra-chave",
    "RETURN_PARENTHESIS": "O valor de retorno deve estar entre parênteses",
    "EXP_SEMI_COLON": "Ponto e vírgula esperado",
    "EXP_TAB": "Tabulação esperada",
    "NO_ARGS_VOID": "Argumento de função vazio requer 'void'",
    "MISALIGNED_VAR_DECL": "Declaração de variável desalinhada",
    "MISALIGNED_FUNC_DECL": "Declaração de função desalinhada",
    "WRONG_SCOPE_COMMENT": "Comentário inválido neste escopo",
    "MACRO_NAME_CAPITAL": "O nome da macro deve estar em maiúsculas",
    "MACRO_FUNC_FORBIDDEN": "Funções de macro são proibidas",
    "ASSIGN_IN_CONTROL": "Atribuição em estrutura de controle",
    "VLA_FORBIDDEN": "Matriz de comprimento variável proibida",
    "TOO_MANY_ARGS": "Função tem mais de 4 argumentos",
    "INCLUDE_HEADER_ONLY": "Inclusões de arquivos .c são proibidas",
    "INCLUDE_START_FILE": "A inclusão deve estar no início do arquivo",
    "HEADER_PROT_ALL": "A proteção de cabeçalho deve incluir todas as instruções",
    "HEADER_PROT_ALL_AF": "Instruções após a proteção de cabeçalho são proibidas",
    "HEADER_PROT_NAME": "Nome de proteção de cabeçalho errado",
    "HEADER_PROT_UPPER": "A proteção de cabeçalho deve estar em maiúsculas",
    "HEADER_PROT_MULT": "Múltiplas proteções de cabeçalho, apenas uma é permitida",
    "HEADER_PROT_NODEF": "Proteção de cabeçalho sem #define",
    "TERNARY_FBIDDEN": "Operadores ternários são proibidos",
    "TOO_MANY_VALS": "Muitos valores na definição",
    "NEWLINE_IN_DECL": "Quebra de linha na declaração",
    "MULT_IN_SINGLE_INSTR": "Múltiplas instruções em uma única linha de estrutura de controle",
    "NEWLINE_DEFINE": "Quebra de linha na definição",
    "MISSING_TYPEDEF_ID": "Identificador em falta na declaração typedef",
    "LABEL_FBIDDEN": "Declarações de rótulo são proibidas",
    "GOTO_FBIDDEN": "Declarações de salto ('goto') são proibidas",
    "PREPROC_GLOBAL": "Pré-processadores só podem ser usados no escopo global",
    "WRONG_SCOPE_FCT": "Protótipo de função no escopo incorreto",
    "WRONG_SCOPE": "Declaração no escopo incorreto",
    "INCORRECT_DEFINE": "Valores incorretos na definição",
    "BRACE_NEWLINE": "Quebra de linha esperada antes da chave",
    "EXP_NEWLINE": "Quebra de linha esperada após a estrutura de controle",
    "ARG_TYPE_UKN": "Tipo de variável não reconhecido",
    "COMMENT_ON_INSTR": "O comentário deve estar em sua própria linha",
    "COMMA_START_LINE": "Vírgula no início da linha",
    "MIXED_SPACE_TAB": "Espaços e tabulações misturados",
    "ATTR_EOL": "Atributo de função deve estar no final da linha",
    "INVALID_HEADER": "Cabeçalho 42 ausente ou inválido",
    "INCLUDE_MISSING_SP": "Faltando espaço entre 'include' e o nome do arquivo",
}


class NormError:
    def __init__(self, errno, line, col=None):
        self.errno = errno
        self.line = line
        self.col = col
        if col is not None:
            self.error_pos = f"(line: {(str(self.line)).rjust(3)}, col: {(str(self.col)).rjust(3)}):\t"
        else:
            self.error_pos = f"(line: {(str(self.line)).rjust(3)}):\t "
        self.prefix = f"Error: {self.errno:<20} {self.error_pos:>21}"
        self.error_msg = f"{errors.get(self.errno, 'ERROR NOT FOUND')}"

    def __str__(self):
        return self.prefix + self.error_msg


class NormWarning:
    def __init__(self, errno, line, col=None):
        self.errno = errno
        self.line = line
        self.col = col
        if col is not None:
            self.error_pos = f"(line: {(str(self.line)).rjust(3)}, col: {(str(self.col)).rjust(3)}):\t"
        else:
            self.error_pos = f"(line: {(str(self.line)).rjust(3)}):\t "
        self.prefix = f"Notice: {self.errno:<20} {self.error_pos:>21}"
        self.error_msg = f"{errors.get(self.errno, 'WARNING NOT FOUND')}"

    def __str__(self):
        return self.prefix + self.error_msg
