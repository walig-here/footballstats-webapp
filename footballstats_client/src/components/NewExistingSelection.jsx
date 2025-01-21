import { SegmentedButton, SegmentedButtonSet } from "actify";

export function NewExistingSelection({existing, setExisting}) {
    return (
        <SegmentedButtonSet
            className="flex flex-row w-full h-full px-1"
        >
            <div  className="flex w-full h-full">
                <SegmentedButton 
                    title="Nowy"
                    label="Nowy"
                    selected={!existing}
                    className="rounded-l-full"
                    onPress={() => setExisting(false)}
                />
                <SegmentedButton 
                    title="Istniejący"
                    label="Istniejący"
                    selected={existing}
                    className="rounded-r-full"
                    onPress={() => setExisting(true)}
                />
            </div>
        </SegmentedButtonSet>
    )
}