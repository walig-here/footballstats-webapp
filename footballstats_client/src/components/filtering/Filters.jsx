import { useState } from "react";
import Section from "../Section";
import { Button, Icon } from "actify";
import { AddNewCriteria } from "./AddNewCriteria";
import {FilterList} from "./FilterList";
import { MetricsNames } from "../../constants";
import { EditExistingCriteria } from "./EditExistingCriteria";




const FiltersState = {
    DISPLAY_CRITERIA: {
        type: "display_criteria",
        desc: "Aktualne kryteria filtrowania"
    },
    ADD_NEW_CRITERIA: {
        type: "add_new_textual_filter",
        desc: "Dodaj nowe kryterium filtrowania"
    },
    EDITING_CRITERIA: {
        type: "edit_exiting_filter",
        desc: "edytuj"
    }
}


export default function Filters({
    onClose, 
    filters, 
    setFilters, 
    filteringAttributes, 
    metricFiltersDisabled, 
    startDate, 
    endDate
}) {
    const [filtersState, setFiltersState] = useState(FiltersState.DISPLAY_CRITERIA);
    const [localFilters, setLocalFilters] = useState(filters);
    const [editedFilterIndex, setEditedFilterIndex] = useState(null);

    const addNewFilter = (newFilter) => {
        setFiltersState(FiltersState.DISPLAY_CRITERIA);
        setLocalFilters(prev => [...prev, newFilter]);
    };
    const deleteFilter = (removeIndex) => {
        setLocalFilters(prev => prev.filter((_, index) => index !== removeIndex));
    };
    const openFilterEditor = (editIndex) => {
        setFiltersState(FiltersState.EDITING_CRITERIA);
        setEditedFilterIndex(editIndex);
    }
    const editFilter = (newFilter) => {
        setFiltersState(FiltersState.DISPLAY_CRITERIA);
        setLocalFilters(prev => prev.map((filter, index) => (
            index === editedFilterIndex ? newFilter : filter
        )));
    }
    const closeFilters = () => {
        setFilters(localFilters);
        onClose();
    }

    const getChildrenForState = () => {
        switch (filtersState.type) {
            case FiltersState.DISPLAY_CRITERIA.type:
                return <FilterList
                    filters={localFilters}
                    onAddFilterPressed={() => setFiltersState(FiltersState.ADD_NEW_CRITERIA)}
                    onEditFilter={openFilterEditor}
                    onDeleteFilter={deleteFilter}
                />
            case FiltersState.ADD_NEW_CRITERIA.type:
                return <AddNewCriteria
                    textualFilteringElements={filteringAttributes}
                    metricFilteringElements={metricFiltersDisabled ? [] : Object.values(MetricsNames)}
                    onConfirm={addNewFilter}
                    onClose={() => setFiltersState(FiltersState.DISPLAY_CRITERIA)}
                />
            case FiltersState.EDITING_CRITERIA.type:
                return <EditExistingCriteria 
                    filter={localFilters[editedFilterIndex]} 
                    editFilters={editFilter}
                    onCancel={() => setFiltersState(FiltersState.DISPLAY_CRITERIA)}
                />
            default:
                return <></>
        }
    }

    return (
        <Section
            className="flex-none w-1/3"
            title="Filtrowanie"
            iconName="filter_list"
            subtitle={filtersState.desc}
            topRightContent={
                <Button variant="tonal" onPress={closeFilters}>
                    <Icon>close</Icon>
                </Button>
            }
        >
            {getChildrenForState()}
        </Section>
    );
}