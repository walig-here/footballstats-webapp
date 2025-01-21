import { Route, Routes } from "react-router";

import AddMatchView from "../views/forms/AddMatchView.jsx";
import ModifyPlayerView from "../views/forms/ModifyPlayerView.jsx";
import ModifyTeamView from "../views/forms/ModifyTeamView.jsx";
import ModifyMatchView from "../views/forms/ModifyMatchView.jsx";
import ModifyPlayerContributionInMatchView from "../views/forms/ModifyPlayerContributionInMatchView.jsx";
import ModifyCountryView from "../views/forms/ModifyCountryView.jsx";
import ModifyLeagueAndSeasonView from "../views/forms/ModifyLeagueAndSeasonView.jsx";
import ModifyEventView from "../views/forms/ModifyEventView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";
import { AddLeagueView } from "../views/forms/AddLeagueView.jsx";
import { AddCountryView } from "../views/forms/AddCountryView.jsx";
import { AddSeasonView } from "../views/forms/AddSeasonView.jsx";
import { AddTeamView } from "../views/forms/AddTeamView";
import { AddPlayerView } from "../views/forms/AddPlayerView.jsx";
import { AddPlayerToMatchView } from "../views/forms/AddPlayerToMatchView.jsx";


export default function FormsRouter() {
    return (
        <Routes>
            <Route path="add_match" element={<AddMatchView/>}/>
            <Route path="modify_player" element={<ModifyPlayerView/>}/>
            <Route path="modify_team" element={<ModifyTeamView/>}/>
            <Route path="modify_match" element={<ModifyMatchView/>}/>
            <Route path="modify_player_contribution" element={<ModifyPlayerContributionInMatchView/>}/>
            <Route path="modify_country" element={<ModifyCountryView/>}/>
            <Route path="modify_league_and_season" element={<ModifyLeagueAndSeasonView/>}/>
            <Route path="add_event/:matchId" element={<ModifyEventView/>}/>
            <Route path="add_league" element={<AddLeagueView/>}/>
            <Route path="add_country" element={<AddCountryView/>}/>
            <Route path="add_season" element={<AddSeasonView/>}/>
            <Route path="add_team" element={<AddTeamView/>}/>
            <Route path="add_player" element={<AddPlayerView/>}/>
            <Route path="add_player_to_match/:matchId/:teamId" element={<AddPlayerToMatchView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
