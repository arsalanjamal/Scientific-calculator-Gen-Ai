import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to perform scientific calculations
def scientific_calculator():
    st.title("Scientific Calculator")
    
    st.subheader("Choose your operation:")
    operation = st.selectbox("Select an operation:", ["Trigonometric", "Logarithmic", "Algebraic"])

    if operation == "Trigonometric":
        angle = st.number_input("Enter the angle (in degrees):", value=45)
        radian = math.radians(angle)
        st.write(f"sin({angle}°):", math.sin(radian))
        st.write(f"cos({angle}°):", math.cos(radian))
        st.write(f"tan({angle}°):", math.tan(radian))

    elif operation == "Logarithmic":
        log_type = st.radio("Select Logarithmic function:", ["ln (log base e)", "log base 10"])
        value = st.number_input("Enter the value for logarithm:", value=1.0)

        if log_type == "ln (log base e)":
            if value > 0:
                st.write(f"ln({value}):", math.log(value))
            else:
                st.warning("Value must be greater than 0!")
        elif log_type == "log base 10":
            if value > 0:
                st.write(f"log10({value}):", math.log10(value))
            else:
                st.warning("Value must be greater than 0!")

    elif operation == "Algebraic":
        algebraic_type = st.selectbox("Choose the algebraic operation:", ["Power", "Square Root", "Factorial"])

        if algebraic_type == "Power":
            base = st.number_input("Enter the base:", value=2.0)
            exponent = st.number_input("Enter the exponent:", value=3.0)
            st.write(f"{base} raised to the power of {exponent} is:", math.pow(base, exponent))

        elif algebraic_type == "Square Root":
            value = st.number_input("Enter the value for square root:", value=16.0)
            if value >= 0:
                st.write(f"Square root of {value} is:", math.sqrt(value))
            else:
                st.warning("Square root of negative numbers is not real!")

        elif algebraic_type == "Factorial":
            value = st.number_input("Enter the integer value for factorial:", value=5, step=1)
            if value >= 0:
                st.write(f"Factorial of {int(value)} is:", math.factorial(int(value)))
            else:
                st.warning("Factorial of negative numbers is undefined!")

# Function to plot graphs
def plot_graph():
    st.title("Graph Plotting")

    plot_type = st.selectbox("Choose a plot type:", ["Line Plot", "Scatter Plot", "Bar Plot", "Histogram"])

    if plot_type == "Line Plot":
        x = np.linspace(-10, 10, 100)
        y = np.sin(x)
        plt.plot(x, y, label='y = sin(x)')
        plt.title('Line Plot - y = sin(x)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        st.pyplot()

    elif plot_type == "Scatter Plot":
        x = np.random.rand(50)
        y = np.random.rand(50)
        plt.scatter(x, y, label='Random Points')
        plt.title('Scatter Plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        st.pyplot()

    elif plot_type == "Bar Plot":
        categories = ['A', 'B', 'C', 'D', 'E']
        values = [10, 15, 7, 12, 5]
        plt.bar(categories, values)
        plt.title('Bar Plot')
        plt.xlabel('Category')
        plt.ylabel('Values')
        st.pyplot()

    elif plot_type == "Histogram":
        data = np.random.randn(1000)
        plt.hist(data, bins=30, alpha=0.75, label='Random Data')
        plt.title('Histogram')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()
        st.pyplot()

# Main function to control the flow of the app
def main():
    st.markdown('<h1 style="color: red;">Scientific Graphical Calculator with Plots</h1>', unsafe_allow_html=True)
    
    # h2 heading for "Developed by Arsalan Jamal"
    st.markdown("## Developed by Arsalan Jamal")

    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Choose an option", ["Scientific Calculator", "Plot Graphs"])

    if app_mode == "Scientific Calculator":
        scientific_calculator()
    elif app_mode == "Plot Graphs":
        plot_graph()

if __name__ == "__main__":
    main()

     
