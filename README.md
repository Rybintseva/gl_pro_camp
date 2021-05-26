# Workflow

1. Checkout to master branch

    ```
    git checkout master
    ```

2. Get latest code from master

    ```
    git pull origin master
    ```

3. Create feature branch for your code

    ```
    git checkout -b <descriptive_feature_name>
    ```

    Where:
    `<descriptive_feature_name>` - human-readable name of new feature (allowed symbols - `[a-zA-Z0-9\-]`)


4. Commit your code to this new feature branch

    ```
    git commit -m "<descriptive_feature_name>"
    ```

    Where:
    `<descriptive_feature_name>` - human-readable name of new feature or descriptive change name


5. Push to repository

    ```
    git push origin <feature_branch_name>
    ```

    Where:

    `<feature_branch_name>` - name of your new feature branch created in item 3


6. Create merge request to dev branch on GitLab.