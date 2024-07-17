import { initializeApp } from "https://";

const firebaseConfig = {
    apiKey: "",
    authDomain: "",
    databaseURL: "https://",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: "",
    measurementId: ""
};

const app = initializeApp(firebaseConfig);
export {app}

console.log("Script loaded");