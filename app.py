"""Catequese Jovem: app Streamlit (Pré-catequese, Eucaristia e Crisma)."""
from datetime import date
from pathlib import Path

import streamlit as st
import yaml

DATA = Path(__file__).parent / "data"
ETAPAS = {"Pré-catequese": "pre_catequese", "Eucaristia": "eucaristia", "Crisma": "crisma"}
ICONES = {"Pré-catequese": "🌱", "Eucaristia": "🍞", "Crisma": "🕊️"}
PONTOS_POR_ACERTO = 10

st.set_page_config(page_title="Catequese Jovem", page_icon="✝️", layout="wide")


@st.cache_data
def carregar(nome: str):
    return yaml.safe_load((DATA / f"{nome}.yaml").read_text(encoding="utf-8"))


SANTOS = carregar("santos")
TEMAS = {etapa: carregar(arq) for etapa, arq in ETAPAS.items()}
TODOS = {t["id"]: t for lista in TEMAS.values() for t in lista}
st.session_state.setdefault("acertos", {})  # id do tema -> melhor nota


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
        "Etapa", list(ETAPAS), default="Pré-catequese", format_func=lambda e: f"{ICONES[e]} {e}"
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


with st.sidebar:
    st.caption("Conteúdo baseado no Catecismo da Igreja Católica e na Bíblia Pastoral. Confirme sempre com seu catequista.")

st.navigation(
    [
        st.Page(inicio, title="Início", icon="🏠", default=True),
        st.Page(estudar, title="Estudar", icon="📚"),
        st.Page(biblioteca, title="Santos", icon="🌟"),
    ]
).run()
