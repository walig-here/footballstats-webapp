import { useState } from "react";
import { CREATE_LEAGUE, CREATE_TEAM, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { TeamForm } from "../../components/forms/TeamForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";

export function AddTeamView() {
    const [team, setTeam] = useState(null);
    const [createTeamMutation, {loading, error, data}] = useMutation(CREATE_TEAM);

    const createLeague = async () => {
        await requestMutation(
            {
                name: team.name,
                countryId: Number.parseInt(team.country)
            },
            createTeamMutation,
            "Dodano druzynę",
            "Nie udało się dodać druzyny!",
            "createTeam"
        )
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj drużynę"}>
                {
                    (error || data?.createTeam?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createTeam?.errors ? 
                            data?.createTeam?.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <TeamForm
                    team={team}
                    setTeam={setTeam}
                />
                {
                    team && Object.values(team).every(Boolean) &&
                    <Button 
                        variant="filled"
                        onPress={() => createLeague()}
                    >
                        <Icon>check</Icon>
                        Dodaj ligę
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    )
}