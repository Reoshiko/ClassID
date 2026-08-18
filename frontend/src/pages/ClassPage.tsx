import { useEffect, useState } from "react";
import { api } from "../api";
import type { SchoolClass } from "../types";

export function ClassesPage() {
    const [classes, setClasses] = useState<SchoolClass[]>([])

    useEffect(() => {
        api<SchoolClass[]>("/classes/").then(setClasses)
    }, [])

    return (
        <div>
            <h1>Classes</h1>
            {classes.map((schoolClass) => (
                <div key={schoolClass.id}>
                    <p>{schoolClass.id} - {schoolClass.name}</p>
                </div>
            ))}
        </div>
    )
}