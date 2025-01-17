import "../styles/components/Title.css"

export function Title({text, style}){
    return (
        <h1 className={style}>
            {text}
        </h1>
    )
}