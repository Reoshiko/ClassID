import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";


export function App() {
    return (
        <BrowserRouter>
          <Routes>
            <Route element={<Layout />}>
              <Route path="/" element={<Navigate to="/students" replace />}/>
            </Route>
          </Routes>
        </BrowserRouter>
    )
}