import { Divider, Icon, IconButton } from "actify";
import { Body } from "./Body";

export function ListItem ({mainText, topText, bottomText, sideText, onEdit, onDelete, onOpen}) {
    return <div className="flex flex-col">
        <div className="px-4 py-2 flex flex-row justify-between">
            <div>
            <Body text={topText} style={"text-on-surface-variant text-xs font-medium"}/>
            <Body text={mainText} style={"text-base"}/>
            <Body text={bottomText} style={"text-sm text-on-surface-variant"}/>
            </div>
            <div className="flex flex-row space-x-2.5 place-items-center">
            <Body text={sideText} style={"text-xs font-medium text-on-surface-variant"}/>
            {
                onEdit &&
                <IconButton onPress={onEdit}>
                    <Icon>edit_square</Icon>
                </IconButton>
            }
            {
                onDelete &&
                <IconButton onPress={onDelete}>
                    <Icon>delete</Icon>
                </IconButton>
            }
            {
                onOpen &&
                <IconButton onPress={onOpen}>
                    <Icon>open_in_new</Icon>
                </IconButton>
            }
            </div>
        </div>
        <Divider/>
    </div>
}