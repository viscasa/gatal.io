<h1 align="center">WELCOME TO GATAL.IO !!!</h1>
<p align="center"> <img src="asset/img/Logo.jpg" width="150"></p>

Gatal.io adalah salah satu platform _e-commerce_ Indonesia untuk menjual barang-barang digital, termasuk _video game indie_, _asset game_, musik, dan banyak lagi.

# Tugas 2
### Proses Pembuatan Proyek Django hingga Melakukan Deployment ke PWS:
- [x] Membuat sebuah proyek Django baru.
1. Buat repositori baru di Github dengan nama ```gatal.io```
2. Buat direktori lokal dan hubungkan dengan repositori di Github dengan _mantra_ :
    ```bash
    git init 
    git remote add origin https://github.com/viscasa/gatal.io.git
    ```
3. Buat _virtual environment_ dengan menjalankan _command_ berikut di direktori lokal:
    ```bash
    python -m venv env
    ```
4. Aktifkan _virtual environment_ dengan _command_ berikut di direktori lokal:
    ```bash
    env\Scripts\activate
    ```
5. Di direktori yang sama, tambahkan _file_ `requirements.txt` untuk membuat _dependencies_ yang berisikan:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
6. Lakukan instalasi terhadap _dependencies_ tadi dengan _command_ berikut:
    ```bash
    pip install -r requirements.txt
    ```
7. Buat proyek Django bernama `gatal_io` dengan _command_ berikut:
    ```bash
    django-admin startproject gatal_io .
    ```

- - - -

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Mengubah `ALLOWED_HOSTS` di file `settings.py` pada direktori proyek untuk keperluan deployment dengan menambahkan:
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "alwie-attar-gatalio.pbp.cs.ui.ac.id"]
    ...
    ```
2. Membuat aplikasi `main` dengan _command_:
    ```bash
    python manage.py startapp main
    ```

- - - -
- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
1. Mendaftarkan aplikasi `main` ke dalam `setting.py`:
    ```python
    INSTALLED_APPS = [
    ...,
    'main'
    ]
    ```

- - - -

- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    - `name`
    - `price`
    - `description`
1. Isi _file_ `models.py` di direktori `main` dengan kode berikut:
    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        rating = models.FloatField()
        genre = models.TextField()
    ```
2. Jalankan _command_ berikut untuk membuat migrasi model:
    ```bash
    python manage.py makemigrations
    ```
3. Jalankan _command_ berikut untuk menerapkan migrasi ke dalam basis data lokal.
    ```bash
    python manage.py migrate
    ```

- - - -

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas Anda.

1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main`.
2. Di dalam direktori `templates`, buat _file_ baru bernama `main.html`. Isi _file_ `main.html` dengan kode berikut:
    ```html
    <h1 align="center">WELCOME TO GATAL.IO !!!</h1>

    <h5>Name: {{ name }}</h5>
    <h5>Class: {{ class }}</h5>
    ```
3. Buka _file_ `views.py` yang terletak di dalam direktori `main`. Lalu ubah isinya menjadi kode berikut:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'name': 'Alwie Attar Elfandra',
            'class': 'PBP D'
        }

        return render(request, "main.html", context)
    ```

- - - -

- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Buat _file_ `urls.py` di dalam direktori `main`
2. Isi file tersebut dengan kode:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
3. _Routing_ url pada file `urls.py` di direktori `gatal_io` sehingga isi file `urls.py` menjadi:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls'))
    ]
    ```

- - - -

- [x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Lakukan tes pada proyek Django yang sudah Anda buat dengan menjalankan perintah `python manage.py runserver`
2. Buka http://localhost:8000/ di incognito mode
3. Jika proyek sudah aman, Anda bisa matikan Django servernya dan melakukan deploy ke situs PWS.
4. Pastikan Anda sudah melakukan registrasi pada situs PWS (https://pbp.cs.ui.ac.id/) dan sudah membuat proyek di PWS tersebut.
5. Jalankan perintah yang terdapat pada informasi _Project Command_ pada halaman PWS, maka proyek Anda sudah berhasil di-_deploy_ ke PWS.
6. Apabila kedepannya ada perubahan pada proyek Django Anda yang ingin Anda push ke PWS, jalankan _command_ berikut:
    ```bash
    git push pws main:master
    ```

- - - -

<h3 align="center">
Bagan <i>Request User</i> ke <i>Web</i> Aplikasi berbasis Django
</h3>

<p align="center"> 
    <img src="asset/img/MVT.jpg">
</p>

Request dari user akan diproses terlebih dahulu sehingga dapat diteruskan ke View yang sesuai. kemudian View tersebut akan membaca/menulis data di Model dan menggunakan Template yang sesuai untuk menampilkan dan mengembalikan response ke user.

- - - -

### Fungsi Git dalam Pengembangan Perangkat Lunak
1. **Versi Kontrol:** Git memungkinkan pengembang melacak perubahan kode sumber dari waktu ke waktu. Setiap perubahan disimpan sebagai versi (_commit_), sehingga mudah untuk kembali ke versi sebelumnya jika diperlukan.

2. **Kolaborasi Tim:** Dengan Git, banyak pengembang dapat bekerja secara bersamaan di proyek yang sama tanpa saling mengganggu pekerjaan satu sama lain. _Branching_ (pembuatan cabang) mempermudah pekerjaan di fitur yang berbeda sebelum digabungkan (_merged_) ke cabang utama.

3. **Pemecahan Konflik:** Git memudahkan deteksi dan resolusi konflik kode ketika dua atau lebih pengembang mengedit file yang sama.

4. **Backup & Repositori Terdistribusi:** Git menyimpan salinan lengkap dari repositori di setiap mesin yang menggunakannya, sehingga kode aman jika server pusat tidak dapat diakses atau hilang.

5. **Branching dan Merging:** Git memungkinkan pembuatan cabang (_branch_) untuk pengembangan fitur baru atau eksperimen tanpa mempengaruhi kode utama. Setelah diuji, perubahan dari cabang ini bisa digabungkan (_merge_) ke cabang utama.

- - - -

### Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

1. Django menggunakan Python yang mudah dipahami, cocok untuk pemula.
2. Banyak fitur bawaan yang langsung siap digunakan tanpa konfigurasi tambahan.
3. Arsitektur Model-View-Template (MVT) membantu pemula memahami struktur kode yang baik.
4. Dokumentasi yang lengkap dan mudah diikuti memudahkan pembelajaran.
5. Komunitas besar dan aktif menyediakan banyak sumber belajar dan bantuan.

- - - -

### Mengapa Model pada Django Disebut sebagai ORM?

Model pada Django disebut sebagai **ORM** (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel dalam database relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan kode Python tanpa harus menulis query SQL secara langsung. Setiap model merepresentasikan tabel dalam database, di mana kolom menjadi atribut objek Python. ORM memudahkan operasi seperti insert, update, dan query data, serta memungkinkan otomatisasi manajemen skema database dan mendukung berbagai jenis database. Selain itu, ORM juga menangani relasi antar tabel dengan mudah, menjadikan pengelolaan data lebih intuitif dan aman.

# Tugas 3
### Mengapa Kita Memerlukan _Data Delivery_ dalam Pengimplementasian Sebuah Platform?

_Data delivery_ diperlukan dalam pengimplementasian sebuah platform untuk memastikan informasi dapat ditransfer secara efisien, cepat, dan aman antara server dan klien. Ini sangat penting dalam platform yang membutuhkan interaksi real-time, seperti _game multiplayer_ atau aplikasi berbasis _cloud_, di mana data harus dikirim dan diterima tanpa jeda signifikan agar pengalaman pengguna tetap lancar. Selain itu, _data delivery_ juga mendukung pemrosesan dan analisis data yang diperlukan untuk meningkatkan performa platform, serta menjaga keamanan dan reliabilitas dalam skala besar seiring dengan bertambahnya pengguna.

- - - -

### Mana yang Lebih Baik antara XML dan JSON?

Saya sendiri lebih menyukai JSON, karena formatnya yang lebih mudah dibaca oleh manusia. Selain itu, format JSON yang cenderung memiliki karakter lebih sedikit dari format lain seperti XML memungkinkan JSON untuk diproses lebih cepat dan lebih populer daripada format lain.

- - - -

### Fungsi dari Method `is_valid()` pada form Django

Method `is_valid()` digunakan untuk memvalidasi isi input dari _form_ tersebut. Dengan memanggil is_valid(), kita bisa menghindari kesalahan dan input data yang tidak konsisten, serta memberikan _feedback_ kepada pengguna jika terdapat kesalahan dalam input mereka. Hal ini untuk menjaga agar data yang diproses tetap aman dan sesuai dengan ketentuan yang telah ditetapkan.

- - - -

### Alasan Kita Membutuhkan `csrf_token` Saat Membuat form di Django?

Fungsi `csrf_token` pada pembuatan form di Django adalah untuk melindungi aplikasi web dari serangan **Cross-Site Request Forgery (CSRF)**. Dengan menyertakan token ini dalam setiap form, Django memastikan bahwa setiap permintaan yang diajukan berasal dari sumber yang sah (yaitu, dari pengguna yang sah di situs tersebut), mencegah aksi tidak sah yang dapat dilakukan oleh penyerang dari situs eksternal. Token ini unik untuk setiap sesi dan permintaan, sehingga meningkatkan keamanan aplikasi web.

- - - -

### Proses Pembuatan _Input Form_ hingga Membuat _Routing URL_ untuk Masing-Masing Views

- [x] Membuat input _form_ untuk menambahkan objek model pada app sebelumnya.

1. Menambahkan direktori `templates` di direktori utama dan `base.html` sebagai _template_ dasar yang dapat digunakan sebagai kerangka umum dari halaman lainnya.

2. Menambahkan lokasi direktori `templates` tersebut ke `settings.py` di direktori `gatal_io`:
    ```python
    TEMPLATES = [
        {
            . . .
            'DIRS': [BASE_DIR / 'templates'],
            . . .
        },
    ]
    ```

3. Menampilkan database ke dalam laman utama, yaitu `main.html` dan juga menjadi _extend_ dari `base.html` di direktori utama:
    ```html
    <h1 align="center">WELCOME TO GATAL.IO !!</h1>
    <p align="center"> <img src="{% static 'Logo.jpg' %}" width="150"></p>

    <h5>Name: {{ name }}</h5>
    <h5>Class: {{ class }}</h5>

    {% if not product_entries %}
    <p>Belum ada data game pada gatal.io.</p>
    {% else %}
    <table>
        <tr>
            <th>Game Name</th>
            <th>Time</th>
            <th>Genre</th>
            <th>Description</th>
            <th>Price</th>
        </tr>

        {% for product_entry in product_entries %}
        <tr>
            <td>{{product_entry.name}}</td>
            <td>{{product_entry.time}}</td>
            <td>{{product_entry.genre}}</td>
            <td>{{product_entry.description}}</td>
            <td>{{product_entry.price}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <br />

    <div align="center">
        <a href="{% url 'main:create_product_entry' %}">
            <button>Add New Game</button>
        </a>
    </div>

    {% endblock content %}
    ```

4. Mengubah _Primary Key_ dari _Integer_ menjadi UUID lalu lakukan migrasi seperti cara di tugas sebelumnya. Hal ini dapat dilakukan dengan cara menambahkan kode berikut di `models.py` pada direktori `main`:
    ```python
    import uuid  # tambahkan baris ini di paling atas
    ...
    class MoodEntry(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
        . . .
    ...
    ```

5. Membuat `forms.py` di direktori `main` dengan isi:
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm) :
        class Meta:
            model = Product
            fields = ["name", "genre","description", "price"]
    ```

6. Menambahkan Method `create_product_entry` untuk menambah entri database di file `views.py` di direktori `main`
    ```python
    def create_product_entry(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)
    ```

7. Mengimplementasikan form yang tadi sudah dibuat ke dalam laman baru dengan template html yang baru `create_product_entry.html` di direktori `main/templates`.

8. Routing URL ke laman yang bersangkutan di file `urls.py` di direktori `main`:
    ```python
    urlpatterns = [
        . . .
        path('create_product_entry', create_product_entry, name='create_product_entry'),
        . . .
    ]
    ```

- - - -

- [x] Tambahkan 4 fungsi _views_ baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by ID_, dan JSON _by ID_.

1. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML baik secara keseluruhan maupun per entri database. Tambahkan kode berikut di `views.py` pada direktori `main`:
    ```python
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

- - - -

- [x] Membuat routing URL untuk masing-masing _views_ yang telah ditambahkan pada poin 2.

1. Merouting kembali URL yang bersangkutan di file `urls.py` di direktori `main`:
    ```python
    urlpatterns = [
        . . .
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

- - - -

### _Screenshot_ Postman

1. **JSON**
<p align="center"> 
    <img src="asset/img/JSON.png">
</p>

2. **JSON by ID**
<p align="center"> 
    <img src="asset/img/JSONbyID.png">
</p>

3. **XML**
<p align="center"> 
    <img src="asset/img/XML.png">
</p>

4. **XML by ID**
<p align="center"> 
    <img src="asset/img/XMLbyid.png">
</p>

# Tugas 4
### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

Di Django, `HttpResponseRedirect()` dan `redirect()` memiliki fungsi yang mirip, tetapi ada beberapa perbedaan penting antara keduanya:

1. Fungsi dan Penggunaan:
    - `HttpResponseRedirect()`: Ini adalah kelas yang digunakan untuk membuat respons redirect HTTP secara eksplisit. Anda harus memberikan URL sebagai argumen, dan ini akan membuat objek respons yang mengalihkan ke URL tersebut.
        ```python
        from django.http import HttpResponseRedirect

        def my_view(request):
            return HttpResponseRedirect('/some-url/')
        ```

    - `redirect()`: Ini adalah fungsi yang lebih tinggi yang lebih fleksibel dan lebih mudah digunakan. Fungsi ini dapat menerima berbagai jenis argumen, termasuk URL sebagai string, nama view, dan argumen untuk view tersebut. Ini akan mengembalikan objek `HttpResponseRedirect`.
        ```python
        from django.shortcuts import redirect

        def my_view(request):
            return redirect('some-view-name')
        ```
2. Fleksibilitas:
    - `redirect()` lebih fleksibel karena dapat digunakan untuk mengarahkan ke URL berdasarkan nama view. Ini memungkinkan penggunaan URL namespaces dan menghasilkan URL yang lebih mudah dipelihara.
    - `HttpResponseRedirect()` lebih langsung, tetapi Anda harus selalu menyediakan URL lengkap.

Kesimpulannya, gunakan redirect() jika kita ingin kemudahan dan fleksibilitas, dan gunakan HttpResponseRedirect() jika kita perlu lebih banyak kontrol langsung atas objek respons yang dihasilkan.

- - - -

### Cara kerja penghubungan model `Product` dengan `User`!
Untuk menghubungkan model `Product` dengan model `User`, kita dapat menggunakan **ForeignKey** untuk membuat relasi one-to-many antara `User` dan `Product`. Ini berarti setiap objek `Product` dapat dikaitkan dengan satu User, sementara satu `User` dapat memiliki banyak objek `Product`. Hal ini bisa dilakukan dengan menambahkan atribut baru pada `Product` yaitu `user` seperti contoh berikut:
```python
. . .
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
. . .
```

- - - -

### Perbedaan antara authentication dan authorization dan bagaimana Django mengimplementasikan kedua konsep tersebut.
**Authentication**: Proses memverifikasi identitas pengguna (apakah pengguna benar-benar siapa yang mereka klaim). Pada Django, ini dilakukan melalui sistem login dan `authenticate()` ataupun `AuthenticationForm`.
**Authorization**: Proses menentukan apa yang dapat dilakukan oleh pengguna setelah mereka diautentikasi. Pada Django, ini dikelola dengan menggunakan izin (`permissions`) dan grup (`groups`) seperti misalnya penggunaan decorator `@login_required`.

- - - -

### Cara Django mengingat pengguna yang telah login serta kegunaan lain dari cookies dan keamanan penggunaan cookies.
Django mengingat pengguna yang telah login dengan menggunakan session yang disimpan di dalam cookies. Ketika seorang pengguna berhasil melakukan login, Django membuat session untuk pengguna tersebut dan menyimpan session ID dalam bentuk cookie di browser pengguna. Setiap kali pengguna mengakses halaman lain, cookie ini dikirim kembali ke server untuk memverifikasi identitas pengguna yang sedang login.

Selain mengingat login pengguna, cookies juga dapat digunakan untuk menyimpan preferensi pengguna, melacak aktivitas pengguna, dan menampilkan konten sesuai preferensi pengguna. Walaupun begitu, tidak semua cookies aman untuk digunakan. Karena cookies bisa menyimpan data kita termasuk data pribadi kita (seperti email, nama, dll) bisa saja terjadi pencurian cookies yang mengakibatkan pencurian data, *hack*, ataupun *phising*.

- - - -

### Proses mengimplementasikan fungsi registrasi, login, dan logout hingga  menampilkan detail informasi pengguna dan menerapkan `cookies`.
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1. Menambahkan fungsi `register`, `login_user`, `logout_user` di `views.py`
    ```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

2. Membuat laman baru pada `main/templates` yaitu `register.html` dan `login.html`.

3. Melakukan routing url dengan menambahkan kode berikut di `urls.py` pada direktori `main`:
    ```python
    urlpatterns = [
        . . .
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        . . .
    ]
    ```

4. Menghubungkan tiap file .html yang satu dengan yang lain dengan urutan register (optional) -> login -> main page  -> logout.

- - - -
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
1. Melakukan registrasi dan menambahkan 2 akun yaitu alwie.attar dan viscasa
2. Menambahkan data pada kedua akun menggunakan interaksi yang ada di website ini.

- - - -
- [x] Menghubungkan model `Product` dengan `User`.
1. Pada `models.py` di direktori main, tambahkan atribut baru yaitu user seperti berikut:
    ```python
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
2. Ubah fungsi `create_product_entry` pada file `views.py` menjadi:
    ```python
    def create_product_entry(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)
    ```
3. Mengubah value dari `product_entries` dan `context` pada fungsi `show_main` menjadi seperti berikut:
    ```python
    def show_main(request):
        product_entries = Product.objects.filter(user=request.user)

        context = {
            . . .
            'last_login': request.COOKIES['last_login'],
        }
    ```
4. Melakukan migrasi model kembali.

- - - -

- [x] Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan *cookies* seperti *last login* pada halaman utama aplikasi.

1. Mengubah value `context` pada fungsi `show_main` di file `views.py` menjadi :
    ```python
    context = {
        'name': request.user.username,
        . . .
    }
    ```

2. Karena pada fungsi `login_user` di `views.py` kita sudah menambahkan cookies, kita hanya perlu menambahkan value pada `context` yaitu:
    ```python
    context = {
        . . .
        'last_login': request.COOKIES['last_login'],
    }
    ```

3. Kita juga sudah mengimplementasikan penghapusan cookies pada fungsi `logout_user`.

4. Menambahkan teks last login pada `main.html`:
    ```html
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

# Tugas 5

### Urutan prioritas pengambilan CSS selector.
Ketika terdapat lebih dari satu style yang didefinisikan untuk elemen HTML, browser akan menerapkan style yang memiliki prioritas paling tinggi. Berikut ini adalah urutan prioritasnya dari yang paling tinggi hingga paling rendah:
1. *Inline Style*: Style yang ditulis langsung pada elemen HTML menggunakan atribut `style`. Karena didefinisikan langsung pada elemen, inline style memiliki prioritas tertinggi. Contoh:
    ```html
    <p style="color: red;">Teks ini berwarna merah.</p>
    ```
2. *Internal dan External Style Sheets*: Style yang didefinisikan di dalam tag `<style>` pada bagian `<head>` dokumen HTML (internal) atau dalam file CSS terpisah yang di-link ke dokumen HTML (external). Kedua style ini memiliki prioritas di bawah inline style. Contoh:
    ```html
    {%comment%} Internal {%endcomment%}
    <style>
    p {
        color: blue;
    }
    </style>

    {%comment%} External {%endcomment%}
    <link rel="stylesheet" href="styles.css">
    ```
3. *Browser Default*: Jika tidak ada style lain yang diterapkan, browser akan menggunakan style default. Ini adalah style bawaan yang diterapkan oleh browser ketika tidak ada style khusus yang didefinisikan oleh pengguna atau pengembang. Contoh:
    ```html
    <p>Teks ini menggunakan style default browser.</p>
    ```
Dengan urutan prioritas ini, *inline style* akan selalu diterapkan jika ada, meskipun external atau internal style mendefinisikan aturan yang sama. Jika tidak ada inline style, *internal atau external stylesheets* akan diterapkan, dan jika keduanya tidak ada, barulah *browser default* yang digunakan.

- - - -

### _Responsive design_ sebagai konsep yang penting dalam pengembangan aplikasi web.
Responsive design menjadi penting dalam pengembangan aplikasi web karena memungkinkan situs beradaptasi dengan berbagai ukuran layar perangkat, seperti smartphone, tablet, dan desktop, sehingga memberikan pengalaman pengguna yang optimal tanpa perlu membuat versi terpisah untuk setiap perangkat. Hal ini juga meningkatkan aksesibilitas, efisiensi biaya, serta mendukung SEO (_Search Engine Optimization_) karena mesin pencari lebih menyukai situs yang responsif.

* Contoh aplikasi dengan _responsive design_: X, Scele, Discord, dll.
* Contoh aplikasi yang belum menerapkannya : Pacil Web Server, aren.cs.ui.ac.id/sda/ , dll.

- - - -

### Perbedaan antara _margin, border, dan padding_, serta cara untuk mengimplementasikan ketiga hal tersebut.
**Margin**, **border**, dan **padding**adalah tiga properti CSS yang digunakan untuk mengatur ruang dan tampilan elemen di dalam halaman web, tetapi mereka memiliki fungsi yang berbeda.

1. **Margin**: Ini adalah ruang di luar elemen, yang digunakan untuk memberi jarak antara elemen satu dengan yang lain. Margin bersifat eksternal dan tidak mempengaruhi ukuran elemen itu sendiri. Contoh:
    ```html
    div {
        margin: 20px;
    }
    ```

2. **Border**: Border adalah garis yang mengelilingi elemen. Border berada di antara margin dan padding, dan dapat dikustomisasi dalam hal warna, lebar, dan gaya (seperti solid, dashed, atau dotted). Contoh:
    ```html
    div {
        border: 2px solid black;
    }
    ```

3. **Padding**: Padding adalah ruang di dalam elemen, antara konten elemen dan border-nya. Padding digunakan untuk memberi jarak antara konten elemen dan tepi elemen itu sendiri. Contoh:
    ```html
    div {
        padding: 15px;
    }
    ```

- - - -

### _Flex box_ dan _grid layout_ serta kegunaannya.
1. Flexbox (Flexible Box Layout)

    Flexbox adalah sistem layout yang digunakan untuk menyusun elemen dalam satu dimensi, baik itu secara horizontal (row) atau vertikal (column). Flexbox sangat berguna untuk mendistribusikan ruang di antara elemen dan menyelaraskan elemen dalam satu baris atau kolom dengan fleksibilitas yang lebih dinamis.

    Kegunaan Flexbox:
    * Membuat tata letak yang fleksibel, baik horizontal maupun vertikal.
    * Mengatur elemen untuk menyesuaikan ruang yang tersedia secara otomatis.
    * Mempermudah pembuatan layout yang responsif tanpa perlu menggunakan float atau positioning.
    * Mengontrol alignment (penyelarasan) dan distribusi elemen dalam container secara efisien.

    Contoh:
    ```html
    .container {
        display: flex;
        justify-content: space-between; /* Mengatur jarak antar item */
        align-items: center; /* Menyelaraskan item di sepanjang garis tengah */
    }
    ```

2. Grid Layout

    CSS Grid Layout adalah sistem layout dua dimensi yang lebih kuat, yang memungkinkan pengembang untuk mengatur elemen baik secara horizontal (baris) maupun vertikal (kolom). Grid memberikan kontrol lebih baik atas struktur kompleks yang terdiri dari baris dan kolom, sehingga memudahkan dalam membuat tata letak yang lebih rumit.

    Kegunaan Grid Layout:
    * Membuat tata letak dua dimensi (baris dan kolom) dengan mudah.
    * Menyusun tata letak yang lebih terstruktur dan kompleks, seperti dashboard, galeri, atau halaman web dengan layout berbasis grid.
    * Mengontrol ukuran elemen dalam grid dan bagaimana elemen tersebut merespons perubahan ukuran layar.

    Contoh:
    ```html
    .container {
        display: grid;
        grid-template-columns: 1fr 2fr; /* Membagi layout dalam dua kolom */
        grid-template-rows: auto;
        gap: 10px; /* Jarak antar elemen grid */
    }
    ```

- - - -

### Proses mengimplementasikan fungsi untuk menghapus dan mengedit product hingga membuat _navigation bar_.

- [x] Implementasikan fungsi untuk menghapus dan mengedit product.
1. Menambahkan dua method baru pada `views.py`, yaitu:
    ```python
    def edit_product(request, id):
        # Get product entry berdasarkan id
        product = Product.objects.get(pk = id)

        # Set product entry sebagai instance dari form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)

    def delete_product(request, id):
        # Get product berdasarkan id
        product = Product.objects.get(pk = id)
        # Hapus product
        product.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
2. Menambahkan import di `urls.py` serta lakukan routing sebagai berikut :
    ```python
    from main.views import ..., edit_product, delete_product
    urlpatterns = [
        . . .
        path('edit-product/<uuid:id>', edit_product, name='edit_product'),
        path('delete/<uuid:id>', delete_product, name='delete_product'),
        . . .
    ]
    ```

- - - -

- [x] Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma).

1. Menyambungkan template Django dengan tailwind, dengan cara menambahkan script tailwind berikut:
    ```html
    <script src="https://cdn.tailwindcss.com">
    ```
2. Membuat folder `static` sebagai tempat penyimpanan asset, seperti gambar, css, dll.
3. Lakukan konfigurasi static dengan cara menambahkan _middleware_ WhiteNoise dan ubah variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` sebagai berikut:
    ```python
    ...
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
        ...
    ]
    ...
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static' # merujuk ke /static root project pada mode development
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
    ...
    ```
4. Mengkustomisasi setiap laman pada `main/templates` dengan CSS dan Tailwind.
5. Pada laman `main.html`, cek apakah sudah ada produk yang terdaftar. Jika belum, munculkan gambar dan pesan bahwa produk belum terdaftar:
    ```html
    {% if not product_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/not_found.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
            <p class="text-center text-white mt-4">Belum ada data product pada GATAL.IO.</p>
        </div>
    ```

6. Buat card product untuk menampilkan product yang ada. Pada `main.html`, tambahkan kode berikut setelah mengecek apakah produk tersedia:
    ```html
    {% else %}
        <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
            {% for product_entry in product_entries %}
                {% include 'card_product.html' with product_entry=product_entry %}
            {% endfor %}
        </div>
    {% endif %}
    ```
    Lalu, buat template baru pada folder `template` yaitu `card_product.html` yang berisikan kode untuk menampilkan tiap atribut pada sebuah produk.

7. Membuat navigation bar dengan cara membuat template baru yaitu `navbar.html` lalu tautkan navigation bar tersebut ke laman yang diinginkan dengan menggunakan tags `include`:
    ```html
    {% extends 'base.html' %}
    {% block content %}
    {% include 'navbar.html' %}
    ...
    {% endblock content%}
    ```

8. Agar navigation bar responsive terhadap ukuran device, bagi kode `navbar.html` menjadi dua tag `<div>` sebagai berikut:
```html
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        ...
    </div>
    <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
        ...
    </div>
```

# Tugas 6

### Manfaat dari Penggunaan JavaScript dalam Pengembangan Aplikasi Web
JavaScript sangat bermanfaat dalam pengembangan aplikasi web karena memungkinkan pembuatan halaman yang interaktif dan dinamis. Bahasa ini berjalan di sisi klien, sehingga mempercepat respon aplikasi dan mengurangi beban server. Dengan kemampuan untuk memanipulasi elemen DOM secara real-time, JavaScript memungkinkan perubahan konten tanpa harus memuat ulang halaman (menggunakan AJAX).

- - - -

### Penggunaan `await` Ketika Menggunakan `fetch()`
Fungsi dari penggunaan `await` ketika menggunakan `fetch()` adalah untuk menunggu hingga *promise* yang dihasilkan oleh `fetch()` selesai dan memberikan hasil, sebelum melanjutkan eksekusi kode berikutnya. `fetch()` mengembalikan sebuah *promise* yang berisi respons dari request yang dibuat, dan dengan menggunakan `await`, kita dapat memastikan bahwa variabel atau operasi berikutnya menggunakan hasil dari request yang sudah selesai.

Jika kita tidak menggunakan `await`, eksekusi kode akan langsung berjalan tanpa menunggu selesainya proses fetch itu sendiri. Akibatnya, variabel yang seharusnya berisi hasil dari fetch mungkin berisi *promise* yang belum selesai, sehingga bisa menyebabkan hasil yang tidak diinginkan atau error ketika mencoba mengakses respons yang belum siap. Misalnya, jika kita mencoba memproses data yang dikembalikan oleh fetch sebelum *promise* tersebut selesai, akan terjadi ketidakcocokan data atau bahkan kegagalan dalam menjalankan logika selanjutnya.

- - - -

### Penggunaan Decorator `csrf_exempt` pada `view` -> AJAX `POST`
Kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST karena CSRF (Cross-Site Request Forgery) protection secara default diaktifkan dalam aplikasi Django untuk melindungi dari serangan CSRF. Serangan ini terjadi ketika sebuah situs web jahat mengirimkan request ke server yang sah atas nama pengguna yang sudah login, tanpa sepengetahuan pengguna tersebut.

Ketika kita mengirim request POST melalui AJAX tanpa menyertakan token CSRF yang valid, server akan menolak request tersebut karena dianggap tidak aman. Namun, dalam beberapa kasus, seperti ketika request AJAX berasal dari sumber yang dapat dipercaya (misalnya internal API), kita mungkin ingin menonaktifkan pemeriksaan CSRF pada view tersebut. Dengan menggunakan `@csrf_exempt`, kita menginstruksikan Django untuk tidak memverifikasi token CSRF pada view tersebut, sehingga AJAX POST dapat diproses tanpa memerlukan token CSRF.

- - - -

### Pembersihan Data Input
Pembersihan data input tidak boleh hanya dilakukan di frontend karena frontend dapat dimanipulasi oleh pengguna, membuat aplikasi rentan terhadap serangan seperti SQL injection atau XSS. Backend bertanggung jawab penuh atas pengelolaan dan penyimpanan data, sehingga harus memvalidasi dan membersihkan input untuk menjaga keamanan dan integritas data. Selain itu, backend sering diakses oleh berbagai klien, bukan hanya satu aplikasi frontend, sehingga validasi di backend memastikan konsistensi dan kontrol yang lebih ketat di seluruh sistem, menjamin perlindungan dari klien yang tidak sah.

- - - -

- [x] AJAX `GET`

1. Ubah variable data untuk `show_json` dan `show_xml` pada `views.py` menjadi:
    ```python
    data = Product.objects.filter(user=request.user)
    ```

2. Ubah kode untuk menampilkan card pada `main.html` menjadi:
    ```html
    <div id="product_entry_cards"></div>
    ```

3. Buat fungsi pada javaScript di `main.html` untuk mengambil produk pengguna:
    ```javaScript
    async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
    ```

4. Buat fungsi pada javaScript di `main.html` untuk merefresh produk yang ada dan menampilkan cardnya:
    ```javaScript
    async function refreshProductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getProductEntries();
        let htmlString = "";
        let classNameString = "";

        if (productEntries.length === 0) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/not_found.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data product pada GATAL.IO.</p>
                </div>
            `;
        }
        else {
            classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
            productEntries.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);
                const genre = DOMPurify.sanitize(item.fields.genre);
                const price = DOMPurify.sanitize(item.fields.price);
                htmlString += `
                <div class="relative break-inside-avoid">
                <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                    <div class="w-[3rem] h-8 bg-gray-400 rounded-md opacity-80 -rotate-90"></div>
                    <div class="w-[3rem] h-8 bg-gray-400 rounded-md opacity-80 -rotate-90"></div>
                </div>
                <div class="relative top-5 bg-green-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-green-300 transform rotate-0 hover:rotate-2 transition-transform duration-300">
                    <div class="bg-green-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-green-300">
                    <h3 class="font-bold text-xl mb-2">${name}</h3>
                    <p class="text-gray-600">${item.fields.time}</p>
                    </div>
                    <div class="p-4">
                    <p class="font-semibold text-lg mb-2">Description</p> 
                    <p class="text-black mb-2">
                        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${description}</span>
                    </p>
                    <div class="mt-4">
                        <p class="text-black font-semibold mb-2">Genre</p>
                        <p class="text-black mb-2">
                        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${genre}</span>
                        </p>
                    </div>
                    <div class="mt-4">
                        <p class="text-black font-semibold mb-2">Price</p>
                        <p class="text-black mb-2">
                        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">Rp ${price}</span>
                        </p>
                    </div>
                    </div>
                </div>
                <div class="absolute top-0 -right-4 flex space-x-1">
                    <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                    </a>
                    <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    </a>
                </div>
                </div>
                `;
            });
        }
    }
    ```

- - - -

- [x] AJAX `POST`

1. Buat button baru di `main.html` untuk menghandle add product menggunakan AJAX :
    ```html
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-green-700 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
        Add New Product by AJAX
    </button>
    ```

2. Buat sebuah fungsi di `views.py` untuk menambahkan produk menggunakan AJAX:
    ```python
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):
        name = strip_tags(request.POST.get("name"))
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))
        genre = strip_tags(request.POST.get("genre"))
        user = request.user

        new_product = Product(
            name = name, price = price, description = description,
            genre = genre, user = user
        )

        if (new_product.name!="" or new_product.description!="" or new_product.genre!="") :
            new_product.save()
            return HttpResponse(b"CREATED", status=201)
        return HttpResponse(b"FAILED", status=301)
    ```

3. Lakukan routing seperti biasa di `urls.py`:
    ```python
    from main.views import ... , add_product_entry_ajax
    urlpatterns = [
        . . .
        path('create-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
        . . .
    ]
    ```

4. Buat sebuah modal untuk menampilkan popup form untuk menambahkan produk di `main.html`:
    ```html
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
            <!-- Modal header -->
            <div class="bg-gray-400 flex items-center justify-between p-4 border-b rounded-t">
            <h3 class="text-xl font-semibold text-gray-900">
                Add New Product Entry
            </h3>
            <button type="button" class="text-gray-600 bg-transparent hover:bg-red-500 hover:text-white rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
            </div>
            <!-- Modal body -->
            <div class="bg-gray-300 px-6 py-4 space-y-6 form-style">
            <form id="productEntryForm">
                <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-400 rounded-md p-2 hover:border-green-700" placeholder="Enter the game name" required>
                </div>
                <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-400 rounded-md p-2 hover:border-green-700" placeholder="Description" required></textarea>
                </div>
                <div class="mb-4">
                <label for="genre" class="block text-sm font-medium text-gray-700">Genre</label>
                <textarea id="genre" name="genre" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-400 rounded-md p-2 hover:border-green-700" placeholder="Genre" required></textarea>
                </div>
                <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Price (0-10000000)</label>
                <input type="price" id="price" name="price" min="0" max="10000000" class="mt-1 block w-full border border-gray-400 rounded-md p-2 hover:border-green-700" required>
                </div>
            </form>
            </div>
            <!-- Modal footer -->
            <div class="bg-gray-400 flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-green-700 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
        </div>
        </div>
    ```

5. Tambahkan script javaScript untuk menambahkan produk, menampilkan modal yang telah dibuat, dan meng-*hide* modal:
    ```javaScript
    function addProductEntry() {
        fetch("{% url 'main:add_product_entry_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productEntryForm')),
        })
        .then(response => {
            if (response.ok) {
                refreshProductEntries();
                hideModal();
            } else {
                alert("Gagal submit form, coba lagi.");
            }
        })

        document.getElementById("productEntryForm").reset(); 

        return false;
    }
    document.getElementById("submitProductEntry").onclick = addProductEntry

    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
        modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);
    ```