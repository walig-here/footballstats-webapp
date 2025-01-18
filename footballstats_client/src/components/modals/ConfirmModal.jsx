import { Button, Icon } from "actify";
import { Body } from "../Body";

export function ConfirmModal({onClose, onConfirm, message}) {
    return (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <div className="bg-surface p-6 rounded-lg shadow-lg w-96">
                <Body text={message} style={"pb-4"}/>
                <div className="flex flex-col space-y-2">
                    <Button 
                        onPress={() => onConfirm()}
                        variant="filled"
                        className="w-full"
                    >
                        <Icon>check</Icon>
                        Tak
                    </Button>
                    <Button 
                        onPress={() => onClose()}
                        variant="outlined"
                        className="w-full"
                    >
                        <Icon>close</Icon>
                        Nie
                    </Button>
                </div>
            </div>
        </div>
    );
}
