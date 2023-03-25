class Writing {

    constructor() {
        this.run = false;
        this.startTime = null;
        this.timeSinceStroke = 0;
        this.danger = 2;
        this.kill = 5;
        this.timerID = null;
        this.words = '';
    }

    now = () => {
        return new Date().getTime() / 1000;
    }

    win = () => {
        this.stopWriting();
        setTimeout(() => alert('You WIN!'), 100);
    }

    fail = () => {
        this.stopWriting();
        setTimeout(() => alert('You lose! You have written ' + this.words + '.'), 100);
    }

    tick = () => {
        if (!this.run) return;
        console.log(this.timeSinceStroke, this.kill)
        if (this.timeSinceStroke >= this.danger) {
            const editor = document.getElementById('editor')
            if (!editor.classList.contains('danger')) editor.classList.add('danger');
            const body = document.body
            if (!body.classList.contains('danger')) body.classList.add('danger');
        } else {
            document.getElementById('editor').classList.remove('danger');
            document.body.classList.remove('danger');
        }
        if (this.timeSinceStroke >= this.kill) return this.fail();
        this.timeSinceStroke += 0.1;
    }

    startWriting = () => {
        this.run = true;
        this.startTime = this.now();
        this.timeSinceStroke = 0;
        const text = document.getElementById('text').value;
        const words = text.trim().length && text.trim().split(/\s+/).length;
        this.words = words + (words === 1 ? ' word' : ' words');
        document.getElementById('wordcount').innerHTML = this.words;
        console.log(this.timeSinceStroke, this.kill)
        if (words >= 100) return this.win();
        if (!this.timerID) this.timerID = setInterval(() => this.tick(), 100);
    }

    stopWriting = () => {
        clearInterval(this.timerID);
        this.timerID = null;
        this.run = false;
        document.getElementById('text').value = '';
        document.body.classList.remove('danger');
        document.getElementById('editor').classList.remove('danger');
        document.getElementById('wordcount').innerHTML = '0 words';
    }

}

const startApp = () => {
    const app = new Writing();
    document.getElementById('text').addEventListener('keydown', app.startWriting);
}

window.addEventListener('load', startApp);
