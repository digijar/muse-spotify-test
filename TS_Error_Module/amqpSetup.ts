import * as amqp from 'amqplib/callback_api';

const hostname = process.env.RABBIT_HOST || 'localhost';
const port = parseInt(process.env.RABBIT_PORT || '5672');
const exchangename = 'group_topic';
const exchangetype = 'topic';

let connection: amqp.Connection;
let channel: amqp.Channel;

export function checkSetup(callback: () => void): void {
    amqp.connect(`amqp://${hostname}:${port}`, (err, conn) => {
        if (err) {
        console.error('AMQP Error:', err);
        console.error('...creating a new connection.');
        return;
        }
        connection = conn;
        connection.createChannel((err, ch) => {
        if (err) throw err;
        channel = ch;
        channel.assertExchange(exchangename, exchangetype, { durable: true });
        callback();
        });
    });
}

export function getChannel(): amqp.Channel {
    return channel;
}