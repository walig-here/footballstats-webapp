import { useContext, useEffect, useState } from "react";
import { DateRangeContext, UserContext } from "../../App";
import { useNavigate } from "react-router";
import { useQuery } from "@apollo/client";
import { List } from "../List";
import { LoadingView } from "../../views/utilities/LoadingView";
import { ListItem } from "../ListItem";
import { isAuthenticated } from "../../data_processing";
import { TOKEN_EXPIRED_ERROR } from "../../constants";
import { Body } from "../Body";

export function PlayersList ({buildQueryFunction, title, subtitle, match, team}) {
    const user = useContext(UserContext);
    const navigate = useNavigate();
    const dateRangeContext = useContext(DateRangeContext);
    const [page, setPage] = useState(1);
    const [filters, setFilters] = useState([]);
    const [sorting, setSorting] = useState({
        direction: "ASCENDING",
        targetAttributeName: "nazwisko",
        metric: {
            targetEventType: null,
            metricParams: []
        }
    });
    const listQuery = useQuery(...buildQueryFunction(
        sorting, filters, page, dateRangeContext.startDate, dateRangeContext.endDate, match, team
    ));

    useEffect(() => {
        listQuery.refetch();
        setPage(1);
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
        return listQuery.data.playersList.map(player => (
            <ListItem
                topText={player.countryOfOrigin.name}
                mainText={`${player.name} ${player.surname}`}
                bottomText={player.nickname}
                sideText={""}
                key={player.id}
                onEdit={isAuthenticated(user.username) ? () => console.log("a") : null}
                onDelete={isAuthenticated(user.username) ? () => console.log("a") : null}
                onOpen={() => navigate(`/player/${player.id}/data`)}
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
            filteringAttributes={listQuery.data ? listQuery.data.playerFilteringAttributes : []}

            sorting={sorting}
            setSorting={setSorting}
            sortingAttributes={listQuery.data ? listQuery.data.playerSortingAttributes : []}

            page={page}
            maxPage={listQuery.data ? Math.floor(listQuery.data.playerListLength.length / 25) + 1 : 1}
            setPage={setPage}
        >
            {getItems()}
        </List>
    );
}