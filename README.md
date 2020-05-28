# FANCY
Predicting privacy risk of functional genomics data.
Pre-print: https://www.biorxiv.org/content/10.1101/775338v1

<b>NOTE 1: The results in the paper are obtained using the MATLAB version of the code.
  
NOTE 2: If you want to skip the training step and use the already trained model, for FANCY (both in matlab (.mat) and pyhton (.sav) format, go to http://homes.gersteinlab.org/people/gg487/FANCY/. For FANCY_low, go to python or matlab folder.</b>
  
* In the python folder, you can find three python scripts:
  
  The dependencies are pyGPs, which can be easily downloaded following: https://www.cse.wustl.edu/~m.neumann/pyGPs_doc/Install.html
  
 

  (1) <b>training_testing_modeling.py</b> takes the feature files in the data folder and divides it into half for training and test. It will then train a Gaussian Process Learning regression model on the trainign data. It will then predict the outcome of the test features and report the R^2 score for the test data. Finally, it will export the model and save it as "<b>FANCY.sav</b>" The kernel parameters are obtained using the optimization in MATLAB, as optimizing it in Python took a long time.

  (2) <b>training_testing_modeling_low.py</b> does the same operations as (1), but it only uses the data if the number of leaking variants are smaller or equal to 1000. It exports the model as  "<b>FANCY_low.sav</b>"

  (3) <b>FANCY.py</b> is the prediction model. It has several user arguments. Below is an example and explanation of the arguments.
  
    <code>python FANCY.py -regressor FANCY -depth 4.04985000000000 -cov 72274436 -assay ATAC-Seq -std 300.96 -skew 103.01 -kurt 12491.18</code>
    
      (a)-regressor is used to chose the model. FANCY for the full model, FANCY_low for low number of variants.
      
      (b)-depth is the mean depth of the sequencing reads.
      
      (c)-cov is the breadth of the coverage.
      
      (d)-assay is the type of the experiment. Options are: RNA-Seq, ATAC-Seq and CHIP-Seq.
      
      (e)-std is the standard deviation of the depth distribution.
      
      (f)-skew is the skewness of the depth distribution.
      
      (g)-kurt is the kurtosis of the depth distribution.
     
     The correct answer for these inputs are 59,278 leaking SNVs and you should obtain a result similar to
  
        Predicted number of leaking variants are  54678.078125 
        
        Between  10388  and  12575  of them are rare
        
        Risk is  red 
        
* In the matlab folder, you can find the following scripts:

   
   (1) <b>trainRegressionModel.m</b> takes the feature files in the data folder and divides it into half for training and test. It will then train a Gaussian Process Learning regression model on the training data. It will then predict the outcome of the test features and report the R^2 score for the test data. Finally, you can export the model and save it as "<b>FANCY.mat</b>" The kernel parameters are obtained using the Statistics and Machine Learning toolbox in MATLAB. You can also train the regressor by using only the data points that are smaller or equalt to 1000 and save the resulting model as "<b>FANCY_low.mat</b>".
   
   (2) <b> fancy.m </b> is the prediction model function. Below is an example on how to run with an explanation
   
   <code> >> load('FANCY.mat') </code>
   
   <code> >> X=[300.96 103.01 12491.18 4.04985000000000 72274436 0 1 0]; </code>
   
   <code> >> [ypred rare1 rare2 alert]= fancy(X) </code>
     
     In the input X, the first column is the standard deviation, second column is the skewness, third column is the kurtosis, fourth column is the mean depth, sixth column is the coverage and sevent, eight and nineth columns are the one-hot encoding of the assay type. RNA-Seq = [0 0 1], ATAC-Seq=[0 1 0] and CHIP-Seq=[1 0 0]
     
     The correct answer for these inputs are 59,278 leaking SNVs and you should obtain a result similar to

      ypred = 5.2579e+04
      rare1 = 9.9900e+03
      rare2 = 1.2093e+04
      alert = 'red'
      
   (3) <b> fancy_low.m </b> is the prediction model function for the number of SNVs smaller or equal to 1000. Below is an example on how to run:
   
   <code> >> load('FANCY_low.mat') </code>
   
   <code> >> X=[0.0582118199131000,9.30898835798000,170.476230689000,1.28473000000000,1879796,0,1,0]; </code>
   
   <code> >> [ypred rare1 rare2 alert]= fancy_low(X) </code>
     
     In the input X, the first column is the standard deviation, second column is the skewness, third column is the kurtosis, fourth column is the mean depth, sixth column is the coverage and sevent, eight and nineth columns are the one-hot encoding of the assay type. RNA-Seq = [0 0 1], ATAC-Seq=[0 1 0] and CHIP-Seq=[0 0 1]
     
     The correct answer for these inputs are 134 leaking SNVs and you should obtain a result similar to

      ypred = 138.5298
      rare1 = 26.3204
      rare2 = 31.8618
      alert = 'yellow'
  
   (4) <b>trainingANDtest_for_classifier.m</b> uses the sequencing statistics (mean depth, coverage, standard deviation, skewness and kurtosis) as inputs and predicts the assay type using a Random Forest Classifier. It first takes the data and divides it into half for test and training. When you run the code, you should obtain something similar to below:
   
       validationAccuracy = 0.9682
       testAccuracy = 0.9679
       
     validationAccuracy is the accuracy on the training data after 5-fold cross-validation and testAccuracy is the accuracy on the test data.
