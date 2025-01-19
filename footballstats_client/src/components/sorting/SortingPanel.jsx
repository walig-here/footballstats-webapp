import { Button, Icon, Select, SelectOption } from "actify";
import Section from "../Section";
import { MetricsNames } from "../../constants";
import { useEffect, useState } from "react";
import { MetricSorting } from "./MetricSorting";

export function SortingPanel ({
    onClose,
    sortingCriteria,
    setSortingCriteria,
    metricCriteriaDisabled,
    sortingAttributes,
}) {
    const [localSorting, setLocalSorting] = useState(sortingCriteria);

    const sortingElements = (
        metricCriteriaDisabled ? sortingAttributes :
        [...sortingAttributes, ...Object.values(MetricsNames)]
    );
    const metricSorting = Object.values(MetricsNames).includes(localSorting.targetAttributeName);

    const closeSorting = () => {
        setSortingCriteria(localSorting);
        onClose();
    }
    const closeButton = <Button variant="tonal" onPress={() => closeSorting()}>
        <Icon>close</Icon>
    </Button>;

    return <Section
        title={"Sortowanie"}
        iconName={"sort"}
        className="flex-none w-1/3"
        subtitle={"Zmień aktualne kryteria sortowania"}
        topRightContent={(!metricSorting || (metricSorting && localSorting.metric.targetEventType)) && closeButton}
    >
        <Select 
            label={"Element sortujący"}
            variant="outlined"
            onSelectionChange={
                (newAttribute) => setLocalSorting(prev => ({...prev, targetAttributeName: newAttribute}))
            }
            selectedKey={localSorting.targetAttributeName}
        >
            {sortingElements.map((element) => (
                <SelectOption key={element} textValue={element}>{element}</SelectOption>
            ))}
        </Select>
        {
            metricSorting &&
            <MetricSorting setSorting={setLocalSorting} sorting={localSorting}/>
        }
        <Select 
            label={"Kierunek sortowania"}
            variant="outlined"
            selectedKey={localSorting.direction}
            onSelectionChange={
                (newDirection) => setLocalSorting(prev => ({...prev, direction: newDirection}))
            }
        >
            <SelectOption key={"ASCENDING"}>Rosnący</SelectOption>
            <SelectOption key={"DESCENDING"}>Malejący</SelectOption>
        </Select>
    </Section>
}