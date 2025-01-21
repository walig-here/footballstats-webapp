import { useState } from "react";
import { ADD_EVENT_TO_MATCH, LoginRequired, requestMutation } from "../../api_client";
import ContentView from "../../components/ContentView";
import { EventForm } from "../../components/forms/EventForm";
import { useNavigate, useParams } from "react-router";
import { useMutation } from "@apollo/client";
import { LoadingView } from "../utilities/LoadingView";
import { Button, Icon } from "actify";
import { Body } from "../../components/Body";

export default function ModifyEventView() {
    const navigate = useNavigate();
    const [newEvent, setNewEvent] = useState(null);
    const {matchId} = useParams();
    const [addEventMutation, {data, loading, error}] = useMutation(ADD_EVENT_TO_MATCH);

    if (loading)
        return <LoadingView/>

    const createEvent = async () => {
        await requestMutation(
            {
                playerId: Number.parseInt(newEvent.player),
                typeId: Number.parseInt(newEvent.type),
                matchId: Number.parseInt(matchId),
                minute: Number.parseFloat(newEvent.occurrenceMinute)
            },
            addEventMutation,
            "Dodano zdarzenie",
            "Nie dodano zdarzenia",
            "addEventToMatch"
        );
        if (error || data?.addEventToMatch?.errors?.length > 0)
            return
        navigate(`/match/${matchId}/data`);
    }

    return (
        <LoginRequired>
            <ContentView title={"Nowe zdarzenie"}>
                {
                    (error || data?.addEventToMatch?.errors?.length > 0)
                    &&
                    <Body 
                        text={
                            data?.addEventToMatch?.errors ? 
                            data.addEventToMatch.errors.map(err => err.messages.join("\n")) : 
                            error.cause.message
                        }
                        style={"text-error"}
                    />
                }
                <EventForm
                    event={newEvent}
                    setEvent={setNewEvent}
                    matchId={Number.parseInt(matchId)}
                />
                {
                    newEvent &&
                    <Button 
                        variant="filled"
                        onPress={() => createEvent()}
                    >
                        <Icon>check</Icon>
                        Dodaj kraj
                    </Button>
                }
            </ContentView>
        </LoginRequired>
    );
}