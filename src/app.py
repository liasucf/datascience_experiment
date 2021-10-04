import streamlit as st
import streamlit.components.v1 as components

from logic  import *

PATH = "./data/raw/mars-2014-complete.csv"

X_train, X_test, y_train, y_test = load_data(PATH)
automl =  load_model(X_train, X_test, y_train, y_test)
components.html(automl.report()._repr_html_())