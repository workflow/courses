from subprocess import call
call(["ls", "-l"])

def setup_standard_dir_structure():
    %cd $DATA_HOME_DIR
    %mkdir validation
    %mkdir results
    # Moving all test images to a class directory of 'unknown', to more easily work with batches
    %mkdir test/unknown
    %mkdir -p sample/train
    %mkdir -p sample/test
    %mkdir -p sample/validation
    %mkdir -p sample/results
