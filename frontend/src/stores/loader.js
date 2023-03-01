import { writable } from "svelte/store";

export const files = writable([]);

export function addFile(file) {
  files.update((list) => {
    list.push(file);
    return list;
  });
}
