const express = require('express');
const cors = require('cors');
const mongodb = require('mongodb');
const bcrypt = require('bcrypt');
const bodyParser = require('body-parser');

const MongoClient = mongodb.MongoClient;
const app = express();
app.use(cors());
app.use(express.json());
app.use(bodyParser.json());

const mongoUri = "mongodb+srv://esdmuse:esdmuse@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(mongoUri, { useNewUrlParser: true, useUnifiedTopology: true, tlsAllowInvalidCertificates: true });

app.post('/auth/authenticate', async (req, res) => {
    const email = req.body.email;
    const password = req.body.password;

    try {
        await client.connect();
        const db = client.db('ESD_Muse');
        const user = await db.collection('user').findOne({ email: email });

        if (user) {
            const stored_hash = user.password.toString(); // Ensure the stored hash is a string
            if (bcrypt.compareSync(password, stored_hash)) {
                res.json({ success: true, access_token: email });
            } else {
                res.json({ success: false });
            }
        } else {
            res.json({ success: false });
        }
    } catch (err) {
        console.error('Error in /api/authenticate:', err); // Log the error message
        res.status(500).json({ success: false });
    }
});

app.post('/auth/createUser', async (req, res) => {
    const email = req.body.email;
    const password = req.body.password;
    const hashedPassword = bcrypt.hashSync(password, bcrypt.genSaltSync());

    try {
        await client.connect();
        const db = client.db('ESD_Muse');
        await db.collection('user').insertOne({ email: email, password: hashedPassword });
        res.json({ success: true });
    } catch (err) {
        res.status(500).json({ success: false });
    }
});

const port = process.env.PORT || 5003;
app.listen(port, () => {
console.log(`Listening on port ${port}`);
});