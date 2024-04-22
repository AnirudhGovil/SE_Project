import {atom, selector } from 'recoil';
import { useSetRecoilState } from 'recoil';

export const loginState = atom(

    // multiple states can be stored in an object

    {
        key: 'loginState',
        default: {
            role: '',
            id: '',
            password: '',
        },
    }

);