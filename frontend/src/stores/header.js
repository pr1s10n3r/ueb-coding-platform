import { writable } from "svelte/store";

export const activeTab = writable(0);

export const Headers = {
    Loader: 0,
    EvaluationCriteria: 1,
    Results: 2,
    Error: 3,
};

export function goToTabById(index) {
    activeTab.set(index);
}
