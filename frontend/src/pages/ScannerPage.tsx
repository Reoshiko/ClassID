import { useState } from "react";
import type { AttendanceEvent, Student } from "../types";
import { api } from "../api";

export function ScannerPage() {
    const [file, setFile] = useState<File | null>(null)
    const [result, setResult] = useState<AttendanceEvent | null>(null)
    const [student, setStudent] = useState<Student | null>(null)
    const [error, setError] = useState("")

    async function scan() {
        if (!file) {
            return
        }
        const form = new FormData()
        form.append("file", file)
    
        try {
            setError("")
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/attendance/school/scan`,
                {
                    method: "POST",
                    body: form
                }
            )
            const data = await response.json()
            if (!response.ok) {
                throw new Error(data.detail)
            }
            setResult(data)
            const studentData = await api<Student>(
                `/students/${data.student_id}`
            )
            setStudent(studentData)
        } catch(error) {
            if (error instanceof Error) {
                setError(error.message)
            }
        }
    }

    return (
        <div>
            <h1>QR Scanner</h1>
            <input type="file" accept="image/*" onChange={(event) => {setFile(event.target.files?.[0] ?? null)}}/>
            <button onClick={scan}>Scan</button>
            {error && (
                <p>{error}</p>
            )}
            {result && student && (
                <div>
                    <p>Student: {student.first_name} {student.last_name}</p>
                    <p>Event: {result.event_type}</p>
                    <p>Source: {result.source}</p>
                </div>
            )}
        </div>
    )
}