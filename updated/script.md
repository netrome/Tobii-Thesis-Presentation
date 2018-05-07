# Data augmentation with Deep Generative Models
- Introduce myself / Thank Alex for beautiful introduction
- Warn people about abscence of direct business value
- Mention that this is a high-level presentation and will not go into technical details

# Outline
...

# Generative modelling
- Emphasize that it is from a probabilistic perspective.
- Contrast with discriminative models.

# Why do we care about generative modelling
- The listed points is just what I came up with from the top of my head. There are probably a lot more reasons.

--> Generative models have historically had a hard time scaling to complex problems and big data. However recently an interesting class of generative models have emerged that challenges this view.

# Deep Generative Models
- Are a class of generative models based on recent deep learning developments.
- Especially two deep generative models have been gaining a lot of attention lately, namely VAEs and GANs.

# VAEs
Add example applications (?)

# GANs
Add example applications (?)

# GANs in practice
...

# Data Augmentation
- So that was a short introduction to the core concepts I have been working with. Let's specify the problem we're considering. As the title says, I have been focusing on utilizing deep generative models for data augmentation.
--> The question I have been working on is

# The question
...
--> The main reason for formulating this question is that we have baked in the quantitative measure of usefulness. What is the benefit of this?

# Measuring the usability of the data
...

# Evaluation by classification
...
- As previously mentioned this procedure is already baked in to the research question.
--> However there is a fundamental problem with this formulation.

# Generating annotated data
...
...
...

# Experiments and results
- Now we know the format of the question and problem, let's see how it worked out in practice.

# Experiments
...
--> The different models were constructed using the same network architecture for the corresponding neural networks. I'll briefly outline the most important architectures for you to get an idea of what the models consists of.

# Network architectures
... Do these quite fast, don't get hung up on the details
- The generator and discriminator are both built up in several stages, corresponding to each other.
- This is a common architectural style and allows progressive training, which have resulted in the best GANs as of today.
--> but

# Progressive GAN failed on our data
... Show timelapse
--> With the progressive GAN out of the picture, let's take a look at the qualitative results of the other models.

# The rest of the qualitative results
... walk through and talk about stuff. (mode collapse, variance)

# Quantitative results
... Explain that they correspond to what we've just said.

# Toy experiments
- Highlight that the AEGAN beat all baselines.

# Concluding remarks
- This work have not provided any direct business value, however it has layed the groundwork for further research within the field and provided an example of a good qualitative measure for GANs. I've also shown that although the methods are complicated they can improve existing models.

# Questions?

# Thank you
