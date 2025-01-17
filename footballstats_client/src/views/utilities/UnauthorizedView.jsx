import { Body } from "../../components/Body";
import ContentView from "../../components/ContentView";

const UNAUTHORIZED_DESC = "Nie posiadasz wystarczających uprawnień do dokonania wybranej akcji. Użyj panelu nawigacyjnego znajdującego siępo lewej stronie, aby kontynuować korzystanie z serwisu."

export default function UnauthorizedView() {
    return (
        <ContentView title={"Brak uprawnień"}>
            <Body text={UNAUTHORIZED_DESC}/>
        </ContentView>
    );
}