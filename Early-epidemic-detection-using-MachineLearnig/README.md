# Early-Epidemic-Detection
Early epidemic detection or surveillance system consists of a well-found database from which to draw data and to which to write the inference and relations for the analysis to happen.
Using CDA or Case Detection Algorithms, using a critical number for the hard boundary for any disease frequency counter. 
For Example, If influenza records 110 cases in a week, and the critical value for that remains at 100 then that particular region is at the start of an epidemic which doesn't fit good. For that purpose, the hard boundary is considered off with a flexibility factor which determines the condition for a hard boundary.
 
## Technologies used
- [Neo4j](https://neo4j.com/)
- [MetaMap](https://metamap.nlm.nih.gov/)
- [Naivechain](https://lhartikk.github.io/) Framework for the early Adoption of recoed creation
- [Python v3.6](https://www.python.org/downloads/release/python-360/)
- [Django](https://www.djangoproject.com/)

**NOTE** Please note thatfor optimal performance the user's to obtain a unified medical language system(*UMLS*) licesnce , since *UMLS* Metathesaurus is used as one of the knowledge source.

## Concept
The current problem persist that patients' data is highly non-trasferable under the security consensus. The biggest challenge that is being faced by health care systems throughout the world is how to share medical data with known and unknown stakeholders for various purposes while ensuring data integrity and protection patient privacy. Although data standards are better than ever, each electronic medical record (EMR) stores data using different workflows, so it is not obvious who recorded what, and when and hence Creating a trusted environment for decision-making is a challenge for medical fraternity. 
The use of [Naivechain](https://lhartikk.github.io/) provides a hassle free block creation and integrity maintaning blockchain without the features of mining.
Each hospital or health care centre works as a node adding blocks to the chain with user's timestamp and signature for authenticity of the system. Each block consists of each electronic medical records.
#### The Later part
consists of an analysis of the medical records data in a graph database to create inferences among entities. 
**MetaMap** utilizes a local database to map biomedical text to the [UMLS](https://www.nlm.nih.gov/research/umls/) Metathesaurus or, equivalently, to discover Metathesaurus concepts referred to in the text. MetaMap uses a knowledge-intensive approach based on symbolic, natural-language processing (NLP) and computational-linguistic techniques. Besides being applied for both IR and data-mining applications, MetaMap is one of the foundations of [NLM](https://ii.nlm.nih.gov/MTI/)'s Medical Text Indexer (MTI) which is being used for both semiautomatic and fully automatic indexing of biomedical literature at NLM.
#### Inference Engine
The process includes stop-words removing lemmatization, tagging and mapping it to specific entities. The graph database, here **Neo4j** uses graph database to create inferences. The results are shown and drawn  to the web interfaces created with *Django*.
## Workflow
![](https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/cc.png)

## Results
#### The Blockchain creation
 
![](https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/BlockChain_create.gif)

#### Database Handling and Prediction
[Video](https://drive.google.com/file/d/19bOmiqjlj3f9pvfv2Q6e6h-Igfpibjpl/preview)

#### Database
**Common Districts in Udaipur**:
![](https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/a.png)

**Common disease for Age greater than 60 for all District**:
![](https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/b.png)

**Top Disease, Age, Gender**
![](https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/c.png)


#### Experience
Running the following files with any javascript enabled browser will yield in the experience of the database

-  	[resultX_graph-422.html](http://htmlpreview.github.io/?https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/resultX_graph-422.html)
-  	[resultY_graph-422.html](http://htmlpreview.github.io/?https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/resultY_graph-422.html)
-  	[resultz_graph-422.html](http://htmlpreview.github.io/?https://github.com/saradindusengupta/Rajasthan_Hackathon/blob/master/sample/resultZ_graph-422.html)

 




