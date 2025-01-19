import { GET_MATCHES } from "../../api_client";
import { convertFiltersToBackendFormat, convertSortingToBackendFormat, isAuthenticated } from "../../data_processing";
import { MatchesList } from "../../components/lists/MatchesList";


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
    return (
        <MatchesList buildQueryFunction={QUERY_MATCH_LIST}/>
    );
}