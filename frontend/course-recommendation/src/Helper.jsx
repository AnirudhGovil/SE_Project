
// declare base api url and export it

const BaseUrl = 'http://localhost:5000/api';
const login_api = BaseUrl + '/auth/login';
const signup_api = BaseUrl + '/auth/signup';



export {
    BaseUrl, 
    login_api, 
    signup_api,
    
};