
// declare base api url and export it
const AuthUrl = 'http://localhost:8080';

const student_base_auth_url = AuthUrl
const instructor_base_auth_url = AuthUrl

const login_student_api = student_base_auth_url + '/login/student';
const signup_student_api = student_base_auth_url + '/sign_up/student';

const login_instructor_api = instructor_base_auth_url + '/login/instructor';
const signup_instructor_api = instructor_base_auth_url + '/sign_up/instructor';


const CourseUrl = 'http://localhost:8080';

const student_base_course_url = CourseUrl
const instructor_base_course_url = CourseUrl

// http://localhost:8080/courses/instructor
const my_courses_instructor_api = instructor_base_course_url + '/courses/instructor/';
const courses_instructor_api = instructor_base_course_url + '/courses/';
const my_courses_student_api = student_base_course_url + '/courses/student/';


export {
    my_courses_instructor_api,
    courses_instructor_api,

    AuthUrl,

    login_student_api,
    login_instructor_api,
    signup_student_api,
    signup_instructor_api

};