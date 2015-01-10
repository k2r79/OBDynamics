from PySide.QtCore import Property, Signal, QRectF, QAbstractAnimation, Slot, QPropertyAnimation
from PySide.QtDeclarative import QDeclarativeItem
from PySide.QtGui import QColor, QPen, QBrush, QGraphicsItem, QPainter


class CircularGauge(QDeclarativeItem):
    radiusChanged = Signal()
    strokeChanged = Signal()
    strokeColorChanged = Signal()
    valueChanged = Signal()
    maxValueChanged = Signal()

    def __init__(self, parent=None):
        QDeclarativeItem.__init__(self, parent)
        self.setFlag(QGraphicsItem.ItemHasNoContents, False)

        self._radius = 0
        self.radiusChanged.connect(self.update)

        self._stroke = 0
        self.strokeChanged.connect(self.update)

        self._strokeColor = QColor(0, 0, 0)
        self.strokeColorChanged.connect(self.update)

        self._value = 0
        self.valueChanged.connect(self.update)

        self._maxValue = 100
        self.maxValueChanged.connect(self.update)

    def paint(self, painter, options, widget):
        pen = QPen(self._strokeColor)
        pen.setWidth(self._stroke)

        brush = QBrush(self._strokeColor)

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.setRenderHints(QPainter.Antialiasing, True)

        value_angle = float(self._value) / float(self._maxValue) * -270
        stroke_radius = self._stroke / 2
        painter.drawArc(self.boundingRect().x() + stroke_radius, self.boundingRect().y() + stroke_radius,
                        self.boundingRect().width() - self._stroke, self.boundingRect().height() - self._stroke,
                        -90 * 16, value_angle * 16)

    def boundingRect(self, *args, **kwargs):
        return QRectF(-self._radius, -self._radius, self._radius * 2, self._radius * 2)

    def getRadius(self):
        return self._radius

    def setRadius(self, radius):
        self._radius = radius

    def getStroke(self):
        return self._stroke

    def setStroke(self, stroke):
        self._stroke = stroke

    def getStrokeColor(self):
        return self._strokeColor

    def setStrokeColor(self, strokeColor):
        self._strokeColor = strokeColor

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value
        self.valueChanged.emit()

    def setValueWithAnimation(self, value):
        if self._value == value:
            pass

        animation = QPropertyAnimation(self, "value", self)
        animation.setStartValue(self._value)
        animation.setEndValue(value)
        animation.setDuration(200)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def getMaxValue(self):
        return self._maxValue

    def setMaxValue(self, maxValue):
        self._maxValue = maxValue

    radius = Property(int, getRadius, setRadius, notify=radiusChanged)
    stroke = Property(int, getStroke, setStroke, notify=strokeChanged)
    strokeColor = Property(QColor, getStrokeColor, setStrokeColor, notify=strokeColorChanged)
    value = Property(int, getValue, setValue, notify=valueChanged)
    maxValue = Property(int, getMaxValue, setMaxValue, notify=maxValueChanged)