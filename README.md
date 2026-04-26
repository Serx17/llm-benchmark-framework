# 🏦 LLM Benchmark Framework for Fintech

> **Production-ready framework** для объективного выбора LLM в финтехе.  
> Оценка качества, latency и TCO (Total Cost of Ownership) моделей для задач взыскания, скоринга и комплаенса с учетом требований 152-ФЗ.

---

## 💼 Business Context & Problem Statement

Финтех-компания обрабатывает **10,000+ запросов/день**. Выбор LLM — это баланс между тремя критическими метриками:
1.  **Quality**: Юридическая точность и соблюдение регламентов (взыскание, 230-ФЗ).
2.  **Latency**: Время отклика (SLA клиентской поддержки < 2 сек).
3.  **Cost**: Юнит-экономика при масштабировании.

### ❌ Проблемы рынка:
*   **Black Box**: Провайдеры не дают прозрачных SLA по качеству ответов в специфических доменах.
*   **Vendor Lock-in**: Сложность миграции между YandexGPT, SberGigaChat и открытыми моделями (Qwen/Llama).
*   **Compliance Risk**: Использование зарубежных API нарушает требования 152-ФЗ о локализации ПДн.

### ✅ Решение:
Архитектура **LLM Benchmark Framework** позволяет проводить A/B-тестирование моделей на реальных кейсах до внедрения в прод, снижая риски переплаты и юридических штрафов.

---

## 📊 Key Findings (MVP Results)

Бенчмарк проведен на датасете из 10 реалистичных финтех-промптов (взыскание, реструктуризация, проверка контрагентов).

| Модель | Провайдер | Latency (p95) | Cost / 1k req | Quality Score* | Compliance (152-ФЗ) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **YandexGPT** | Yandex Cloud | ~2,300 ms | ~$0.10 | ⭐⭐⭐⭐⭐ | ✅ РФ Сервера |
| **Qwen 2.5-7B** | Hugging Face | ~1,080 ms | $0.00 (Free) | ⭐⭐⭐⭐ | ⚠️ Требуется Self-hosted |
| **GigaChat** | SberCloud | TBD | TBD | TBD | ✅ РФ Сервера |

*> **Quality Score**: Комбинированная метрика (Keyword Coverage + Semantic Similarity).  
> 💡 **Инсайт**: Для операционных задач (чат-боты) Qwen выигрывает по скорости/цене. Для юридических консультаций YandexGPT незаменим из-за резидентности данных.

---

## 🏗️ System Architecture

Проект построен по принципу **Security-by-Design** и модульности.

```mermaid
graph TD
    User[User / Colab Notebook] -->|Secure Auth| Secrets[Colab Secrets / Env Vars]
    Secrets -->|IAM Token| Gateway[API Gateway]
    Gateway -->|Routing| Yandex[Yandex GPT API]
    Gateway -->|Routing| HF[HuggingFace Inference API]
    
    Yandex -->|Response| Metrics[Metrics Collector]
    HF -->|Response| Metrics
🔧 Tech Stack
Core: Python 3.10+, requests, asyncio (planned)
Data & Viz: pandas, matplotlib, numpy
Auth & Security: PyJWT, cryptography, Colab Secrets Manager
Infrastructure: Google Colab (Dev), Yandex Cloud (Prod-ready)
🛡️ Compliance & Security (152-ФЗ Ready)
Zero-Hardcode Secrets: Токены хранятся только в защищенном хранилище (userdata.get()), никогда не коммитятся в Git.
Data Residency: Приоритет провайдерам с серверами в РФ (Yandex/Sber).
Auditability: Логирование всех запросов и метрик для внутреннего аудита.
🚀 Quick Start
Option 1: Google Colab (Recommended for Demo)
Open Stage 1: Basic Benchmark or Stage 2: Quality Evaluation.
Add secrets in the left panel (🔑):
YANDEX_IAM_TOKEN: Your IAM token from Yandex Cloud.
YANDEX_FOLDER_ID: Your Folder ID.
HF_TOKEN: HuggingFace API token (for Qwen/Llama).
Run Runtime -> Run all.
Option 2: Local Environment
git clone https://github.com/Serx17/llm-benchmark-framework.git
cd llm-benchmark-framework
pip install -r requirements.txt

# Set environment variables
export YANDEX_IAM_TOKEN="t1..."
export HF_TOKEN="hf_..."

python src/benchmark_runner.py
🗺️ Roadmap
Phase
Focus Area
Status
Business Value
MVP
API Integration, Basic Metrics (Latency/Cost)
✅ Done
Proof of Concept
v0.2
Custom Dataset (50+ cases), Quality Metrics
✅ Done
Domain-specific evaluation
v0.3
Async Load Testing, Caching, Auto-Rotation
📅 Planned
Production readiness
v1.0
Web Dashboard (Streamlit), PDF Reports, CI/CD
📅 Planned
Stakeholder reporting
👤 About the Author
AI Solutions Architect | FinTech Domain Expert
14+ years experience bridging Legal, Operations, and AI Transformation.
Expertise: Designing secure AI pipelines for regulated industries (FinTech, LegalTech).
Focus: TCO optimization, Compliance-by-Design, LLM Evaluation Frameworks.
📫 Connect:
Telegram: @nspoli
Email: snantonenko17@gmail.com
    
   
