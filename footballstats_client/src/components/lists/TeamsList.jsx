import { useContext, useEffect, useState } from "react";
import { DateRangeContext, UserContext } from "../../App";
import { useNavigate } from "react-router";
import { useQuery } from "@apollo/client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { TOKEN_EXPIRED_ERROR } from "../../constants";
import { Body } from "../Body";
import { ListItem } from "../ListItem";
import { List } from "../List";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat, isAuthenticated } from "../../data_processing";
import { GET_TEAMS } from "../../api_client";


const BUILD_TEAMS_QUERY = (sorting, filters, page, startDate, endDate, matchId, playerId) => {
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
                endDate: endDate,
                playerId: playerId,
                matchId: matchId
            },
        }
    ]
}


export function TeamsList({title, subtitle, matchId, playerId, onEdit, onDelete}) {
    const user = useContext(UserContext);
    const navigate = useNavigate();
    const dateRangeContext = useContext(DateRangeContext);
    const [page, setPage] = useState(1);
    const [filters, setFilters] = useState([]);
    const [sorting, setSorting] = useState({
        direction: "ASCENDING", 
        targetAttributeName: "nazwa", 
        metric: {
            targetEventType: null,
            metricParams: []
        }
    });
    const listQuery = useQuery(...BUILD_TEAMS_QUERY(
        sorting, filters, page, dateRangeContext.startDate, dateRangeContext.endDate, matchId, playerId
    ));

    useEffect(() => {
        listQuery.refetch();
    }, [dateRangeContext]);

    if (listQuery.loading)
        return <LoadingView/>;

    const getItems = () => {
        if (listQuery.error){
            console.log(listQuery.error);
            if (listQuery.error.cause.message === TOKEN_EXPIRED_ERROR){
                return <Body text={"Uprawnienia wygasły, odśwież stronę, aby załadować zawartość!"}/>
            } else {
                return <Body text={listQuery.error.cause.message} style={"text-error"}/>
            }
        }
        return listQuery.data.teamsList.map(team => (
            <ListItem
                topText={team.countryOfOrigin.name}
                mainText={team.name}
                bottomText={""}
                sideText={""}
                key={team.id}
                onEdit={onEdit && isAuthenticated(user.username) ? () => onEdit(team.id) : null}
                onDelete={onDelete && isAuthenticated(user.username) ? () => onDelete(team.id) : null}
                onOpen={() => navigate(`/team/${team.id}/data`)}
            />
        ));
    }

    return (
        <List 
            title={title}
            iconName={"group"}
            subtitle={subtitle}

            filters={filters}
            setFilters={setFilters}
            metricFiltersDisabled={false}
            filteringAttributes={listQuery.data ? listQuery.data.teamFilteringAttributes : []}

            sorting={sorting}
            setSorting={setSorting}
            sortingAttributes={listQuery.data ? listQuery.data.teamSortingAttributes : []}

            page={page}
            maxPage={listQuery.data ?  Math.floor(listQuery.data.teamsListLength.length / 25) + 1 : 1}
            setPage={setPage}
        >
            {getItems()}
        </List>
    );
}