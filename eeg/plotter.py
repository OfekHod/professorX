import matplotlib.pyplot as plt


def plot(dataArray):
    fig, ax = plt.subplots()
    xar = []
    lowGamma = []
    highGamma = []
    highAlpha = []
    delta = []
    highBeta = []
    lowAlpha = []
    lowBeta = []
    theta = []
    for eachLine in dataArray:
        x = float(eachLine['time'])
        xar.append(int(x))
        lowGamma.append(int(eachLine['lowGamma']))
        highGamma.append(int(eachLine['highGamma']) + 1000)
        highAlpha.append(int(eachLine['highAlpha']) + 1000)
        delta.append(int(eachLine['delta']) + 1000)
        highBeta.append(int(eachLine['highBeta']) + 1000)
        lowAlpha.append(int(eachLine['lowAlpha']) + 1000)
        lowBeta.append(int(eachLine['lowBeta']) + 1000)
        theta.append(int(eachLine['theta']) + 1000)

    ax.plot(xar, lowGamma)
    ax.plot(xar, highGamma)
    ax.plot(xar, highAlpha)
    ax.plot(xar, delta)
    ax.plot(xar, highBeta)
    ax.plot(xar, lowAlpha)
    ax.plot(xar, lowBeta)
    ax.plot(xar, theta)
    ax.set_title("My EEG")

    plt.show()
