import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {UserService} from '../../services';

@Component({
  selector: 'app-authentication',
  templateUrl: './authentication.component.html',
  styleUrls: ['./authentication.component.css']
})
export class AuthenticationComponent{
  error: any;
  email = new FormControl();
  password = new FormControl();
  form = new FormGroup({
    email: this.email,
    password: this.password
  });

  constructor(private userService: UserService) {
  }

  save(): void {
    this.userService.authenticateUser(this.form.getRawValue())
      .subscribe(response => {
        window.localStorage.setItem('accessToken', response.access);
        window.localStorage.setItem('refreshToken', response.refresh);
        window.alert('Authenticate successfully!'); },
          error => this.error = error.error);
  }
}
