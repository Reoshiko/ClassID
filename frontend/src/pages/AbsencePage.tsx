import { useEffect, useState } from "react";
import { api } from "../api";
import type { AbsenceRequest } from "../types";

export function AbsencePage() {
    const [requests, setRequest] = useState<AbsenceRequest[]>([])

    useEffect(() => {
        api<AbsenceRequest[]>("/absence/").then(setRequest)
    }, [])

    return (
        <div>
            <h1>Statement of absence</h1>
            {requests.map((request) => (
                <div key={request.id}>
                    <p>Student #{request.student_id}</p>
                    <p>Reason: {request.reason}</p>
                    <p>{request.date_from} - {request.date_to}</p>
                    <p>Status: {request.status}</p>
                </div>
            ))}
        </div>
    )
}