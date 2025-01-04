import { Route, Routes } from "react-router";

import HomeView from "./views/utilities/HomeView.jsx";
import PageNotFoundView from "./views/utilities/PageNotFoundView.jsx"
import MatchRoutes from "./router/MatchRoutes.jsx"

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<HomeView/>}/>
      <Route path="/match/:id/*" element={<MatchRoutes/>}/>
      <Route path="*" element={<PageNotFoundView/>}/>
    </Routes>
  )
}
