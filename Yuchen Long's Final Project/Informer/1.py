import numpy as np
setting = 'informer_ETT_ftMS_sl120_ll90_pl30_dm256_nh8_el2_dl1_df2048_atprob_fc5_ebtimeF_dtTrue_mxTrue_test_0'
preds = np.load(r'C:\Users\Administrator\Desktop\Informer2020-main\results\informer_custom_ftMS_sl96_ll48_pl24_dm512_nh8_el2_dl1_df2048_atprob_fc5_ebtimeF_dtTrue_mxTrue_test_1\real_prediction.npy')
print(preds .shape)