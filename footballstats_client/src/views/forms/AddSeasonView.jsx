import { useState } from "react";
import { CREATE_LEAGUE, CREATE_SEASON, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { LeagueForm } from "../../components/forms/LeagueForm";
import { useMutation } from "@apollo/client";
import { Button, Icon } from "actify";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";
import { LeagueSelector } from "../../components/selections/LeagueSelector";
import { SeasonForm } from "../../components/forms/SeasonForm";

export function AddSeasonView() {
    const [season, setSeason] = useState(null);
    const [createSeasonMutation, {loading, error, data}] = useMutation(CREATE_SEASON);

    const createSeason = async () => {
        await requestMutation(
            {
                name: season.name,
                leagueId: Number.parseInt(season.league)
            },
            createSeasonMutation,
            "Dodano sezon",
            "Nie udało się dodać sezonu!",
            "createLeagueSeason"
        )
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj sezon ligi"}>
                {
                    (error || data?.createLeagueSeason?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createLeagueSeason?.errors ? 
                            data?.createLeagueSeason?.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <SeasonForm
                    seasonData={season}
                    setSeasonData={setSeason}
                />
                {
                    season && Object.values(season).every(Boolean) &&
                    <Button 
                        variant="filled"
                        onPress={() => createSeason()}
                    >
                        <Icon>check</Icon>
                        Dodaj ligę
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    )
}