import { getApiUrl } from "./config"

export async function api<T>(path: string, options?: RequestInit): Promise<T> {
    const response = await fetch(`${getApiUrl()}${path}`, options)

    if (!response.ok) {
        const data = await response.json().catch(() => null)
        throw new Error(data?.detail ?? `Request failed: ${response.status}`)
    } 
    return response.json()
}
