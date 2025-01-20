import { GET_PLAYERS } from "../../api_client";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";




export default function AllPlayersListView() {
    return (
        <ContentView title={"Lista zawodników"}>
            <DataRangeControl/>
            <PlayersList
                subtitle={"Przeglądaj wszystkich zawodników z aktualnie wybranego zakresu dat."}
                title={"Wszyscy zawodnicy"}
            />
        </ContentView>
    );
}