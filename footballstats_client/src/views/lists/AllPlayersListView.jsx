import { GET_PLAYERS } from "../../api_client";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";


const QUERY_PLAYER_LIST = (sorting, filters, page, startDate, endDate) => {
    const [textualFilters, metricFilters] = convertFiltersToBackendFormat(filters);
    return [
        GET_PLAYERS,
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

export default function AllPlayersListView() {
    return (
        <ContentView title={"Lista zawodników"}>
            <DataRangeControl/>
            <PlayersList
                buildQueryFunction={QUERY_PLAYER_LIST}
                subtitle={"Przeglądaj wszystkich zawodników z aktualnie wybranego zakresu dat."}
                title={"Wszyscy zawodnicy"}
            />
        </ContentView>
    );
}