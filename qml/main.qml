import QtQuick 2.1
import QtQuick.Layouts 1.0
import QtQuick.Controls 1.0

RowLayout {
    spacing: 10
    x: 40
    y: 50
    TextField {
        id: colorField
        implicitWidth: 74
    }
    Button {
        id: colorChooserBtn
        text: "color"
        objectName: "pushBtn"
    }
}
