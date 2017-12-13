## dropout
Dropout is often used to deal with the overfitting problem during the machine learning.
Here is a simple example to show the effection

In the code,we dropout 50% data judging by this code:`sess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:0.5})`.
If you want to keep all the data to train, you should change above code to `sess.run(train_step,feed_dict={xs:X_train,ys:y_train,keep_prob:1})`

## show in tensorboard

run:
```bash
tensorboard --logdir logs1_keep_0.5
```


## Result
When `keep_prob = 1`
![_config.yml](https://github.com/lym0302/tensorflow_learning/blob/master/dropout/keep_0.5.png)

When `keep_prob = 0.5`
![_config.yml](https://github.com/lym0302/tensorflow_learning/blob/master/dropout/keep_1.png)
