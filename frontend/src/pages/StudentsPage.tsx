import { useEffect, useState } from "react";

import { api } from "../api";
import { getApiUrl } from "../config";
import type { Student } from "../types";


export function StudentsPage() {
    const [students, setStudents] = useState<Student[]>([]);
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [middleName, setMiddleName] = useState("");
    const [classId, setClassId] = useState("");

    async function loadStudents() {
        const data = await api<Student[]>("/students/");
        setStudents(data);
    }

    async function createStudent() {
        await api<Student>("/students/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                first_name: firstName,
                last_name: lastName,
                middle_name: middleName || null,
                class_id: Number(classId),
            }),
        });
        setFirstName("");
        setLastName("");
        setMiddleName("");
        setClassId("");
        await loadStudents();
    }

    useEffect(() => {
        loadStudents();
    }, []);

    return (
        <div>
            <h1>Students</h1>
            <h2>Add student</h2>
            <input placeholder="First name" value={firstName} onChange={(event) => setFirstName(event.target.value)}/>
            <input placeholder="Last name" value={lastName} onChange={(event) => setLastName(event.target.value)}/>
            <input placeholder="Middle name" value={middleName} onChange={(event) => setMiddleName(event.target.value)}/>
            <input type="number" placeholder="Class ID" value={classId} onChange={(event) => setClassId(event.target.value)}/>
            <button onClick={createStudent}>Create</button>
            <hr />
            {students.map((student) => (
                <div key={student.id}>
                    <p>
                        #{student.id}{" "}
                        {student.last_name}{" "}
                        {student.first_name}{" "}
                        {student.middle_name}
                        {" — "}
                        class #{student.class_id}
                    </p>
                    <a href={`${getApiUrl()}/students/${student.id}/qr`} target="_blank">QR</a>
                </div>
            ))}
        </div>
    );
}