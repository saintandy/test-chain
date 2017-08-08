import {UI} from "UI";
import {StyleSheet, styleRule} from "UI";

export class IndexPageStyle extends StyleSheet {
    @styleRule
    container = {
        height: "100%",
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
    };

    @styleRule
    indexPage = {
        height: "600px",
        width: "500px",
        maxHeight: "100%",
        maxWidth: "100%",

        backgroundColor: "#eee",
    };

    @styleRule
    header = {
        height: "100px",
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        fontSize: "34px",
    };

    @styleRule
    body = {
    };
}