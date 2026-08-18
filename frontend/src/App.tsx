import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";
import { StudentsPage } from "./pages/StudentsPage";
import { ClassesPage } from "./pages/ClassPage";
import { AttendancePage } from "./pages/AttendancePage";
import { ScannerPage } from "./pages/ScannerPage";


export function App() {
    return (
        <BrowserRouter>
          <Routes>
            <Route element={<Layout />}>
              <Route path="/" element={<Navigate to="/students" replace />}/>
              <Route path="/students" element={<StudentsPage />}/>
              <Route path="/classes" element={<ClassesPage />}/>
              <Route path="/attendance" element={<AttendancePage />}/>
              <Route path="/scanner" element={<ScannerPage />}/>
            </Route>
          </Routes>
        </BrowserRouter>
    )
}