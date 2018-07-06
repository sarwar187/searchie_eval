import numpy as np

def cosine_similarity(qrm_dembed):
    qrm,d_embed = qrm_dembed
    #print('qrm shape ' + tf.shape(qrm) + '\t' + tf.shape(d_embed.shape))
    q_squared = np.square(qrm)
    q_norm_summed = np.sum(q_squared, axis=1)
    q_norm = np.sqrt(q_norm_summed)
    d_squared = np.square(d_embed)
    d_norm_summed = np.sum(d_squared, axis=1)
    d_norm = np.sqrt(d_norm_summed)
    norm = np.multiply(q_norm, d_norm)
    element_wise_product = np.multiply(qrm, d_embed)
    dot_product = np.sum(element_wise_product, axis=1)
    out_temp = np.divide(dot_product, norm)
    return out_temp

a = [[1,2],[3,4]]
b = [[1,2],[1,2]]

print (cosine_similarity([a,b]))