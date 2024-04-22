import { atom, selector } from 'recoil';
import { useSetRecoilState } from 'recoil';

import { signup_api } from '../Helper';

export const signupState = atom(

    // multiple states can be stored in an object

    {
        key: 'signupState',
        default: {
            role: '',
            email: '',
            password: '',
        },
    }
);


