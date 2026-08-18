import { useEffect, useState } from "react";
import { api } from "../api";
import type { SchoolClass } from "../types";

export function ClassesPage() {
    const [classes, setClasses] = useState<SchoolClass[]>([])
    const [name, setName] = useState("")

    async function loadClasses() {
        const data = await api<SchoolClass[]>("/classes/")
        setClasses(data)
    }

    async function createClass() {
        await api<SchoolClass>("/classes/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name
            })
        })
        setName("")
        await loadClasses()
    }

    useEffect(() => {
        loadClasses()
    }, [])

    return (
        <div>
            <h1>Classes</h1>
            <input placeholder="Class name" value={name} onChange={(event) => setName(event.target.value)}/>
            <button onClick={createClass}>Create</button>
            <hr />
            {classes.map((schoolClass) => (
                <div key={schoolClass.id}>
                    <p>{schoolClass.id} - {schoolClass.name}</p>
                </div>
            ))}
        </div>
    )
}