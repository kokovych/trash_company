import { Component, OnInit } from '@angular/core';

import {CheckAuthService} from '../_services/check-auth.service';

@Component({
  selector: 'app-page-header',
  templateUrl: './page-header.component.html',
  styleUrls: ['./page-header.component.css']
})
export class PageHeaderComponent implements OnInit {

  constructor(private _checkAuth: CheckAuthService) { }
  userIsAuthorized: boolean = this._checkAuth.isAuthorized();
  ngOnInit() {
    console.log("you are in ngOnInit PageHeaderComponent");
    console.log(this.userIsAuthorized);
  }

}
