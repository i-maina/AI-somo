import streamlit as st

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "pick a cuisine", ["Italian", "Indian", "Chinese", "Mexican", "American"]
)


def generate_restaurant_name_and_items(cuisine):
    return {"restaurant_name": "Curry Delight", "menu_items": "samosa, Paneer tikka"}


if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"])
    menu_items = response["menu_items"].split(",")
    st.write("*** Menu Items ***")

    for item in menu_items:
        st.write("-", item)
