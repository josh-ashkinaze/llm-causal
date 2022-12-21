# Predicting Causal Effects of Text with Large Language Models 

Autoregressive language models, such as GPT-3, work by predicting a word given a sequence. I.e: P(W|X), where X is some prior sequence. When we think about the causal effect of information -- e.g: how reading Fox News may affect one's likelihood of believing a claim -- we are thinking about a similar conditional probability: `P(Claim|Information=1) - P(Claim|Information=0)`. 

Can we use language models to estimate the causal effect of information? That is, we can think about the likely affect of a headline on believing a claim as `P(EndorseClaim|Headline=1) - P(EndorseClaim|Headline=0).` 

Concretely, I use a list of headlines from various political sources as prompts to GPT-3. After prompting GPT-3 with these headlines, I ask GPT-3 various political questions (such as support for climate change policy etc). I then measure to what extent different news sources make the endorsement of subsequent claims more or less likely. 

To get headlines from news sources, I use: https://newscatcherapi.com/
