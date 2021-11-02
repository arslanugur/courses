# *Getting and Cleaning Data* Course Project
This repository contains the files that correspond to the Course Project for the *Getting and Cleaning Data* course on Coursera. It contains the following files:  

- `run_analysis.R`: this is the R script that does all the modifications in the data and creates the tidy data set. The script does the following:  
  1. Gets the data from the web
  2. Gets the data into R
  3. Merges the training and the test sets to create one data set.
  4. Extracts only the measurements on the mean and standard deviation for each measurement.
  5. Uses descriptive activity names to name the activities in the data set
  6. Appropriately labels the data set with descriptive variable names.
  7. From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.
- `CodeBook.md` : indicates the variables and summaries calculated, explaining what is contained in the `tidy_dataset.txt` file.
- `tidy_dataset.txt`: is the tidy dataset containing the mean value of each of the **mean** and **standard deviation** measurements for each subject in each one of the recorded activities.  

## Project description
One of the most exciting areas in all of data science right now is wearable computing. Companies like Fitbit, Nike, and Jawbone Up are racing to develop the most advanced algorithms to attract new users. The data linked to from the course website represent data collected from the accelerometers from the Samsung Galaxy S smartphone. A full description is available at the [site](http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones) where the data was obtained. This data is part of the "Human Activity Recognition Using Smartphones Data Set".    

[Here are the data for the project](https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip)  

## Data set information
The following information comes from the "Human Activity Recognition Using Smartphones Data Set" website.  

> The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. Each person performed six activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. The experiments have been video-recorded to label the data manually. The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data.  
The sensor signals (accelerometer and gyroscope) were pre-processed by applying noise filters and then sampled in fixed-width sliding windows of 2.56 sec and 50% overlap (128 readings/window). The sensor acceleration signal, which has gravitational and body motion components, was separated using a Butterworth low-pass filter into body acceleration and gravity. The gravitational force is assumed to have only low frequency components, therefore a filter with 0.3 Hz cutoff frequency was used. From each window, a vector of features was obtained by calculating variables from the time and frequency domain.
