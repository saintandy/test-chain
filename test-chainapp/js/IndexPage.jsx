import {
    UI,
    registerStyle,
} from "UI";
import {IndexPageStyle} from "./IndexPageStyle";


@registerStyle(IndexPageStyle)
export class IndexPage extends UI.Element {
    extraNodeAttributes(attr) {
        attr.addClass(this.styleSheet.container);
    }

    render() {
        return [
            <div className={this.styleSheet.indexPage}>
                <div className={this.styleSheet.header}>
                    Welcome saintandy!
                </div>
                <div className={this.styleSheet.body}>
                    <p>This is the beginning of your Stem project.</p>
                    <p>Try to edit it and see the changes.</p>
                </div>
            </div>
        ]
    }
}