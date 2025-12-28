# 🛡️ Mini-SIEM – SSH Brute Force Tespit Aracı

Mini-SIEM, Linux sistemlerde **SSH brute force saldırılarını gerçek zamanlı tespit etmek** için geliştirilmiş Python tabanlı hafif bir SIEM aracıdır.

---

## 🚀 Özellikler

- SSH loglarını **systemd journal (journalctl)** üzerinden okur
- Gerçek zamanlı brute force tespiti
- Zaman bazlı korelasyon (son X dakika)
- Tekrarlayan alarmları engelleme (cooldown)
- 5 saniyede bir sürekli kontrol
- **systemd servisi** olarak çalışabilir
- JSON alarm çıktısı

---

## 🧠 Tespit Mantığı

- Aynı IP’den belirli süre içinde çok sayıda başarısız SSH denemesi
- Eşik aşılırsa **HIGH seviye alarm** üretilir

---

## 📂 Proje Yapısı

mini-siem/
├── core/        # Log okuma, parse, alarm ve state yönetimi
├── detectors/   # Tespit kuralları
├── reports/     # Alarm çıktıları
├── main.py
└── README.md

## Çalıştırma
- sudo python3 main.py

## Örnek çıktı
- 🚨 [HIGH] SSH_BRUTE_FORCE - IP: 127.0.0.1 (6 deneme)

## Servise olarak çalıştırma
- sudo systemctl start mini-siem
- sudo systemctl enable mini-siem
- journalctl -u mini-siem -f

