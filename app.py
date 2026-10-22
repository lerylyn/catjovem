"""Catequese Jovem: app Streamlit (Pré-catequese, Eucaristia e Crisma)."""
from datetime import date

import streamlit as st

st.set_page_config(page_title="Catequese Jovem", page_icon="✝️", layout="wide")

ICONES = {"Pré-catequese": "🌱", "Eucaristia": "🍞", "Crisma": "🕊️"}
PONTOS_POR_ACERTO = 10

# ----------------------------------------------------------------------------
# CONTEÚDO: para adicionar santos ou temas, copie um bloco e edite.
# ----------------------------------------------------------------------------
SANTOS = {
    "agostinho": {
        "nome": "Santo Agostinho", "festa": "28/08", "virtude": "busca sincera por Deus",
        "historia": "Na juventude, Agostinho procurou felicidade em festas, fama e prazeres, mas continuava vazio. Com as orações de sua mãe, Santa Mônica, e a ajuda de Santo Ambrósio, encontrou Jesus e se converteu. Descobriu que o coração humano só descansa em Deus.",
    },
    "jeronimo": {
        "nome": "São Jerônimo", "festa": "30/09", "virtude": "amor à Palavra de Deus",
        "historia": "Estudioso do século IV, São Jerônimo dedicou anos a traduzir a Bíblia para o latim, a língua do povo daquela época. Ele ensinava que não conhecer as Escrituras é não conhecer Cristo.",
    },
    "carlo_acutis": {
        "nome": "São Carlo Acutis", "festa": "12/10", "virtude": "amor à Eucaristia",
        "historia": "Adolescente italiano que gostava de computadores e videogames, Carlo ia à Missa todos os dias. Usou a informática para criar um site sobre milagres eucarísticos. Morreu aos 15 anos, em 2006, oferecendo seu sofrimento pela Igreja, e foi canonizado em 2025.",
    },
    "tarcisio": {
        "nome": "São Tarcísio", "festa": "15/08", "virtude": "coragem",
        "historia": "Jovem cristão dos primeiros séculos, em Roma, levava a Eucaristia aos presos e doentes. Segundo a tradição, foi atacado no caminho e preferiu morrer a entregar o Santíssimo Sacramento.",
    },
    "cura_dars": {
        "nome": "São João Maria Vianney (Cura d’Ars)", "festa": "04/08", "virtude": "misericórdia",
        "historia": "Padre francês do século XIX, estudou com muita dificuldade, mas virou pároco de Ars. Passava longas horas no confessionário, e pessoas de toda a França iam até lá para receber o perdão de Deus.",
    },
    "joana_darc": {
        "nome": "Santa Joana d’Arc", "festa": "30/05", "virtude": "coragem e fidelidade",
        "historia": "Camponesa francesa do século XV, ainda adolescente sentiu que Deus a chamava para ajudar seu país. Enfrentou grandes autoridades e permaneceu fiel à fé mesmo quando foi condenada. Morreu aos 19 anos.",
    },
    "frassati": {
        "nome": "São Pier Giorgio Frassati", "festa": "04/07", "virtude": "amor aos pobres",
        "historia": "Jovem italiano do início do século XX, amava montanhismo, amigos e a Eucaristia. Visitava e ajudava os pobres de Turim, muitas vezes em segredo. Morreu aos 24 anos e foi canonizado em 2025.",
    },
}

TEMAS = {
    "Pré-catequese": [
        {
            "id": "deus_amigo",
            "titulo": "Deus quer ser meu amigo",
            "resumo": "Deus nos criou por amor e colocou no nosso coração o desejo de procurá-lo. Ele não está distante, mas quer ter amizade com cada um de nós.",
            "pontos": [
                "Deus é infinitamente feliz em si mesmo e, por pura bondade, nos criou para compartilhar conosco a sua vida.",
                "O desejo de Deus está no coração de todas as pessoas. Por isso buscamos sentido, amor e felicidade.",
                "Deus nunca deixa de chamar cada pessoa para procurá-lo.",
            ],
            "reflexao": "Onde eu costumo procurar felicidade? Já pensei em procurá-la em Deus?",
            "cic": [1, 27, 30],
            "biblia": [
                {"ref": "Jo 15,15", "explicacao": "Jesus diz que já não nos chama de servos, mas de amigos, porque nos conta tudo o que ouviu do Pai."},
                {"ref": "Gn 1,26-27", "explicacao": "Deus cria o ser humano à sua imagem. Isso mostra o valor e a dignidade de cada pessoa."},
            ],
            "santos": ["agostinho"],
            "quiz": [
                {"pergunta": "Por que Deus nos criou, segundo o Catecismo?",
                 "opcoes": ["Porque estava sozinho e precisava de companhia", "Por pura bondade, para nos fazer participar da sua vida feliz", "Para testar se somos bons"],
                 "correta": 1, "explicacao": "CIC §1: Deus nos criou livremente, por bondade, para compartilhar conosco a sua vida feliz."},
                {"pergunta": "O desejo de Deus que sentimos no coração mostra que…",
                 "opcoes": ["só alguns são chamados a procurar Deus", "fomos criados por Deus e para Deus", "devemos esconder esse desejo"],
                 "correta": 1, "explicacao": "CIC §27: o ser humano foi criado por Deus e para Deus."},
            ],
        },
        {
            "id": "biblia",
            "titulo": "A Bíblia, Deus fala comigo",
            "resumo": "A Bíblia é formada por muitos livros inspirados por Deus. Por meio dela, Deus fala com palavras humanas para nos mostrar quem Ele é e como viver.",
            "pontos": [
                "Deus é o autor principal da Bíblia e inspirou os autores humanos, que escreveram com seu próprio jeito e cultura (CIC 105-106).",
                "A Bíblia se divide em Antigo Testamento, antes de Jesus, e Novo Testamento, com Jesus e a Igreja nascente.",
                "A Igreja venera a Bíblia como venera o Corpo do Senhor, pois nas duas mesas recebemos alimento para a vida (CIC 103).",
            ],
            "reflexao": "Que horário do meu dia poderia reservar para ler um trecho da Bíblia?",
            "cic": [101, 103, 105, 106, 133],
            "biblia": [
                {"ref": "2Tm 3,16-17", "explicacao": "Toda a Escritura é inspirada por Deus e ajuda a ensinar, corrigir e preparar o cristão para o bem."},
                {"ref": "Lc 24,27", "explicacao": "No caminho de Emaús, Jesus explica aos discípulos o que as Escrituras diziam sobre Ele."},
            ],
            "santos": ["jeronimo"],
            "quiz": [
                {"pergunta": "Quem é o autor principal da Bíblia?",
                 "opcoes": ["Os escritores humanos, sozinhos", "Deus, que inspirou os autores humanos", "A Igreja, séculos depois"],
                 "correta": 1, "explicacao": "CIC §105-106: Deus inspirou os autores humanos."},
                {"pergunta": "A Igreja venera a Bíblia como venera…",
                 "opcoes": ["o Corpo do Senhor", "um livro de história", "uma lenda antiga"],
                 "correta": 0, "explicacao": "CIC §103: a Igreja sempre venerou as Escrituras como venera o Corpo do Senhor."},
            ],
        },
    ],
    "Eucaristia": [
        {
            "id": "presenca_real",
            "titulo": "Jesus está na Eucaristia",
            "resumo": "Na Missa, o pão e o vinho se tornam o Corpo e o Sangue de Jesus. Não é um símbolo, é o próprio Jesus, verdadeiramente presente.",
            "pontos": [
                "A Eucaristia é “fonte e ápice” da vida cristã. Toda a vida da Igreja nasce dela e caminha para ela (CIC 1324).",
                "Na Última Ceia, Jesus entregou o pão e o vinho como seu Corpo e Sangue e pediu que fizéssemos isso em memória dele (CIC 1337).",
                "A presença de Cristo é verdadeira, real e substancial. A Igreja chama essa mudança de transubstanciação (CIC 1374 e 1376).",
            ],
            "reflexao": "Como posso me preparar para receber Jesus com mais atenção na próxima Missa?",
            "cic": [1324, 1337, 1374, 1376],
            "biblia": [
                {"ref": "Lc 22,19-20", "explicacao": "Na Última Ceia, Jesus parte o pão e passa o cálice, dizendo que são seu corpo e seu sangue entregues por nós."},
                {"ref": "Jo 6,51", "explicacao": "Jesus se apresenta como o pão vivo descido do céu e promete vida para quem o recebe."},
            ],
            "santos": ["carlo_acutis", "tarcisio"],
            "quiz": [
                {"pergunta": "Na Eucaristia, o pão e o vinho consagrados são…",
                 "opcoes": ["apenas símbolos de Jesus", "verdadeiramente o Corpo e o Sangue de Jesus", "uma lembrança da Última Ceia"],
                 "correta": 1, "explicacao": "CIC §1374 e 1376: Cristo está verdadeira, real e substancialmente presente."},
                {"pergunta": "O que significa dizer que a Eucaristia é “fonte e ápice” da vida cristã?",
                 "opcoes": ["É um momento opcional", "Toda a vida da Igreja nasce dela e caminha para ela", "Só serve para os padres"],
                 "correta": 1, "explicacao": "CIC §1324: a Eucaristia é o centro da vida da Igreja."},
            ],
        },
        {
            "id": "reconciliacao",
            "titulo": "Reconciliação, recomeçar com Deus",
            "resumo": "Quando erramos, nossa relação com Deus e com os outros se machuca. No sacramento da Reconciliação (Confissão), Deus nos perdoa e nos dá força para recomeçar.",
            "pontos": [
                "Quem procura esse sacramento recebe o perdão de Deus e se reconcilia com a Igreja (CIC 1422).",
                "Ele tem vários nomes: Penitência, Confissão, Perdão e Reconciliação (CIC 1423-1424).",
                "Quem tem consciência de pecado grave deve se confessar antes de comungar (CIC 1385 e 1457).",
                "O padre age em nome de Cristo e guarda segredo absoluto sobre o que ouve (CIC 1467).",
            ],
            "reflexao": "O que me impede de pedir perdão, a Deus ou a alguém? O que mudaria se eu desse esse passo?",
            "cic": [1385, 1422, 1424, 1457, 1467],
            "biblia": [
                {"ref": "Lc 15,11-24", "explicacao": "O pai espera o filho que se perdeu, corre ao seu encontro e faz festa. Assim é Deus com quem volta para Ele."},
                {"ref": "Jo 20,22-23", "explicacao": "Jesus ressuscitado dá o Espírito aos apóstolos e o poder de perdoar pecados."},
            ],
            "santos": ["cura_dars"],
            "quiz": [
                {"pergunta": "Antes de comungar, quem tem consciência de pecado grave deve…",
                 "opcoes": ["esperar o tempo passar", "receber o sacramento da Reconciliação", "pedir perdão só em silêncio"],
                 "correta": 1, "explicacao": "CIC §1385 e 1457: é preciso se confessar antes de comungar."},
                {"pergunta": "O que o padre deve guardar sobre o que ouve na confissão?",
                 "opcoes": ["Sigilo absoluto, nunca revela", "Pode contar ao catequista", "Pode contar aos pais do penitente"],
                 "correta": 0, "explicacao": "CIC §1467: o sigilo sacramental é absoluto."},
            ],
        },
    ],
    "Crisma": [
        {
            "id": "dons_espirito",
            "titulo": "O Espírito Santo e seus dons",
            "resumo": "O Espírito Santo é a terceira Pessoa da Santíssima Trindade. Na Crisma, Ele nos une mais a Cristo e à Igreja e nos fortalece com seus dons.",
            "pontos": [
                "“Espírito Santo” é o nome próprio da terceira Pessoa da Santíssima Trindade (CIC 691).",
                "A Crisma completa o Batismo e dá uma força especial do Espírito Santo (CIC 1285 e 1303).",
                "São sete dons: sabedoria, entendimento, conselho, fortaleza, ciência, piedade e temor de Deus, que é respeito amoroso, não medo (CIC 1831).",
            ],
            "reflexao": "Qual desses dons eu mais preciso pedir hoje? Por quê?",
            "cic": [691, 1285, 1303, 1831],
            "biblia": [
                {"ref": "At 2,1-4", "explicacao": "No dia de Pentecostes, o Espírito Santo desce sobre os apóstolos, que passam a anunciar Jesus com coragem."},
                {"ref": "Is 11,2-3", "explicacao": "O profeta anuncia o Espírito de sabedoria, conselho, fortaleza e temor do Senhor, que repousa sobre o Messias."},
            ],
            "santos": ["joana_darc"],
            "quiz": [
                {"pergunta": "Qual destes é um dos sete dons do Espírito Santo?",
                 "opcoes": ["Fortaleza", "Riqueza", "Fama"],
                 "correta": 0, "explicacao": "CIC §1831: sabedoria, entendimento, conselho, fortaleza, ciência, piedade e temor de Deus."},
                {"pergunta": "A Crisma serve para…",
                 "opcoes": ["substituir o Batismo", "completar o Batismo, fortalecendo-nos com o Espírito Santo", "ganhar um presente da Igreja"],
                 "correta": 1, "explicacao": "CIC §1285 e 1303: a Crisma completa o Batismo e dá força especial do Espírito."},
            ],
        },
        {
            "id": "testemunhas",
            "titulo": "Crismados, testemunhas de Jesus",
            "resumo": "Quem recebe a Crisma é chamado a viver e defender a fé com palavras e atitudes, sendo testemunha de Cristo no dia a dia.",
            "pontos": [
                "A Crisma dá força especial para espalhar e defender a fé com palavras e atos (CIC 1285 e 1303).",
                "O sinal do sacramento é a unção com o óleo do crisma, junto com as palavras do rito (CIC 1300).",
                "A Crisma deixa uma marca espiritual e, por isso, é recebida uma só vez (CIC 1304).",
                "Testemunhar é viver a fé em casa, na escola, com os amigos e nas redes sociais.",
            ],
            "reflexao": "Em que situação do meu dia a dia posso mostrar Jesus com minhas atitudes?",
            "cic": [1285, 1300, 1303, 1304],
            "biblia": [
                {"ref": "At 1,8", "explicacao": "Jesus promete a força do Espírito Santo e diz que seremos suas testemunhas."},
                {"ref": "Mt 5,14-16", "explicacao": "Jesus diz que somos luz do mundo. Nossas boas obras devem levar os outros a louvar a Deus."},
            ],
            "santos": ["frassati"],
            "quiz": [
                {"pergunta": "Quantas vezes a Crisma pode ser recebida?",
                 "opcoes": ["Uma só vez, pois deixa marca espiritual", "Todo ano", "Sempre que a pessoa quiser"],
                 "correta": 0, "explicacao": "CIC §1304: a Crisma imprime uma marca espiritual e não se repete."},
                {"pergunta": "Qual é o sinal visível principal da Crisma?",
                 "opcoes": ["A unção com o óleo do crisma, com as palavras do rito", "Água derramada na cabeça", "Pão e vinho"],
                 "correta": 0, "explicacao": "CIC §1300: o sinal é a unção com o óleo, acompanhada das palavras do rito."},
            ],
        },
    ],
}

TODOS = {t["id"]: t for lista in TEMAS.values() for t in lista}
st.session_state.setdefault("acertos", {})  # id do tema -> melhor nota


# ----------------------------------------------------------------------------
# FUNÇÕES
# ----------------------------------------------------------------------------
def santo_do_dia():
    hoje = date.today()
    for s in SANTOS.values():
        if s["festa"] == hoje.strftime("%d/%m"):
            return s, True
    lista = list(SANTOS.values())
    return lista[hoje.timetuple().tm_yday % len(lista)], False


def card_santo(s, titulo=None):
    with st.container(border=True):
        st.subheader(titulo or s["nome"])
        st.caption(f"📅 Festa: {s['festa']}  •  💛 Virtude: {s['virtude']}")
        st.write(s["historia"])


def quiz(t):
    with st.form(f"quiz_{t['id']}"):
        respostas = [
            st.radio(f"**{i + 1}. {q['pergunta']}**", q["opcoes"], index=None, key=f"{t['id']}_{i}")
            for i, q in enumerate(t["quiz"])
        ]
        enviado = st.form_submit_button("Conferir respostas", type="primary")
    if not enviado:
        return
    if None in respostas:
        st.warning("Responda todas as perguntas antes de conferir.")
        return
    acertos = 0
    for q, r in zip(t["quiz"], respostas):
        ok = q["opcoes"].index(r) == q["correta"]
        acertos += ok
        (st.success if ok else st.error)(("Acertou! " if ok else "Quase! ") + q["explicacao"])
    st.session_state.acertos[t["id"]] = max(acertos, st.session_state.acertos.get(t["id"], 0))
    if acertos == len(t["quiz"]):
        st.balloons()
    else:
        st.toast("Releia o conteúdo e tente de novo!", icon="📖")


def inicio():
    st.title("✝️ Catequese Jovem")
    st.write("Aprenda a fé católica de forma simples e direta. Vá em **Estudar**, leia, reflita e teste o que aprendeu!")
    feitos = len(st.session_state.acertos)
    c1, c2 = st.columns(2)
    c1.metric("Temas estudados", f"{feitos} de {len(TODOS)}")
    c2.metric("Pontos", sum(st.session_state.acertos.values()) * PONTOS_POR_ACERTO)
    st.progress(feitos / len(TODOS))
    for col, (etapa, lista) in zip(st.columns(len(TEMAS)), TEMAS.items()):
        ok = sum(t["id"] in st.session_state.acertos for t in lista)
        with col, st.container(border=True):
            st.markdown(f"### {ICONES[etapa]} {etapa}")
            st.progress(ok / len(lista), text=f"{ok} de {len(lista)} temas")
    santo, e_hoje = santo_do_dia()
    card_santo(santo, ("🌟 Santo do dia: " if e_hoje else "🌟 Para conhecer hoje: ") + santo["nome"])


def estudar():
    etapa = st.segmented_control(
        "Etapa", list(TEMAS), default="Pré-catequese", format_func=lambda e: f"{ICONES[e]} {e}"
    ) or "Pré-catequese"
    tid = st.selectbox(
        "Tema",
        [t["id"] for t in TEMAS[etapa]],
        key=f"tema_{etapa}",
        format_func=lambda i: ("✅ " if i in st.session_state.acertos else "📖 ") + TODOS[i]["titulo"],
    )
    t = TODOS[tid]
    aba1, aba2, aba3, aba4 = st.tabs(["📖 Conteúdo", "📜 Palavra de Deus", "🌟 Exemplo de santo", "🎯 Quiz"])
    with aba1:
        st.header(t["titulo"])
        st.write(t["resumo"])
        for p in t["pontos"]:
            st.markdown(f"- {p}")
        st.info("💭 **Para pensar:** " + t["reflexao"])
        st.caption("Fonte: Catecismo da Igreja Católica, §§ " + ", ".join(map(str, t["cic"])))
    with aba2:
        for b in t["biblia"]:
            with st.expander(f"📜 {b['ref']}", expanded=True):
                st.write(b["explicacao"])
        st.caption("Leia a passagem completa na sua Bíblia Pastoral.")
    with aba3:
        for sid in t["santos"]:
            card_santo(SANTOS[sid])
    with aba4:
        quiz(t)


def biblioteca():
    st.title("🌟 Biblioteca de santos")
    busca = st.text_input("Buscar", placeholder="Digite um nome ou uma virtude...").lower()
    achados = [s for s in SANTOS.values() if busca in (s["nome"] + s["virtude"]).lower()]
    if not achados:
        st.info("Nenhum santo encontrado.")
    for col, grupo in zip(st.columns(2), (achados[0::2], achados[1::2])):
        with col:
            for s in grupo:
                card_santo(s)


# ----------------------------------------------------------------------------
# NAVEGAÇÃO
# ----------------------------------------------------------------------------
with st.sidebar:
    st.caption("Conteúdo baseado no Catecismo da Igreja Católica e na Bíblia Pastoral. Confirme sempre com seu catequista.")

st.navigation(
    [
        st.Page(inicio, title="Início", icon="🏠", default=True),
        st.Page(estudar, title="Estudar", icon="📚"),
        st.Page(biblioteca, title="Santos", icon="🌟"),
    ]
).run()
