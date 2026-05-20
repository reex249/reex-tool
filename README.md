
# 🚀 REEX-TOOL: UNISOC EXPLORATION & ROOT TOOL
> **Optimized for Linux & Termux Environments** 🐧📱

---

## 📌 نبذة عن الأداة (Overview)
أداة متطورة ومخصصة للعمل على بيئات **Linux** وتطبيق **Termux** على الأندرويد. تهدف الأداة إلى فحص والتعامل مع الأجهزة التي تعمل بمعالجات **Unisoc / Spreadtrum** لاستكشاف الثغرات، تخطي حماية محمل الإقلاع (Bootloader)، وتسهيل عمليات الروت.

---

## ⚡ الميزات الرئيسية (Key Features)

| الرقم | الميزة | الوصف |
| :---: | :--- | :--- |
| **1️⃣** | **Verify Android Local Node Connections** | التحقق من استقرار اتصال الجهاز بالكمبيوتر أو الهاتف الآخر عبر `ADB` و `Fastboot`. |
| **2️⃣** | **Execute Unisoc Bootloader Exploit Bypass** | تنفيذ ثغرات برمجية لتخطي حماية قفل الإقلاع (Bootloader) المخصصة لمعالجات Unisoc. |
| **3️⃣** | **Extract Kernel 'boot.img' Allocation** | سحب واستخراج كتل ملف الإقلاع `boot.img` الخاص بالنواة (Kernel) مباشرة. |
| **4️⃣** | **Generate Direct Magisk Root Flash Steps** | توليد خطوات تفصيلية ومباشرة لكيفية تفليش روت `Magisk` المتوافق مع جهازك. |

---

## 📥 خطوات التثبيت الكاملة (Full Installation)

قم بفتح الطرفية (Terminal) في **Termux** أو **Linux** ونفذ الأوامر التالية خطوة بخطوة:

### 🔹 الخطوة 1: تحديث حزم النظام والبيئة
bash
# لمستخدمي تطبيق Termux:

pkg update && pkg upgrade -y  


# لمستخدمي توزيعات Linux (مثل Ubuntu / Kali):

sudo apt update && sudo apt upgrade -y


### 🔹 الخطوة 2: تثبيت لغة Python وأدوات الأندرويد الأساسية

 bash
pkg install python android-tools git ndk-sysroot clang -y

### 🔹 الخطوة 3: تثبيت المكتبات الاعتمادية والتشفير (Dependencies)
 bash
pip3 install pycryptodome libusb python-adb unisoc-unlock

---

## 🛠️ طريقة التشغيل (Usage)

بعد تحميل ملف الأداة وتثبيت المتطلبات، قم بإعطاء الملف صلاحية التنفيذ ثم ابدأ التشغيل:

 bash
# إعطاء صلاحية التنفيذ للملف
cd reex-tool

chmod +x reex_tool.py

# تشغيل الأداة
./reex_tool.py

reex_tool.py

  
---

## 👥 للتواصل والدعم الفني (Contact & Support)

إذا واجهتك أي مشكلة أو كان لديك استفسار، يمكنك التواصل مباشرة عبر حساب التليجرام:

* 📢 **Telegram Account:**  @HC_XA

