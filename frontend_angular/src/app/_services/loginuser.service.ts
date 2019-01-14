import { Injectable } from '@angular/core';
import { HttpClient  } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { User, UserLoginData } from '../_models/user';
import { environment} from "../../environments/environment";

@Injectable()
export class LoginUserService {
  constructor(
    private httpClient: HttpClient) { }
  loginUserUrl = environment.baseUrl + 'api/user/login/';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };
  loginUser(user: User): Observable<UserLoginData>{
    return this.httpClient.post<UserLoginData>(this.loginUserUrl, user, this.httpOptions)
  }
}
