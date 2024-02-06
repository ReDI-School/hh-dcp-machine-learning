# Web Applications

## Introduction

Models can be deployed as web applications to make them accessible to a wider audience. This is useful when you want to make your model available to the public or to a specific group of people.

There are several frameworks you can use to deploy your model as a web application. Some of the popular ones are:

1. Flask
2. Django
3. FastAPI
4. Streamlit
5. Dash
6. Shiny

The teacher can decide which one to teach. For a simple start I would suggest to use Streamlit, since it is extremely easy to use and has a very low learning curve.

## Streamlit

Streamlit is an open-source app framework for Machine Learning and Data Science teams. It is a Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

Streamlit is extremely easy to use and has a very low learning curve. It is a great tool for quickly deploying your models as web applications.

### Installation

You can install Streamlit using pip:

```bash
pip install streamlit
```

### Usage

You can create a simple web application using Streamlit by writing a Python script. Here is an example of a simple web application that displays a title and a plot:

```python
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('My First Web Application')

st.write("Here's our first attempt at using data to create a table:")
```

