# Project 2 – Exploratory Analysis & NLP

Uses the cleaned dataset to perform exploratory analysis and natural language processing on bestseller descriptions. I hoped to answer the central question: What can I and other aspiring novelists learn from the patterns of the NYT bestseller market?

## Notebooks
### `exploratory_da.ipynb`
- Category and author trends
- Rank distributions
- Weeks-on-list analysis
- Publisher patterns

#### EDA Insight Summary:
1. The bestseller market is extremely top-heavy. Most books last only a week on the list; a small minority dominate for months.
2. Author reputation is an important factor. A handful of recurring, commercially established authors account for a large share of placements. Building a brand over time is impactful for making it onto the list.
3. Publisher strength influences outcomes. Big houses like Little, Brown produce high longevity books and the largest number of unique bestsellers.
4. Books can perform well even without being commercial. Several high-lifespan titles are literary or award-winning, indicating that book quality and acclaim can counterbalance market dominance by commercial authors.
5. Fall is the peak release and competition season. Most new bestsellers break onto the list in September and October. Aspiring writers should understand both the advantages and challenges of launching in Q4.

### `nlp_analysis.ipynb`
- Text cleaning + lemmatization
- Word frequency + wordcloud
- TF–IDF features
- Topic modeling (LDA)
- Sentiment analysis (VADER)

#### Example Visualizations:
![](/images/common_bigrams_barplot.png)
![](/images/top_books_weeks_on_list_filtered.png)
![](/images/top_tf_idf_terms.png)
![](/images/average_sentiment_by_topic.png)

#### NLP Analysis Insights:
1. The NYT bestseller list is dominated by series fiction. Topic 1 (series-driven books) has the longest average lifespan on the list, likely due to loyal fanbases, consistent releases, and strong author branding. These books hit lower rankings on average but maintain weeks of stable performance.
2. Strong female-led narratives are common in the modern bestseller. Words such as woman, mother, sister, daughter appear at  high rates, indicating a market shaped by stories about women and for women, echoing purchasing demographics.
3. The most common themes reflect domestic suspense, trauma, family, and identity. Topics 2 and 5, which revolve around missing persons, family conflict, generational secrets, and emotional trauma, are the most common topics overall.
4. Negative sentiment is common on the NYT bestseller list. Every topic cluster shows negative sentiment, indicating that narratives with dark themes are popular across bestselling books.