# --- CONFIG ---
import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

### --- Email --- ###
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS", "").split(",")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

### --- RSS Feeds --- ###
RSS_FEEDS = [
    "https://www.databricks.com/fr/feed",           # Databricks
    "https://www.inria.fr/fr/news_events/rss.xml",  # INRIA
    "https://towardsdatascience.com/feed",          # Towards Data Science
    "https://www.datasciencecentral.com/category/technical-topics/data-science/feed",   # Data Science Central
    "https://machinelearningmastery.com/rss-feed/",  # Machine Learning Mastery
    "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml",      # ScienceDaily
    "https://www.cnil.fr/fr/rss.xml",               # CNIL
    "https://www.actuia.com/feed/",                 # ActuaIA
]

### --- Autres paramètres --- ###
DAYS_BACK = 7  # Nombre de jours pour filtrer les articles récents
SUMMARY_MODEL = "facebook/bart-large-cnn"
