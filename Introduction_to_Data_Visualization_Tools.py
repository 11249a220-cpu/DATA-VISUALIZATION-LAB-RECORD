Experiment No. 1: Introduction to Various Data Visualization Tools

## Aim
To study different tools used for data visualization and check the installed versions of Python libraries commonly used in data handling and graphical presentation.

## Description
Data visualization is a technique of displaying information in a graphical form using charts, diagrams, plots, and dashboards. It makes data easier to understand and helps users recognize relationships, variations, and important patterns.

It is useful in fields such as education, banking, healthcare, marketing, and scientific research. Python offers a variety of libraries for visual representation, whereas applications such as Tableau and Power BI help users prepare interactive reports and business dashboards.

## Applications of Data Visualization
- Converts complicated datasets into understandable visual information.
- Makes it easier to compare data values.
- Reveals changes, relationships, and recurring patterns.
- Communicates analytical results effectively.
- Assists in planning and decision-making.
- Helps evaluate progress and organizational activities.

## Algorithm
1. Begin the program.
2. Import the Matplotlib, Seaborn, Plotly, and Pandas libraries.
3. Access the version attribute of each imported library.
4. Print the library names along with their version details.
5. Observe and check the output.
6. Terminate the program.

## Program

```python
import matplotlib
import seaborn
import plotly
import pandas

print("Matplotlib Version:", matplotlib.__version__)
print("Seaborn Version:", seaborn.__version__)
print("Plotly Version:", plotly.__version__)
print("Pandas Version:", pandas.__version__)
```

## Program Explanation

- **Matplotlib:** Provides functions for generating different types of graphs, including line charts, bar charts, and histograms.
- **Seaborn:** Supports statistical data presentation with a variety of visual styles and plotting options.
- **Plotly:** Enables the creation of interactive visual charts that users can explore.
- **Pandas:** Offers data structures and functions for handling datasets and performing data operations.
- **`__version__`:** Provides information about the version of a library installed in the Python environment.

The program loads four Python libraries and retrieves the version information associated with each one. The output helps confirm which versions are available in the current environment.

## Common Python Visualization Libraries

| Library | Purpose |
|---|---|
| Matplotlib | Produces graphs and conventional data charts. |
| Seaborn | Supports statistical charts and graphical analysis. |
| Plotly | Creates interactive and dynamic visual representations. |
| Pandas | Manages datasets and performs data manipulation. |

## Introduction to Data Analytics Using Python

Data analytics refers to the examination of collected information to identify meaningful results and improve decision-making. Data may originate from student records, commercial activities, medical systems, online platforms, and other sources.

The process usually involves gathering data, correcting errors, transforming information, applying analytical techniques, creating visual representations, and interpreting the findings. Python is an important language in this field because it supports data processing, numerical computation, statistical methods, and graphical analysis.

Data analytics enables organizations to measure results, discover customer behaviour, recognize potential risks, and develop strategies based on evidence.

### Types of Data Analytics

1. **Descriptive Analytics:** Summarizes available data to present information about past events.
2. **Diagnostic Analytics:** Examines data to determine the possible reasons behind an outcome.
3. **Predictive Analytics:** Applies statistical techniques and models to forecast future events.
4. **Prescriptive Analytics:** Suggests suitable decisions or actions based on analytical results.

Each category provides a different perspective on data. Together, they help organizations review previous results, understand challenges, estimate future possibilities, and select appropriate actions.

## Data Measurement Scales

Measurement scales describe how data values are categorized and interpreted. The four main scales are:

- **Nominal Scale:** Groups observations into separate categories without ranking, such as department names or colours.
- **Ordinal Scale:** Arranges categories in a particular sequence, such as beginner, intermediate, and advanced.
- **Interval Scale:** Represents numerical values with consistent differences but without a true zero point, such as temperature in Celsius.
- **Ratio Scale:** Contains numerical values with equal intervals and a genuine zero, such as age, weight, and product quantity.

Selecting the correct measurement scale is important because it influences the statistical calculations and visual techniques suitable for a dataset.

## Data Visualization Tools

A range of software applications and programming libraries can be used to represent and interpret data:

- **Matplotlib:** Provides plotting functions for creating different two-dimensional graphs.
- **Seaborn:** Offers statistical graphics and tools for exploring data distributions.
- **Plotly:** Supports interactive charts that allow users to examine individual data points.
- **Tableau:** Helps users build visual reports and interactive business dashboards.
- **Power BI:** Combines data from different sources to create analytical reports.
- **Google Looker Studio:** Supports the preparation and sharing of visual reports.
- **Microsoft Excel:** Provides spreadsheet-based calculations, charts, and basic analytical features.
- **Jupyter Notebook:** Allows code, explanatory text, analysis, and graphical results to be presented together.

The appropriate tool can be selected according to the amount of data, the complexity of the analysis, the required visual features, and the needs of the audience.

## Major Areas of Data Analytics

Data analytics includes several techniques that help transform raw information into useful knowledge:

- **Statistics:** Uses numerical methods to summarize information and examine data relationships.
- **Data Mining:** Searches datasets for significant patterns and associations.
- **Business Intelligence:** Uses reports and analytical summaries to support business activities.
- **Data Visualization:** Communicates data findings through graphical elements.
- **Simulation:** Models possible situations to understand potential results.
- **Modelling and Optimization:** Develops representations of problems and identifies effective solutions.
- **What-if Analysis:** Evaluates how changes in assumptions or input values influence results.

### Basic Predictive Analytics Workflow

Historical Data → Predictive Algorithm → Trained Model

New Data → Trained Model → Predicted Outcome

In predictive analytics, a model is developed using previously collected observations. After training, the model processes new inputs to generate estimates or forecasts. Testing the model with suitable evaluation methods helps determine its accuracy and usefulness.

## Role of Data Professionals

A **data analyst** works with datasets to identify trends, prepare reports, and present findings through charts and dashboards. A **data scientist** may work on more advanced tasks, including predictive modelling, statistical experimentation, and machine learning.

Both professionals use data interpretation, technical knowledge, critical thinking, and communication skills to solve problems and support decisions.

## Sample Output

```text
Matplotlib Version: [installed version]
Seaborn Version: [installed version]
Plotly Version: [installed version]
Pandas Version: [installed version]
```

Note: The displayed version values will vary depending on the Python environment and the versions of the libraries installed.

## Result

The experiment demonstrates how to import four commonly used Python libraries and obtain their installed version details. It also provides an overview of visualization software, data analytics techniques, measurement scales, and the applications of analytical methods.

Hence, data visualization and analytics tools help transform raw information into meaningful results that can be interpreted and communicated effectively.
