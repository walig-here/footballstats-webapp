import { Button, Divider, Icon, IconButton } from "actify";
import { Body } from "../Body";
import { capitalize, filteringCriteriaToText } from "../../data_processing";
import { MatchEvents, MatchEventsNames } from "../../constants";

const NEW_FILTER = "Nowy filtr";

function FilterListItem({ attribute, criteria, parameters, metric, onDelete, onEdit }) {
    return (
        <div>
            <div className="p-4 flex flex-col place-content-between space-y-2">
                <div className="flex flex-row justify-between place-items-center">
                    <div>
                        <Body
                            text={MatchEventsNames[metric.targetMatchEvent]}
                            style={"text-xs font-medium text-on-surface-variant"}
                        />
                        <Body
                            style={"text-base"}
                            text={capitalize(attribute)}
                        />
                        {
                            metric.metricParams.length > 0 &&
                            <Body 
                                style={"text-xs font-medium text-on-surface-variant"}
                                text={metric.metricParams.toString()}
                            />
                        }
                    </div>
                    <div className="flex flex-row">
                        <IconButton onPress={onEdit}>
                            <Icon>edit</Icon>
                        </IconButton>
                        <IconButton onPress={onDelete}>
                            <Icon>delete</Icon>
                        </IconButton>
                    </div>
                </div>
                <div>
                    <Body
                        text={`${filteringCriteriaToText(criteria)}: ${parameters.toString()}`}
                        style={"text-sm"}
                    />
                </div>
            </div>
            <Divider />
        </div>
    )
}


export function FilterList({ filters, onAddFilterPressed, onDeleteFilter, onEditFilter }) {
    const listItems = filters.map((filter, index) => (
        <FilterListItem
            key={index}
            attribute={filter.attribute}
            criteria={filter.criteria}
            parameters={filter.parameters}
            onDelete={() => onDeleteFilter(index)}
            onEdit={() => onEditFilter(index)}
            metric={filter.metric}
        />
    ));

    return (
        <div className="flex flex-col space-y-4">
            <div>
                {listItems}
            </div>
            <Button
                variant="filled"
                onPress={() => onAddFilterPressed()}
            >
                <Icon>add</Icon>{NEW_FILTER}
            </Button>
        </div>
    );
}