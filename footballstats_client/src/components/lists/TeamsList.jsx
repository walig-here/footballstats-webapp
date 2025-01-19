import { useContext, useEffect, useState } from "react";
import { DateRangeContext, UserContext } from "../../App";
import { useNavigate } from "react-router";
import { useQuery } from "@apollo/client";
import { LoadingView } from "../../views/utilities/LoadingView";
import { TOKEN_EXPIRED_ERROR } from "../../constants";
import { Body } from "../Body";
import { ListItem } from "../ListItem";
import { List } from "../List";
import { isAuthenticated } from "../../data_processing";

export function TeamsList({buildQueryFunction, title, subtitle}) {
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
    const listQuery = useQuery(...buildQueryFunction(
        sorting, filters, page, dateRangeContext.startDate, dateRangeContext.endDate
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
                onEdit={isAuthenticated(user.username) ? () => console.log(team.id) : null}
                onDelete={isAuthenticated(user.username) ? () => console.log(team.id) : null}
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