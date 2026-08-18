import { useEffect, useState } from "react";
import { api } from "../api";
import type { Student } from "../types";

export function StudentsPage() {
    const [students, setStudents] = useState<Student[]>([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")

    useEffect(() => {
        api<Student[]>("/students/").then(setStudents).catch((error) => setError(error.message)).finally(() => setLoading(false))
    }, [])
    
    if (loading) {
        return <p>Loading...</p>
    }
    if (error) {
        return <p>{error}</p>
    }

    return (
        <div>
            <div className="page-header">
                <div>
                    <h1>Students</h1>
                    <p>List of registered students</p>
                </div>
            </div>
            <div className="table-card">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Full name</th>
                            <th>Class</th>
                            <th>QR</th>
                        </tr>
                    </thead>
                    <tbody>
                        {students.map((student) => (
                            <tr key={student.id}>
                                <td>{student.id}</td>
                                <td>{student.last_name}{" "}{student.first_name}{" "}{student.middle_name}</td>
                                <td>{student.class_id}</td>
                                <td><a href={`${import.meta.env.VITE_API_URL}/students/${student.id}/qr`} target="_blank">Open QR</a></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}