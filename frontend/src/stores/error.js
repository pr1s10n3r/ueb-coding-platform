import { writable} from "svelte/store";

export const reqError = writable(null);

export function setError(err) {
    reqError.set(err);
}