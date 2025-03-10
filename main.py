import flet as ft


def calcular_inss(salario):
    faixas = [(1518.00, 0.075), (2793.88, 0.09), (4190.83, 0.12), (8157.41, 0.14)]

    inss_total = 0
    salario_restante = salario
    anterior = 0
    memoria_calculo = []

    for limite, aliquota in faixas:
        if salario_restante > 0:
            faixa = min(salario_restante, limite - anterior)
            desconto = faixa * aliquota
            inss_total += desconto
            salario_restante -= faixa
            anterior = limite
            memoria_calculo.append(
                ft.Text(f"{faixa:,.2f} * {aliquota*100:.1f}% = {desconto:,.2f}")
            )

    memoria_calculo.append(
        ft.Text(f"Total INSS: {inss_total:,.2f}", weight=ft.FontWeight.BOLD)
    )
    return round(inss_total, 2), memoria_calculo


def calcular_irrf(salario, dependentes, desconto_simplificado):
    deducao_por_dependente = 189.59 * dependentes
    desconto_simplificado_valor = 564.80 if desconto_simplificado else 0
    memoria_calculo = []

    salario -= deducao_por_dependente + desconto_simplificado_valor
    memoria_calculo.append(ft.Text(f"Salário Base: {salario:,.2f}"))
    memoria_calculo.append(
        ft.Text(
            f"Deduções: Dependentes ({deducao_por_dependente:,.2f}), Simplificado ({desconto_simplificado_valor:,.2f})"
        )
    )

    tabela_irrf = [
        (2259.20, 0, 0),
        (2826.65, 0.075, 169.44),
        (3751.05, 0.15, 381.44),
        (4664.68, 0.225, 662.77),
        (float("inf"), 0.275, 896.00),
    ]

    for limite, aliquota, deducao in tabela_irrf:
        if salario <= limite:
            imposto = (salario * aliquota) - deducao
            memoria_calculo.append(
                ft.Text(
                    f"Base {salario:,.2f} * {aliquota*100:.1f}% - {deducao:,.2f} = {imposto:,.2f}"
                )
            )
            memoria_calculo.append(
                ft.Text(f"Total IRRF: {imposto:,.2f}", weight=ft.FontWeight.BOLD)
            )
            return round(imposto, 2), memoria_calculo

    return 0, memoria_calculo


def formatar_numero(valor):
    return valor.replace(".", "").replace(",", ".")


def main(page: ft.Page):
    page.title = "Calculadora de INSS e IRRF"

    salario_input = ft.TextField(
        label="Digite seu salário bruto",
        value="0",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    dependentes_input = ft.TextField(
        label="Número de dependentes", value="0", keyboard_type=ft.KeyboardType.NUMBER
    )
    desconto_simplificado_chk = ft.Checkbox(
        label="Aplicar desconto simplificado", value=True
    )
    resultado_text = ft.Column()
    memoria_text = ft.Column(spacing=10)

    def calcular(event):
        salario_bruto = float(formatar_numero(salario_input.value))
        dependentes = int(dependentes_input.value)
        desconto_simplificado = desconto_simplificado_chk.value

        inss, memoria_inss = calcular_inss(salario_bruto)
        base_irrf = salario_bruto - inss
        irrf, memoria_irrf = calcular_irrf(
            base_irrf, dependentes, desconto_simplificado
        )
        salario_liquido = salario_bruto - inss - irrf

        resultado_text.controls = [
            ft.Text(
                f"INSS: R$ {inss:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            ),
            ft.Text(
                f"Base IRRF: R$ {base_irrf:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            ),
            ft.Text(
                f"IRRF: R$ {irrf:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            ),
            ft.Text(
                f"Salário Líquido: R$ {salario_liquido:,.2f}".replace(",", "X")
                .replace(".", ",")
                .replace("X", "."),
                weight=ft.FontWeight.BOLD,
            ),
        ]

        memoria_text.controls = (
            [ft.Text("📌 Memória de Cálculo do INSS:", weight=ft.FontWeight.BOLD)]
            + memoria_inss
            + [ft.Text("📌 Memória de Cálculo do IRRF:", weight=ft.FontWeight.BOLD)]
            + memoria_irrf
        )

        page.update()

    calcular_btn = ft.ElevatedButton("Calcular", on_click=calcular)

    page.add(
        salario_input,
        dependentes_input,
        desconto_simplificado_chk,
        calcular_btn,
        resultado_text,
        memoria_text,
    )


ft.app(target=main, view=ft.WEB_BROWSER)
# ft.app(target=main)
