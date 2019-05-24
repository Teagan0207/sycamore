

Information Extraction for UN Resolutions
===================================
  In current system, only the pdf or word documents are stored in the system.<h1\><br />
  It is hard for managers to query keywords or file in terms of categories. <h1\><br />
  This project aims to solve this problem for the UN resolution system.


1. Metadata with Regular Expression
-----------------------------------
  Since all of the metadata has some specific pattern, RE would be efficient to locate these basic information\<h2\><br />
  This task consists of two parts: fields extraction and basic segementation.<h2\><br />


### 1.1 Metadata for documents
> The sample extracted metadata fields are shown below.
>
> Title and Closing Formula, which are not necessaily metadata, are also included. <h3\><br />

  * Doc Name：N1846596
  <br/>Note*：Doc Name does not need extraction. It is set as index.
  * ID：A/RES/73/277
  * Session: Seventy-third Session
  * Agenda Items：148
  * Proponent Authority：The Fifth Committee
  * Approval Date: 2018-12-22
  * Title
      * Financing of the International Residual Mechanism for Criminal Tribunals
  * Closing Formula
      * 65th plenary meeting
      * 22 December 2018 <h3\><br />

The result is shown as follows:<h3\><br />
![images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/01.png "01")

### 1.2 Paragraph Segmentation
> We extract   `operative, preamble, annex and footnote information`, which would be crucial to content analysis and future extraction.
>
> For example:
  ![2-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/02.png "02")




2. Task-based information extraction
-----------------------------------
  This part consists of document abbreviation, deadlines extraction, references extraction and database filtering.<h2\><br />
  These tasks are based on the first part, and are required with higher precision. <h2\><br />

### 2.1 Document abbreviation
> The abbreviation is only done for   `operative paragraphs`.
>
> The sample output is shown as follows. Words in red belong to   `wrong abbreviations`.
>
> The testing accuracy for this task is  `0.88`
  ![3-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/WeChat%20Image_20190401230504.png "03")

### 2.2 Refences and deadlines
> Here our goal is to find out past resolutions and future dates.
>
> We can make more precise matches thanks to their    `specific formats`.
>
> Sample output:<h3\><br />

    `Refences`:
      >>>b.refence(file)
      ['resolutions 1980/67 1989/84',
      'resolution 69/313',
      'resolutions 53/199 61/185',
      'decision XIII/5',
      'decision 14/30',
      'decision XII/19',
      'resolution 70/1',
      'decision 14/5']

    `Referred resolutions`:
      >>>b.refered_doc(file,df)
      ['N1523222', 'N0650553', 'N1529189']

    `Future Date and Year`:
      >>>b.future_date(file)
      (['8 June 2020', '11 June 2020'], ['2030', '2020', '2019'])
      ###Note that there are two lists returned
      ###Year list is used when only year or year range is mentioned

### 2.3 Word count and word-based filtered database
> These two functions are only exploratory, no need to evaluate.
>
> Only     `nouns and adjectives` are kept for Word count, since they are loaded with more meaning.
>
> Users can      `specify columns` to search keywords,      `case_sensitive` is also supported.]
>
> Sample output:<h3\><br />
#### word-based filtered database
![4-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/03.png "04")
#### word-count
![5-images](https://github.com/Teagan0207/sycamore/blob/master/spacy指北以北/04.png "05")


3. Document classification
-----------------------------------
In this part, the goal is to do classification of the documents based on      `UNBIS`.<h2\><br />
We build algorithm based on      `Bidirectional-LSTM`, relying on preamble, operatives and title.<h2\><br />

> Model and methodology:
>
> > Instead of using pre-trained      `embedding` layer directly, we set up this layer from scratch.
>
> >      `3 LSTMs` are applied parallelly. They are expected to deal with preamble, operatives, title separately.
>
> >      `Dropout` layer added to fight against overfitting.

![6-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/06.png "06")

> Results and evaluation
![7-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/07.png "07")

> Sample predictions
![8-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/08.png "08")

4. Content analysis
-----------------------------------
In this part, we applied LDA topic modeling for subset databases and we also do named entity recognitions. <h2\><br />

### 4.1 LDA topic modeling
> Latent Dirichlet Allocation (LDA) allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.
>
> Users can input all of the database, or subsets of database filtered by       `keywords or categories`.
>
> Sample output: (original HTML)

![9-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/09.png "009")

### 4.2 Named Entity Recognitions





5. Django website
-----------------------------------
In order to visualize our results to the maximum degree, a repository website is established. <h2\><br />
This website is still under construction... <h2\><br />

Current views:
![10-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/10.png "010")
![11-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/11.png "011")
![12-images](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/12.png "012")




Original Code
-----------------------------------
1.[点击这里你可以链接到www.google.com](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/basic.py)<br />
2.[点击这里我你可以链接到我的博客](https://github.com/Teagan0207/sycamore/blob/master/spacy%E6%8C%87%E5%8C%97%E4%BB%A5%E5%8C%97/example.ipynb)<br />
