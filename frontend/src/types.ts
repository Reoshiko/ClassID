export interface Student {
    id: number
    first_name: string
    last_name: string
    middle_name: string | null
    class_id: number
    qr_token: string
}

export interface SchoolClass {
    id: number
    name: string
}

export type AttendanceEventType =
  | "school_enter"
  | "school_exit"
  | "lesson_present"
  | "boarding_present"

export type AttendanceSource = 
  | "camera"
  | "teacher"
  | "scanner"

export interface AttendanceEvent {
    id: number
    student_id: number
    event_type: AttendanceEventType
    source: AttendanceSource
    created_at: string
}

export type AbsenceStatus =
  | "pending"
  | "approved"
  | "rejected"

export interface AbsenceRequest {
    id: number
    student_id: number
    reason: string
    date_from: string
    date_to: string
    status: AbsenceStatus
}