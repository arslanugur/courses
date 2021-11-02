########## Description ##########
# This script is for creating a tidy data set with some of the information provided in the "UCI HAR Dataset".
# It:
# 1. Retives the data from the web
# 2. Reads the data into R
# 3. Merges the training and the test sets to create one data set.
# 4. Extracts only the measurements on the mean and standard deviation for each measurement.
# 5. Uses descriptive activity names to name the activities in the data set
# 6. Appropriately labels the data set with descriptive variable names.
# 7. From the data set in step 4, creates a second, independent tidy data set with the average of each variable for each activity and each subject.
################################### 

##### Required libraries #####
if(!require(dplyr)) {
        install.packages("dplyr")
}
library(dplyr)

if (!require(data.table)){
        install.packages("data.table")
}
library(data.table)

##### 1. Getting the data from the web #####
path <- getwd() # After setting the working directory as the directory where the files will be downloaded

folder <- "UCI HAR Dataset"
if(!file.exists(folder)) {
        url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fprojectfiles%2FUCI%20HAR%20Dataset.zip" 
        download.file(url, file.path(path, "dataFiles.zip"))
        unzip(zipfile = "dataFiles.zip")        
}


##### 2.  Reading data #####

## Activity labels and features
activity_labels <- fread(file.path(path, "UCI HAR Dataset/activity_labels.txt"), 
        col.names = c("Label", "Activity")) # Reads activities
features <- fread(file.path(path, "UCI HAR Dataset/features.txt"), 
        col.names = c("Index", "Feature")) # Reads features 
features$Feature <- gsub('[()]', '', features$Feature) # Remove parenthesis from the feature name 

## Training data set
train_data <- fread(file.path(path, "UCI HAR Dataset/train/X_train.txt"), 
        col.names = c(features$Feature)) # Train data
train_activities <- fread(file.path(path, "UCI HAR Dataset/train/y_train.txt"), 
        col.names = c("Activity")) # Activity code
train_subjects <- fread(file.path(path, "UCI HAR Dataset/train/subject_train.txt"), 
        col.names = c("Subject")) # Subject code

train <- cbind(train_subjects, train_activities, train_data) # Merges all the training information

## Test data set
test_data <- fread(file.path(path, "UCI HAR Dataset/test/X_test.txt"), 
        col.names = c(features$Feature)) # Test data
test_activities <- fread(file.path(path, "UCI HAR Dataset/test/y_test.txt"), 
        col.names = c("Activity")) # Activity code
test_subjects <- fread(file.path(path, "UCI HAR Dataset/test/subject_test.txt"), 
        col.names = c("Subject")) # Subject code

test <- cbind(test_subjects, test_activities, test_data) # Merges all the testing information

##### 3. Merging the training and the test sets #####
complete_set <- rbind(test, train)


##### 4. Extracting only the measurement on the mean and standard deviation for each measurement #####
# Select which columns to keep based on column name
keep_columns <- grepl("Subject|Activity|[Mm]ean|std", colnames(complete_set))

# Subset only the columns of interest
complete_set <- complete_set[, ..keep_columns]


##### 5.  Using descriptive activity names to name the activities in the data set #####
# Changes the numeric code to the activity description
complete_set$Activity <- factor(complete_set$Activity, 
         levels = activity_labels[, Label], labels = activity_labels[, Activity])


##### 7. Labeling the data set with decriptive variable names #####
# Get column names
complete_set_names <- colnames(complete_set)

# Expand abbreviations and clean up names
complete_set_names <- gsub("Freq", "Frequency", complete_set_names)
complete_set_names <- gsub("^f", "FrequencyDomain", complete_set_names)
complete_set_names <- gsub("^t", "TimeDomain", complete_set_names)
complete_set_names <- gsub("Acc", "Accelerometer", complete_set_names)
complete_set_names <- gsub("Gyro", "Gyroscope", complete_set_names)
complete_set_names <- gsub("Mag", "Magnitude", complete_set_names)
complete_set_names <- gsub("mean", "Mean", complete_set_names)
complete_set_names <- gsub("std", "StandardDeviation", complete_set_names)

# Correct typo
complete_set_names <- gsub("BodyBody", "Body", complete_set_names)

# Rename data frame columns
colnames(complete_set) <- complete_set_names

##### 8. Creating an independent tidy dataset with the average of each variable for each activity and each subject #####
tidy_dataset <- complete_set %>%
        group_by(Subject, Activity) %>%
        summarize_all(funs(mean))

write.table(tidy_dataset, file = "tidy_dataset.txt", quote = FALSE, row.names = FALSE)
