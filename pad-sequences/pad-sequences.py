import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len = max((len(seq) for seq in seqs),default=0)
    if not seqs:
        return np.empty((0,max_len),dtype=int)
    result =[]

    for seq in seqs:
        truncated = list(seq[:max_len])
        padded=truncated+[pad_value]*(max_len-len(truncated))
        result.append(padded)

    return np.array(result,dtype=int)