# SafeInNet

[Get Lat-Long](https://www.latlong.net/convert-address-to-lat-long.html)

# SafeInNet

## Introduction
We present to you SafeInNet, a dynamic social network to help women determine the safest roads and prevent their journey from being full of despair. We are a community of users who support each other and make sure all of us feel safe and can live without fear. Utilizing intent analysis and location mapping, we provide a modern solution to women's safety!

Our features include a map of all the streets in the country and reviews by our users of how safe/unsafe they've felt on that particular street. A safety score is provided, alongside reviews by fellow users; the app displays a map of the area, allowing users to better visualize important landmarks near them. The street-level utility is configured by inferential analysis of user sentiments/intents about a particular road/street. We integrate machine learning based-analysis for generating these particular scores. At the same time, we understand that having information about a location may not be enough; therefore, we provide an in-house SOS mechanism, which utilizes the Twilio API for sending messages to users near and around your location, alerting them of your predicament and bringing aid for you!

We also have a personified form application named Asha whose name represents hope in Sanskrit - The hope that all women are safe here and are supported by other members of the community. Asha helps a user register an incident. It records the description, location, time of incident. For users who are willing to share their names for more authenticity, we provide a name column however, it is not a requirement. We understand it's hard coming forward and thus, anonymization of names is also an option.

## Inspiration

In a world, where women are trying their best to compete and come forward in their respective fields, trying to push mountains, already having a ton of problems to face at work, their night commute should be the least of their concerns. The fear of whether or not they are safe at night, should not be looming over their heads. 

As a woman,  I am taught to be leery of unknown men. I have grown up reading about brutal crimes against women and this constant fear that something like that could happen to me troubles not only me but my family as well. The fear of violence is as profound as violence itself and it narrows our lives in so many ways. We forgo a nighttime event because we don't want to travel home alone afterwards. We forgo an evening jog because running at night is a luxury only men possess. We forgo a comment or an outfit or a friendship because it might imply an invitation we don't wish to convey. 

Profound newspapers like the Guardian and Washington Post have reported that one in five women never go out by themselves at night. And the women who do go out are less likely to travel solo. 

But even after following precautions, the solution isn’t to close walls on the women of your family and never let them leave their homes at night. There are situations that force us to walk and confront the monsters at night. Thus a lot of women plan their lives and routes home according to where they believe they’ll be safest. Thus, we came up with the idea of SafeInNet.

## Impact

Women’s safety is one of the largest social issues enveloping our community. Not localized to any place, these heinous acts run rampant around the world. Safety is the lack of fear, and when venturing into unknown territories, this fear is at its highest, therefore an application that formalizes locational information with respect to street safety is much needed. Not only is our application giving a sense of security by aggregating safety measures against the multitude of our userbase, but also allows the users to register documentable complaints. Our introduction of Asha, an application for registration and download of incident reports allows information retention, which may even be used by local administrative authorities for further analysis and action.

Some primary impacts we’d like to highlight:
Improving on current security standards by benchmarking and recording street safety.
Giving users an in-house SOS emergency alert system, giving near-by members a chance to be there on time.
Giving administrative bodies detailed incident reports, allowing them to make changes to unsafe localities.

## What it does

SafeInNet is a dynamic social network application, which extracts, documents, inferences and reports security metrics of different streets used by its members. The application uses Streamlit for full-stack deployment, and is attuned with an easy to navigate user interface.

We provide the following primary functions through our application:

Women’s Safety Score
The model uses sentiment analysis backed by a pre-processing and text2vectorization pipeline coupled with decision-based machine learning application. The inference analyzed is then combined with local-ratings by computing the weighted average between their score and the geometric mean of the geographical score of the area. This provides our metric score a foundation by the user comments as well as their ratings.

Incident Reporting System
The system uses Streamlit to deploy Asha, a personified form application for incident recording. The application utilizes Streamlit Form container for formalizing reports.

SOS Alert System
Taking into account the objective of our project, an in-house SOS system integrated with Twilio has been developed. The application inferring locational data of other members of the community, sends an alert message to users involved. This will ensure fast action, by other members even in remote/difficult-to-reach locations.

## How we built it

We used Streamlit for creating our application. While building we utilized the concept of abstraction and inheritance to create a simple to understand infrastructure for our product. Streamlit is one of the few untapped tools for python enthusiasts that allows one to quickly build highly interactive web applications around their data, machine learning models, and pretty much anything.
We used vector-based sentiment analysis models and the concept of weighted averaging metric standardization for generating a safety score for a given location. The two combined provided a backdrop for safety and security of our users. These models became the backbone of our product.

## Challenges we ran into

The integration of machine learning models with application and choosing one which gave a good utility-performance tradeoff was difficult. As we came to understand that larger models may not be scalable. We solved the aforementioned issue when we realized that vector-based transformations, if coupled with decision-based models, give satisfactory results. Thereby, we analyzed models like Naive Bayes, SVM, Decision Trees, and finally Random Forest which gave an Accuracy 0.93, giving us a foundation to fall in-trust with our sentiment model. For this training backdrop we required a complaint based dataset, which was furnished with the “Twitter US Airline Sentiment” Dataset sourced from Kaggle.

## Accomplishments that we're proud of

Built a social network, which uses locational link analysis for dynamic processing of user-data to guide security standards of local streets.
Built and deployed an inference model on women’s safety on roads with a Accuracy of 93%.
Created a form based application platform for incident reporting and downloading.

## What we learned

Some of the key take-aways from developing this project underline our newfound love for developing for a supportive community. We learnt a lot about social-media spaces, on-the-edge sentiment analysis, and crowdsourced retrieval systems.

## What's next for SafeInNet

We hope to make the application available on native mobile devices. As well as integrate live location tracking through it!
