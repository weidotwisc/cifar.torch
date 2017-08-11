rm -fr log.std*
(th train.lua --max_epoch 105 --model vgg_bn_drop -s logs/vgg -batchSize 128 --epoch_step 25 --type cuda --backend cudnn > ./log.stdout) &> ./log.stderr
