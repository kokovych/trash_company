import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor(private router: Router) {
    this.router.routeReuseStrategy.shouldReuseRoute = function() {
      return false;
    };
  }

  ngOnInit() {
    let auth_token = localStorage.getItem(
      'auth_token'
    );
    console.log('auth_token');
    if(auth_token){
      localStorage.removeItem('auth_token');
    }
    this.router.navigate(['/']);
  }

}
