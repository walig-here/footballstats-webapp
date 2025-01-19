import { Button, Icon } from "actify";
import {FilteringCriteria} from "../../constants";
import {FullTextSearchForm} from "./textual/FullTextSearchForm";
import { SetForm } from "./textual/SetForm";
import { useState } from "react";
import EqualsForm from "./numeric/EqualsForm";
import { RangeForm } from "./numeric/RangeForm";


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
        case FilteringCriteria.numeric.NUMERIC_EQUALS:
            form = <EqualsForm
                setFilter={(newFilter) => setEditedFilter(newFilter)}
                value={editedFilter.parameters[0]}
            />
            break;
        case FilteringCriteria.numeric.NUMERIC_IN_CLOSED_RANGE:
            form = <RangeForm
                from={editedFilter.parameters[0]}
                to={editedFilter.parameters[1]}
                setFilter={(newFilter) => setEditedFilter(newFilter)}
            />
            break;
        case FilteringCriteria.numeric.NUMERIC_NOT_IN_CLOSED_RANGE:
            form = <RangeForm
                from={editedFilter.parameters[0]}
                to={editedFilter.parameters[1]}
                setFilter={(newFilter) => setEditedFilter(newFilter)}
            />
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