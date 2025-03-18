import os
import streamlit as st
import json
from chatbot import get_answer
from scraper import scrape_articles

# 📌 Titre et message d'accueil
st.title("🤖 Chatbot IA basé sur RAG")
st.write("Bienvenue sur votre agent conversationnel, veuillez me poser votre question.")

# 📌 Scraping des articles
base_url = "https://www.agenceecofin.com/"
documents = scrape_articles(base_url)

if documents:
    articles_data = [{"title": doc.page_content.split("\n")[0], "url": doc.metadata["url"], "content": doc.page_content} for doc in documents]
    with open("data/documents_scrapes.json", "w", encoding="utf-8") as f:
        json.dump(articles_data, f, ensure_ascii=False, indent=4)

    # 📌 Interface utilisateur
    question = st.text_input("Posez votre question ici :")
    if st.button("🔍 Obtenir une réponse"):
        if question:
            with st.spinner("💡 Génération de la réponse..."):
                response_text, source_docs = get_answer(question, documents)

            st.markdown("### 📝 Réponse :")
            st.write(response_text)

            if source_docs:
                st.markdown("### 📚 Sources utilisées :")
                for doc in source_docs:
                    st.markdown(f"- [{doc.metadata['url']}]({doc.metadata['url']})")
        else:
            st.warning("⚠️ Veuillez entrer une question.")

    # 📌 Bouton de téléchargement des articles scrappés
    st.download_button(
        label="📥 Télécharger les articles scrappés",
        data=json.dumps(articles_data, ensure_ascii=False, indent=4),
        file_name="documents_scrapes.json",
        mime="application/json"
    )
else:
    st.warning("⚠️ Aucun article trouvé. Vérifiez l'URL.")
