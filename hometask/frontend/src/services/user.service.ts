import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {ITokenResponse, IUser} from '../models';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  url = 'http://localhost:8000/api/v1/';
  authData: any = {};

  constructor(private httpClient: HttpClient) { }

  createUser(userData: FormData): Observable<IUser> {
    console.log(userData);
    return this.httpClient.post<IUser>(this.url + 'users/add/', userData);
  }


  authenticateUser(user: any): Observable<ITokenResponse> {
    return this.httpClient.post<ITokenResponse>(this.url + 'auth/', user);
  }


}
