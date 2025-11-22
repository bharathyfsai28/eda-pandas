### Install package manager UV

    For mac/linux, run command -     curl -LsSf https://astral.sh/uv/install.sh | sh


###  BootStrap Project using UV

    uv init pandas-demo

    uv venv pandas_demo

    source pandas_demo/bin/activate

    uv pip install pandas


### Pandas Dataframe

    Creating Dataframes

    From Dictionary

        data = {

            "Name" : ["Poovalingam", "Saroja"],
            "Age" : [71,70],
            "Score" : [98,98]

            }

        df = pd.DataFrame(data)



    From List

        emp_list = [

        ["Poovalingam", "Saroja"],
        [71,70],
        [98,98]

        ];

        df = pd.DataFrame(emp_list)


    From files