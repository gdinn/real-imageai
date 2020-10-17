# Computer Vision zero to hero: A tutorial about coin recognition
Computer vision is interesting, huh? Have you seen the demos of x, y, and z?
However, it's common when there are no pre-trained models, no benchmark datasets, no easy to follow tutorials, and you don't have a whole team to develop wonderful machine learning models.
How to achieve, in a very short time and with little prior knowledge, acceptable results that may serve as proof of concept? 
In this tutorial you'll learn this process end to end, following a practical example about coin recognition

----

## Reducing the scope
4 coin to 1 
Easy lighting 
Small occlusion 

## Choosing the technologies
Do not reinvent the wheel
Easy to understand, with acceptable results, with good documentation and tutorials
You may change it in the future when faced with constraints like computational performance or easiness to deploy, but now the focus is just to prove that your project can be done

## Labeling a dataset
You already defined your scope, now: what type of data you need to represent the information you need?
In our case will be enough to have photos of several coins on the table and on our hand, with bounding boxes around the one of 1 real, under normal indoor lighting. We decided to annotate 250 images, but it was just a guess: you may need more, you may need less, you may have to label more data after trying to train the model and not achieving good enough results, it depends. 
We'll use this data to train our model, but how we'll know how well it will be when faced with new data, in a real situation? 
We may want to label more data in the future and compare the model's predictions with our own labels. It's a good idea, but why not label this "test dataset" just now? Even better, why not just hold out part of the already labeled dataset, excluding it from training and using it only for testing?

## Training a model
You don't want, now, to spend much time training or to pay a small fortune in cloud computing. Furthermore, you don't want to perform a careful fine-tuning in the model, you just need an acceptable precision (that, for most problems, is much lower than the state of the art)

## Reporting and communicating
If your model can save time or help someone to do its job, it already worth the effort. Your model doesn't need human-level precision to be useful.
Be clear, explain your metric, understand what was done (this is not an extensive tutorial in theoretical background, but we highly recommend you to go deeper and understand what was done), show that there is still a lot of room for improvement and this was just an initial result