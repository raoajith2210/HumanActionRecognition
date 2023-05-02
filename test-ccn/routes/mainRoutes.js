const express = require('express');
const mainController = require('../controllers/mainController')

const router = express.Router();

router.post('/', mainController.index);

router.get('/about', mainController.about);

router.get('/contact', mainController.contact);

router.post('/test', mainController.test);

router.post('/result', mainController.result);










module.exports = router;