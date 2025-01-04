import { Route, Routes } from "react-router";

import HomeView from "./views/utilities/HomeView.jsx";
import PageNotFoundView from "./views/utilities/PageNotFoundView.jsx"

import MatchRouter from "./router/MatchRoutes.jsx"
import PlayerRouter from "./router/PlayerRouter.jsx"
import TeamRouter from "./router/TeamRouter.jsx"
import ListRouter from "./router/ListRouter.jsx";
import FormsRouter from "./router/FormsRouter.jsx";
import AuthRouter from "./router/AuthRouter.jsx";

export default function App() {
  return (
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
  )
}
