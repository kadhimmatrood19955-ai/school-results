import streamlit as st
import pandas as pd
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# دالة أساسية لتنظيم الخط العربي ومنع الخربطة
def fix_ar(text):
    if isinstance(text, str):
        return get_display(reshape(text))
    return text

st.set_page_config(page_title="نتائج ابن خلدون")

# عنوان الموقع مرتب
st.title(fix_ar("نتائج متوسطة ابن خلدون للبنين"))

# قراءة ملف البيانات
try:
    df = pd.read_excel("Final_School_System.db")
    
    # خانة البحث
    search = st.text_input(fix_ar("أدخل اسم الطالب أو رقم الجلوس:"))

    if search:
        # البحث في كل الأعمدة
        result = df[df.astype(str).apply(lambda x: search in x.values, axis=1)]
        
        if not result.empty:
            st.success(fix_ar("تم العثور على النتيجة:"))
            # عرض البيانات بشكل منظم
            for col in result.columns:
                val = result[col].values[0]
                st.write(f"*{fix_ar(col)}*: {val}")
        else:
            st.error(fix_ar("عذراً، لم يتم العثور على هذا الاسم"))
except Exception as e:
    st.error("تأكد من رفع ملف قاعدة البيانات بشكل صحيح")
