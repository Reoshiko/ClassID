const API_URL = import.meta.env.VITE_API_URL;

export async function api<T>(path: string, options?: RequestInit): Promise<T> {
    const response = await fetch(`${API_URL}${path}`, options)

    if (!response.ok) {
        const data = await response.json().catch(() => null)
        throw new Error(data?.detail ?? `Request failed: ${response.status}`)
    } 
    return response.json()
}