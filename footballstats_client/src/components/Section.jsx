import { Card, Divider, Icon } from "actify";
import { Title } from "./Title";
import { Body } from "./Body";



export default function Section({children, topLeftContent, title, subtitle, iconName}) {
    return (
        <Card variant="outlined" className="p-4 flex flex-col space-y-3">
            <div className="flex flex-row space-x-3 pb-3">
                <Icon>{iconName}</Icon>
                <div>
                    <Title text={title} style={"title-medium"}/>
                    <Body text={subtitle}/>
                </div>
            </div>
            <Divider/>
            <div className="pt-4 flex flex-col space-y-4">
                {children}
            </div>
        </Card>
    );
}