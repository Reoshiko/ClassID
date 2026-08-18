import { BookOpen, ClipboardCheck, QrCode, School, Users } from "lucide-react";
import { NavLink, Outlet } from "react-router-dom";

const links = [{to: "/students", label: "Students", icon: Users}, {to: "/classes", label: "Classes", icon: School}, {to: "/attendance", label: "Attendance", icon: ClipboardCheck}, {to: "/scanner", label: "QR Scanner", icon: QrCode}, {to: "/absence", label: "Absences", icon: BookOpen}]

export function Layout() {
    return (
        <div className="layout">
            <aside className="sidebar">
                <div className="logi">
                    <QrCode size={28} />
                    <span>ClassID</span>
                </div>
            <nav>
                {links.map((link) => {
                    const Icon = link.icon;
                        return (
                            <NavLink key={link.to} to={link.to} className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>
                                <Icon size={20} />
                                {link.label}
                            </NavLink>);
                    })}
            </nav>
            </aside>
            <main className="content">
                <Outlet />
            </main>
        </div>
    )
}