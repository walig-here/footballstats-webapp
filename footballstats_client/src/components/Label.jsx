import "../styles/components/Label.css"

export function Label({text, style}){
    return (
        <h1 className={style}>
            {text}
        </h1>
    )
}