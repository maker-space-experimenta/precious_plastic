import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11
import QtQuick.Controls.Material 2.12
import QtMultimedia 5.15

ApplicationWindow {

    id: window
    visible: true
    visibility: "FullScreen"

    Material.theme: Material.Dark
    Material.accent: Material.Purple

    Rectangle { 
        id: 'background'
        anchors.fill: parent
        color: "#0d141f"; 

        Rectangle {
            id: 'menu'
            anchors.left: parent.left
            anchors.top: parent.top
            color: '#141f30'
            width: parent.width
            height: 150

            Rectangle {
                id: 'button_color_select_black'
                anchors.top: parent.top
                anchors.topMargin: 25
                anchors.left: parent.left
                anchors.leftMargin: 25
                color: '#000000'
                width: 100
                height: 100

                Text {
                    anchors.centerIn: parent
                    text: "SCHWARZ"
                    color: '#ffffff'
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        print("color is black")
                    }
                }
            }

            Rectangle {
                id: 'button_color_select_white'
                anchors.top: parent.top
                anchors.topMargin: 25
                anchors.left: parent.left
                anchors.leftMargin: 25 + (1 * 125)
                color: '#FFFFFF'
                width: 100
                height: 100

                Text {
                    anchors.centerIn: parent
                    text: "WEIS"
                    color: '#000000'
                }
            }

            Rectangle {
                id: 'button_color_select_red'
                anchors.top: parent.top
                anchors.topMargin: 25
                anchors.left: parent.left
                anchors.leftMargin: 25 + (2 * 125) 
                color: '#FF0000'
                width: 100
                height: 100

                Text {
                    anchors.centerIn: parent
                    text: "ROT"
                    color: '#ffffff'
                }
            }

            Rectangle {
                id: 'button_color_select_green'
                anchors.top: parent.top
                anchors.topMargin: 25
                anchors.left: parent.left
                anchors.leftMargin: 25 + (3 * 125) 
                color: '#00FF00'
                width: 100
                height: 100

                Text {
                    anchors.centerIn: parent
                    text: "GRÜN"
                    color: '#ffffff'
                }
            }

            Rectangle {
                id: 'button_color_select_blue'
                anchors.top: parent.top
                anchors.topMargin: 25
                anchors.left: parent.left
                anchors.leftMargin: 25 + (4 * 125) 
                color: '#0000FF'
                width: 100
                height: 100

                Text {
                    anchors.centerIn: parent
                    text: "BLAU"
                    color: '#ffffff'
                }
            }





            Rectangle {
                id: "menu_bottom_border"
                anchors.left: parent.left
                anchors.top: parent.bottom
                color: '#3f5f91'
                width: parent.width
                height: 2
            }
        }
        

        Rectangle {
            id: 'content_area'
            anchors.left: parent.left
            anchors.bottom: parent.bottom
            color: '#0d141f'
            width: parent.width
            height: parent.height - 152

            Image { 
                id: "cv_image"
                source: "image://cvimage/test.jpg"
                anchors.fill: parent
                cache: false
            }

            // MediaPlayer {
            //     id: player
            //     source: "file://video.webm"
            //     autoPlay: true
            //     // anchors.fill: parent

            // }

            // VideoOutput {
            //     id: videoOutput
            //     source: player
            //     anchors.fill: parent
            // }
        }
    }


}