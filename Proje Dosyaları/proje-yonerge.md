# Genel Bilgiler
## Amacınız: 
Bu projede, dersimiz boyunca öğrendiğiniz yöntem ve teknikleri kullanarak kendi yazılımınızı tasarlayacak ve geliştireceksiniz. Proje, insan kaynaklarından muhasebeye, iş takibinden oyun geliştirmeye kadar geniş bir yelpazede olabilir.
## Gruplar: 
Projeler en fazla 4 kişiden oluşacak şekilde gruplar halinde yapılacaktır. Gruptaki kişi sayısına göre ek bazı görevler olacaktır.
## Yazılım gereksinimleri: 
Programınız komut satırı üzerinden çalışmalıdır. İsteğe bağlı olarak, Tkinter, PyQt, Streamlit, Django veya Flask gibi kütüphaneler kullanarak görsel bir arayüz ekleyebilirsiniz.
## Araştırma: 
Dersimizde görmemiş olduğunuz yeni yöntemleri araştırıp projenize entegre etmeniz gerekmektedir.
## Sunum: 
Dersin son haftasında projenizin sunumu yapılacaktır.
## Destek kullanımı: 
Yapay zeka destekli kod kullanımı serbesttir fakat kodun çalışma mantığını kendi cümlelerinizle ifade edebilmelisiniz. Sunum sırasında bunun testi yapılacaktır. Yazdığınız bir kodun ne işe yaradığı ve nasıl çalıştığı gibi şeyleri bilmiyorsanız bu ciddi bir puan kaybına sebep olacak, hatta projenin kabul edilmemesine sebep olabilecektir. Bunun kontrolü sunumlar esnasında yapılacaktır. Grup çalışmasında kendi yazmadığı kısımları da temel seviyede açıklayabiliyor olmanız gerekmektedir.
# Kodlama standartları
## Kod kalitesi: 
- Kodlama yapılırken temiz kod yazmaya özen gösterilmeli. (Puanlamada önemli bir yere sahip olacaktır)
- Yorum satırları aktif şekilde kullanılmalı. Sadece çalışan bir kod vermeniz yeterli olmayacak kodları okuyan birinin sistemin çalışma şeklini anlamasına yardımcı olacak bilgilendirmeler yapmanız gerekecektir.
- Her fonksiyon ve modül başlangıcında, o kısmın ne işe yaradığını açıklayan yorum satırları eklenmeli.
- Karmaşık algoritmalar veya işlevler için adım adım yorumlar eklenmeniz önerilir.
- Değişken isimlendirmelerine dikkat edilmeli.
- Fonksiyonlar: Tekrar eden kod bloklarını önlemek için fonksiyonlar tanımlayın.
- Veri Yönetimi: Veri tabanı kullanarak veriler ve işlem kayıtları tutulmalıdır.
Harika, işte yukarıdaki düzenlenmiş başlıkların altına rehberlik edecek şekilde, **doğrudan çözüm vermeden**, sadece ipucu tarzında küçük notlar ekledim:

---

**Proje Hakkında Genel Açıklama**  
Bu proje, dersimiz boyunca edindiğiniz programlama bilgilerini uygulayarak kapsamlı bir yazılım geliştirme deneyimi kazanmanızı hedeflemektedir. Seçeceğiniz konu, insan kaynakları yönetiminden muhasebeye, iş takibinden oyun geliştirmeye kadar geniş bir yelpazeyi kapsayabilir. Ancak hangi alan seçilirse seçilsin, projelerinizin belirli yazılım geliştirme standartlarına ve teknik gereksinimlere uygun olması beklenmektedir.

Projenin değerlendirilmesinde sadece işlevsellik değil; kod kalitesi, sistem tasarımı, modüler yapı, veri tabanı kullanımı, kullanıcı yönetimi ve nesne yönelimli programlama prensiplerine uygunluk da dikkate alınacaktır.

Ayrıca proje sürecinde ders kapsamında doğrudan işlemediğimiz yeni teknikleri veya kütüphaneleri araştırarak projeye entegre etmeniz gerekmektedir. Bu sayede kendi başınıza öğrenme becerinizi geliştirmeniz de amaçlanmaktadır.

Aşağıda, projenizde mutlaka bulunması gereken yapısal ve işlevsel unsurlar detaylı şekilde listelenmiştir. Bu gereksinimlerin tamamına uygun geliştirme yapmanız, projenizin başarısı için zorunludur.

---

## Program İşleyişi ve Modüler Yapı Gereklilikleri

- **Modüler Yapı:**
  - Proje, çok uzun ve karmaşık tek bir dosya içermemelidir.
  - Kodlar işlevlerine göre bölünerek modüller oluşturulmalı ve modüllerin işleyişi bir `README` dosyasında açıklanmalıdır.  
    🔹 *İpucu:* Her modül bir işlev grubuna hitap etmeli (örneğin: `kullanici.py`, `veritabani.py`, `raporlama.py` gibi).

- **Program Başlangıcı:**
  - Program çalıştırıldığında ekrana sistemin kısa bir tanıtım yazısı gelmelidir.
  - Tanıtım sonrasında kullanıcı girişi yapılmalıdır.  
    🔹 *İpucu:* Ana program (`main.py`) çalıştığında önce bir `print()` ile tanıtım yazısı göster, sonra bir `input()` ile giriş isteyebilirsin.

- **Kullanıcı Yönetimi:**
  - Kullanıcı giriş ekranında:
    - Mevcut kullanıcı ile giriş yapılabilmeli.
    - İstenirse yeni kullanıcı kaydı oluşturulabilmelidir.
  - Sistemde en az üç farklı kullanıcı tipi bulunmalıdır:
    - Örnek: Yönetici, Standart Kullanıcı, Ziyaretçi.
  - Yönetici (Admin) hesabı önceden tanımlı olarak sistemde bulunmalıdır.
  - Her kullanıcı tipinin yetkileri ve erişim ekranları birbirinden farklı olmalıdır.  
    🔹 *İpucu:* Kullanıcı tiplerini temsil eden sabitler (`"admin"`, `"user"`, `"guest"`) belirleyip kullanıcı nesnesine bir `role` veya `yetki` alanı ekleyebilirsin.

- **Nesne Yönelimli Kullanıcı Yapısı:**
  - Her kullanıcı tipi, kendine özgü bir sınıf (class) ile temsil edilmelidir.
  - Kullanıcı tipine özel işlemler bu sınıf içinde fonksiyonlar (methodlar) olarak tanımlanmalıdır.
  - Kullanıcı işlemleri, sınıf içi fonksiyonlar çağrılarak gerçekleştirilmelidir.  
    🔹 *İpucu:* Ortak özellikler için bir `Kullanici` ana sınıfı (base class) tanımlayıp, diğer kullanıcı tiplerini bu sınıftan türetebilirsin (`inheritance`).

- **İşlem ve Kayıt Yönetimi:**
  - Kullanıcı girişinden sonra yapılabilecek tüm işlemler bir liste halinde kullanıcıya sunulmalıdır.
  - Kullanıcıların gerçekleştirdiği işlemler veri tabanında kaydedilmelidir.
  - Her kullanıcı, sistemden kendisine özel raporlar alabilmelidir.
  - Yönetici kullanıcılar, herhangi bir kullanıcıya ait işlem kayıtlarının raporunu görüntüleyip çıktı alabilmelidir.  
    🔹 *İpucu:* İşlem kayıtlarını bir `islem_kaydi` tablosunda saklayabilir, kullanıcı id'si ile ilişkilendirebilirsin.

---

## Grup Çalışması Özel Kriterleri

Gruplarda aşağıdaki kriterlerin;  
- 2 kişilik bir grup için en az **2 tanesi**,  
- 3 kişilik bir grup için en az **3 tanesi**,  
- 4 kişilik bir grup için en az **4 tanesi**  
projeye entegre edilmelidir.

### Seçilebilecek Kriterler:
- Veri tabanı işlemlerinin özel bir **veri tabanı sınıfı** üzerinden gerçekleştirilmesi.
- **SQLAlchemy** kütüphanesinin kullanılması.
- **API entegrasyonu** yapılarak gerçek zamanlı veri kullanımı.
- Veri tabanında **One-to-One**, **One-to-Many** ve **Many-to-Many** ilişkilerinin tamamının bulunması ve bu ilişkileri ifade eden bir **ER (Entity-Relationship) diagramı** çizilmesi.
- **Soyut sınıflar**, **kapsülleme**, **çok biçimlilik** ve **çoklu kalıtım** gibi nesne yönelimli programlama prensiplerinin etkin şekilde kullanılması ve projeye uygun bir **UML diagramı** hazırlanması.
- Projeye bir **görsel arayüz** eklenmesi. (Örneğin: Tkinter, PyQt, Streamlit gibi araçlarla)
- Kullanıcının sisteme **dosya yükleyebilmesi**, **dosya kaydedebilmesi** veya veri çıktısı alabilmesi. (Örneğin: PDF/CSV rapor oluşturma)
- Kullanıcılara metin tabanlı raporların yanında **grafik destekli raporlar** sunulması. (Örneğin: `matplotlib`, `plotly`, `seaborn` gibi kütüphaneler kullanılarak)
- **Admin kullanıcılarının**, diğer kullanıcıların yetkilerini değiştirebileceği basit bir **yönetim paneli** oluşturulması.
- Sistemde **oturum açan kullanıcıların tüm işlemlerinin** ve bu işlemlere ait **tarih/saat bilgilerinin** kaydedilmesi.

---
