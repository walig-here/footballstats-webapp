import ContentView from "../../components/ContentView";
import LoginForm from "../../components/forms/LoginForm";
import Section from "../../components/Section";

const LOGIN_SECTION_TITLE = "Zaloguj sie"
const LOGIN_SECTION_SUBTITLE = "Wprowadź login oraz haslo, aby zalogować się na swoje konto administratora."

const REGISTRATION_SECTION_TITLE = "Zarejestruj się"
const REGISTRATION_SECTION_SUBTITLE = "Wprowadź login, hasło i token otrzymany od właściciela, aby zarejestrować konto administratora."

export default function LoginAndRegistrationView() {
    return (
        <ContentView title="Logowanie i rejestracja" data-testid='loginView'>
            <Section iconName={"login"} title={LOGIN_SECTION_TITLE} subtitle={LOGIN_SECTION_SUBTITLE}>
                <LoginForm/>
            </Section>
            <Section iconName={"person_add"} title={REGISTRATION_SECTION_TITLE} subtitle={REGISTRATION_SECTION_SUBTITLE}>
                Ala ma kota
            </Section>
        </ContentView>
    );
}