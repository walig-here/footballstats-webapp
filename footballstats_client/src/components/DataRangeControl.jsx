import { useContext, useEffect, useState } from "react";
import {DateRangeContext} from "../App"
import Section from "./Section";
import { Body } from "./Body";
import { Button, Icon, Slider } from "actify";
import { convertDateStringToInteger, convertNumberToDateString } from "../data_processing";


export function DataRangeControl () {
    const dateRange = useContext(DateRangeContext);
    const [localDateRange, setLocalDateRange] = useState([dateRange.startDate, dateRange.endDate]);
    
    useEffect(() => {
        setLocalDateRange([dateRange.startDate, dateRange.endDate]);
    }, [dateRange])

    return (
        <Section
            title="Aktualny zakres dat"
            iconName="date_range"
            subtitle="Wybierz i zatwierdź zakres dat, z którego pochodzić mają używane przez aplikacje dane."
            topRightContent={
                (localDateRange[0] != dateRange.startDate || localDateRange[1] != dateRange.endDate) &&
                <Button 
                    variant="filled"
                    onPress={() => dateRange.setRange(...localDateRange)}
                >
                    <Icon>check</Icon>
                    Zatwierdź nowy zakres
                </Button>
            }
        >
            <div className="px-4 flex flex-col">
                <Body 
                    text={`${localDateRange[0]} - ${localDateRange[1]}`}
                    style={"text-on-surface-variant text-base font-medium"}
                />
                <Slider
                    color="primary"
                    aria-label="wybór daty"
                    step={1}
                    minValue={convertDateStringToInteger(dateRange.minStartDate)}
                    maxValue={convertDateStringToInteger(dateRange.maxEndDate)}
                    value={[
                        convertDateStringToInteger(localDateRange[0]),
                        convertDateStringToInteger(localDateRange[1]),
                    ]}
                    onChange={
                        (range) => setLocalDateRange([
                            convertNumberToDateString(range[0]),
                            convertNumberToDateString(range[1])
                        ])
                    }
                    formatOptions={{ style: 'currency', currency: 'USD' }}
                />
            </div>
        </Section>
    )
}