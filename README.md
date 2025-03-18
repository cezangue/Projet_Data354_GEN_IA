# Projet_Data354_GEN_IA

# 🤖 Chatbot IA basé sur RAG

Ce projet est un **agent conversationnel** basé sur la génération augmentée par récupération (**Retrieval-Augmented Generation - RAG**) utilisant **LangChain** et **Hugging Face**. Il permet d'extraire des articles d'une source d'actualités, d'indexer les contenus avec **FAISS** et de générer des réponses pertinentes aux questions des utilisateurs.

---

## 🚀 Installation et Exécution en Local  

Le projet est conçu pour être **déployé et testé localement** à l’aide d’un **notebook Jupyter**.

### 🔧 **1. Prérequis**
Assurez-vous d’avoir **Python 3.8+** et **Jupyter Notebook** installés.  
Installez ensuite les dépendances nécessaires :

```sh
pip install -q streamlit pyngrok langchain-huggingface langchain faiss-cpu sentence-transformers beautifulsoup4 requests langchain-community
```

### ▶️ **2. Exécuter le chatbot localement**  
1. Ouvrez **Jupyter Notebook** et exécutez le fichier :  
   ```
   notebooks/Projet_Data354_GEN_IA.ipynb
   ```
2. Une fois le notebook exécuté, l’application Streamlit démarrera automatiquement sur **localhost**.
3. Vous pourrez alors interagir avec le chatbot en accédant à **http://localhost:8501** depuis votre navigateur.

---

## 🌍 Déploiement en ligne (Optionnel)  

Bien que le projet soit conçu pour une exécution locale, vous pouvez le **déployer en ligne** via **ngrok** ou un serveur cloud.  
Exemple de tunnel avec **ngrok** :
```sh
pyngrok ngrok authtoken VOTRE_TOKEN_NGROK
ngrok http 8501
```
Cela vous fournira une **URL publique** pour accéder à votre chatbot.

---

## 📚 Fonctionnalités  

✔ **Scraping d’articles** depuis un site d’actualités.  
✔ **Indexation et recherche intelligente** via FAISS.  
✔ **Génération de réponses IA** basées sur un modèle **Hugging Face**.  
✔ **Déploiement local via Jupyter Notebook et Streamlit**.  

---

## 📂 Structure du projet  

```
/Projet_Data354_GEN_IA
│── /src
│   ├── app.py                  # Fichier principal de l'application Streamlit
│   ├── scraper.py               # Module de scraping des articles
│   ├── chatbot.py               # Module pour le chatbot RAG
│── /notebooks
│   ├── Projet_Data354_GEN_IA.ipynb  # Notebook Jupyter pour exécution locale
│── /data
│   ├── documents_scrapes.json   # Articles scrappés
│── requirements.txt             # Liste des dépendances
│── README.md                    # Documentation
│── .gitignore                    # Fichiers à ignorer sur GitHub
```

---

💡 **Le projet est principalement conçu pour être exécuté localement via le notebook Jupyter.**  
Toutefois, il est possible d'explorer un déploiement en ligne si nécessaire. 🚀
