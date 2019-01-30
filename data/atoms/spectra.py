import pandas as pd


def make_spectrum():
    """Make an artificial spectrum using the lines from NIST
    """
    # Load the list of peaks
    df = pd.read_csv('persistent_lines.csv')

    print(df.head())


if __name__ == "__main__":
    make_spectrum()
