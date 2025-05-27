# 🧰 InfraToolBox – Scripts de Automação para Infraestrutura

Este é um conjunto de ferramentas em **PowerShell** e **Python** voltado para **infraestrutura de TI**, focado em monitoramento, segurança, suporte técnico e automações administrativas.

---

## 🎯 Funcionalidades

- 🧠 **Monitoramento de Recursos:** Exibe o uso de CPU e memória em tempo real
- 🌐 **Ping em Massa:** Testa a conectividade de vários hosts simultaneamente
- 📧 **Alerta por E-mail:** Envia aviso automático quando um host está offline
- 🔐 **Firewall Automático:** Bloqueia IPs suspeitos diretamente no firewall do Windows
- 📑 **Exportação de Logs:** Coleta logs do sistema e salva para análise

---

## 🧱 Requisitos

### ⚙️ PowerShell

- PowerShell 5.1+ (nativo no Windows)
- Para permitir execução de scripts:
```powershell
Set-ExecutionPolicy RemoteSigned
```

### 🐍 Python 3.x

- Python instalado: [https://python.org](https://python.org)
- Pacotes:
  - `psutil` – Monitoramento de sistema
  - `smtplib` – E-mails (nativo no Python)
  - `subprocess`, `socket` – Nativos

Instale os pacotes com:

```bash
pip install psutil
```

---

## 📁 Estrutura do Projeto

```
InfraToolBox/
├── powershell/
│   ├── monitor-recursos.ps1
│   ├── verificar-ping-em-massa.ps1
│
├── python/
│   ├── monitor_cpu_memoria.py
│   ├── alerta_email_queda.py
│
├── docs/
│   ├── tutorial_instalacao.md
│   └── exemplos_outputs.md
```

---

## ▶️ Como Executar

### 💻 PowerShell

```powershell
cd .\powershell\
.\monitor-recursos.ps1
```

### 🐍 Python

```bash
cd python
python monitor_cpu_memoria.py
```

---

## 📚 Exemplos e Documentação

Acesse a pasta `docs/` para tutoriais completos, prints de exemplo e instruções passo a passo.

---

## 🛡️ Licença

Distribuído sob a Licença MIT. Você pode usar, modificar e distribuir com liberdade (mas dá aquela moral com um ⭐, né?)

---

## 👨‍💻 Autor

**Wallan Peixoto**  
Especialista em Infraestrutura, Cloud, Suporte, Automação  
GitHub: [@WallanDavid](https://github.com/WallanDavid)
