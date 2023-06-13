#!/usr/bin/python3
def multiple_returns(results):
    if results == "":
        return (0, None)
    return (len(results), results[0])
