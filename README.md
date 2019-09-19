# FANCY
Predicting privacy risk of functional genomics data

NOTE data the results in the paper are obtained using the MATLAB version of the code.

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
        
  * In the matlab folder, you can find 
