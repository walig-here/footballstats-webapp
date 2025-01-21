import { useContext } from "react";
import { DELETE_TEAM, GET_TEAMS, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { DataRangeControl } from "../../components/DataRangeControl";
import { PlayersList } from "../../components/lists/PlayersList";
import { TeamsList } from "../../components/lists/TeamsList";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat } from "../../data_processing";
import { ModalContext } from "../../components/modals/ModalManager";
import { useMutation } from "@apollo/client";
import { LoadingView } from "../utilities/LoadingView";

export default function AllTeamsListView() {
    const modalContext = useContext(ModalContext);
    const [deleteTeamMutation, deleteTeamResponse] = useMutation(DELETE_TEAM);

    const deleteTeam = (teamId) => {
        requestMutation(
            {teamId: Number.parseInt(teamId)},
            deleteTeamMutation,
            "Usunięto drużynę",
            "Nie udało się usunąć drużyny!",
            "removeTeam"
        )
    }

    if (deleteTeamResponse.loading)
        return <LoadingView/>

    return (
        <ContentView title={"Lista drużyn"}>
            <DataRangeControl/>
            <TeamsList
                subtitle={"Przeglądaj wszystkie drużyny z aktualnie wybranego zakresu dat."}
                title={"Wszystkie drużyny"}
                onDelete={(teamId) => modalContext.openModal(
                    "Czy na pewno chcesz usunąć drużynę?",
                    () => deleteTeam(teamId)
                )}
            />
        </ContentView>
    );
}