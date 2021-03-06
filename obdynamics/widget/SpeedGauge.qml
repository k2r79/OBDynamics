import QtQuick 1.0
import ODBWidgets 1.0

Rectangle {
    id: circularGaugeContainer
    width: 220
    height: 320
    color: "transparent"

    MouseArea {
        anchors.fill: parent
        onClicked: {
            speedGauge.value = 100
        }
    }

    CircularGauge {
        id: speedGauge
        objectName: "speedGauge"
        radius: 100
        stroke: 35
        strokeColor: Qt.rgba(0 / 255, 150 / 255, 255 / 255, 0.7)

        value: 0
        maxValue: 200

        anchors.centerIn: parent

        SequentialAnimation {
            running: true
            NumberAnimation {
                target: speedGauge
                properties: "value"
                from: 0
                to: speedGauge.maxValue
                duration: 1000
            }
            NumberAnimation {
                target: speedGauge
                properties: "value"
                from: speedGauge.maxValue
                to: 0
                duration: 750
            }
        }

        Behavior on value {
            NumberAnimation {
                duration: 200
                easing.type: Easing.Linear
            }
        }
    }

    Text {
        text: speedGauge.value

        color: "white"
        font.pixelSize: 30

        anchors.centerIn: parent
    }
}