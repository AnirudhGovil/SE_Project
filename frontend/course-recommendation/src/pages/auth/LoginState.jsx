import {atom, selector } from 'recoil';
import { useSetRecoilState } from 'recoil';

import { login_api } from '../../Helper';

export const loginState = atom(

    // multiple states can be stored in an object

    {
        key: 'loginState',
        default: {
            token: '',
            username: '',
            loggedIn: false,
        },
    }


);