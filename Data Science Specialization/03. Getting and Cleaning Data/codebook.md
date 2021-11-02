# Codebook
This codebook explains the information contained in the `tidy_dataset.txt` file contained in this repository. See the README.md file for background information on this data set.  

The dataset contains the mean value of each of the **mean** and **standard deviation** measurements for each subject in each one of the recorded activities.

## Identifiers
- **Subject**: identification number for each one of the subjects.
- **Activity**: represents the activity that the subject was performing when the measurement was recorded. There are six different activities, declared with their descriptive name:  
  - Walking
  - Walking upstairs
  - Walking downstairs
  - Sitting
  - Standing
  - Laying  

## Variables (measurements)
There are 86 different variables in the data set. Each one has a descriptive name.  

From the codebook of the original data, we see that:  

>The features selected for this database come from the accelerometer and gyroscope 3-axial raw signals tAcc-XYZ and tGyro-XYZ. These time domain signals (prefix 't' to denote time) were captured at a constant rate of 50 Hz. Then they were filtered using a median filter and a 3rd order low pass Butterworth filter with a corner frequency of 20 Hz to remove noise. Similarly, the acceleration signal was then separated into body and gravity acceleration signals (tBodyAcc-XYZ and tGravityAcc-XYZ) using another low pass Butterworth filter with a corner frequency of 0.3 Hz.  
Subsequently, the body linear acceleration and angular velocity were derived in time to obtain Jerk signals (tBodyAccJerk-XYZ and tBodyGyroJerk-XYZ). Also the magnitude of these three-dimensional signals were calculated using the Euclidean norm (tBodyAccMag, tGravityAccMag, tBodyAccJerkMag, tBodyGyroMag, tBodyGyroJerkMag).  
Finally a Fast Fourier Transform (FFT) was applied to some of these signals producing fBodyAcc-XYZ, fBodyAccJerk-XYZ, fBodyGyro-XYZ, fBodyAccJerkMag, fBodyGyroMag, fBodyGyroJerkMag. (Note the 'f' to indicate frequency domain signals).  
These signals were used to estimate variables of the feature vector for each pattern:  
'-XYZ' is used to denote 3-axial signals in the X, Y and Z directions.  

In this data set, I got the mean value for each one of the selected measures for each subject in each one of the activities; for each of the variables in the _time domain_ there's a **mean** value and a **standard deviation** value whereas in the _frequency value_ there's a **mean** value, a **standard deviation** value and a **mean frequency** value. I gave a descriptive name to each one of the variables (these transformations were made using the `gsub` command). The variables in the data set are the following:  

- **In the time domain**
- From the accelerometer (measures were taken in three axis: *Y*, *Y* and *Z*, so there's one value for each one.)
  - Body measures
    - `TimeDomainBodyAccelerometer-Mean-X`                                  
    - `TimeDomainBodyAccelerometer-Mean-Y`                                  
    - `TimeDomainBodyAccelerometer-Mean-Z`                                  
    - `TimeDomainBodyAccelerometer-StandardDeviation-X`                     
    - `TimeDomainBodyAccelerometer-StandardDeviation-Y`                     
    - `TimeDomainBodyAccelerometer-StandardDeviation-Z`     
  - Gravity measures
    - `TimeDomainGravityAccelerometer-Mean-X`                               
    - `TimeDomainGravityAccelerometer-Mean-Y`                               
    - `TimeDomainGravityAccelerometer-Mean-Z`                               
    - `TimeDomainGravityAccelerometer-StandardDeviation-X`                  
    - `TimeDomainGravityAccelerometer-StandardDeviation-Y`                  
    - `TimeDomainGravityAccelerometer-StandardDeviation-Z`
  - Body Jerk
    - `TimeDomainBodyAccelerometerJerk-Mean-X`                              
    - `TimeDomainBodyAccelerometerJerk-Mean-Y`                              
    - `TimeDomainBodyAccelerometerJerk-Mean-Z`                              
    - `TimeDomainBodyAccelerometerJerk-StandardDeviation-X`                 
    - `TimeDomainBodyAccelerometerJerk-StandardDeviation-Y`                 
    - `TimeDomainBodyAccelerometerJerk-StandardDeviation-Z`
- From the gyroscope
  - Body measures
    - `TimeDomainBodyGyroscope-Mean-X`                                      
    - `TimeDomainBodyGyroscope-Mean-Y`                                      
    - `TimeDomainBodyGyroscope-Mean-Z`                                      
    - `TimeDomainBodyGyroscope-StandardDeviation-X`                         
    - `TimeDomainBodyGyroscope-StandardDeviation-Y`                         
    - `TimeDomainBodyGyroscope-StandardDeviation-Z`     
  - Gyroscope Jerk
    - `TimeDomainBodyGyroscopeJerk-Mean-X`                                  
    - `TimeDomainBodyGyroscopeJerk-Mean-Y`                                  
    - `TimeDomainBodyGyroscopeJerk-Mean-Z`                                  
    - `TimeDomainBodyGyroscopeJerk-StandardDeviation-X`                     
    - `TimeDomainBodyGyroscopeJerk-StandardDeviation-Y`                     
    - `TimeDomainBodyGyroscopeJerk-StandardDeviation-Z`
- Magnitudes
  - Body accelerometer magnitude
    - `TimeDomainBodyAccelerometerMagnitude-Mean`                           
    - `TimeDomainBodyAccelerometerMagnitude-StandardDeviation`
  - Gravity accelerometer magnitude
    - `TimeDomainGravityAccelerometerMagnitude-Mean`                        
    - `TimeDomainGravityAccelerometerMagnitude-StandardDeviation`
  - Body accelerometer jerk magnitude
    - `TimeDomainBodyAccelerometerJerkMagnitude-Mean`                       
    - `TimeDomainBodyAccelerometerJerkMagnitude-StandardDeviation`
  - Body gyroscope magnitude
    - `TimeDomainBodyGyroscopeMagnitude-Mean`                               
    - `TimeDomainBodyGyroscopeMagnitude-StandardDeviation`
  - Body gyroscope jerk magnitude
    - `TimeDomainBodyGyroscopeJerkMagnitude-Mean`                           
    - `TimeDomainBodyGyroscopeJerkMagnitude-StandardDeviation`  

- **In the frecuency domain**
- From the accelerometer
  - Body measures
    - `FrequencyDomainBodyAccelerometer-Mean-X`                        
    - `FrequencyDomainBodyAccelerometer-Mean-Y`                        
    - `FrequencyDomainBodyAccelerometer-Mean-Z`                        
    - `FrequencyDomainBodyAccelerometer-StandardDeviation-X`           
    - `FrequencyDomainBodyAccelerometer-StandardDeviation-Y`           
    - `FrequencyDomainBodyAccelerometer-StandardDeviation-Z`           
    - `FrequencyDomainBodyAccelerometer-MeanFrequency-X`               
    - `FrequencyDomainBodyAccelerometer-MeanFrequency-Y`               
    - `FrequencyDomainBodyAccelerometer-MeanFrequency-Z`   
  - Body jerk
    - `FrequencyDomainBodyAccelerometerJerk-Mean-X`                    
    - `FrequencyDomainBodyAccelerometerJerk-Mean-Y`                    
    - `FrequencyDomainBodyAccelerometerJerk-Mean-Z`                    
    - `FrequencyDomainBodyAccelerometerJerk-StandardDeviation-X`       
    - `FrequencyDomainBodyAccelerometerJerk-StandardDeviation-Y`       
    - `FrequencyDomainBodyAccelerometerJerk-StandardDeviation-Z`       
    - `FrequencyDomainBodyAccelerometerJerk-MeanFrequency-X`           
    - `FrequencyDomainBodyAccelerometerJerk-MeanFrequency-Y`           
    - `FrequencyDomainBodyAccelerometerJerk-MeanFrequency-Z`  
- From the gyroscope
  - Body measures  
    - `FrequencyDomainBodyGyroscope-Mean-X`                            
    - `FrequencyDomainBodyGyroscope-Mean-Y`                            
    - `FrequencyDomainBodyGyroscope-Mean-Z`                            
    - `FrequencyDomainBodyGyroscope-StandardDeviation-X`               
    - `FrequencyDomainBodyGyroscope-StandardDeviation-Y`               
    - `FrequencyDomainBodyGyroscope-StandardDeviation-Z`               
    - `FrequencyDomainBodyGyroscope-MeanFrequency-X`                   
    - `FrequencyDomainBodyGyroscope-MeanFrequency-Y`                   
    - `FrequencyDomainBodyGyroscope-MeanFrequency-Z`  
- Magnitudes
  - Body accelerometer magnitude
    - `FrequencyDomainBodyAccelerometerMagnitude-Mean`                 
    - `FrequencyDomainBodyAccelerometerMagnitude-StandardDeviation`    
    - `FrequencyDomainBodyAccelerometerMagnitude-MeanFrequency`   
  - Body accelerometer jerk magnitude
    - `FrequencyDomainBodyAccelerometerJerkMagnitude-Mean`             
    - `FrequencyDomainBodyAccelerometerJerkMagnitude-StandardDeviation`
    - `FrequencyDomainBodyAccelerometerJerkMagnitude-MeanFrequency`    
  - Body gyroscope magnitude
    - `FrequencyDomainBodyGyroscopeMagnitude-Mean`                     
    - `FrequencyDomainBodyGyroscopeMagnitude-StandardDeviation`        
    - `FrequencyDomainBodyGyroscopeMagnitude-MeanFrequency`     
  - Body gyroscope jerk magnitude
    - `FrequencyDomainBodyGyroscopeJerkMagnitude-Mean`                 
    - `FrequencyDomainBodyGyroscopeJerkMagnitude-StandardDeviation`    
    - `FrequencyDomainBodyGyroscopeJerkMagnitude-MeanFrequency`  

- **Additional vectors** obtained by averaging the signals in a signal window sample. These are used on the **angle** variable
    - `angletBodyAccelerometerMean,gravity`                                 
    - `angletBodyAccelerometerJerkMean,gravityMean`                         
    - `angletBodyGyroscopeMean,gravityMean`                                 
    - `angletBodyGyroscopeJerkMean,gravityMean`                             
    - `angleX,gravityMean`                                                  
    - `angleY,gravityMean`                                                  
    - `angleZ,gravityMean`
