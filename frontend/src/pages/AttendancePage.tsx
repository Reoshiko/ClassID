import { useEffect, useState } from "react";
import { api } from "../api";
import type { AttendanceEvent } from "../types";

export function AttendancePage() {
    const [events, setEvents] = useState<AttendanceEvent[]>([])

    useEffect(() => {
        api<AttendanceEvent[]>("/attendance/").then(setEvents)
    }, [])

    return (
        <div>
            <h1>Attendance</h1>
            {events.map((event) => (
                <div key={event.id}>
                    <p>
                        Student #{event.student_id}
                        {" | "}
                        {event.event_type}
                        {" | "}
                        {event.source}
                        {" | "}
                        {new Date(event.created_at).toLocaleDateString()}
                    </p>
                </div>
            ))}
        </div>
    )
}