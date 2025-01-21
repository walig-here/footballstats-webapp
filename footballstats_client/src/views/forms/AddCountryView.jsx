import { useState } from "react";
import { CREATE_COUNTRY, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { LeagueForm } from "../../components/forms/LeagueForm";
import { CountryForm } from "../../components/forms/CountryForm";
import { Button, Icon } from "actify";
import { useMutation } from "@apollo/client";
import { LoadingView } from "../utilities/LoadingView";
import { Body } from "../../components/Body";

export function AddCountryView() {
    const [country, setCountry] = useState(null);
    const [createCountryMutation, {loading, data, error}] = useMutation(CREATE_COUNTRY);

    const createCountry = async () => {
        await requestMutation(
            {
                name: country.name
            },
            createCountryMutation,
            "Dodano kraj",
            "Nie udało się dodać kraju!",
            "createCountry"
        )
        console.log(data)
    }

    if (loading)
        return <LoadingView/>;

    return (
        <LoginRequired>
            <ContentView title={"Dodaj kraj"}>
                {
                    (error || data?.createCountry?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.createCountry?.errors ? 
                            data.createCountry.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <CountryForm
                    setCountry={new_country => setCountry(new_country)}
                    country={country}
                />
                {
                    country &&
                    <Button 
                        variant="filled"
                        onPress={() => createCountry()}
                    >
                        <Icon>check</Icon>
                        Dodaj kraj
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    )
}