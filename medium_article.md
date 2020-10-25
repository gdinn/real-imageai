>> Você quer colocar um pouco dos códigos no meio do texto? Ou só texto corrido mesmo? 

# Computer Vision zero to hero: A tutorial about coin recognition
Computer vision is interesting, huh? Have you seen the demos of Pulse [1] or NVIDIA Maxine [2]?  
However, it's common when there are no pre-trained models for your task, no benchmark datasets, no easy to follow tutorials, and you don't have a whole team to develop wonderful machine learning models. #review  
How to achieve, in a very short time and with little prior knowledge, acceptable results that may serve as proof of concept?  
In this tutorial you'll learn this process end to end, following a practical example about coin recognition  

----

## Reducing the scope
Our objective is simple: to indentify brazilian coins. 
Well... not that simple: there are 4 different types of coin, that can be rusted or in bad condition, which may be partially ocluded in the photo, the scenes can vary greatly in illumination, among other challanges.
So we decided to reduce the scope of the project to the bare minimum, the simplest feature that could demonstrate that the idea could work: to identify one type of coin (the one of 1 brazilian real, as shown in Figure 1), under normal indoor lighting, in clear and "easy" photographs.

[[Figure 1]]

## Choosing the technologies
Do not reinvent the wheel  
Easy to understand, with acceptable results, with good documentation and tutorials  
You may change it in the future when faced with constraints like computational performance or easiness to deploy, but now the focus is just to prove that your project can be done
>> Por quê você escolheu a imageai? Você vei alguma comparação legal com outras bibliotecas (performance, flexibilidade, facilidade de aprendizado, etc)? 

## Labeling a dataset
You already defined your scope, now: what type of data you need to represent the information you need?  
In our case will be enough to have photos of several coins on the table and on our hand, taken with cellphone camera (today's cellphone have nice cameras to do 
tasks like this), with bounding boxes around the one of 1 real (1BRL). 

We decided to annotate 250 images, but it was just a guess: you may need more, you may need less, you may have to label more data after trying to train the model and not achieving good enough results, it depends.  
We'll use this data to train our model, but how we'll know how well it will be when faced with new data, in a real situation?  
We may want to label more data in the future and compare the model's predictions with our own labels. It's a good idea, but why not label this "test dataset" just now? Even better, why not just hold out part of the already labeled dataset, excluding it from training and using it only for testing?  
Word of advice: The labelling proccess is very long and trust me, this needs to be done right. So take your time, put some music on and do this with attention.  

## Training a model
You don't want, now, to spend much time training or to pay a small fortune in cloud computing. Furthermore, you don't want to perform a careful fine-tuning in the model, you just need an acceptable precision (that, for most problems, is much lower than the state of the art)

We'll use a famous architecture, YoloV3, pretrained on a famous dataset, ImageNet. This will speed up the training and make it easier to get good results, that is exactly what we want. Comparing with this [example](https://imageai.readthedocs.io/en/latest/customdetection/) of the ImageAI library, they've used 400 epochs in a dataset of 300 images, taking 300s per epoch. In our case, we used 30 epochs with 3000s each. WHY? Because our images were HUGE, and the higher the resolution the higher will be the training time. Lesson learned: use images as clear as you can get and with a resolution that capture all the details you need, but NOT MORE than that.
>>>> Cuidado: eles demoraram 300s/epoch em um computador diferente do teu, talvez a comparação não seja válida. A lição aprendida é boa, mas talvez a comparação direta seja enganosa

## Reporting and communicating
If your model can save time or help someone to do its job, it already worth the effort. Your model doesn't need human-level precision to be useful.
Be clear, explain your metric, understand what was done (this is not an extensive tutorial in theoretical background, but we highly recommend you to go deeper and understand what was done), show that there is still a lot of room for improvement and this was just an initial result

# References
[1] - Pulse, http://pulse.cs.duke.edu/
[2] - NVIDIA Maxine, https://blogs.nvidia.com/blog/2020/10/05/gan-video-conferencing-maxine/
