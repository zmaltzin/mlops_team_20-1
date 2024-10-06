# Acoustic Features Dataset Description

**File:** Acoustic Features.csv  
**Size:** 168.3 KB

## Class Labels
- Relax
- Happy
- Sad
- Angry


| Variable Name                                                      | Role     | Type       | Description | Units | Missing Values |
|--------------------------------------------------------------------|----------|------------|-------------|-------|----------------|
| Class                                                              | Target   | Categorical|             |       | no             |
| _RMSenergy_Mean                                                   | Feature  | Continuous |             |       | no             |
| _Lowenergy_Mean                                                   | Feature  | Continuous |             |       | no             |
| _Fluctuation_Mean                                                 | Feature  | Continuous |             |       | no             |
| _Tempo_Mean                                                       | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_1                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_2                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_3                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_4                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_5                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_6                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_7                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_8                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_9                                                      | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_10                                                     | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_11                                                     | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_12                                                     | Feature  | Continuous |             |       | no             |
| _MFCC_Mean_13                                                     | Feature  | Continuous |             |       | no             |
| _Roughness_Mean                                                   | Feature  | Continuous |             |       | no             |
| _Roughness_Slope                                                  | Feature  | Continuous |             |       | no             |
| _Zero-crossingrate_Mean                                           | Feature  | Continuous |             |       | no             |
| _AttackTime_Mean                                                  | Feature  | Continuous |             |       | no             |
| _AttackTime_Slope                                                 | Feature  | Continuous |             |       | no             |
| _Rolloff_Mean                                                     | Feature  | Continuous |             |       | no             |
| _Eventdensity_Mean                                                | Feature  | Continuous |             |       | no             |
| _Pulseclarity_Mean                                                | Feature  | Continuous |             |       | no             |
| _Brightness_Mean                                                  | Feature  | Continuous |             |       | no             |
| _Spectralcentroid_Mean                                           | Feature  | Continuous |             |       | no             |
| _Spectralspread_Mean                                             | Feature  | Continuous |             |       | no             |
| _Spectralskewness_Mean                                           | Feature  | Continuous |             |       | no             |
| _Spectralkurtosis_Mean                                           | Feature  | Continuous |             |       | no             |
| _Spectralflatness_Mean                                           | Feature  | Continuous |             |       | no             |
| _EntropyofSpectrum_Mean                                          | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_1                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_2                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_3                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_4                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_5                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_6                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_7                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_8                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_9                                               | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_10                                              | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_11                                              | Feature  | Continuous |             |       | no             |
| _Chromagram_Mean_12                                              | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_Mean                            | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_Std                             | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_Slope                           | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_PeriodFreq                     | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_PeriodAmp                      | Feature  | Continuous |             |       | no             |
| _HarmonicChangeDetectionFunction_PeriodEntropy                   | Feature  | Continuous |             |       | no             |

## Additional Variable Information
Features such as Mel Frequency Cepstral Coefficients (MFCCs), Tempo, Chromagram, Spectral and Harmonic features have been extracted to analyze the emotional content in music signals. MIR toolbox is used for feature extraction.