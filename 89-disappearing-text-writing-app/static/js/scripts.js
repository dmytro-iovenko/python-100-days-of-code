class Writing {

    constructor() {
        this.run = false;
        this.startTime = null;
        this.timeSinceStroke = 0;
        this.kill = 5;
        this.timerID = null;
    }

    now = () => {
        return new Date().getTime() / 1000;
    }

    fail = () => {
      this.stopWriting();
    }

    tick = () => {
        if (!this.run) return;
        console.log(this.timeSinceStroke, this.kill)
        if (this.timeSinceStroke >= this.kill) return this.fail();
        this.timeSinceStroke += 0.1;
    }

    startWriting = () => {
        this.run = true;
        this.startTime = this.now();
        this.timeSinceStroke = 0;
        console.log(this.timeSinceStroke, this.kill)
        if (!this.timerID) this.timerID = setInterval(() => this.tick(), 100);
    }

    stopWriting = () => {
        clearInterval(this.timerID);
        this.timerID = null;
        document.getElementById('text').value = '';
    }

}

const startApp = () => {
    const app = new Writing();
    document.getElementById('text').addEventListener('keyup', app.startWriting);
}

window.addEventListener('load', startApp);
