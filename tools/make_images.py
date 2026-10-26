"""Converts project screenshots (from the project repos next to this site) into small WebP files for the site."""
from pathlib import Path
from PIL import Image

SRC = Path(__file__).resolve().parents[2]          # D:/GitHub_Work
OUT = Path(__file__).resolve().parents[1] / "assets" / "img"

# output name: (source path relative to D:/GitHub_Work, max width)
IMAGES = {
    "hero-rag-chat":        ("rag-pdf-chat/demo/shots/app_chat.png", 1400),
    "rag-how":              ("rag-pdf-chat/demo/visuals/03_how_it_works.png", 1400),
    "rag-results":          ("rag-pdf-chat/demo/visuals/04_results.png", 1400),
    "rag-app":              ("rag-pdf-chat/demo/visuals/02_app.png", 1200),
    "rag-poster":           ("rag-pdf-chat/demo/visuals/card_intro.png", 1280),
    "inv-before-after":     ("ai-invoice-extraction/portfolio/before_after_invoice_021_scan.jpg", 1400),
    "inv-accuracy":         ("ai-invoice-extraction/portfolio/accuracy.png", 1400),
    "inv-how":              ("ai-invoice-extraction/portfolio/how_it_works.png", 1400),
    "inv-excel":            ("ai-invoice-extraction/portfolio/excel.png", 1600),
    "inv-n8n":              ("ai-invoice-extraction/portfolio/n8n_workflow.png", 1400),
    "inv-app":              ("ai-invoice-extraction/portfolio/app.png", 1400),
    "fc-product":           ("sales-forecasting/portfolio/product_85123A.png", 1400),
    "fc-accuracy":          ("sales-forecasting/portfolio/accuracy.png", 1400),
    "fc-app":               ("sales-forecasting/portfolio/app_stock_plan.png", 1400),
    "fc-app-product":       ("sales-forecasting/portfolio/app_product.png", 1400),
    "fc-backtest":          ("sales-forecasting/portfolio/backtest_store.png", 1400),
    "nyc-cover":            ("nyc-real-estate-dashboard/assets/portfolio/00_cover.jpg", 1400),
    "nyc-estimator":        ("nyc-real-estate-dashboard/assets/portfolio/04_price_estimator.jpg", 1400),
    "nyc-investor":         ("nyc-real-estate-dashboard/assets/portfolio/05_investor_view.jpg", 1400),
    "nyc-map":              ("nyc-real-estate-dashboard/assets/portfolio/03_map.jpg", 1400),
    "pbi-overview":         ("powerbi-sales-dashboard/portfolio/screens/01_sales_overview.png", 1422),
    "pbi-products":         ("powerbi-sales-dashboard/portfolio/screens/02_products.png", 1422),
    "pbi-customers":        ("powerbi-sales-dashboard/portfolio/screens/03_customers.png", 1422),
    "pbi-slide":            ("powerbi-sales-dashboard/portfolio/slides/slide_01.jpg", 1400),
    "leads-coverage":       ("business-lead-list/portfolio/coverage.png", 1200),
}

OUT.mkdir(parents=True, exist_ok=True)
total = 0
for name, (rel, max_w) in IMAGES.items():
    im = Image.open(SRC / rel).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    path = OUT / f"{name}.webp"
    im.save(path, "WEBP", quality=80, method=6)
    total += path.stat().st_size
    print(f"{name:18} {im.width}x{im.height}  {path.stat().st_size // 1024} KB")
print(f"total {total // 1024} KB")
