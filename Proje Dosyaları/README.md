Bu metin GitHub' ın standart tanıtım yazısının çevirisini içermektedir. Github ile ilgili genel bir tanıtım yazısıdır.

---

# :wave: GitHub'ın Temelleri

## 🤓 Dersin Genel Tanıtımı ve Öğrenme Hedefleri

Bu kursun amacı, size GitHub hakkında kısa bir giriş sunmaktır. Ayrıca, ileri seviye öğrenme için kaynaklar ve platformumuzda başlamanız için bazı fikirler de sağlayacağız. 🚀

## :octocat: Git ve GitHub

Git, bir **dağıtık Versiyon Kontrol Sistemi (VCS)**'dir. Yani kodunuzda yaptığınız değişiklikleri kolayca takip etmenize, iş birliği yapmanıza ve paylaşmanıza yarayan bir araçtır.  
Git ile projenizde yaptığınız değişiklikleri izleyebilir, geçmiş çalışmalara kolayca dönebilir ve başkalarıyla aynı proje üzerinde iş birliği yapabilirsiniz.

GitHub ise Git’in tüm gücünü çevrimiçi ve kullanımı kolay bir arayüzle kullanmanızı sağlar. Yazılım dünyasında ve diğer birçok alanda iş birliği yapmak ve projelerin geçmişini korumak için kullanılır.

GitHub, dünyadaki en gelişmiş teknolojilerin bazılarının evidir. İster veri görselleştiriyor olun, ister yeni bir oyun geliştiriyor olun, GitHub'da bir sonraki adımınıza yardımcı olacak bir topluluk ve araç seti bulabilirsiniz.  
Bu kurs, GitHub'ın temelleriyle başlayacak, ancak ileride daha derin konulara da gireceğiz.

## :octocat: GitHub Akışı (Flow) Anlamak

GitHub akışı, projeler üzerinde kolayca denemeler yapmanızı ve iş birliği yapmanızı sağlayan hafif bir iş akışıdır. Böylece önceki çalışmalarınızı kaybetme riski olmadan ilerleyebilirsiniz.

### Depolar (Repositories)

Bir depo, proje çalışmalarınızın gerçekleştiği yerdir – proje klasörünüz gibi düşünebilirsiniz. Tüm proje dosyalarınızı ve değişiklik geçmişinizi içerir.  
Tek başınıza çalışabilir veya başkalarını bu depoya katkıda bulunmaları için davet edebilirsiniz.

### Klonlama (Cloning)

Bir depo GitHub’da oluşturulduğunda, uzak sunucuda (☁️) saklanır. Bir depoyu klonladığınızda, bilgisayarınızda yerel bir kopyasını oluşturursunuz ve Git kullanarak iki tarafı senkronize edebilirsiniz.  
Bu sayede düzenlemeleri kolaylaştırabilir, daha büyük değişiklikleri rahatça yapabilirsiniz. Ayrıca dilediğiniz kod editörünü kullanabilirsiniz.  
Klonlama sırasında, sadece dosyaları değil, deponun tüm geçmişini de indirirsiniz. Böylece geçmiş bir sürüme kolayca dönebilirsiniz.  
[Klonlama hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

### Commit ve Push Yapmak

**Commit**, yaptığınız değişiklikleri bir kontrol noktası gibi kaydetmenizi sağlar.  
Her commit’e açıklayıcı bir **commit mesajı** ekleyerek (örneğin: “Proje için README eklendi”) hem kendinize hem takım arkadaşlarınıza bilgi verebilirsiniz.

**Push** komutu ise yerel (bilgisayarınızdaki) commit’leri GitHub’daki uzak depoya göndermenizi sağlar.  
İlk başta yeni gelebilir ama zamanla çok doğal bir alışkanlık haline gelecektir. 🙂

## 💻 GitHub’da Bilmeniz Gereken Terimler

### Depolar (Repositories)

Depolar, çalışmalarınızın yapıldığı yerdir. GitHub'da çalıştıkça birçok deponuz olacak, ama ["GitHub kontrol paneliniz"](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard) üzerinden bunları kolayca yönetebilirsiniz.

Depolar ayrıca **README** dosyası içerir. README, projenizin amacını, nasıl kullanılacağını ve neden önemli olduğunu açıklayan bir dosyadır.  
Bu kurs da bir README dosyası ile size aktarılmaktadır. 😄  
[Daha fazla bilgi: Repositories hakkında](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) | [README hakkında](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes)

### Dallar (Branches)

Branch’ler (dallar), proje üzerinde değişiklik yaparken ana kodu bozmadan çalışmanızı sağlar.  
Yeni bir özellik eklemek, hata düzeltmek veya farklı bir fikir denemek için ana branch’ten (`main`) yeni bir dal oluşturabilirsiniz.  
Değişiklikler tamamlandığında, bu dalı ana dal (main) ile birleştirebilirsiniz.  
[Dallar hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches)

### Forklar (Forks)

Fork, bir başkasının deposunu kendi GitHub hesabınıza kopyalamanızdır.  
Genellikle açık kaynak projelere katkı sağlamak için kullanılır.  
[Forklama hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

### Pull Request’ler

Branch'ler üzerinde çalıştıktan sonra, değişikliklerin ana projeye katılması için **pull request** açabilirsiniz.  
Pull request sayesinde değişiklikleri tartışabilir, gözden geçirebilir ve onaylandığında birleştirebilirsiniz.  
[Pull request hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)

### Issues (Sorunlar)

Issues, projede geliştirme yapılacak işleri, hataları veya yeni özellik fikirlerini takip etmek için kullanılır.  
Özellikle büyük projelerde işleri düzenli tutmak için çok faydalıdır.  
[Issues hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/managing-your-work-on-github/about-issues)

### Kullanıcı Profili

Profil sayfanız, yaptığınız katkıları, ilginizi çeken projeleri ve katıldığınız tartışmaları gösterir.  
Ayrıca bir **Profil README’si** oluşturarak kendinizi tanıtabilirsiniz!  
[Profil README’si hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme)

### GitHub’da Markdown Kullanımı

Markdown, GitHub’da yazılarınızı biçimlendirmenin kolay bir yoludur. Başlıklar, listeler, kalın yazılar ekleyebilir veya görseller yerleştirebilirsiniz.  
[Markdown hakkında daha fazla bilgi edinin.](https://guides.github.com/features/mastering-markdown/)

### GitHub Topluluğuyla Etkileşim

GitHub topluluğu çok geniştir: Öğrenciler, profesyonel geliştiriciler, açık kaynak katkıcıları ve daha fazlası burada buluşur.  
İşte toplulukla etkileşim kurabileceğiniz bazı yollar:

#### Depoları Yıldızlamak (Star)

Beğendiğiniz veya takip etmek istediğiniz depolara yıldız (⭐) verebilirsiniz.  
[Yıldızlama hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/getting-started-with-github/saving-repositories-with-stars)

#### Kullanıcıları Takip Etmek

İlgilendiğiniz kişileri takip ederek onların faaliyetlerinden haberdar olabilirsiniz.  
[Kullanıcı takip etmek hakkında daha fazla bilgi edinin.](https://docs.github.com/en/github/getting-started-with-github/following-people)

#### GitHub Explore'u Kullanmak

Yeni projeler, geliştiriciler ve etkinlikler keşfetmek için [GitHub Explore](https://github.com/explore)'u kullanabilirsiniz.

---

## 📝 İsteğe Bağlı Sonraki Adımlar

- Bir pull request açarak öğretmeninize kursu tamamladığınızı bildirin.  
- Depoda yeni bir markdown dosyası oluşturun ve neler öğrendiğinizi yazın!  
- Kendi profil README’nizi oluşturun ve kendinizi tanıtın.  
- Kontrol panelinizden yeni bir depo oluşturun ve özellikleri keşfedin.  
- [Eğitim ekibine geri bildirim verin.](https://support.github.com/contact/education)

## 📚 Kaynaklar

- [GitHub Nedir? - Kısa Video](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be)
- [Git ve GitHub Öğrenme Kaynakları](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources)
- [GitHub Akışı (GitHub Flow) Anlamak](https://guides.github.com/introduction/flow/)
- [GitHub Dallarını Kullanma](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
- [Etkileşimli Git Eğitim Materyalleri](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
- [GitHub Learning Lab](https://lab.github.com/)
- [Eğitim Topluluğu Forumu](https://education.github.community/)
- [GitHub Topluluğu Forumu](https://github.community/)

---
