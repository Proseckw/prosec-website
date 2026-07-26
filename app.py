from flask import Flask, render_template_string, request, send_file, Response
import datetime
import os

app = Flask(__name__)

# مسار ذكي لجلب اللوجو تلقائياً لتجنب بطء التحميل ومشاكل المسارات
@app.route("/logo")
def get_logo():
    possible_paths = [
        "logo.jpg", "logo.png", "logo.jpeg",
        "prosec logo.jpg", "prosec logo.png",
        "static/logo.jpg", "static/logo.png", "static/prosec logo.jpg", "static/prosec logo.png"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return send_file(path)
    return Response(status=404)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>شركة بروسيك للأنظمة الأمنية | ProSec Security Systems</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts (Cairo) -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 flex flex-col min-h-screen">

    <!-- Navbar / القائمة العلوية -->
    <header class="bg-slate-800/90 backdrop-blur border-b border-slate-700 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-6 py-3 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <!-- شعار الشركة -->
                <div class="bg-white p-1.5 rounded-xl border border-red-500/30 shadow-md flex items-center justify-center">
                    <img src="/logo" alt="ProSec Logo" class="h-10 w-auto object-contain">
                </div>
                <div>
                    <h1 class="text-xl font-bold tracking-wide text-white leading-tight">ProSec</h1>
                    <span class="text-red-500 text-xs font-semibold block">بروسيك للأجهزة والأنظمة الأمنية</span>
                </div>
            </div>
            <nav class="hidden md:flex gap-8 font-semibold text-slate-300">
                <a href="#home" class="hover:text-red-500 transition">الرئيسية</a>
                <a href="#about" class="hover:text-red-500 transition">عن بروسيك</a>
                <a href="#services" class="hover:text-red-500 transition">خدماتنا</a>
                <a href="#contact" class="hover:text-red-500 transition">تواصل معنا</a>
            </nav>
            <a href="#contact" class="bg-red-600 hover:bg-red-700 text-white font-bold px-5 py-2.5 rounded-lg transition shadow-lg shadow-red-600/30">
                طلب عرض سعر
            </a>
        </div>
    </header>

    <!-- Hero Section / الواجهة الرئيسية -->
    <section id="home" class="relative py-24 bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900 overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 text-center relative z-10">
            <span class="inline-block bg-red-500/10 text-red-400 border border-red-500/20 rounded-full px-4 py-1.5 text-sm font-semibold mb-6">
                <i class="fa-solid fa-shield-halved ml-2"></i> الحلول الأمنية الذكية والمتكاملة
            </span>
            <h2 class="text-4xl md:text-6xl font-extrabold text-white leading-tight mb-6">
                نحمي ممتلكاتك بأحدث <br><span class="text-red-500">الأنظمة والتقنيات الأمنية</span>
            </h2>
            <p class="text-slate-300 text-lg md:text-xl max-w-2xl mx-auto mb-10 leading-relaxed">
                تقدم شركة بروسيك أحدث أجهزة المراقبة، أنظمة التحكم بالدخول، وأجهزة الإنذار للمؤسسات والشركات والمنازل بأعلى معايير الأمان والدقة.
            </p>
            <div class="flex justify-center gap-4 flex-wrap">
                <a href="#services" class="bg-red-600 hover:bg-red-700 text-white font-bold px-8 py-3.5 rounded-xl transition shadow-lg shadow-red-600/30 text-lg">
                    استكشف خدماتنا
                </a>
                <a href="#about" class="bg-slate-700 hover:bg-slate-600 text-white font-bold px-8 py-3.5 rounded-xl transition text-lg border border-slate-600">
                    تعرّف علينا
                </a>
            </div>
        </div>
    </section>

    <!-- About Section / عن بروسيك -->
    <section id="about" class="py-20 bg-slate-800/50 border-y border-slate-800">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div class="flex justify-center">
                    <div class="relative group w-full max-w-md">
                        <div class="absolute -inset-1 bg-gradient-to-r from-red-600 to-red-900 rounded-3xl blur opacity-30 group-hover:opacity-60 transition duration-1000"></div>
                        <div class="relative bg-slate-900 border border-slate-700 p-8 rounded-3xl text-center shadow-2xl">
                            <div class="bg-white p-6 rounded-2xl inline-block mb-6 shadow-inner">
                                <img src="/logo" alt="ProSec Logo" class="w-48 h-auto mx-auto">
                            </div>
                            <h4 class="text-2xl font-bold text-white mb-2">ProSec Security Systems</h4>
                            <p class="text-red-500 font-semibold">بروسيك للأجهزة والأنظمة الأمنية</p>
                        </div>
                    </div>
                </div>

                <div>
                    <span class="text-red-500 font-bold text-sm tracking-wider uppercase">من نحن</span>
                    <h3 class="text-3xl md:text-4xl font-extrabold text-white mt-2 mb-6">شريكك الموثوق في الحماية والأمان</h3>
                    <p class="text-slate-300 leading-relaxed mb-6 text-lg">
                        تعتبر شركة <strong>بروسيك (ProSec)</strong> من الشركات الرائدة المتخصصة في توريد وتركيب وتكامل **الأجهزة والأنظمة الأمنية الحديثة**. نحن نلتزم بتقديم أحدث تقنيات الأمان لحماية المؤسسات، الشركات، والمنازل بأعلى كفاءة.
                    </p>
                    <p class="text-slate-300 leading-relaxed mb-8">
                        تشمل حلولنا أنظمة كاميرات المراقبة المتقدمة، أنظمة التحكم بالدخول والبصمة، أجهزة الإنذار ضد السرقة، والحلول الشبكية الذكية، مع توفير الدعم الفني والصيانة المستمرة عبر فريق متكامل من المهندسين والفنيين المتخصصين.
                    </p>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="flex items-start gap-3 bg-slate-900/80 p-4 rounded-xl border border-slate-700/60">
                            <i class="fa-solid fa-circle-check text-red-500 text-xl mt-1"></i>
                            <div>
                                <h5 class="font-bold text-white">أجهزة معتمدة وعالية الجودة</h5>
                                <p class="text-slate-400 text-sm">مواكبة لأعلى معايير الأمان العالمية.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-3 bg-slate-900/80 p-4 rounded-xl border border-slate-700/60">
                            <i class="fa-solid fa-headset text-red-500 text-xl mt-1"></i>
                            <div>
                                <h5 class="font-bold text-white">دعم وصيانة مستمرة</h5>
                                <p class="text-slate-400 text-sm">فريق مهندسين جاهز للتجاوب السريع.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section / الخدمات -->
    <section id="services" class="py-20 bg-slate-950">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h3 class="text-3xl md:text-4xl font-bold text-white mb-4">خدماتنا وحلولنا الأمنية</h3>
                <p class="text-slate-400 text-lg">نوفر باقة متكاملة من أحدث أجهزة الحماية المعتمدة</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="bg-slate-900 border border-slate-800 p-8 rounded-2xl hover:border-red-500/50 transition group">
                    <div class="w-14 h-14 bg-red-600/10 text-red-500 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-red-600 group-hover:text-white transition">
                        <i class="fa-solid fa-video"></i>
                    </div>
                    <h4 class="text-xl font-bold text-white mb-3">كاميرات المراقبة (CCTV)</h4>
                    <p class="text-slate-400 leading-relaxed">أنظمة مراقبة مرئية بدقة عالية مع ربط مباشر عبر شبكة الإنترنت والمتابعة من الهاتف الذكي.</p>
                </div>
                <div class="bg-slate-900 border border-slate-800 p-8 rounded-2xl hover:border-red-500/50 transition group">
                    <div class="w-14 h-14 bg-red-600/10 text-red-500 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-red-600 group-hover:text-white transition">
                        <i class="fa-solid fa-fingerprint"></i>
                    </div>
                    <h4 class="text-xl font-bold text-white mb-3">أجهزة البصمة والتحكم بالدخول</h4>
                    <p class="text-slate-400 leading-relaxed">أقفال إلكترونية، أنظمة بصمة الوجه والأصبع للتحكم في دخول الموظفين وتنظيم الصلاحيات.</p>
                </div>
                <div class="bg-slate-900 border border-slate-800 p-8 rounded-2xl hover:border-red-500/50 transition group">
                    <div class="w-14 h-14 bg-red-600/10 text-red-500 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-red-600 group-hover:text-white transition">
                        <i class="fa-solid fa-bell"></i>
                    </div>
                    <h4 class="text-xl font-bold text-white mb-3">أنظمة الإنذار ضد السرقة</h4>
                    <p class="text-slate-400 leading-relaxed">أجهزة ألمار وحساسات حركة متطورة للحماية من الاقتحام والتنبيه الفوري عند حالات الطوارئ.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact / نموذج التواصل -->
    <section id="contact" class="py-20 bg-slate-900">
        <div class="max-w-4xl mx-auto px-6">
            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-8 md:p-12 shadow-2xl">
                <h3 class="text-2xl md:text-3xl font-bold text-white mb-2 text-center">اطلب استشارة أو عرض سعر</h3>
                <p class="text-slate-400 text-center mb-8">أدخل بياناتك وسيتواصل معك فريق مهندسي بروسيك في أسرع وقت</p>
                
                {% if success %}
                <div class="bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 p-4 rounded-xl mb-6 text-center font-bold">
                    ✓ تم إرسال طلبك بنجاح! سيتم التواصل معك قريباً.
                </div>
                {% endif %}

                <form method="POST" action="/" class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-slate-300 font-semibold mb-2">الاسم الكريم</label>
                            <input type="text" name="name" required placeholder="أدخل اسمك" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-red-500">
                        </div>
                        <div>
                            <label class="block text-slate-300 font-semibold mb-2">رقم الهاتف</label>
                            <input type="tel" name="phone" required placeholder="مثال: 965XXXXXXXX+" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-red-500">
                        </div>
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-2">الخدمة المطلوبة</label>
                        <select name="service" class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-red-500">
                            <option>تركيب كاميرات مراقبة</option>
                            <option>أجهزة بصمة وتحكم بالدخول</option>
                            <option>أنظمة إنذار وحماية</option>
                            <option>صيانة وتطوير أنظمة قائمة</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-slate-300 font-semibold mb-2">التفاصيل أو الاستفسار</label>
                        <textarea name="message" rows="4" placeholder="اكتب تفاصيل طلبك هنا..." class="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-red-500"></textarea>
                    </div>
                    <button type="submit" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3.5 rounded-xl transition shadow-lg shadow-red-600/30 text-lg">
                        إرسال الطلب
                    </button>
                </form>
            </div>
        </div>
    </section>

    <footer class="bg-slate-950 border-t border-slate-800 py-8 mt-auto">
        <div class="max-w-7xl mx-auto px-6 text-center text-slate-500 text-sm">
            <p>© {{ year }} شركة بروسيك للأجهزة والأنظمة الأمنية (ProSec Security Systems). جميع الحقوق محفوظة.</p>
        </div>
    </footer>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    success = False
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        service = request.form.get("service")
        message = request.form.get("message")
        
        print(f"[طلب جديد] الاسم: {name} | الهاتف: {phone} | الخدمة: {service} | التفاصيل: {message}")
        success = True
    
    current_year = datetime.datetime.now().year
    return render_template_string(HTML_TEMPLATE, success=success, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)