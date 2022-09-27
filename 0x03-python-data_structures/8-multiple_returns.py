#!/usr/bin/python3
def multiple_returns(sentence):
    """return tuple with the length of a string & its first character"""
    if len(sentence) == 0:
        return(len(sentence), None)
    return (len(sentence), sentence[0])
