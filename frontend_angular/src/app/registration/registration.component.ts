import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, FormBuilder,  ValidationErrors, ValidatorFn, Validators} from '@angular/forms';
import { Router} from '@angular/router';
import { AbstractControl } from '@angular/forms';

import { User } from '../_models/user';
import { UserRegistrationData} from '../_models/user';
import { CheckAuthService } from "../_services/check-auth.service";
import { MustMatch } from '../_services/must-mutch.validator';
import { RegistrationUserService } from '../_services/registration.service';


@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {

  constructor(
    private router: Router,
    private _registrationUserService: RegistrationUserService,
    private _checkAuth: CheckAuthService,
    private formBuilder: FormBuilder) { }

  user: UserRegistrationData = new UserRegistrationData();
  userRegistrationForm: FormGroup;
  userIsAuthorized: boolean = this._checkAuth.isAuthorized();
  errorRregistration: boolean = false;
  keyErrorObj: string = '';
  valueErrorObj: string = '';


  ngOnInit() {
    this.userRegistrationForm = this.formBuilder.group({
      firstName: new FormControl(this.user.firstName),
      lastName: new FormControl(this.user.lastName),
      username: new FormControl(this.user.username),
      email: new FormControl(this.user.email,
        [ Validators.required, Validators.pattern('[^ @]*@[^ @]*')]),
      password: new FormControl(this.user.password,
        [ Validators.required]),
      passwordConfirm: new FormControl(this.user.passwordConfirm,
        [ Validators.required ])
    }, {
      validator: MustMatch("password", "passwordConfirm") });
  }

  // convenience getter for easy access to form fields
  get f() { return this.userRegistrationForm.controls; }

  onSubmit(user: UserRegistrationData) {
    console.log('user');
    console.log(user);
    console.log(typeof user);

    this._registrationUserService.registrationUser(user)
      .subscribe(
        data => {
          console.log("POST Request is successful ", data);
          // save token to localstorage
          // let auth_token = data.token;
          // localStorage.setItem('auth_token', auth_token);
          // redirect to main page

          console.log("before navigate");
          // this.ngZone.run(() => this.router.navigateByUrl("/"))
          this.router.navigate(['/login'], { queryParams: { "registration": "true" } });
          // window.location.href = '/';
          // window.location.reload();

        },
        error => {
          console.log("Error", error);
          this.errorRregistration = true;
          let error_obj = error.error;
          console.log(error_obj);
          this.keyErrorObj = Object.keys(error_obj)[0];
          this.valueErrorObj = Object["values"](error_obj)[0][0];
          let elementError = document.getElementById("id_errorRregistration");
          if (elementError) {
            elementError.style.display = '';
          }
        }
      );
  }

  removeErrorDescription() {
    let elementError = document.getElementById("id_errorRregistration");
    if (elementError) {
      elementError.style.display = 'none';
    }
  }

}
