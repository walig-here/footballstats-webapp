import { Autocomplete, AutocompleteItem, Button, Icon } from "actify";
import { DataSeries, MetricsNames } from "../../constants";
import { DataSeriesForm } from "./DataSeriesForm";
import { useEffect } from "react";

export function MetricForm({metricName, setMetricName, onSubmit, dataSeries, setDataSeries}) {
    return (<>
        <Autocomplete
            variant="outlined"
            label={"Wybierz metrykę"}
            selectedKey={metricName}
            onSelectionChange={(newMetricName) => setMetricName(newMetricName)}
        >
            {
                Object.values(MetricsNames).map((metricName) => (
                    <AutocompleteItem key={metricName}>{metricName}</AutocompleteItem>
                ))
            }
        </Autocomplete>
        {
            metricName &&
            <DataSeriesForm
                metricName={metricName}
                setDataSeries={setDataSeries}
                dataSeries={dataSeries}
            />
        }
    </>);
}