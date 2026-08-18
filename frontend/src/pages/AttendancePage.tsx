import { useEffect, useState } from "react";
import { api } from "../api";
import type { AttendanceEvent, SchoolClass, Student } from "../types";

export function AttendancePage() {
    const [events, setEvents] = useState<AttendanceEvent[]>([])
    const [classes, setClasses] = useState<SchoolClass[]>([])
    const [students, setStudents] = useState<Student[]>([])
    const [classId, setClassId] = useState("")

    useEffect(() => {
        api<SchoolClass[]>("/classes/").then(setClasses)
        api<Student[]>("/students/").then(setStudents)
    }, [])

    async function loadAttendance() {
        if (!classId) {
            return
        }

        const data = await api<AttendanceEvent[]>(
            `/attendance/class/${classId}`
        )

        setEvents(data)
    }

    function getStudent(studentId: number) {
        return students.find((student) => student.id === studentId)
    }

    return (
        <div>
            <h1>Attendance</h1>

            <select
                value={classId}
                onChange={(event) => setClassId(event.target.value)}
            >
                <option value="">Select class</option>

                {classes.map((schoolClass) => (
                    <option
                        key={schoolClass.id}
                        value={schoolClass.id}
                    >
                        {schoolClass.name}
                    </option>
                ))}
            </select>

            <button onClick={loadAttendance}>Load</button>

            <hr />

            {events.map((event) => {
                const student = getStudent(event.student_id)

                return (
                    <div key={event.id}>
                        <p>
                            {student
                                ? `${student.first_name} ${student.last_name}`
                                : `Student #${event.student_id}`
                            }
                            {" | "}
                            {event.event_type}
                            {" | "}
                            {event.source}
                            {" | "}
                            {new Date(event.created_at).toLocaleString()}
                        </p>
                    </div>
                )
            })}
        </div>
    )
}