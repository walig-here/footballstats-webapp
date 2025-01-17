import { Button, Divider, Icon} from "actify";
import TopBar from "./TopBar";
import { useLocation, useNavigate } from "react-router";
import { useContext, useEffect, useState } from 'react';
import {UserContext} from '../App.jsx';

import * as constants from "../constants.js"
import * as utils from "../data_processing.js"
import { Label } from "./Label.jsx";
import "../styles/components/AppNavigation.css";



function getDataForNavigationList(username){
    const navigationMenuData = {
        "FootballStats": [
            {icon: 'home', name: "Strona główna", route: "/"},
            {icon: 'passkey', name: "Logowanie i rejestracja", route: constants.LOGIN_PAGE_PATH},
        ],
        "Listy": [
            {icon: 'sports_soccer', name: "Lista meczów", route: constants.MATCH_LIST_PAGE_PATH},
            {icon: 'man', name: "Lista zawodników", route: constants.PLAYERS_LIST_PAGE_PATH},
            {icon: 'group', name: "Lista drużyn", route: constants.TEAM_LIST_PAGE_PATH},
        ]
    };

    if (utils.isOwner(username)) {
        navigationMenuData["Właściciel"] = [
            {icon: 'shield_person', name: "Administratorzy", route: constants.ADMINS_LIST_PAGE_PATH},
            {icon: 'key_vertical', name: "Generowanie tokenów rejestracji", route: constants.REGISTRATION_TOKENS_PAGE_PATH},
        ]
    } else if (utils.isAuthenticated(username)) {
        navigationMenuData['FootballStats'].push(
            {icon: 'add_circle', name: "Dodaj mecz", route: constants.ADD_MATCH_PAGE_PATH}
        )
    }
    return navigationMenuData;
}

export default function AppNavigation({ children }) {
    const navigate = useNavigate();
    const location = useLocation();
    const user = useContext(UserContext);
    const [navigationHidden, setNavigationHidden] = useState(false);

    const navigationList = Object.entries(getDataForNavigationList(user.username)).map(([title, elements], index) => (
        <div key={index}>
            <Label style="title-small px-4 py-4" text={title}/>
            {
                elements.map((item) => (
                    <div
                        className={`px-4 py-4 space-x-3 w-full flex flex-row hover:bg-secondary-container hover:cursor-pointer rounded-full 
                            ${location.pathname === item.route ? "bg-secondary-container text-on-surface" : "text-on-surface-variant"}`}
                        key={item.route}
                        onClick={() => {navigate(item.route)}}
                    >
                        <Icon>{item.icon}</Icon>
                        <Label style="label-large" text={item.name}/>
                    </div>
                ))
            }
            <Divider/>
        </div>
    ))

    return (
        <div className="flex flex-col w-full h-screen">
            <TopBar 
                username={user.username} 
                hideNavigation={() => {setNavigationHidden(navigationHidden => !navigationHidden)}}
                logoutFunction={user.logoutFunction}
            />
            <div className="mt-16 flex flex-row">
                {   
                    !navigationHidden &&
                    <div className="fixed w-72 h-screen bg-surface-container-low flex-none flex-col px-3 py-3 rounded-2xl">
                        {navigationList}
                    </div>
                }
                <div
                    className="flex overflow-x-hidden"
                    style={!navigationHidden ? {marginLeft: "288px"} : {}}
                >
                    {children}
                </div>
            </div>
        </div>
    );
}