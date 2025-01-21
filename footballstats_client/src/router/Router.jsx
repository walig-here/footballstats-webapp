import { Route, Routes } from "react-router";
import { BrowserRouter } from 'react-router'

import HomeView from "../views/utilities/HomeView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx"

import MatchRouter from "./_MatchRoutes.jsx"
import PlayerRouter from "./_PlayerRouter.jsx"
import TeamRouter from "./_TeamRouter.jsx"
import ListRouter from "./_ListRouter.jsx";
import FormsRouter from "./_FormsRouter.jsx";
import AuthRouter from "./_AuthRouter.jsx";
import AppNavigation from "../components/AppNavigation.jsx";
import {Background} from "../components/Background.jsx"
import { ModalContext, ModalManager } from "../components/modals/ModalManager.jsx";


export default function Router() {
    return (
        <Background>
            <BrowserRouter>
                <ModalManager>
                    <AppNavigation>
                        <Routes>
                            <Route path="/" element={<HomeView/>}/>
                            <Route path="/match/:id/*" element={<MatchRouter/>}/>
                            <Route path="/player/:id/*" element={<PlayerRouter/>}/>
                            <Route path="/team/:id/*" element={<TeamRouter/>}/>
                            <Route path="/list/*" element={<ListRouter/>}/>
                            <Route path="/form/*" element={<FormsRouter/>}/>
                            <Route path="/auth/*" element={<AuthRouter/>}/>
                            <Route path="*" element={<PageNotFoundView/>}/>
                        </Routes>
                    </AppNavigation>
                </ModalManager>
            </BrowserRouter>
        </Background>
    );
}