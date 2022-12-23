import splitfolders

splitfolders.ratio("data", # The location of dataset
                   output="train_data", # The output location
                   seed=42, # The number of seed
                   ratio=(.7, .3), # The ratio of splited dataset
                   group_prefix=None, # If your dataset contains more than one file like ".jpg", ".pdf", etc
                   move=False # If you choose to move, turn this into True
                   )