def transformation_engine(data, *funcations):
    for func in funcations:
        data = func(data)
    return data

## This funcation applies each transformation in sequence using the power of *args.
