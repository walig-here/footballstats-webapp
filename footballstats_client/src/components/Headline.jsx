import "../styles/components/Headline.css"

export function Headline(props){
    const {text, style} = props;
    return (
        <h1 data-testid={props["data-testid"]} className={style}>
            {text}
        </h1>
    );
}