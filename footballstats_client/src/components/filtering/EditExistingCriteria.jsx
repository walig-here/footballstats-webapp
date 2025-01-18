import { Button, Icon } from "actify";
import {FilteringCriteria} from "../../constants";
import {FullTextSearchForm} from "./textual/FullTextSearchForm";
import { SetForm } from "./textual/SetForm";
import { useState } from "react";


export function EditExistingCriteria({filter, editFilters, onCancel}) {
    const [editedFilter, setEditedFilter] = useState(filter);

    let form = null;
    switch(filter.criteria) {
        case FilteringCriteria.textual.TEXTUAL_FULL_TEXT_SEARCH:
            form = <FullTextSearchForm searchText={editedFilter.parameters[0]} setNewFilter={setEditedFilter}/>;
            break;
        case FilteringCriteria.textual.TEXTUAL_IN_SET:
            form = <SetForm 
                attribute={filter.attribute} 
                chosenElements={editedFilter.parameters} 
                setChosenElements={(newParams) => setEditedFilter(prev => ({...prev, parameters:newParams}))}
            />;
            break;
    }

    return <>
        {form && form}
        <div className="flex flex-col space-y-2">
                {
                    editedFilter.parameters.length != 0 &&
                    <Button 
                        variant="filled"
                        onPress={() => editFilters(editedFilter)}
                    >
                        <Icon>Check</Icon>
                        Zapisz
                    </Button>
                }
                <Button 
                    variant="tonal"
                    onPress={() => onCancel()}
                >
                    <Icon>cancel</Icon>
                    Anuluj
                </Button>
        </div>
    </>
}