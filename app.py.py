import streamlit as st
import sqlite3
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# دالة لتعديل النصوص العربية لتظهر بشكل صحيح في المتصفح
def fix_arabic(text):
    if text:
        reshaped_text = reshape(text)
        return get_display(reshaped_text)
    return text

# اسم قاعدة البيانات التي نقلتها للمجلد
DB_NAME = "Final_School_System.db"

st.set_page_config(page_title="نتائج الطلاب", layout="centered")

st.title(fix_arabic("منظومة استعلام نتائج الطلاب"))
st.write("---")

code_input = st.text_input(fix_arabic("أدخل كود الطالب الخاص بك:"))

if st.button(fix_arabic("عرض النتيجة")):
    if code_input:
        try:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            # يبحث عن الطالب بالكود في جدول students
            cursor.execute("SELECT * FROM students WHERE student_code=?", (code_input,))
            result = cursor.fetchone()
            conn.close()

            if result:
                st.success(fix_arabic(f"أهلاً بك: {result[2]}")) # الاسم
                st.metric(label=fix_arabic("السعي النهائي"), value=result[8]) # الدرجة
            else:
                st.error(fix_arabic("عذراً، الكود غير موجود"))
        except Exception as e:
            st.error(fix_arabic("حدث خطأ في الاتصال بقاعدة البيانات"))
    else:
        st.warning(fix_arabic("يرجى إدخال الكود أولاً"))