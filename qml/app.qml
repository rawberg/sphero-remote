import "app.js" as App
import QtQuick 2.1
import QtQuick.Dialogs 1.0
import QtQuick.Controls 1.0
import QtQuick.Controls.Styles 1.0
import QtQuick.Layouts 1.0
import QtQuick.Window 2.0

ApplicationWindow {
    visible: true
    id: appWindow
    width: 600
    height: 500
    title: "Sphero Controller"

    Item {
        id: appViewport
        width: appWindow.width
        height: appWindow.height
    }

    statusBar: StatusBar {
        RowLayout {
            Label {
                id: statusBarLabel
                text: ""
            }
        }
    }

    Component.onCompleted: App.windowReady()
}
