#!/usr/bin/env python3

import pandas as pd
import sys

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')
    return df
    


def main():
    cyclists()
if __name__ == "__main__":
    main()
