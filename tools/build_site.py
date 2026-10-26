"""Builds the portfolio pages (index, 6 case studies, 404, sitemap, robots) from the content below.
Edit the text here, then run:  python tools/build_site.py"""
import hashlib
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://tadrous-william.github.io"
UPWORK = "https://www.upwork.com/freelancers/~019622575b1d53884b"
GITHUB = "https://github.com/Tadrous-William"
UP_ITEM = UPWORK + "?p="
# cache-busting version: changes whenever the CSS or JS changes
VER = hashlib.md5((ROOT / "assets/css/style.css").read_bytes() + (ROOT / "assets/js/main.js").read_bytes()).hexdigest()[:8]

# ---------------------------------------------------------------- small inline icons
ARROW = '<svg class="arrow" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 10h11M11 5l5 5-5 5"/></svg>'
UPWORK_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.6 13.5c-1 0-2-.4-2.8-1.1l.2-1.1v-.1c.2-1.2.9-3.2 2.6-3.2a2.7 2.7 0 0 1 0 5.5Zm0-8.2c-2.4 0-4.3 1.6-5.1 4.2-1.2-1.8-2.1-4-2.6-5.8H8.3v7.1a2.3 2.3 0 0 1-4.6 0V3.7H1v7.1a5 5 0 0 0 10 0V9.6c.5 1 1.1 2 1.8 2.9l-1.6 7.4h2.7l1.2-5.4c1 .7 2.2 1.1 3.5 1.1a5.4 5.4 0 0 0 0-10.9Z"/></svg>'
GITHUB_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2.2c-3.3.7-4-1.4-4-1.4-.6-1.4-1.4-1.8-1.4-1.8-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-5.9 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.7 1.7.3 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5Z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M7 4.5v15l13-7.5z"/></svg>'

ICON_CHAT = '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 6.5h18a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H12l-5 4v-4H5a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2Z"/><path class="dr" d="M9 12h10M9 15.5h6"/></svg>'
ICON_CHART = '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 24h20M4 4v20"/><path class="dr" d="M8 19l5-6 4 3 6-8"/></svg>'
ICON_EXTRACT = '<svg viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3h9l5 5v17H8z"/><path d="M17 3v5h5"/><path class="dr" d="M12 14h6M12 18h6M12 22h4"/></svg>'
ICON_STAR = '<svg viewBox="0 0 24 24" fill="#F97316" aria-hidden="true"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 20 20" fill="none" stroke="#16A34A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 10.5l3.5 3.5 7.5-8"/></svg>'
ICON_SHIELD = '<svg viewBox="0 0 20 20" fill="none" stroke="#C2410C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2.5l6 2.5v4.5c0 4-2.6 6.6-6 8-3.4-1.4-6-4-6-8V5z"/><path d="M7.5 10l2 2 3.5-4"/></svg>'


def upwork_btn(label="Hire me on Upwork", cls="btn btn-primary"):
    return f'<a class="{cls}" href="{UPWORK}" target="_blank" rel="noopener">{UPWORK_ICON}{label}{ARROW}</a>'


def frame(img, alt, w, h, eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<div class="frame"><div class="fbar"><i></i><i></i><i></i></div>'
            f'<img src="{img}" alt="{escape(alt)}" width="{w}" height="{h}" {load}></div>')


SAT_VISUAL = """<div class="sat" role="img" aria-label="Satellite tiles of 10 land types, 97.12% accuracy, 3rd place nationally">
  <div class="tiles">""" + "".join(
    f'<i style="background:{c};animation-delay:{i * 0.18:.2f}s"></i>'
    for i, c in enumerate(["#A3D9A5", "#5E9F6B", "#C9E4A6", "#B9B4AC", "#D6CFC4", "#93C9A0", "#E7D49A", "#E8B9A0", "#7DB6D8", "#5B9BD5",
                           "#5E9F6B", "#A3D9A5", "#7DB6D8", "#E7D49A", "#B9B4AC", "#C9E4A6", "#E8B9A0", "#93C9A0", "#D6CFC4", "#5B9BD5"])) + """</div>
  <div class="sat-score"><b>97.12%</b><span>test accuracy, 10 land types</span><div class="medal">3rd place nationally</div></div>
</div>"""

# ---------------------------------------------------------------- case studies
# images: (file, alt, width, height)
PROJECTS = [
    dict(
        slug="rag-pdf-chat", short="Chat with your PDFs", tag="AI chatbot · RAG", tint="#FFF1E6", tagc=("#FFEAD8", "#C2410C"),
        title="Chat with your PDFs: a chatbot that only answers from your documents",
        card_text="A RAG chatbot that answers from your own PDFs, shows the file and page for every answer, and says so when the answer is not there. Runs 100% on your own computer.",
        desc="RAG chatbot case study: answers only from your PDFs with page citations, 22/22 correct and 8/8 outside questions refused, runs locally.",
        metrics=[("22/22", "questions answered with the right source"), ("8/8", "outside questions correctly refused"), ("1.4 s", "average time per answer")],
        img=("hero-rag-chat.webp", "The chat app: an answer with its PDF and page, and a refusal when the answer is not in the files", 1400, 875),
        problem=["Most chatbots answer with confidence even when the answer is not in your documents. For a business that is a real risk: a wrong policy answer or a made-up product spec costs money and trust.",
                 "The goal: a chatbot you can check. Every answer must come from your files, point to the page, and refuse politely when the information is not there."],
        built=["<b>Upload and index:</b> PDFs are read page by page, so every piece of text keeps its file name and page number.",
               "<b>Hybrid search:</b> each question is matched by meaning (vector embeddings) <b>and</b> by keywords (BM25), and the two rankings are merged with Reciprocal Rank Fusion. Exact terms like product codes are not missed.",
               "<b>Strict answering rules:</b> the model may only use the passages it is given and must cite each one, like [1].",
               "<b>Two guards against made-up answers:</b> if nothing in the files is close to the question, the app refuses before the AI is even asked; if the AI says the answer is not there, the app returns a clear \"no information\" reply.",
               "<b>Private by design:</b> runs locally with Ollama (qwen2.5:7b and nomic-embed-text), so documents never leave the computer. The same pipeline can use OpenAI, Claude or Gemini by changing one function.",
               "<b>Measured, not guessed:</b> an evaluation script asks 30 questions and scores every answer automatically."],
        result_intro="Tested on 30 questions about two sample PDFs (an employee handbook and a product manual): 22 questions that are answered in the files and 8 that are not.",
        table=[("Test", "Result"), ("Answered from the PDFs, with the right source", "<b>22 / 22</b>"), ("Questions not in the PDFs, correctly refused", "<b>8 / 8</b>"), ("Average time per answer (laptop GPU)", "<b>1.4 s</b>")],
        video=("https://cdn.jsdelivr.net/gh/Tadrous-William/rag-pdf-chat@main/demo/RAG_Chat_with_PDFs_demo.mp4", "rag-poster.webp"),
        gallery=[("rag-how.webp", "How it works: read, split, embed, hybrid search, answer with citations", 1400, 1050),
                 ("rag-results.webp", "Evaluation results: 30 out of 30", 1400, 1050)],
        tech=["Python", "Streamlit", "Ollama", "qwen2.5:7b", "nomic-embed-text", "PyMuPDF", "NumPy", "BM25", "RAG"],
        github="rag-pdf-chat", upwork=None,
    ),
    dict(
        slug="ai-invoice-extraction", short="AI Invoice Extraction", tag="AI document extraction", tint="#EAF7F0", tagc=("#DCF5E7", "#0F766E"),
        title="AI invoice and receipt extraction: from scans and photos to checked Excel",
        card_text="Invoices and receipts (PDFs, scans and phone photos) turned into clean, checked Excel data by a local AI model. No cost per page, and documents never leave the computer.",
        desc="AI invoice extraction case study: local LLM and OCR turn invoices and receipts into checked Excel data. Tested on 206 documents, 96-100% fully correct.",
        metrics=[("96%", "of 80 test invoices with every field right"), ("100%", "on 26 public invoice images"), ("206", "documents tested with known answers")],
        img=("inv-before-after.webp", "Before: a noisy, tilted scanned invoice. After: every field extracted and all checks passed", 1400, 875),
        problem=["Typing invoices into Excel is slow and full of small mistakes. Cloud OCR services charge per page and send private financial documents to someone else's servers.",
                 "The goal: drop in PDFs, scans or phone photos and get clean, checked data, with anything doubtful flagged for a human."],
        built=["<b>Read any document:</b> the PDF text layer when there is one, otherwise OCR (RapidOCR) for scans and photos. The page layout is rebuilt line by line and tilted scans are straightened, so prices stay on the right row.",
               "<b>Extract with a local AI model:</b> Qwen 2.5 7B in Ollama fills a fixed schema: vendor, number, dates, customer, currency, subtotal, discount, tax, total and every line item.",
               "<b>Rules for what AI should not guess:</b> dates are read in code in the document's own format, currency symbols become ISO codes, and key fields have layout-based backups.",
               "<b>Math checks:</b> line items vs subtotal, subtotal minus discount plus tax vs total, valid dates. Anything that does not add up goes to a <b>Needs review</b> sheet.",
               "<b>Delivered three ways:</b> an Excel file (Invoices, Line items, Needs review), a web API, and an n8n workflow for automation."],
        result_intro="Tested on 206 documents where the right answers are known:",
        table=[("Test set", "Documents", "Result"), ("Test invoices: PDFs plus noisy, tilted scans (US, UK, EU formats)", "80", "<b>every field right on 96%</b>; totals, dates, customer and all line items 100%"),
               ("Public invoice images (katanaml dataset)", "26", "<b>every field right on 100%</b>"), ("Real scanned shop receipts (ICDAR 2019 SROIE)", "100", "<b>total 95%</b>, shop name 91%, date 91%")],
        result_after="About 20 seconds per document on a laptop GPU, OCR included, with no cost per page.",
        gallery=[("inv-accuracy.webp", "Accuracy on each test set", 1400, 788), ("inv-how.webp", "How the pipeline works", 1400, 788),
                 ("inv-excel.webp", "The Excel output", 1600, 255), ("inv-n8n.webp", "The n8n automation workflow", 1400, 612), ("inv-app.webp", "The web app: drop files, download Excel", 1400, 875)],
        tech=["Python", "Ollama", "Qwen 2.5 7B", "RapidOCR", "FastAPI", "Streamlit", "n8n", "Excel"],
        github="ai-invoice-extraction", upwork="2105389445908152320",
    ),
    dict(
        slug="sentinel2-land-classification", short="Satellite Land Classification", tag="Deep learning · Computer vision", tint="#EEF0FD", tagc=("#E6E4FB", "#4338CA"),
        title="Satellite land classification: 97% accuracy and 3rd place nationally",
        card_text="A deep learning model that recognises 10 types of land (crops, forest, rivers, roads, homes and more) in Sentinel-2 satellite images. I led the team to 3rd place in the national DEPI Data Science track.",
        desc="Sentinel-2 land classification case study: EfficientNet-B0 with transfer learning, 97.12% test accuracy, 3rd place nationally at DEPI (team lead).",
        metrics=[("97.12%", "test accuracy on 10 land types"), ("3rd", "place nationally, DEPI Data Science track"), ("6", "team members, led by me")],
        img=None,
        problem=["Land-cover maps support city planning, farming and environmental monitoring, but labelling satellite images by hand is slow.",
                 "The task: automatically classify Sentinel-2 satellite images (EuroSAT dataset, 10 classes) into land types such as annual crop, forest, highway, industrial, residential, river and sea/lake."],
        built=["<b>Led a 6-person team:</b> project management, the Flask deployment and the final integration.",
               "<b>Clean data split:</b> 70% training, 15% validation, 15% test, with augmentation (rotations, flips, crops) on the training set only.",
               "<b>Honest baselines first:</b> 5 classical models on engineered features such as NDVI and band statistics. The best, Random Forest, reached 81.3%.",
               "<b>Deep learning:</b> compared ResNet-50 and EfficientNet-B0 with ImageNet transfer learning, early stopping and dropout. EfficientNet-B0 gave the best accuracy for its size.",
               "<b>Demo:</b> the model was served as a Flask REST API with a web page to upload an image and get its land type."],
        result_intro="EfficientNet-B0 reached <b>97.12%</b> test accuracy (97.00% on validation), far above the classical baselines:",
        table=[("Model", "Accuracy"), ("<b>EfficientNet-B0 (final)</b>", "<b>97.12%</b>"), ("Random Forest", "81.3%"), ("SVM", "77.6%"), ("KNN", "75.7%"), ("Decision Tree", "69.4%"), ("Logistic Regression", "63.1%")],
        result_after="The project placed <b>3rd nationally</b> in the DEPI Data Science track.",
        gallery=[],
        tech=["Python", "PyTorch", "EfficientNet-B0", "ResNet-50", "Transfer learning", "scikit-learn", "Flask"],
        github="sentinel2-land-classification", upwork="2028129726975729664",
    ),
    dict(
        slug="sales-forecasting", short="Sales Forecasting & Stock Plan", tag="Machine learning · Forecasting", tint="#E8F4FD", tagc=("#DDEFFC", "#0369A1"),
        title="Demand forecasting and stock planning for 200 products",
        card_text="Weekly demand forecasts with a low-high range for the 200 best-selling products of an online store, and a stock plan that covers the next 4 weeks 9 times out of 10.",
        desc="Sales forecasting case study: LightGBM forecasts and stock plan for 200 products, 15% less error than the best simple method, tested on 7 dates.",
        metrics=[("15%", "less error than the best simple method"), ("7", "test dates, 9,694 product-weeks checked"), ("84%", "of real weeks inside the forecast range")],
        img=("fc-app-product.webp", "Forecast app: one product's history, 8-week forecast and low-high range", 1400, 972),
        problem=["An online store has to decide every week how much to order for each product. Too little means lost sales; too much means cash stuck on shelves.",
                 "Real sales data from a UK online gift store (UCI Online Retail II, 1.07M order lines, Dec 2009 to Dec 2011), with wholesale customers whose large orders make single weeks hard to predict."],
        built=["<b>Weekly demand per product</b> for the 200 best sellers, with the store calendar (trading days, Christmas closure, Easter).",
               "<b>Features that matter:</b> recent sales per trading day, the same weeks last year, category and store seasonality, price changes and weeks to Christmas.",
               "<b>LightGBM quantile models</b> give a low, middle and high forecast for each of the next 8 weeks.",
               "<b>Stock plan:</b> the stock that covers the next 4 weeks of demand 9 times out of 10.",
               "<b>Delivered as</b> an Excel workbook (stock plan, weekly forecast, ranges) and a Streamlit app."],
        result_intro="The forecast was made on 7 dates in 2011, each time using only the weeks before that date, and compared with what really sold. Error is WAPE (lower is better):",
        table=[("Method", "Each product, 4 weeks", "Whole store, 4 weeks"), ("<b>My forecast</b>", "<b>39.4%</b>", "<b>12.0%</b>"), ("8-week average", "42.0%", "14.2%"),
               ("Same week last year", "51.5%", "14.5%"), ("Last year x trend", "58.3%", "18.7%"), ("Last week", "63.5%", "22.3%")],
        result_after="That is <b>15% less error</b> than the best simple method on whole-store demand. The ranges are honest too: 84% of real weeks fell inside the low-high range (target 80%).",
        gallery=[("fc-accuracy.webp", "Accuracy against 5 simple methods", 1400, 537), ("fc-backtest.webp", "Backtest: forecast vs real sales for the whole store", 1400, 560),
                 ("fc-app.webp", "The stock plan in the app", 1400, 972)],
        tech=["Python", "LightGBM", "pandas", "DuckDB", "Plotly", "Streamlit", "Excel"],
        github="sales-forecasting", upwork="2105392346625941504",
    ),
    dict(
        slug="nyc-real-estate-dashboard", short="NYC Real Estate Dashboard", tag="Dashboard · Machine learning", tint="#FDF0F5", tagc=("#FDE7EF", "#BE185D"),
        title="NYC real estate investor dashboard with a home price estimator",
        card_text="An interactive dashboard on 367,189 real New York City property sales: market trends, neighbourhoods, a home price estimator with comparable sales, and rental yields by zip code.",
        desc="NYC real estate dashboard case study: 367,189 sales, XGBoost price estimator with 15.3% median error on unseen 2026 sales, rental yields for 136 zip codes.",
        metrics=[("367K", "real property sales, 2019 to 2026"), ("15.3%", "median price error on unseen 2026 sales"), ("136", "zip codes with rental yields")],
        img=("nyc-cover.webp", "NYC real estate investor dashboard", 1400, 1050),
        problem=["Property investors jump between sales records, rent indexes and spreadsheets to answer simple questions: what is this home worth, which areas are rising, and where do rents pay best?",
                 "The goal: one dashboard that answers all three with real data."],
        built=["<b>Data:</b> 367,189 NYC property sales (January 2019 to August 2026), Zillow rent data and US Census zip code centres, downloaded and cleaned by script.",
               "<b>Market overview:</b> sales volume, median price and price per sq ft with year-over-year change, by borough.",
               "<b>Neighbourhoods:</b> fastest-rising areas compared like for like (houses with houses, condos with condos), a sortable table and a map.",
               "<b>Price estimator:</b> an XGBoost model trained on 155,643 sales of 1-3 family homes, with a likely price range and the 6 most comparable recent sales.",
               "<b>Investor view:</b> gross rental yield for 136 zip codes, price vs rent, and an automatic monthly PDF market report."],
        result_intro="The price estimator was tested on <b>11,304 sales from 2026 that it had never seen</b>:",
        table=[("Metric", "Model", "Simple baseline"), ("Median error", "<b>15.3%</b>", "22.7%"), ("Estimates within ±20%", "<b>63%</b>", "-")],
        gallery=[("nyc-estimator.webp", "Price estimator with comparable sales", 1400, 875), ("nyc-investor.webp", "Investor view: rental yields by zip code", 1400, 875), ("nyc-map.webp", "Map of recent sales", 1400, 763)],
        tech=["Python", "Streamlit", "XGBoost", "pandas", "Plotly", "Parquet"],
        github="nyc-real-estate-dashboard", upwork="2105391619908190208",
    ),
    dict(
        slug="powerbi-sales-dashboard", short="Power BI Sales Dashboard", tag="SQL · Power BI · Insights", tint="#FFF8E1", tagc=("#FFF1C7", "#A16207"),
        title="Online store sales: from 1 million messy rows to a Power BI dashboard and 5 recommendations",
        card_text="1,067,371 raw order lines cleaned and modelled in SQL, a 4-page Power BI dashboard, and a 12-slide insights deck with 5 clear recommendations.",
        desc="Power BI case study: 1.07M order lines cleaned in SQL with 9 automated checks, a 4-page dashboard and an insights deck. £19.3M revenue analysed.",
        metrics=[("1.07M", "raw order lines cleaned"), ("£19.3M", "revenue analysed over 2 years"), ("9", "automated data checks")],
        img=("pbi-overview.webp", "Power BI sales overview page", 1422, 800),
        problem=["The raw export of a UK online gift retailer had duplicates, cancellations, fee lines and same-day corrections. A dashboard built on that data would mislead.",
                 "The goal: data you can trust, a dashboard the team can use, and clear answers to where the money comes from."],
        built=["<b>8-step SQL pipeline</b> (DuckDB): removes duplicates, cancellations, fee lines and same-day corrections and fixes country names.",
               "<b>9 automated checks:</b> revenue reconciles, keys are unique, no orphan rows.",
               "<b>Star schema:</b> sales and returns facts with product (4,719), customer (5,849, with RFM segment and cohort), country (43) and date tables.",
               "<b>4-page Power BI report</b> with shared Year and Region filters: sales overview, products (80/20), customers (RFM and cohort retention), returns and order timing.",
               "<b>12-slide insights deck</b> with 5 recommendations."],
        result_intro="What the data showed:",
        table=[("Finding", "Number"), ("Revenue over 2 years", "<b>£19.3M</b> from 39,326 orders"), ("September to November", "<b>36%</b> of the year's revenue"),
               ("Top 20% of products", "<b>78%</b> of revenue"), ("\"Champions\" (22% of customers)", "<b>70%</b> of revenue"), ("Exact duplicate lines removed", "<b>34,335</b>")],
        gallery=[("pbi-products.webp", "Products page: the 80/20 view", 1422, 800), ("pbi-customers.webp", "Customers page: RFM segments and cohort retention", 1422, 800),
                 ("pbi-slide.webp", "The insights deck", 1400, 788)],
        tech=["SQL", "DuckDB", "Power BI", "DAX", "Python", "pandas"],
        github="powerbi-sales-dashboard", upwork="2105390078023376896",
    ),
]

# ---------------------------------------------------------------- shared page parts
def head(title, desc, path, depth):
    up = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<meta name="theme-color" content="#FBF8F3">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{SITE}/{path}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{up}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/css/style.css?v={VER}">
<script>document.documentElement.classList.add("js")</script>
<script src="{up}assets/js/main.js?v={VER}" defer></script>
"""


def nav(depth, home=True):
    up = "../" * depth
    base = "" if home else f"{up}index.html"
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="{up}index.html" aria-label="Tadrous William, home"><span class="mono-mark">TW</span><span>Tadrous William</span></a>
    <nav class="nav-links" aria-label="Main">
      <a href="{base}#about">About</a>
      <a href="{base}#services">Services</a>
      <a href="{base}#work">Work</a>
      <a href="{base}#process">Process</a>
      {upwork_btn()}
    </nav>
    <button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
"""


def footer(depth):
    up = "../" * depth
    return f"""<footer>
  <div class="wrap">
    <span>© <span id="year">2026</span> Tadrous William · AI Engineer &amp; Data Scientist</span>
    <nav aria-label="Footer">
      <a href="{UPWORK}" target="_blank" rel="noopener">Upwork</a>
      <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
      <a href="{up}index.html#top">Back to top</a>
    </nav>
  </div>
</footer>
<div class="sticky-cta">{upwork_btn()}</div>
</body>
</html>
"""


# ---------------------------------------------------------------- home page
def project_card(p, i):
    flip = " flip" if i % 2 else ""
    bg, ink = p["tagc"]
    visual = SAT_VISUAL if p["img"] is None else frame(f"assets/img/{p['img'][0]}", p["img"][1], p["img"][2], p["img"][3])
    pills = "".join(f'<div class="pill"><b>{v}</b><span>{escape(l)}</span></div>' for v, l in p["metrics"][:3])
    return f"""<article class="project{flip} reveal">
  <div class="shot" style="--tint:{p['tint']}">{visual}</div>
  <div class="body">
    <span class="tag" style="background:{bg};color:{ink}">{escape(p['tag'])}</span>
    <h3>{escape(p['short'])}</h3>
    <p>{escape(p['card_text'])}</p>
    <div class="pills">{pills}</div>
    <div class="actions">
      <a class="btn btn-dark" href="work/{p['slug']}.html">Read the case study{ARROW}</a>
      <a class="btn btn-ghost" href="{GITHUB}/{p['github']}" target="_blank" rel="noopener">{GITHUB_ICON}Code</a>
    </div>
  </div>
</article>"""


def mini(name, repo, text):
    return f'<a class="mini" href="{GITHUB}/{repo}" target="_blank" rel="noopener"><b>{name}</b><span>{text}</span></a>'


def build_index():
    work = "\n".join(project_card(p, i) for i, p in enumerate(PROJECTS))
    marquee_items = ["RAG chatbots", "OpenAI API", "Ollama", "Local LLMs", "Python", "PyTorch", "scikit-learn", "XGBoost", "LightGBM",
                     "Streamlit", "FastAPI", "n8n", "Power BI", "SQL", "OCR", "Web scraping", "Selenium", "Playwright", "Excel automation"]
    marquee = "".join(f"<span>{m}</span>" for m in marquee_items * 2)
    jsonld = ('{"@context":"https://schema.org","@type":"Person","name":"Tadrous William","jobTitle":"AI Engineer & Data Scientist",'
              f'"url":"{SITE}/","sameAs":["{UPWORK}","{GITHUB}"],"address":{{"@type":"PostalAddress","addressCountry":"EG"}},'
              '"knowsAbout":["Retrieval-augmented generation","Machine learning","Data science","Power BI","Web scraping"]}')
    html = head("Tadrous William | AI Engineer & Data Scientist (RAG, ML)",
                "Freelance AI engineer and data scientist. I build RAG chatbots that answer from your documents, tested ML models and data pipelines. 100% Job Success on Upwork.",
                "", 0)
    html += f'<script type="application/ld+json">{jsonld}</script>\n</head>\n<body id="top">\n' + nav(0)
    html += f"""<main id="main">

<!-- HERO -->
<section class="hero">
  <div class="bg-dots"></div><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
  <div class="wrap hero-grid">
    <div>
      <div class="status rise"><span class="pulse"></span>Available for new projects on Upwork</div>
      <h1 class="rise d1">I build AI chatbots and ML models that are <span class="hl">tested<svg viewBox="0 0 200 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14 C 50 5, 120 18, 197 8"/></svg></span> before you get them.</h1>
      <p class="lead rise d2">Chatbots that answer from your own documents, machine learning models you can trust, and the data pipelines that feed them. You get clear results, clean code and a short guide.</p>
      <div class="cta-row rise d3">
        {upwork_btn()}
        <a class="btn btn-ghost" href="#work">See my work{ARROW}</a>
      </div>
      <div class="trust rise d3"><span class="stars" aria-hidden="true">★★★★★</span><span>5.0 on every rated job</span><span class="dot"></span><span>100% Job Success</span><span class="dot"></span><span>Replies within a few hours</span></div>
    </div>
    <div class="demo rise d4" aria-label="Animated demo of the PDF chatbot answering questions with sources">
      <div class="window">
        <div class="window-bar"><i></i><i></i><i></i><span>chat-with-your-pdfs</span></div>
        <div class="chat" aria-live="off"><div class="typing"><b></b><b></b><b></b></div></div>
      </div>
      <div class="chip-float c1"><span class="ic" style="background:#DCF5E7">{ICON_CHECK}</span><div>22/22 answered<small>with the right page</small></div></div>
      <div class="chip-float c2"><span class="ic" style="background:#FFEAD8">{ICON_SHIELD}</span><div>8/8 refused<small>when it's not in your files</small></div></div>
    </div>
  </div>
</section>

<!-- PROOF -->
<section class="proof" aria-label="Results">
  <div class="wrap proof-grid">
    <div class="stat reveal" style="--c:#F97316"><div class="num"><span data-count="100">100</span><small>%</small></div><p>Job Success on Upwork</p></div>
    <div class="stat reveal d1" style="--c:#F59E0B"><div class="num"><span data-count="5" data-decimals="1">5.0</span><small>/5</small></div><p>on every rated client job</p></div>
    <div class="stat reveal d2" style="--c:#5EC4A0"><div class="num"><span data-count="3">3</span><small>rd</small></div><p>place nationally at DEPI, as team lead</p></div>
    <div class="stat reveal d3" style="--c:#6366F1"><div class="num"><span data-count="30">30</span><small>/30</small></div><p>chatbot test questions right</p></div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<!-- ABOUT -->
<section id="about">
  <div class="wrap about-grid">
    <div class="portrait reveal"><span class="ring r2"></span><div class="photo"><img src="assets/img/portrait.webp" alt="Tadrous William" width="440" height="440" loading="lazy"></div></div>
    <div class="reveal d1">
      <span class="eyebrow">About me</span>
      <h2>Hi, I'm Tadrous.</h2>
      <p class="lead">I'm an AI engineer and data scientist from Egypt. I study Computer Science at Assiut University and work with clients on Upwork, with 100% Job Success and a 5.0 rating on every rated job.</p>
      <p>I led my team to 3rd place nationally in the DEPI Data Science track with a satellite image model at 97% accuracy. What I care about most is work you can trust: every chatbot is checked with real questions, every model is tested without data leakage, and you get the results in plain English.</p>
      <div class="facts">
        <div><b>15+</b><span>public projects</span></div>
        <div><b>Arabic</b><span>native</span></div>
        <div><b>English</b><span>fluent</span></div>
      </div>
      <div class="cta-row">{upwork_btn()}<a class="btn btn-ghost" href="{GITHUB}" target="_blank" rel="noopener">{GITHUB_ICON}GitHub</a></div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section id="services">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Services</span>
      <h2>What I can build for you</h2>
      <p class="lead">Three kinds of work, all done the same way: a clear plan, real tests, and results explained in plain English.</p>
    </div>
    <div class="services-grid">
      <div class="card reveal">
        <div class="svc-icon" style="background:#FFEAD8;color:#C2410C">{ICON_CHAT}</div>
        <h3>AI chatbots &amp; LLM apps</h3>
        <p>Chatbots that answer from your PDFs, manuals, policies or knowledge base, show the file and page for every answer, and say "not in the documents" instead of making things up.</p>
        <ul>
          <li>ChatGPT (OpenAI), Claude, Gemini, or a private local model</li>
          <li>Hybrid search, anti-hallucination checks, chat memory, OCR</li>
          <li>Tested with real questions before delivery</li>
          <li>As a web app, an API, a website chat, or an n8n, Slack or Telegram bot</li>
        </ul>
        <a class="more" href="{UPWORK}" target="_blank" rel="noopener">Start a chatbot project{ARROW}</a>
      </div>
      <div class="card reveal d1">
        <div class="svc-icon" style="background:#DCF5E7;color:#0F766E">{ICON_CHART}</div>
        <h3>Machine learning &amp; dashboards</h3>
        <p>Prediction, classification and forecasting models, plus data analysis with clear charts, reports and Power BI or Streamlit dashboards.</p>
        <ul>
          <li>Tested properly: cross-validation, backtests, no data leakage</li>
          <li>You see what drives the predictions</li>
          <li>scikit-learn, XGBoost, LightGBM, PyTorch, SQL, Power BI</li>
          <li>A short report your team can read</li>
        </ul>
        <a class="more" href="{UPWORK}" target="_blank" rel="noopener">Start an ML project{ARROW}</a>
      </div>
      <div class="card reveal d2">
        <div class="svc-icon" style="background:#DDEFFC;color:#0369A1">{ICON_EXTRACT}</div>
        <h3>Data extraction &amp; scraping</h3>
        <p>Data from websites, APIs, PDFs, invoices and scanned documents turned into clean Excel, CSV or Google Sheets, plus the script so you can run it again.</p>
        <ul>
          <li>Requests, BeautifulSoup, Selenium, Playwright</li>
          <li>OCR and AI extraction for scans and photos</li>
          <li>Checks that flag anything that does not add up</li>
          <li>Automation with n8n or a scheduled script</li>
        </ul>
        <a class="more" href="{UPWORK}" target="_blank" rel="noopener">Start a data project{ARROW}</a>
      </div>
    </div>
    <p class="note reveal">Native Arabic and fluent English, so I can also build chatbots and models for Arabic text and documents.</p>
  </div>
</section>

<!-- WORK -->
<section id="work" style="background:linear-gradient(180deg, transparent, #F5EFE6 12%, #F5EFE6 88%, transparent)">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Selected work</span>
      <h2>Real projects, real tests</h2>
      <p class="lead">Every number below comes from the project's own evaluation, and the code is public on GitHub.</p>
    </div>
    <div class="work-list">
{work}
    </div>
    <div class="strip reveal">
      <div><h3>Need something like this?</h3><p>Send me your documents or data on Upwork and I'll reply with a plan.</p></div>
      {upwork_btn()}
    </div>
  </div>
</section>

<!-- MORE -->
<section id="more">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">More projects</span>
      <h2>More of my work</h2>
    </div>
    <div class="more-grid">
      <div class="group reveal">
        <h4>Data extraction</h4>
        {mini("B2B Lead List Builder", "business-lead-list", "<em>9,485</em> Texas dental practices from public sources, 96% with a valid phone")}
        {mini("Assisted Living Data Extraction", "assisted-living-data-extraction", "A PDF directory turned into a clean CSV, missing websites filled in")}
        {mini("Book Scraper", "book-scraping-project", "<em>1,000</em> books scraped with Requests and BeautifulSoup")}
        {mini("Google Calendar to Sheets", "google-calendar-to-sheets-automation", "Calendar events written to Google Sheets through the APIs")}
      </div>
      <div class="group reveal d1">
        <h4>Machine learning</h4>
        {mini("Breast Cancer Classification", "breast-cancer-classification", "7 models compared, <em>97.4%</em> accuracy, 0.999 AUC")}
        {mini("Loan Approval Classification", "loan-approval-classification", "XGBoost, <em>93%</em> accuracy on 45,000 loans")}
        {mini("Student Performance Prediction", "student-performance-prediction", "Exam score regression, <em>R² 0.83</em>")}
        {mini("COVID-19 Data Collection", "covid19-data-collection-python", "Daily data for 15 countries, 2022 to 2024, from an API")}
      </div>
      <div class="group reveal d2">
        <h4>Software engineering</h4>
        {mini("AgileFlow", "AgileFlow-.net", "Team project: agile project manager in ASP.NET Core 9 with real-time Kanban")}
        {mini("MiniFAT file system", "OS-Tasks", "A FAT-style file system on a virtual disk, built from scratch in Python")}
        {mini("GLB 3D Model Downloader", "glb-3d-model-downloader", "Automated download of .glb 3D models")}
      </div>
    </div>
    <div class="client reveal">
      <div class="badge">{ICON_STAR}</div>
      <div>
        <h3>Private client work, rated 5.0</h3>
        <p>For a repeat client on Upwork, three AI projects, all rated 5.0: a <a href="{UP_ITEM}2105393879232954368" target="_blank" rel="noopener">deep neural network built from scratch in NumPy</a> (AUC 0.95), a <a href="{UP_ITEM}2105394494344470528" target="_blank" rel="noopener">reinforcement learning agent that learned to land a spacecraft</a> (DQN vs a genetic algorithm), and machine learning notebooks in R.</p>
        <p>Research: a model that predicts acute kidney injury in ICU patients (AUROC 0.965).</p>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIAL -->
<section style="padding-top:40px">
  <div class="wrap">
    <div class="quote-box reveal">
      <span class="quote-mark" aria-hidden="true">&ldquo;</span>
      <blockquote>He delivers high-quality work and it is a pleasure to work with him.</blockquote>
      <div class="stars5" aria-label="5 out of 5 stars">★★★★★</div>
      <cite>Upwork client</cite>
    </div>
  </div>
</section>

<!-- PROCESS -->
<section id="process">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Process</span>
      <h2>How I work</h2>
      <p class="lead">Simple and clear, so you always know what is happening.</p>
    </div>
    <div class="steps">
      <span class="line"></span>
      <div class="step"><div class="n">01</div><h3>We agree on the plan</h3><p>I ask questions and confirm the plan, timeline and price before I start.</p></div>
      <div class="step"><div class="n">02</div><h3>You see a sample first</h3><p>On bigger jobs you get a small working sample early, so there are no surprises.</p></div>
      <div class="step"><div class="n">03</div><h3>I build and test</h3><p>Tested on real data, and you get the numbers, not just "it works".</p></div>
      <div class="step"><div class="n">04</div><h3>You own everything</h3><p>Revisions until it matches your brief. All the code is yours, with a short guide.</p></div>
    </div>
    <div class="send reveal">
      <div><b>For a chatbot</b><span>a few sample documents and the questions your users ask</span></div>
      <div><b>For machine learning</b><span>your data and the question you want answered</span></div>
      <div><b>For extraction or scraping</b><span>the website or documents and the fields you need</span></div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section id="contact" style="padding-top:20px">
  <div class="wrap">
    <div class="final reveal">
      <span class="glow g1"></span><span class="glow g2"></span>
      <h2>Have documents, data or a website to work with?</h2>
      <p>Send me what you have on Upwork and I'll reply with a plan, timeline and price, usually within a few hours.</p>
      <div class="cta-row">{upwork_btn()}<a class="btn btn-ghost" href="{GITHUB}" target="_blank" rel="noopener">{GITHUB_ICON}View my GitHub</a></div>
    </div>
  </div>
</section>

</main>
"""
    html += footer(0)
    (ROOT / "index.html").write_text(html, encoding="utf-8")


# ---------------------------------------------------------------- case study pages
def table_html(rows):
    head_row = "".join(f"<th>{c}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:])
    return f'<table class="table"><thead><tr>{head_row}</tr></thead><tbody>{body}</tbody></table>'


def build_case(p, nxt):
    bg, ink = p["tagc"]
    metrics = "".join(f'<div class="stat rise d3" style="--c:{ink}"><div class="num">{v}</div><p>{escape(l)}</p></div>' for v, l in p["metrics"])
    visual = SAT_VISUAL if p["img"] is None else frame(f"../assets/img/{p['img'][0]}", p["img"][1], p["img"][2], p["img"][3], eager=True)
    built = "".join(f"<li>{b}</li>" for b in p["built"])
    problem = "".join(f"<p>{escape(t)}</p>" for t in p["problem"])
    after = f"<p>{p['result_after']}</p>" if p.get("result_after") else ""
    video = ""
    if p.get("video"):
        src, poster = p["video"]
        video = (f'<h2>Demo video</h2><div class="video" data-src="{src}" role="button" tabindex="0" aria-label="Play the demo video">'
                 f'<img src="../assets/img/{poster}" alt="Chat with your PDFs demo video" width="1280" height="720" loading="lazy">'
                 f'<span class="play">{PLAY}</span></div><p style="margin-top:10px;color:var(--muted);font-size:.9rem">Click to play (1.8 MB).</p>')
    gallery = ""
    if p["gallery"]:
        figs = "".join(f'<figure class="reveal">{frame("../assets/img/" + f, c, w, h)}<figcaption>{escape(c)}</figcaption></figure>' for f, c, w, h in p["gallery"])
        gallery = f'<section><h2>Screens</h2><div class="gallery">{figs}</div></section>'
    tech = "".join(f"<span>{escape(t)}</span>" for t in p["tech"])
    links = f'<a class="btn btn-ghost" href="{GITHUB}/{p["github"]}" target="_blank" rel="noopener">{GITHUB_ICON}Code on GitHub</a>'
    if p["upwork"]:
        links += f'<a class="btn btn-ghost" href="{UP_ITEM}{p["upwork"]}" target="_blank" rel="noopener">{UPWORK_ICON}On my Upwork</a>'

    html = head(f"{p['short']}: case study | Tadrous William", p["desc"], f"work/{p['slug']}.html", 1)
    html += "</head>\n<body id=\"top\">\n" + nav(1, home=False)
    html += f"""<main id="main">
<section class="cs-hero">
  <div class="bg-dots"></div><div class="blob b1"></div><div class="blob b3"></div>
  <div class="wrap" style="position:relative">
    <a class="crumb" href="../index.html#work">← All work</a><br>
    <span class="tag rise" style="background:{bg};color:{ink}">{escape(p['tag'])}</span>
    <h1 class="rise d1">{escape(p['title'])}</h1>
    <p class="lead rise d2">{escape(p['card_text'])}</p>
    <div class="metrics">{metrics}</div>
  </div>
</section>
<div class="wrap"><div class="cs-shot reveal" style="--tint:{p['tint']}">{visual}</div></div>
<section>
  <div class="wrap cs-body">
    <div>
      <section class="reveal"><h2>The problem</h2>{problem}</section>
      <section class="reveal"><h2>What I built</h2><ul>{built}</ul></section>
      <section class="reveal"><h2>The result</h2><p>{p['result_intro']}</p>{table_html(p['table'])}{after}{video}</section>
      {gallery}
      <a class="next reveal" href="{nxt['slug']}.html"><div><small>Next case study</small><b>{escape(nxt['short'])}</b></div><span class="arrow">→</span></a>
    </div>
    <aside class="aside">
      <div class="box"><h4>Tech</h4><div class="chips">{tech}</div></div>
      <div class="box"><h4>Links</h4>{links}</div>
      <div class="box" style="background:#FFF7EF"><h4>Want something like this?</h4><p style="font-size:.95rem;color:var(--ink-2)">Tell me about your project on Upwork and I'll reply with a plan, timeline and price.</p>{upwork_btn()}</div>
    </aside>
  </div>
</section>
</main>
"""
    html += footer(1)
    (ROOT / "work" / f"{p['slug']}.html").write_text(html, encoding="utf-8")


def build_404():
    html = head("Page not found | Tadrous William", "This page does not exist.", "404.html", 0)
    # absolute paths: GitHub Pages serves 404.html for missing pages at any depth
    html = html.replace('href="favicon', 'href="/favicon').replace('href="apple', 'href="/apple').replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/')
    html += '<meta name="robots" content="noindex">\n</head>\n<body id="top">\n'
    html += f"""<main id="main" class="nf"><div class="wrap">
  <b>404</b><h1 style="font-size:2rem">This page does not exist.</h1>
  <p class="lead" style="margin:0 auto 26px">The link may be old. Here is the way back.</p>
  <div class="cta-row" style="justify-content:center"><a class="btn btn-dark" href="/">Go to the home page{ARROW}</a>{upwork_btn()}</div>
</div></main>
</body>
</html>
"""
    (ROOT / "404.html").write_text(html, encoding="utf-8")


def build_meta():
    urls = [f"{SITE}/"] + [f"{SITE}/work/{p['slug']}.html" for p in PROJECTS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n"
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    (ROOT / "work").mkdir(exist_ok=True)
    build_index()
    for i, p in enumerate(PROJECTS):
        build_case(p, PROJECTS[(i + 1) % len(PROJECTS)])
    build_404()
    build_meta()
    print("built index.html, 404.html, sitemap.xml, robots.txt and", len(PROJECTS), "case studies")
