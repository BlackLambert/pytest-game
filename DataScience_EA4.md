```python
import numpy
import pandas
import sys

#setup
columnNames = ["Country", "People", "Area", "BIP", "Currency"]
url = 'https://raw.githubusercontent.com/edlich/eternalrepo/master/DS-WAHLFACH/countries.csv'
frame = pandas.read_csv(filepath_or_buffer=url, dtype=object, names=columnNames)
frame = frame.drop(0)
frame = frame.reset_index(drop=True)
print(frame)
```

        Country     People     Area   BIP Currency
    0   Germany   82521653   357385  3466      EUR
    1     Japan  126045000   377835  4938      YEN
    2    Canada   36503097  9984670  1529      CAD
    3     Italy   60501718   301338  1850      EUR
    4  Brazilia  208360000  8515770  1798     REAL
    


```python
#General information
print("Rows count: {0}".format(frame.shape[0]))
print("Columns count: {0}".format(frame.shape[1]))
```

    Rows count: 5
    Columns count: 5
    


```python
#People data analysis
numPeopleColumn = pandas.to_numeric(frame[columnNames[1]])
print("The average people count {0}".format(numPeopleColumn.mean()))
print("The sum of people in these countries is: {0}".format(numPeopleColumn.sum()))
indexOfMax = numPeopleColumn.argmax()
print("The country with most people ({0}) is {1}".format(numPeopleColumn[indexOfMax], frame[columnNames[0]][indexOfMax]))
```

    The average people count 102786293.6
    The sum of people in these countries is: 513931468
    The country with most people (208360000) is Brazilia
    


```python
#Area data analysis
numAreaColumn = pandas.to_numeric(frame[columnNames[2]])
print("The average area is: {0}".format(numAreaColumn.mean()))
print("The whole area of all countries is: {0}".format(numAreaColumn.sum()))
indexOfMax = numAreaColumn.argmax()
print("The largest country ({0}) is {1}".format(numAreaColumn[indexOfMax], frame[columnNames[0]][indexOfMax]))
```

    The average area is: 3907399.6
    The whole area of all countries is: 19536998
    The largest country (9984670) is Canada
    


```python
#BIP data analysis
numBIPColumn = pandas.to_numeric(frame[columnNames[3]])
print("The average area is: {0}".format(numBIPColumn.mean()))
indexOfMax = numBIPColumn.argmax()
print("The wealthiest country ({0}) is {1}".format(numBIPColumn[indexOfMax], frame[columnNames[0]][indexOfMax]))
```

    The average area is: 2716.2
    The wealthiest country (4938) is Japan
    


```python
#Last 4 rows
count = frame.shape[0]
frame.iloc[count-4:count]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rows of countries using Euro

filteredFrame = frame.where(frame[columnNames[4]] == "EUR", other="")
filteredFrame = filteredFrame.loc[filteredFrame[columnNames[0]]!= ""]
filteredFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rows of countries using Euro (only name and currency column)
filteredFrame[[columnNames[0], columnNames[4]]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>EUR</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rows of countries with BIP > 2000
filteredFrame = frame.where(numBIPRow > 2000, other="")
filteredFrame = filteredFrame.loc[filteredFrame[columnNames[0]]!= ""]
filteredFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Rows of countries with inhabitants between 50 and 150 Mio.
filter = (numPeopleColumn > 50000000) & (numPeopleColumn < 150000000)
filteredFrame = frame.where(filter, other="")
filteredFrame = filteredFrame.loc[filteredFrame[columnNames[0]]!= ""]
filteredFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>BIP</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Renaming BIP column
frame.rename(columns={columnNames[3]:'Bip'}, inplace=True)
np_columnNames = numpy.array(columnNames)
columnNames = numpy.where(np_columnNames==columnNames[3], "Bip", np_columnNames) 
frame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Bip sum
print("The sum of bip in these countries is: {0} Billion".format(numBIPColumn.sum()))
```

    The sum of bip in these countries is: 13581 Billion
    


```python
#Average people count: see first cell
#Sort alphabetically
frame.sort_values(columnNames[0])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>8515770</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>9984670</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>357385</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>301338</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>377835</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Replacing area cells with BIG or SMALL
areaReplaced = numAreaColumn.where(numAreaColumn > 1000000, "BIG").where(numAreaColumn < 1000000, "SMALL")
frame.assign(Area=areaReplaced)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>People</th>
      <th>Area</th>
      <th>Bip</th>
      <th>Currency</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Germany</td>
      <td>82521653</td>
      <td>BIG</td>
      <td>3466</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Japan</td>
      <td>126045000</td>
      <td>BIG</td>
      <td>4938</td>
      <td>YEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Canada</td>
      <td>36503097</td>
      <td>SMALL</td>
      <td>1529</td>
      <td>CAD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Italy</td>
      <td>60501718</td>
      <td>BIG</td>
      <td>1850</td>
      <td>EUR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brazilia</td>
      <td>208360000</td>
      <td>SMALL</td>
      <td>1798</td>
      <td>REAL</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
