import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgbButtonsModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';
import { HomepageComponent } from './homepage/homepage.component';
import { RegistrationComponent } from './registration/registration.component';
import { LoginUserService } from './_services/loginuser.service';

import { AddHeaderInterceptor} from './_services/auth.interceptor';
import { HTTP_INTERCEPTORS} from '@angular/common/http';
import { UserDataService } from "./_services/userdata.service";
import { CheckAuthService } from "./_services/check-auth.service";
import { PageHeaderComponent } from './page-header/page-header.component';
import { LogoutComponent } from './logout/logout.component';
import {RegistrationUserService} from "./_services/registration.service";
import { PageFooterComponent } from './page-footer/page-footer.component';


@NgModule({
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule.forRoot(),
    ReactiveFormsModule,
    HttpClientModule
  ],
  declarations: [
    AppComponent,
    PageHeaderComponent,
    LoginComponent,
    HomepageComponent,
    RegistrationComponent,
    LogoutComponent,
    PageFooterComponent,
  ],
  providers: [
    LoginUserService,
    RegistrationUserService,
    UserDataService,
    CheckAuthService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AddHeaderInterceptor,
      multi: true,
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
