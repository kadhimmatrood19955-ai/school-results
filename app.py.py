import streamlit as st
import pandas as pd
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# دالة أساسية لتنظيم الخط العربي ومنع خربطته
def fix_ar(text):
    if isinstance(text, str):
        return get_display(reshape(text))
    return str(text)

st.set_page_config(page_title="نتائج ابن خلدون")

# عنوان الموقع (تم إصلاحه ليظهر مرتباً)
st.title(fix_ar("نتائج متوسطة ابن خلدون للبنين"))

try:
    # قراءة ملف الإكسل
    df = pd.read_excel("Final_School_System.db")
    
    # خانة البحث
    search = st.text_input(fix_ar("أدخل اسم الطالب أو رقم الجلوس:"))

    if search:
        # البحث في البيانات
        result = df[df.astype(str).apply(lambda x: search in x.values, axis=1)]
        
        if not result.empty:
            st.success(fix_ar("تم العثور على النتيجة:"))
            # عرض البيانات بشكل منظم مع تصحيح الخط لكل خلية
            for col in result.columns:
                val = result[col].values[0]
                st.write(f"*{fix_ar(col)}*: {fix_ar(val)}")
        else:
            st.error(fix_ar("عذراً، لم يتم العثور على نتيجة"))
except Exception as e:
    st.error(fix_ar("تأكد من رفع ملف قاعدة البيانات بشكل صحيح"))
