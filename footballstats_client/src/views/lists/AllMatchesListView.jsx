import { DELETE_MATCH_MUTATION, GET_MATCHES, requestMutation } from "../../api_client";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat, isAuthenticated } from "../../data_processing";
import { MatchesList } from "../../components/lists/MatchesList";
import { DataRangeControl } from "../../components/DataRangeControl";
import ContentView from "../../components/ContentView";
import { useContext, useState } from "react";
import { ConfirmModal } from "../../components/modals/ConfirmModal";
import { useMutation } from "@apollo/client";
import { LoadingView } from "../utilities/LoadingView";
import { ModalContext } from "../../components/modals/ModalManager";


const QUERY_MATCH_LIST = (sorting, filters, page, startDate, endDate) => {
    const [textualFilters, metricFilters] = convertFiltersToBackendFormat(filters);
    return [
        GET_MATCHES,
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


export default function AllMatchesListView() {
    const [deleteMatchMutation, deleteMatchResponse] = useMutation(DELETE_MATCH_MUTATION);
    const modalContext = useContext(ModalContext);

    const deleteMatch = (matchId) => {
        requestMutation(
            {matchId: Number.parseInt(matchId)},
            deleteMatchMutation,
            "Usunięto mecz!",
            "Nie udało się usunąć meczu!",
            "removeMatch"
        )
    }

    if (deleteMatchResponse.loading)
        return <LoadingView/>

    return (
        <ContentView title={"Lista meczów"}>
            <DataRangeControl/>
            <MatchesList 
                subtitle={"Przeglądaj wszystkie mecze z aktualnie wybranego zakresu dat."}
                title={"Wszystkie mecze"}
                onDelete={(matchId) => modalContext.openModal(
                    "Czy na pewno chcesz usunąć mecz?",
                    () => deleteMatch(matchId)
                )}
            />
        </ContentView>
    );
}