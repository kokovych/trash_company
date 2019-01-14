import { Injectable } from '@angular/core';
import { HttpClient  } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { UserRegistrationData } from '../_models/user';
import { environment} from "../../environments/environment";

@Injectable()
export class RegistrationUserService {
  constructor(
    private httpClient: HttpClient) { }
  registrationUserUrl = environment.baseUrl + 'api/user/registration/';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  };
  registrationUser(_userRegistration: UserRegistrationData): Observable<any>{
    return this.httpClient.post<any>(this.registrationUserUrl, _userRegistration, this.httpOptions)
  }
}
