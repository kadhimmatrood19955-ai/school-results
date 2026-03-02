# عنوان الموقع (تم إصلاحه ليظهر مرتباً)
st.title(fix_ar("نتائج متوسطة ابن خلدون للبنين"))

# قراءة البيانات
df = pd.read_excel("Final_School_System.db") # تأكد من اسم ملفك هنا

# خانة البحث
search = st.text_input(fix_ar("أدخل اسم الطالب أو رقم الجلوس:"))

if search:
    # فلترة النتائج
    result = df[df.astype(str).apply(lambda x: search in x.values, axis=1)]
    if not result.empty:
        # عرض النتيجة بشكل مرتب
        for col in result.columns:
            st.write(f"*{fix_ar(col)}*: {result[col].values[0]}")
    else:
        st.error(fix_ar("لم يتم العثور على نتيجة"))
