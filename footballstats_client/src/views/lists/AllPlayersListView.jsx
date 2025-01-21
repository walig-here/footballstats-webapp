import { useContext } from "react";
import { DELETE_PLAYER, GET_PLAYERS, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/pLAYERSList";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";
import { ModalContext } from "../../components/modals/ModalManager";
import { useMutation } from "@apollo/client";
import { LoadingView } from "../utilities/LoadingView";




export default function AllPlayersListView() {
    const modalContext = useContext(ModalContext);
    const [deletePlayerMutation, deletePlayerResponse] = useMutation(DELETE_PLAYER);

    const deletePlayer = (playerId) => {
        requestMutation(
            {playerId: Number.parseInt(playerId)},
            deletePlayerMutation,
            "Usunięto zawodnika!",
            "Nie udało się usunąć zawodnika!",
            "removePlayer"
        );
    }

    if (deletePlayerResponse.loading)
        return <LoadingView/>

    return (
        <ContentView title={"Lista zawodników"}>
            <DataRangeControl/>
            <PlayersList
                subtitle={"Przeglądaj wszystkich zawodników z aktualnie wybranego zakresu dat."}
                title={"Wszyscy zawodnicy"}
                onDelete={(playerId) => modalContext.openModal(
                    "Czy na pewno chcesz usunąć zawodnika z systemu?",
                    () => deletePlayer(playerId)
                )}
            />
        </ContentView>
    );
}