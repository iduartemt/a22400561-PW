from ninja import Schema


class IngredienteInputSchema(Schema):
    nome: str


class IngredienteOutputSchema(IngredienteInputSchema):
    id: int


class UtilizadorInputSchema(Schema):
    nome: str
    email: str


class UtilizadorOutputSchema(UtilizadorInputSchema):
    id: int


class ReceitaInputSchema(Schema):
    titulo: str
    descricao: str
    tempo_preparacao: int
    utilizador_id: int
    ingredientes_ids: list[int]


class ReceitaOutputSchema(ReceitaInputSchema):
    id: int

    @staticmethod
    def resolve_ingredientes_ids(receita):
        return list(receita.ingredientes.values_list("id", flat=True))
