import QtQuick 1.0
import "./obdynamics/widget"

Rectangle {
    color: "#111111"
    width: 480
    height: 320

    Grid {
        columns: 2
        spacing: 15
        anchors.centerIn: parent

        SpeedGauge {}
        Grid {
            columns: 2
            spacing: 15
            anchors.verticalCenter: parent.verticalCenter

            // 0 to 30 km/h
            Text {
                text: "0 to 30 km/h : "
                color: "white"
                font.pixelSize: 16
            }

            Text {
                id: timeToThirty

                text: "-"

                color: "white"
                font.pixelSize: 16
            }

            // 0 to 60 km/h
            Text {
                text: "0 to 60 km/h : "
                color: "white"
                font.pixelSize: 16
            }

            Text {
                id: timeToSixty

                text: "-"

                color: "white"
                font.pixelSize: 16
            }

            // 0 to 80 km/h
            Text {
                text: "0 to 80 km/h : "
                color: "white"
                font.pixelSize: 16
            }

            Text {
                id: timeToEighty

                text: "-"

                color: "white"
                font.pixelSize: 16
            }

            // 0 to 100 km/h
            Text {
                text: "0 to 100 km/h : "
                color: "white"
                font.pixelSize: 16
            }

            Text {
                id: timeToHundred

                text: "-"

                color: "white"
                font.pixelSize: 16
            }
        }
    }

    function setZeroToThirtyText(newText) {
        timeToThirty.text = newText
    }

    function setZeroToSixtyText(newText) {
        timeToSixty.text = newText
    }

    function setZeroToEightyText(newText) {
        timeToEighty.text = newText
    }

    function setZeroToHundredText(newText) {
        timeToHundred.text = newText
    }
}