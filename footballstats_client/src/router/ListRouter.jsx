import { Route, Routes } from "react-router";

import AllTeamsListView from "../views/lists/AllTeamsListView.jsx";
import AllPlayersListView from "../views/lists/AllPlayersListView.jsx";
import AllMatchesListView from "../views/lists/AllMatchesListView.jsx";
import AllAdminsListView from "../views/lists/AllAdminsListView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";


export default function ListRouter() {
    return (
        <Routes>
            <Route path="teams" element={<AllTeamsListView/>}/>
            <Route path="players" element={<AllPlayersListView/>}/>
            <Route path="matches" element={<AllMatchesListView/>}/>
            <Route path="admins" element={<AllAdminsListView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
