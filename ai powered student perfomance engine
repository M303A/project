import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem
import pyqtgraph as pg

# Sample student data
data = {
    'Subject': ['Math', 'History', 'Physics', 'Chemistry', 'Biology', 'English', 'Geography'],
    'Score': [85, 78, 82, 80, 83, 87, 81]
}
df = pd.DataFrame(data)
avg_score = df['Score'].mean()
below_avg = df[df['Score'] < avg_score]

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Performance Dashboard')
        self.resize(700, 500)
        layout = QVBoxLayout()

        # Summary
        summary = QLabel(f"<b>Average Score:</b> {avg_score:.2f}   <b>Subjects Below Avg:</b> {', '.join(below_avg['Subject'])}")
        layout.addWidget(summary)

        # Table
        table = QTableWidget(df.shape[0], df.shape[1])
        table.setHorizontalHeaderLabels(df.columns)
        for i, row in df.iterrows():
            for j, val in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(val)))
        layout.addWidget(table)

        # Plot
        plot_widget = pg.PlotWidget(title="Scores by Subject")
        plot_widget.plot(list(range(len(df))), df['Score'], pen=pg.mkPen('b', width=2), symbol='o')
        plot_widget.getPlotItem().getAxis('bottom').setTicks([list(enumerate(df['Subject']))])
        layout.addWidget(plot_widget)

        # Central widget
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dash = Dashboard()
    dash.show()
    sys.exit(app.exec_())
