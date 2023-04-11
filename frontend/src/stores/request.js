import { writable } from "svelte/store";

export const reqFormData = writable(new FormData());

export function setFiles(files) {
  reqFormData.update((fd) => {
    files.forEach((file) => {
      console.log(`Adding ${file.name} file`);
      fd.append("file", file);
    });

    console.log("FormData files set");
    console.log(fd);

    return fd;
  });
}

export function clearRequestData() {
  reqFormData.set(new FormData());
}

export function setEvaluationCriteria(input, output, complexity, time, func) {
  reqFormData.update((fd) => {
    fd.append("input", input);
    fd.append("output", output);
    fd.append("complexity", complexity);
    fd.append("time", time);
    fd.append("function", func);

    console.log(`FormData evaluation criteria set`);
    console.log(fd);

    return fd;
  });
}
