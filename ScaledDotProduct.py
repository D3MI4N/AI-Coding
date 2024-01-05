import torch
import numpy as np

import torch
import numpy as np

def scaled_dot_product_attention(Q, K, V):
    """
    Computes the scaled dot product attention using PyTorch.

    The function calculates the attention scores for a query set Q against a set of keys K, and then applies these scores to a set of values V.

    Attention(Q,K,V)=softmax((QK^T)/ sqrt(d_k)) * V

    Args:
    Q: Query tensor of shape [batch_size, seq_len, feature_dim]
    K: Key tensor of shape [batch_size, seq_len, feature_dim]
    V: Value tensor of shape [batch_size, seq_len, feature_dim]

    Returns:
    Tuple of:
    - attention_output: The output after applying the attention mechanism, shape [batch_size, seq_len, feature_dim].
    - attention_weights: The attention weights, shape [batch_size, seq_len, seq_len].
    """

    # 1. Calculate the dot product between Q and the transpose of K.
    # Transpose K from [batch_size, seq_len, feature_dim] to [batch_size, feature_dim, seq_len].
    # This aligns the feature dimensions of Q and K for the dot product.
    matmul_QK = torch.matmul(Q, K.transpose(-2, -1))

    # 2. Scale the dot products by the square root of the feature dimension of K.
    # This helps stabilize gradients, as larger feature dimensions could lead to large values in the softmax.
    d_K = K.shape[-1]  # Feature dimension of K
    scaled_attention_logits = matmul_QK / np.sqrt(d_K)

    # 3. Apply softmax to the scaled dot products to obtain attention weights.
    # Softmax is applied over the last axis (seq_len) of scaled_attention_logits.
    # This results in a distribution over the sequence, indicating the relevance of each element.
    attention_weights = torch.softmax(scaled_attention_logits, dim=-1)

    # 4. Multiply the attention weights with V to get the final output.
    # This operation applies the calculated attention to the value tensor V.
    attention_output = torch.matmul(attention_weights, V)

    return attention_output, attention_weights


def test_scaled_dot_product_attention():
    # Example usage
    Q= torch.tensor([[[[1, 2, 3], [4, 5, 6]]]])
    K = torch.tensor([[[[7, 8, 9], [10, 11, 12]]]])
    V = torch.tensor([[[[0.1, 0.2], [0.3, 0.4]]]])

    attention_output, attention_weights = scaled_dot_product_attention(Q, K, V)
    print("Attention Output:")
    print(attention_output)
    print("Attention Weights:")
    print(attention_weights)


if __name__ == "__main__":
    test_scaled_dot_product_attention()



def test_dimensionality():

    # Define the dimensions
    batch_size = 2
    seq_len = 3
    feature_dim = 4

    # Randomly initialize Q, K, V matrices
    Q = np.random.rand(batch_size, seq_len, feature_dim)
    K = np.random.rand(batch_size, seq_len, feature_dim)
    V = np.random.rand(batch_size, seq_len, feature_dim)

    # Accessing the last axis (feature_dim)
    d_k = K.shape[-1]

    print("Shape of Q:", Q.shape)  # (2, 3, 4)
    print("Shape of K:", K.shape)  # (2, 3, 4)
    print("Shape of V:", V.shape)  # (2, 3, 4)
    print("Dimensionality of the key vectors (d_k):", d_k)  # 4


if __name__ == "__main__":
    test_dimensionality()
    #test_scaled_dot_product_attention()
    #test_scaled_dot_product_attention_numpy_easy()





