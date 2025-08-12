import pandas as pd
from fairlearn.metrics import MetricFrame, selection_rate

# Toggle for testing: True = make it pass, False = make it fail
PASS_MODE = True

if PASS_MODE:
    data = pd.DataFrame({
        'y_true':    [1, 0, 1, 0, 1, 0],
        'y_pred':    [1, 0, 1, 0, 1, 0],  # Equal selection rates
        'group':     ['A', 'A', 'B', 'B', 'A', 'B']
    })
else:
    data = pd.DataFrame({
        'y_true':    [1, 0, 1, 0, 1, 0],
        'y_pred':    [1, 0, 0, 0, 1, 1],  # Biased predictions
        'group':     ['A', 'A', 'B', 'B', 'A', 'B']
    })

mf = MetricFrame(
    metrics=selection_rate,
    y_true=data['y_true'],
    y_pred=data['y_pred'],
    sensitive_features=data['group']
)

print("Selection rate per group:")
print(mf.by_group)

diff = abs(mf.by_group.max() - mf.by_group.min())

if diff > 0.2:
    print(f"❌ Bias check failed! Difference = {diff:.2f}")
    exit(1)
else:
    print(f"✅ Bias check passed! Difference = {diff:.2f}")
