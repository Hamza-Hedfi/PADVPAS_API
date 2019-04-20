# Description

This is an implementation in python for a method to detect vocal pathologies in the arabic speech.

The method is fully described in this paper [Probabilistic Approach for Detection of Vocal Pathologies in the Arabic Speech](https://www.researchgate.net/publication/274832247_Probabilistic_Approach_for_Detection_of_Vocal_Pathologies_in_the_Arabic_Speech).

It's implemented as a REST API.

The API expose one endpoint `/classification` [**POST**]

It accepts 
```` json
{
    "speech": "ARARBIC SPEECH"
}
````
and returns
```` json
{
    "classification": "CLASSIFICATION"
}
````

The returned CLASSIFICATION result:

- Healthy

    OR

- Pathological

#####This project is part of my guratduation project. This is not the full picture.