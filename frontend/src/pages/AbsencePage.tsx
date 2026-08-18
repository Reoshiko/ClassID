import { useEffect, useState } from "react";
import { api } from "../api";
import type { AbsenceRequest } from "../types";

export function AbsencePage() {
    const [requests, setRequests] = useState<AbsenceRequest[]>([]);
    const [studentId, setStudentId] = useState("");
    const [reason, setReason] = useState("");
    const [dateFrom, setDateFrom] = useState("");
    const [dateTo, setDateTo] = useState("");

    async function loadRequests() {
        const data = await api<AbsenceRequest[]>("/absence/");
        setRequests(data);
    }

    async function createRequest() {
        await api<AbsenceRequest>("/absence/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                student_id: Number(studentId),
                reason,
                date_from: dateFrom,
                date_to: dateTo,
            }),
        });
        setStudentId("");
        setReason("");
        setDateFrom("");
        setDateTo("");
        await loadRequests();
    }

    async function setStatus(id: number, status: "approved" | "rejected",) {
        await api<AbsenceRequest>(
            `/absence/${id}/status?status=${status}`,
            {
                method: "PATCH",
            },
        );
        await loadRequests();
    }

    useEffect(() => {
        loadRequests();
    }, []);

    return (
        <div>
            <h1>Statement of absence</h1>
            <h2>Create statement</h2>
            <input type="number" placeholder="Student ID" value={studentId} onChange={(event) => setStudentId(event.target.value)}/>
            <input placeholder="Reason" value={reason} onChange={(event) => setReason(event.target.value)}/>
            <input type="date" value={dateFrom} onChange={(event) => setDateFrom(event.target.value)}/>
            <input type="date" value={dateTo} onChange={(event) => setDateTo(event.target.value)}/>
            <button onClick={createRequest}>Create</button>
            <hr />
            {requests.map((request) => (
                <div key={request.id}>
                    <p>#{request.id} — ученик #{request.student_id}</p>
                    <p>{request.reason}</p>
                    <p>{request.date_from} — {request.date_to}</p>
                    <p>Статус: {request.status}</p>
                    {request.status === "pending" && (
                        <>
                            <button onClick={() => setStatus(request.id, "approved")}>Approve</button>
                            <button onClick={() => setStatus(request.id, "rejected")}>Reject</button>
                        </>
                    )}
                    <hr />
                </div>
            ))}
        </div>
    );
}