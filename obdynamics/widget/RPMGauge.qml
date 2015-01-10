import QtQuick 1.0
import ODBWidgets 1.0

Rectangle {
    width: 500
    height: 500
    color: "transparent"

    MouseArea {
        anchors.fill: parent
        onClicked: {
            circularGauge.value = 100
        }
    }

    CircularGauge {
        id: circularGauge
        radius: 200
        stroke: 60
        strokeColor: Qt.rgba(0 / 255, 150 / 255, 255 / 255, 0.7)

        value: 0
        maxValue: 100

        anchors.centerIn: parent

        NumberAnimation {
            id: testGauge
            target: circularGauge
            properties: "value"
            from: circularGauge.value
            to: 100
            duration: 4000
            easing.type: Easing.Linear
        }

        Behavior on value {
            NumberAnimation {
                duration: 200
                easing.type: Easing.Linear
            }
        }
    }

    Text {
        text: circularGauge.value

        color: "white"
        font.pixelSize: 30

        anchors.centerIn: parent
    }
}