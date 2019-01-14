import { Injectable } from '@angular/core';
import { HttpClient  } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { User, UserLoginData } from '../_models/user';
import {environment} from '../../environments/environment';

@Injectable()
export class UserDataService {
  constructor(
    private httpClient: HttpClient) { }
  userDataUrl = environment.baseUrl + 'api/user/';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };
  getUserData(): Observable<any>{
    return this.httpClient.get<any>(this.userDataUrl, this.httpOptions)
  }
}
