import { Injectable } from '@angular/core';


@Injectable()
export class CheckAuthService {
  constructor() { }

  isAuthorized(): boolean{
    let auth_token = localStorage.getItem(
      'auth_token'
    );

    if (auth_token){
      console.log(auth_token);
      return true;
    }
    return false;
  }
}
