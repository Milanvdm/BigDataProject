Idea for the Experiment

Step 1: Run the MapReduce program with a set of default settings of parameters for result comparison for further steps.
     Output: HadoopOutput-control.txt (Control)
     Notes: 4 parameters could vary - a. ratings weighting factor
                                      b. distance thershold
                                      c. referenced variance
                                      d. deviation multiplier

Step 2: Study the effect on Number of Clusters (NoC) by altering a. ratings weighting factor
    Output: HadoopOutput-varWeighting1.txt (halve the parameter compared to Control)
            HadoopOutput-varWeighting2.txt (double the parameter compared to Control)
            HadoopOutput-varWeighting3.txt (triple the parameter compared to Control)
    Observation: The ratings weighting factor increases, the NoC decreases

Step 3: Study the effect on NoC by removing dimension ratings
    Method: Set the ratings weighting factor to 0 to minimize code change and simulate the removal of ratings
    Output: None
    Observation: Results are too large to be extracted (NoC = 8083) and takes >30 minutes to complete
    
Step 4: Study the effect on NoC by altering b. distance thershold
    Output: HadoopOutput-varDistance1.txt (halve the parameter compared to Control)
            HadoopOutput-varDistance2.txt (double the parameter compared to Control)
            HadoopOutput-varDistance3.txt (triple the parameter compared to Control)
    Observation: The distance thershold increases, the NoC decreases

Step 5: Study the effect on NoC by altering c. referenced variance
    Output: HadoopOutput-varVariance1.txt (slightly adjust the parameter on latitude dimension compared to Control, set it to 2)
            HadoopOutput-varVariance2.txt (slightly adjust the parameter on longitude dimension compared to Control, set it to 2)
            HadoopOutput-varVariance3.txt (slightly adjust the parameter on ratings dimension compared to Control, set it to 2)
            HadoopOutput-varVariance4.txt (slightly adjust the parameter on all dimensions compared to Control, set them all to 2)
            HadoopOutput-varVariance5.txt (increase magnitudes of the parameter on all dimensions compared to Control, set them all to 5)
            HadoopOutput-varVariance6.txt (increase magnitudes of the parameter on all dimensions compared to Control, set them all to 8)
            HadoopOutput-varVariance7.txt (increase magnitudes of the parameter on all dimensions compared to Control, set them all to 10)
            HadoopOutput-varVariance8.txt (increase magnitudes of the parameter on all dimensions compared to Control, set them all to 15)
    Observation: No effect on NoC regardless the change of single dimension or multiple dimensions as long as the referenced variance is adjusted slightly
                 The magnitudes of referenced variance in all dimensions increase, the NoC decreases

Step 6: Study the effect on NoC by altering d. deviation multiplier
    Output: HadoopOutput-varDeviation1.txt (halve the parameter compared to Control)
            HadoopOutput-varDeviation2.txt (double the parameter compared to Control)
            HadoopOutput-varDeviation3.txt (triple the parameter compared to Control)
    Observation: The deviation multiplier increases, the NoC decreases

Step 7: Reduce the NoC based on experiment results from steps 2, 4, 5 and 6
    Output: HadoopOutput-varMultiParameters1.txt
    Results: NoC is reduced from 108 in Control to 42
    
Step 8: Apply the parameters settings in step 7 and rework step 3 to see if the NoC can be greatly reduced
    Method: Apply same parameters setting as in step 7 except ratings weighting factor and the referenced variance on ratings dimension.
            Set both to 0 to minimize code change and simulate the removal of ratings
    Output: None
    Observation: Results are still too large to be extracted (NoC = 7469) and takes >30 minutes to complete

Step 9: Deduce conclusion on the effect of ratings to NoC by combing results from steps 2, 3, 7 and 8
    Conclusion: From steps 2 and 3 -> the ratings weighting factor decreases, the NoC increases non-proportionally
                From steps 3, 7 and 8, NoC cannot be greatly reduced if paramter ratings is excluded 
                    -> paramter ratings plays an important part in clstering, especially when the ratings weighting factor is taken into account
                    
            