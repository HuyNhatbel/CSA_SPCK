import streamlit as st

def menu():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/1_ptich_du_lieu.py", label="Phân tích dữ liệu")
    st.sidebar.page_link("pages/2_them_du_lieu.py", label="Thêm dữ liệu tập test")
    st.sidebar.page_link("pages/3_du_doan_mo_hinh.py", label="Phân tích dự đoán")

if __name__ == "__main__":
    st.set_page_config(
        page_title="",  # tên sản phẩm
        layout="centered",
        page_icon="👋",
    )

    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.title("Ảnh hưởng của âm nhạc tới sức khỏe tinh thần")  # tên sản phẩm
    st.header("Chức năng")
    st.markdown(
        """
    1. Xem phân tích tập dữ liệu ...
    2. Thêm dữ liệu mới và cập nhật các biểu đồ
    3. Sử dụng AI để dự đoán ...
    """
    )

    st.subheader("Credits")
    st.markdown(
        """
        Ứng dựng được xây dựng với [streamlit](https://streamlit.io) và [Plotly](https://plotly.com/).
        
        Được phát triển bởi [Huy Nhật](https://github.com/HuyNhatbel/CSA_SPCK)
        """
    )

    menu()