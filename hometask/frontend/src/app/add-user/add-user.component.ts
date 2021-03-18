import {Component, OnInit} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {UserService} from '../../services';
import {IProfile, IUser} from "../../models";

@Component({
  selector: 'app-add-full-user',
  templateUrl: './add-user.component.html',
  styleUrls: ['./add-user.component.css']
})

export class AddUserComponent {
  formData: FormData;
  photoToUpload: File;
  fullInfoFlag = false;

  error: any;

  email = new FormControl();
  password = new FormControl();
  name = new FormControl();
  surname = new FormControl();
  age = new FormControl();
  profession = new FormControl();
  photo = new FormControl();
  form = new FormGroup({
    email: this.email,
    password: this.password,
    name: this.name,
    surname: this.surname,
    age: this.age,
    profession: this.profession,
    photo: this.photo
  });

  constructor(private userService: UserService) {}

  saveUser(): void {
    this.formData = new FormData();
    if (this.fullInfoFlag) {
      for (const [key, value] of Object.entries(this.form.getRawValue())) {
        this.formData.append(key, String(value));
      }
      this.formData.set('photo', this.photoToUpload);
      this.userService.createUser(this.formData)
        .subscribe(response => window.alert('Created full user successfully!'),
                    error => this.error = error.error);
    } else {
      this.formData.append('email', this.form.getRawValue().email);
      this.formData.append('password', this.form.getRawValue().password);

      this.userService.createUser(this.formData)
        .subscribe(response => window.alert('Created simple user successfully!'),
                    error => this.error = error.error);
    }
  }

  handleInputFile(target): void {
    this.photoToUpload = target.files[0];
  }

  allowFullInfo(): void {
    this.fullInfoFlag = !this.fullInfoFlag;
  }

}
