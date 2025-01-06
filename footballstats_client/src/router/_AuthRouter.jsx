import { Route, Routes } from "react-router";

import LoginAndRegistrationView from "../views/utilities/LoginAndRegistrationView.jsx";
import PageNotFoundView from "../views/utilities/PageNotFoundView.jsx";
import UnauthorizedView from "../views/utilities/UnauthorizedView.jsx";
import GenerateRegistrationTokenView from "../views/utilities/GenerateRegistrationTokenView.jsx";


export default function AuthRouter() {
    return (
        <Routes>
            <Route path="login" element={<LoginAndRegistrationView/>}/>
            <Route path="unauthorized" element={<UnauthorizedView/>}/>
            <Route path="generate_registration_token" element={<GenerateRegistrationTokenView/>}/>
            <Route path="*" element={<PageNotFoundView/>}/>
        </Routes>
    )
}
