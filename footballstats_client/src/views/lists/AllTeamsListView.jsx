import { GET_TEAMS } from "../../api_client";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { TeamsList } from "../../components/lists/TeamsList";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";

const QUERY_TEAMS_LIST = (sorting, filters, page, startDate, endDate) => {
    const [textualFilters, metricFilters] = convertFiltersToBackendFormat(filters);
    return [
        GET_TEAMS,
        {
            variables: {
                page: page - 1,
                textualFilters: textualFilters,
                metricFilters: metricFilters,
                sorting: convertSortingToBackendFormat(sorting),
                startDate: startDate,
                endDate: endDate
            },
        }
    ]
}

export default function AllTeamsListView() {
    return (
        <ContentView title={"Lista drużyn"}>
            <DataRangeControl/>
            <TeamsList
                buildQueryFunction={QUERY_TEAMS_LIST}
                subtitle={"Przeglądaj wszystkie drużyny z aktualnie wybranego zakresu dat."}
                title={"Wszystkie drużyny"}
            />
        </ContentView>
    );
}