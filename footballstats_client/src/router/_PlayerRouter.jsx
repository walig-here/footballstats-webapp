import { Route, Routes } from "react-router";

import PlayerDataView from "../views/players/PlayerDataView.jsx";
import PlayerComparisonView from "../views/players/PlayerComparisonView.jsx";
import PlayerThroughTimeView from "../views/players/PlayerThroughTimeView.jsx";
import PlayerMatchesAndTeamsView from "../views/players/PlayerMatchesAndTeamsView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";
import HistoryOfChangesView from "../views/utilities/HistoryOfChangesView.jsx";


export default function PlayerRouter() {
    return (
        <Routes>
            <Route path="data" element={<PlayerDataView/>}/>
            <Route path="comparison" element={<PlayerComparisonView/>}/>
            <Route path="through_time" element={<PlayerThroughTimeView/>}/>
            <Route path="matches_and_teams" element={<PlayerMatchesAndTeamsView/>}/>
            <Route path="history" element={<HistoryOfChangesView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
