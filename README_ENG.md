# Subjective evaluation experiment on the readability of text areas in a scene image

## Purpose
Today, images are widely used for communication due to the spread of smartphones and social networking services (SNS).

However, because images are large, they must be compressed when used for communication.

When compressing images, it is necessary to maintain the quality of text areas that are considered important in the image.

However, an objective evaluation of the readability of text is not sufficient.

Therefore, we would like to request a subjective evaluation of the quality of the text area in the image.

We understand that you are busy, but we would appreciate your cooperation.

There are 150 text images. It should take about 15 minutes to complete the evaluation.

## Repository contents
By copying this repository, you can use python to display images while entering scores on the terminal.

## Preparing the program
It is recommended to run the image display locally. The program runs in python3.

First, you can put this repository locally by executing the following command.

```
$ git clone https://github.com/gasakiii/subquestions2.git
```

Next, move to the copied directory (subquestions2) and build the environment.

```
$ cd subquestions2
```

For miniconda, use the following command to create a new environment and install the necessary packages (numpy, matplotlib, pillow, opencv).

If you already have an environment with the required packages, you can skip the following commands.

```
$ conda create --name gasakiii2 python==3.7
$ conda activate gasakiii2
$ pip install -r requirements.txt
```

## Experimental Methods
When you are ready, you can start the evaluation experiment by executing the following command. You must enter the **specified id** as the first argument.

The id is specified in the thread of the corresponding message in slack.

```
$ python main.py {id}
```

When executed, an image with the specified text area surrounded by a red frame and the following text on the terminal will be displayed.

<p align="center">
  <img width="196" height="128" src="https://github.com/gasakiii/subquestions2/blob/main/imgs/Ino_area_1_0.png">
</p>
<!-- ![temp](https://github.com/gasakiii/subquestions/blob/main/temp_img/85_1_1.png "サンプル") -->

```
+--------------------------------------------------
| image  1 / 150
+--------------------------------------------------
| 5点 ： 全て問題なく読める
| 4点 ： 概ね読めるが、一部読みづらい文字がある
| 3点 ： 一部読めない文字がある
| 2点 ： 大半が読めない
| 1点 ： 全く読めない
+--------------------------------------------------
Put your score >> 
```

```
image  1 / 150
```

This section shows the current progress.

Determine and enter a readability score for the text area image displayed, according to the score given.

Enter a score of 1-5 and press Enter to move on to the next text area image.


## How to Submit

Once you have answered all images, a "result_{id}.txt" file will be generated in the directory.

Send this to the following link.

https://www.dropbox.com/request/rIWq2KDb8yV8hnrJfW62

You have submitted your files and your survey is now closed! Thank you for your cooperation!!!


## Optional: Delete the created environment

If you wish to delete the environment you have just created, you can do so by executing the following command.

```
$ conda deactivate gasakiii2
$ conda remove -n gasakiii2 --all
```

If you cannot deactivate, please restart the terminal once and then delete the environment (execute the second line above).

Thank you in advance.