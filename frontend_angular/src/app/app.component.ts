import { Component, OnInit } from '@angular/core';
// import { CheckAuthService} from './_services/check-auth.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  constructor(){
    console.log('AppComponent');
  };
  title = 'Application Personal Account';
  ngOnInit() {
    console.log('in ngOnInit  AppComponent');

  }
}
