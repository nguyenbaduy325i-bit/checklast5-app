import streamlit as st

st.title("CheckLast5 App 📱")

numbers = st.text_input("Nhập 20 số (cách nhau bởi dấu phẩy):", "5,7,3,7,2,9,1,4,6,2,8,5,3,9,7,7,3,5,7,2")
val = st.number_input("Nhập số cần kiểm tra:", min_value=0, max_value=9, step=1)

if st.button("Kiểm tra"):
    nums = [int(x.strip()) for x in numbers.split(",") if x.strip().isdigit()]
    
    if len(nums) < 20:
        st.error("Bạn phải nhập đủ 20 số!")
    else:
        unique_last = []
        for n in reversed(nums):
            if n not in unique_last:
                unique_last.append(n)
            if len(unique_last) == 5:
                break
        
        st.write("5 số gần nhất không trùng:", unique_last)
        
        if val in unique_last:
            st.success("✅ Kết quả: G")
        else:
            st.warning("❌ Kết quả: X")
