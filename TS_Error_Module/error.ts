import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { MongoClient, MongoError, InsertOneResult } from 'mongodb';
import * as amqp from 'amqplib/callback_api';
import { Channel } from 'amqplib/callback_api';

const hostname = process.env.rabbit_host || 'localhost';
const port = parseInt(process.env.rabbit_port || '5672');

let connection: amqp.Connection;
let channel: amqp.Channel;

dotenv.config({ path: 'spotify_api_keys.env' });

const user = process.env.user;
const password = process.env.password;

const mongoUri = `mongodb+srv://${user}:${password}@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority`;
const client = new MongoClient(mongoUri);

const app = express();
app.use(cors());
app.use(express.json());

client.connect()
const db = client.db('ESD_Muse');


app.post('/api/v1/error', (req, res) => {
checkSetup((channel: Channel) => {
    const queue_name = 'Error';
    channel.consume(queue_name, (msg) => {
    if (msg) {
        processError(db, msg.content.toString());
    }
    }, { noAck: true });

    const queue_name2 = 'Error2';
    channel.consume(queue_name2, (msg) => {
        if (msg) {
            processError(db, msg.content.toString());
        }
    }, { noAck: true });
});

res.status(200).json({ message: 'Error sent to error microservice' });
});

app.listen(4997, () => {
console.log('Error microservice running on port 4997');
});

function checkSetup(callback: (channel: Channel) => void) {
    amqp.connect(`amqp://${hostname}:${port}`, (err, conn) => {
        if (err) throw err;

        conn.createChannel((err, channel) => {
            if (err) throw err;

            channel.assertExchange('group_topic', 'topic', { durable: true });
            channel.assertExchange('top_topic', 'topic', { durable: true });

            channel.assertQueue('Error', { durable: true }, (err, q) => {
                if (err) throw err;
                channel.bindQueue(q.queue, 'group_topic', '*.error');
                callback(channel);
            });
            channel.assertQueue('Error2', { durable: true }, (err, q) => {
                if (err) throw err;
                channel.bindQueue(q.queue, 'top_topic', '*.error');
                callback(channel);
            });
        });
    });
}

function processError(db: any, errorMsg: string) {
    console.log('Printing the error message:');

    try {
        const error = JSON.parse(errorMsg);
        console.log('--JSON:', error);

        db.collection('error_log').insertOne({
            email: 'digijar@live.com',
            code: error.code,
            message: error.message,
        }, (err: MongoError | null, res: InsertOneResult<any>) => {
            if (err) {
                console.error('Error inserting error log:', err);
            } else {
                console.log('Error log inserted successfully:', res);
            }
        });
    } catch (e) {
        console.log('--NOT JSON:', e);
        console.log('--DATA:', errorMsg);
    }
    console.log();
}