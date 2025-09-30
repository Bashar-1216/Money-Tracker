



# 💰 مشروع متتبع أسعار العملات - Money Tracker

مرحبًا! 👋  
في هذا المشروع، عملت على **متتبع بسيط لأسعار صرف العملات**.  
الفكرة الأساسية: نجيب أسعار العملات من الإنترنت، نرسلها باستخدام **Kafka**، ونخزنها في **MongoDB** للرجوع إليها لاحقًا 🔄.

---

## 🛠 مكونات المشروع

- **Producer (`producer.py`)**  
  🏭 يسحب أسعار العملات من [ExchangeRate API](https://api.exchangerate.host/latest) كل 60 ثانية، ويرسل البيانات إلى **Kafka topic** باسم `money-tracker`.

- **Consumer (`consumer.py`)**  
  👂 يستمع على الـ topic `money-tracker`، يعالج الرسائل، ويحفظ البيانات في **MongoDB** مع ترتيب وفهارس لتسهيل البحث 🔍.

---

## 📋 المتطلبات

- 🐍 Python 3.x  
- ⚡ Kafka يعمل على `localhost:9092`  
- 🗄 MongoDB يعمل على `mongodb://localhost:27017`  
- مكتبات بايثون:
  - kafka-python  
  - requests  
  - pymongo  

---

## ⚙️ طريقة الإعداد

1. تثبيت **Kafka** و **MongoDB** والتأكد أنهما يعملان على الجهاز.  
2. تثبيت المكتبات المطلوبة في بايثون:
   ```bash
   pip install kafka-python requests pymongo

3. تشغيل **Producer**:

   ```bash
   python producer.py
   ```
4. تشغيل **Consumer**:

   ```bash
   python consumer.py
   ```

---

## 🔄 كيف يعمل المشروع

1. الـ Producer يسحب أسعار الدولار مقابل الريال اليمني (YER) والريال السعودي (SAR) كل 60 ثانية ⏱.
2. يرسل البيانات بصيغة JSON إلى **Kafka topic** `money-tracker` 📨.
3. الـ Consumer يستقبل الرسائل، يحللها، ويخزنها في **MongoDB collection** باسم `money.money-tracker` 🗂.
4. تم إضافة **Indexes** على الحقول `currency` و `fetched_at` لتسريع البحث 🚀.

---

## ⚠️ ملاحظات

* مفتاح الـ API في السكربت قد لا يكون مطلوبًا حسب سياسة API المستخدمة 🔑.
* إذا كان Kafka أو MongoDB على سيرفر أو منفذ مختلف، عدّل عناوين الاتصال في السكربتات ✏️.
* الـ Consumer يقوم بـ commit للـ offsets تلقائيًا ويعالج الرسائل من أول offset 🏁.

---

## 📄 الترخيص

المشروع متاح **كما هو** بدون أي ضمان.

---

🎉 انتهينا! الآن المشروع جاهز للعمل، ويمكنك متابعة أسعار العملات مباشرة على جهازك باستخدام Kafka وMongoDB 💻💵.




