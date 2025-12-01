import time
import re
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =====================================================================
# CONFIGURAÇÕES
# =====================================================================
ISSUES_URL = "https://gitlab.com/lappis-unb/projetos-energia/mec-energia/mec-energia-web/-/issues?sort=created_date&state=closed&label_name%5B%5D=BUG&first_page_size=100"

WAIT = 8  # Tempo aumentado para garantir que o JS carregue o conteúdo dinâmico

# =====================================================================
# INICIAR SELENIUM
# =====================================================================
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    options=options
)

print("✔ Selenium iniciado")

# =====================================================================
# FUNÇÃO: OBTER LINKS DAS ISSUES
# =====================================================================
def get_issue_links(url):
    print(f"➡ Navegando para a lista de issues: {url}")
    driver.get(url)
    time.sleep(WAIT)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = {}
    
    issue_elements = soup.find_all("a", class_="gl-link", href=lambda href: href and "/issues/" in href)
    
    for element in issue_elements:
        full_url = "https://gitlab.com" + element["href"]
        # Extrai o ID da issue do href
        match = re.search(r'/issues/(\d+)', element["href"])
        if match:
            issue_id = match.group(1)
            links[issue_id] = full_url
            
    print(f"✔ {len(links)} links de issues encontrados.")
    return links

# =====================================================================
# FUNÇÃO: EXTRAIR INFO DE UMA ISSUE (CORRIGIDA)
# =====================================================================
def parse_issue(url):
    print("➡ Lendo:", url)
    driver.get(url)
    time.sleep(WAIT)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # título
    title_tag = soup.find("title")
    title = title_tag.text.split("·")[0].strip() if title_tag else "UNKNOWN"

    # criação
    created_tag = soup.find("span", {"data-testid": "work-item-created"})
    created_time_tag = created_tag.find("time", datetime=True) if created_tag else None
    created = created_time_tag["datetime"] if created_time_tag else None

    # fechamento → último <time> da página
    all_times = soup.find_all("time", datetime=True)
    # A data de fechamento é geralmente a última data na página de uma issue fechada.
    # Se houver mais de uma data (criação e fechamento), a última é o fechamento.
    closed = all_times[-1]["datetime"] if len(all_times) >= 2 else None

    return {
        "Issue": title,
        "Created": created,
        "Closed": closed
    }


# =====================================================================
# FUNÇÃO: CALCULAR LEAD TIME OF CHANGES
# =====================================================================
def calc_ltc(created, closed):
    if not created or not closed:
        return None

    created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
    closed_dt = datetime.fromisoformat(closed.replace("Z", "+00:00"))

    return closed_dt - created_dt  # timedelta

# =====================================================================
# PIPELINE PRINCIPAL
# =====================================================================
try:
    links = get_issue_links(ISSUES_URL)
except Exception as e:
    print(f"Erro ao obter links das issues: {e}")
    links = {}

rows = []

for issue_id, url in links.items():
    data = parse_issue(url)
    if data and data["Created"] and data["Closed"]:
        ltc = calc_ltc(data["Created"], data["Closed"])
        
        # Conversão para dias, horas e minutos
        total_seconds = ltc.total_seconds()
        ltc_dias = total_seconds // 86400
        ltc_horas = (total_seconds % 86400) // 3600
        ltc_minutos = (total_seconds % 3600) // 60

        rows.append({
            "ID": issue_id,
            "Issue": data["Issue"],
            "Created": data["Created"],
            "Closed": data["Closed"],
            "LTC_timedelta": str(ltc), # Convertendo timedelta para string para salvar
            "LTC_dias": ltc_dias,
            "LTC_horas_total": total_seconds / 3600,
            "LTC_formatado": f"{int(ltc_dias)} dias, {int(ltc_horas)} horas e {int(ltc_minutos)} minutos"
        })
    elif data:
        print(f"Aviso: Dados incompletos para a issue {issue_id}. LTC não calculado.")
        rows.append({
            "ID": issue_id,
            "Issue": data["Issue"],
            "Created": data["Created"],
            "Closed": data["Closed"],
            "LTC_timedelta": None,
            "LTC_dias": None,
            "LTC_horas_total": None,
            "LTC_formatado": "Dados Incompletos"
        })

if rows:
    df = pd.DataFrame(rows)
    print("\n✔ EXTRAÇÃO FINALIZADA!\n")
    print(df[["ID", "Issue", "LTC_formatado"]]) # Exibindo colunas chave
    
    # =====================================================================
    # SALVAR CSV
    # =====================================================================
    df.to_csv("issues_with_ltc.csv", index=False, encoding="utf-8")
    print("\n✔ Arquivo issues_with_ltc.csv gerado!")
else:
    print("\n❌ Nenhuma issue processada com sucesso.")


# =====================================================================
# FINALIZAR SELENIUM
# =====================================================================
driver.quit()
print("✔ Selenium encerrado")