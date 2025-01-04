import { Route, Routes } from "react-router";

import MatchDataView from "../views/matches/MatchDataView.jsx";
import MatchMetricsView from "../views/matches/MatchMetricsView.jsx";
import MatchParticipantsView from "../views/matches/MatchParticipantsView.jsx"
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";
import HistoryOfChangesView from "../views/utilities/HistoryOfChangesView.jsx";


export default function MatchRoutes() {
    return (
        <Routes>
            <Route path="data" element={<MatchDataView/>}/>
            <Route path="metrics" element={<MatchMetricsView/>}/>
            <Route path="participants" element={<MatchParticipantsView/>}/>
            <Route path="history" element={<HistoryOfChangesView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
