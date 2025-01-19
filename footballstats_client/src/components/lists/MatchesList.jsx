import { useQuery } from "@apollo/client";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router";
import { LoadingView } from "../../views/utilities/LoadingView";
import ContentView from "../ContentView";
import {List} from "../List";
import {ListItem} from "../ListItem";
import { DateRangeContext, UserContext } from "../../App";
import { isAuthenticated } from "../../data_processing";
import { TOKEN_EXPIRED_ERROR } from "../../constants";
import { Body } from "../Body";


export function MatchesList({buildQueryFunction, title, subtitle}) {
    const user = useContext(UserContext);
    const navigate = useNavigate();
    const dateRangeContext = useContext(DateRangeContext);
    const [page, setPage] = useState(1);
    const [filters, setFilters] = useState([]);
    const [sorting, setSorting] = useState({
        direction: "DESCENDING", 
        targetAttributeName: "data rozegrania", 
        metric: {
            targetEventType: null,
            metricParams: []
        }
    });
    const listQuery = useQuery(...buildQueryFunction(
        sorting, filters, page, dateRangeContext.startDate, dateRangeContext.endDate
    ));

    useEffect(() => {
        listQuery.refetch()
    }, [dateRangeContext])

    if (listQuery.loading)
        return <LoadingView/>

    const getItems = () => {
        if (listQuery.error){
            console.log(listQuery.error);
            if (listQuery.error.cause.message === TOKEN_EXPIRED_ERROR){
                return <Body text={"Uprawnienia wygasły, odśwież stronę, aby załadować zawartość!"}/>
            } else {
                return <Body text={listQuery.error.cause.message} style={"text-error"}/>
            }
        }
        return listQuery.data.matchesList.map(match => (
            <ListItem
                topText={match.gameDate}
                mainText={`${match.teamsScores[0].teamName} - ${match.teamsScores[1].teamName}`}
                bottomText={`${match.teamsScores[0].score} - ${match.teamsScores[1].score}`}
                sideText={match.leagueSeason.league.name}
                key={match.id}
                onEdit={isAuthenticated(user.username) ? () => console.log(match.id) : null}
                onDelete={isAuthenticated(user.username) ? () => console.log(match.id) : null}
                onOpen={() => navigate(`/match/${match.id}/data`)}
            />
        ));
    }


    return (
        <List 
            title={title}
            iconName={"sports_soccer"}
            subtitle={subtitle}

            filters={filters}
            setFilters={setFilters}
            metricFiltersDisabled={false}
            filteringAttributes={listQuery.data ? listQuery.data.matchFilteringAttributes : []}

            sorting={sorting}
            setSorting={setSorting}
            sortingAttributes={listQuery.data ? listQuery.data.matchSortingAttributes : []}

            page={page}
            maxPage={listQuery.data ? listQuery.data.matchListLength + 1 : 1}
            setPage={setPage}
        >
            {getItems()}
        </List>
    );
}