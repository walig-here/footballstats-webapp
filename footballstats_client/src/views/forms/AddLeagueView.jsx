import { useState } from "react";
import { CREATE_LEAGUE, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { LeagueForm } from "../../components/forms/LeagueForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";

export function AddLeagueView() {
    const [league, setLeague] = useState(null);
    const [createLeagueMutation, {loading, error, data}] = useMutation(CREATE_LEAGUE);

    const createLeague = async () => {
        await requestMutation(
            {
                name: league.name,
                countryId: Number.parseInt(league.country)
            },
            createLeagueMutation,
            "Dodano ligę",
            "Nie udało się dodać ligi!",
            "createLeague"
        )
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj ligę"}>
                {
                    (error || data?.createLeague?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createLeague?.errors ? 
                            data.createLeague.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <LeagueForm
                    setLeague={(newLeague) => setLeague(newLeague)}
                    league={league}
                />
                {
                    league && Object.values(league).every(Boolean) &&
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