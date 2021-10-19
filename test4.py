import matplotlib.pyplot as plt
import numpy as np

x = np.array([422, 132])
plt.pie(x, labels=['Interested\n' + str(int((x[0]/sum(x)) * 100)) + '%', 'Not Interested\n' + str(int((x[1] / sum(x)) * 100)) + '%'])
plt.legend(['Interested', 'Not Interested'])
plt.title('Students interested in taking up new courses')
plt.show()