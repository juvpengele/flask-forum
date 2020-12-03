class Errors {
    constructor() {
        this.errors = {}
    }

    has(key) {
        return !! this.errors.hasOwnProperty(key);
    }

    get(key) {
        return this.errors[key][0] || null;
    }

    record(errors) {
        this.errors = errors;
    }

    clear(key) {
        delete this.errors[key];
    }

    clearAll() {
        this.errors = {};
    }

}

export default Errors;