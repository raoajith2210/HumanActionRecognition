
const http = require('http');

const FormData = require('form-data');
const fs = require('fs');
const multer = require('multer');

exports.index = (req, res) => {
    res.render('index')
};

exports.about = (req, res) => {
    res.render('./about');
};

exports.contact = (req, res) => {
    res.render('./contact');
};

exports.result = (req, res, next) => {
    const dataToRender = req.body.dataToRender;
    res.render('./result', {dataToRender});
}


exports.test = (reqs, ress, next) => {
    // Define the form data to be sent
    // const upload = multer({ dest: './back-end/' });
    console.log("reqs.file")
    const storage = multer.diskStorage({
        destination: function (req, file, cb) {
          cb(null, './back-end'); // Directory where files will be uploaded
        },
        filename: function (req, file, cb) {
          cb(null, file.originalname); // Set the filename to be the original filename
        }
      });
      
    const upload = multer({ storage: storage, limits: { fileSize: 100 * 1024 * 1024 } });
    upload.single('file')(reqs, ress, function (err) {
        if (err instanceof multer.MulterError) {
            // Handle multer error
            console.error(err);
            // Send an appropriate response or throw an error as needed
        } else if (err) {
            // Handle other errors
            console.error(err);
            // Send an appropriate response or throw an error as needed
        }

        // File data can now be accessed from reqs.file
        const file = reqs.file;
        console.log(file); // Access file data as needed


        // Create a readable stream from the file path
        const fileStream = fs.createReadStream(file.path);
        
        const formData = new FormData();

        formData.append('file', fileStream); // Append the file stream to the form data
        formData.append('originalname', file.originalname);
        // Define the options for the HTTP request
        const options = {
            hostname: '44.204.16.217',
            port: 80,
            path: '/upload',
            method: 'POST',
            headers: formData.getHeaders() // Set the headers from the form data
        };
    
        // Send the HTTP request

        const req = http.request(options, res => {
            let responseData = '';
            res.on('data', data => {
                responseData = data.toString();
                console.log(data.toString());
                // io.emit('data', data.toString())
                // $('#responseContainer').append(data.toString());
            });

            res.on('end', () => {
                // After receiving all data, render it in the frontend view
                const dataToRender = responseData;
                ress.json(dataToRender) // Assuming the data received is in JSON format
                // ress.render('./result', { dataToRender }); // Modify this line to pass the data to your view
            });
        });
        req.on('error', error => {
            console.error(error);
        });
        formData.pipe(req); // Pipe the form data to the request
    });
};






