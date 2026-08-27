# ITHZ MCP + CCG: návod na kolegiálny test

Tento návod je pre verejný generický build `0.1.0a7` s CCG jadrom
`mcp35.0-cached-prefix-current-projection-multilab-v1`.

Balík obsahuje ITHZ projektovú pamäť, generickú CCG ústavu, päťrolové
shadow-review, Gemini/Grok druhého oponenta, adaptívny Daybreak bezpečnostný
oponent, overiteľný ledger a bezpečný sandboxový demo broker.

## Dôležitá hranica súkromia

Verejný artefakt neobsahuje žiadnu firemnú ústavu, interné zdrojové registre,
projektové profily, taskové dôkazy ani prístupové údaje. Obsahuje iba generický
profil `ccg-universal-baseline`.

Súkromný profil sa nepridáva do tohto repozitára. Ak ho má kolega dostať, musí
ísť samostatným schváleným privátnym kanálom a zostať v lokálnom projekte.
Adresár `.ccg/` pridajte do `.gitignore`, ak obsahuje neverejný profil.

## 1. Inštalácia na Windows

Požiadavky: Git, Python 3.10 alebo novší a Codex CLI/aplikácia prihlásená na
účte, ktorý môže spúšťať zvolené Codex modely.

```powershell
git clone --branch codex/mcp35-generic-public https://github.com/thegobi/ithz_mcp.git
cd ithz_mcp
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install .\artifacts\ithz_mcp-0.1.0a7-py3-none-any.whl
python -m ithz_mcp version
```

Očakávané identity:

- package version: `0.1.0a7`
- build: `public-generic-mcp35-cached-prefix-multilab.20260827.1`
- CCG: `mcp35.0-cached-prefix-current-projection-multilab-v1`

Wheel SHA-256:

```text
22e8c4fb6bf1b6ef1d42da261f4ded3f747041c0fd743e9e6cd0617a9e9b18b7
```

## 2. Inicializácia bezpečného testovacieho projektu

Použite nový lokálny priečinok bez produkčných dát:

```powershell
$testProject = "C:\temp\ithz-ccg-test"
ccg-ithz init --project $testProject
ccg-ithz status --project $testProject --backend scripted
```

Príkaz vytvorí generickú ústavu v `.ccg/constitution.json`, lokálny dôkazový
ledger v `.ithz-ccg/` a demo sandbox v `.ccg-sandbox/`. Dôkazový ledger a
sandbox majú vlastné ignore pravidlá; pri privátnej ústave ignorujte aj `.ccg/`.

## 3. Kam vložiť Gemini API kľúč

Odporúčaný spôsob na Windows:

```powershell
ccg-ithz settings
```

Otvorí sa lokálna stránka iba na `127.0.0.1`. Do poľa Gemini vložte kľúč,
ponechajte model `gemini-3.7-flash`, thinking level `low` a druhého oponenta
`gemini`. Kliknite na uloženie a potom na test spojenia.

Kľúč sa neukladá do Gitu ani do Codex konfigurácie. Je šifrovaný Windows DPAPI
pre aktuálneho používateľa v:

```text
%APPDATA%\ITHZ\ccg-mcp\secrets.dpapi.json
```

Nekryptované modelové nastavenia sú v:

```text
%APPDATA%\ITHZ\ccg-mcp\settings.json
```

Alternatíva len pre aktuálny shell alebo CI secret store:

```powershell
$env:GEMINI_API_KEY = "VLOZTE_KLUC_LEN_LOKALNE"
$env:CCG_GEMINI_MODEL = "gemini-3.7-flash"
$env:CCG_GEMINI_THINKING_LEVEL = "low"
$env:CCG_OPPONENT_2_PROVIDER = "gemini"
```

Premenná `GEMINI_API_KEY` má prednosť pred DPAPI. Nedávajte ju do
`.codex/config.toml`, repozitára, screenshotu ani chatu. xAI/Grok je voliteľný;
pri bežnom teste ho môžete nechať nenastavený.

## 4. Pripojenie do Codexu

Skopírujte `ccg_codex_config.sample.toml` do dôveryhodného testovacieho projektu
ako `.codex/config.toml` alebo príslušné bloky vložte do používateľského
`%USERPROFILE%\.codex\config.toml`. V oboch MCP serveroch upravte dve absolútne
cesty:

1. cestu k `.venv\Scripts\python.exe`,
2. cestu k testovanému projektu.

Potom Codex úplne reštartujte. V zozname MCP nástrojov majú byť oba servery:
`ithz_memory` a `ccg_shadow`.

Verejné CCG MCP zámerne ponúka iba tieto nástroje:

```text
ccg_status
ccg_initialize_project
ccg_run_case
ccg_execute_demo
ccg_get_case
ccg_verify_case
ccg_list_cases
```

## 5. Testy bez modelových nákladov

```powershell
python .\tests\test_public_ccg_release.py
python -m ithz_mcp mcp-server --project $testProject --mode read-only --protocol mcp --storage-profile native-archive --smoke
ccg-ithz demo --project $testProject --backend scripted --opponent-2 off --use-grok off --use-daybreak off --reuse-decision off --no-execute
```

Očakávajte úspešný unit test, `"passed": true`, verdikt
`ALLOW_WITH_LIMITS` a platný ledger. `--no-execute` zabezpečí, že demo iba
preskúma návrh a nevytvorí ani sandboxový súbor.

## 6. Lacný reálny Gemini test

Po úspešnom teste spojenia spustite jeden malý read-only prípad:

```powershell
ccg-ithz run `
  --project $testProject `
  --task "Posúď read-only návrh kontroly lokálneho README bez zápisov." `
  --risk low `
  --capability analysis.read `
  --backend codex `
  --opponent-2 gemini `
  --use-grok off `
  --use-daybreak off `
  --reuse-decision off
```

Tento beh používa Codex role a Gemini 3.7 Flash ako druhého oponenta. Množstvo
tokenov závisí od vstupu a odpovedí modelov; začnite krátkym low-risk prípadom.
Daybreak je predvolene určený pre `high` a `critical`, preto ho v prvom lacnom
smoke teste vypíname.

Z výsledku skopírujte `case_id` a overte reťazec:

```powershell
ccg-ithz verify --project $testProject --case-id "SEM_VLOZTE_CASE_ID"
```

## 7. Čo výsledok neznamená

CCG beží v shadow režime. Verdikt je auditovateľný oponentský dôkaz, nie
oprávnenie na deployment, externý zápis, platbu, produkčný zásah, spracovanie
citlivých dát alebo odoslanie komunikácie. Takéto akcie stále vyžadujú presný
ľudský mandát a vlastné runtime brány.

## 8. Odovzdanie výsledkov testu

Kolega nech pošle iba:

- výstup `python -m ithz_mcp version`,
- výstup `ccg-ithz status --backend scripted` bez lokálnych tajomstiev,
- `case_id`, finálny verdikt a výstup `ccg-ithz verify`,
- typ klienta a Python verziu,
- presný chybový text, ak test zlyhá.

Nikdy neposiela Gemini/xAI kľúč, obsah `secrets.dpapi.json`, capability token ani
neverejnú ústavu.
