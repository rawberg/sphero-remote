"use strict";

function windowReady() {
    var locatorView = Qt.createComponent("locator.qml");
    locatorView.createObject(appViewport);
}

function showMainView() {
    colorChooserBtn.clicked.connect(showColorChooser);
}

function showColorChooser() {
    debugger;
    var colorDialog = Qt.createQmlObject('import QtQuick.Dialogs 1.0; ColorDialog { title: "Pick a Color"; visible: true; }', appWindow, 'colorDialog');
    colorDialog.accepted.connect(function() {
    	colorField.text = String(colorDialog.color);
    	colorField.deselect();
    });
}
