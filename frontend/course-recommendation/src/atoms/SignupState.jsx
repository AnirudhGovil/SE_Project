import { atom, selector } from 'recoil';
import { useSetRecoilState } from 'recoil';

export const signupState = atom(

    // multiple states can be stored in an object

    {
        key: 'signupState',
        default: {
            role: '',
            id: '',
            name: '',
            email: '',
            password: '',
        },
    }
);


