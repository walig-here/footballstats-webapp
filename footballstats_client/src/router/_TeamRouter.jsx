import { Route, Routes } from "react-router";

import TeamDataView from "../views/teams/TeamDataView.jsx";
import TeamThroughTimeView from "../views/teams/TeamThroughTimeView.jsx";
import TeamComparisonView from "../views/teams/TeamComparisonView.jsx";
import TeamPlayersComparisonView from "../views/teams/TeamPlayersComparisonView.jsx";
import HistoryOfChangesView from "../views/utilities/HistoryOfChangesView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";


export default function TeamRouter() {
    return (
        <Routes>
            <Route path="data" element={<TeamDataView/>}/>
            <Route path="through_time" element={<TeamThroughTimeView/>}/>
            <Route path="comparison" element={<TeamComparisonView/>}/>
            <Route path="players_comparison" element={<TeamPlayersComparisonView/>}/>
            <Route path="history" element={<HistoryOfChangesView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
