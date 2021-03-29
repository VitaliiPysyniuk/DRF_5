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
  userProfile: IProfile;
  fullInfoFlag = false;
  shortData: any = null;
  fullData: any = null;
  error: any;

  email = new FormControl('a@gmail.com');
  password = new FormControl('xxx');
  name = new FormControl('xx');
  surname = new FormControl('xx');
  age = new FormControl(3);
  profession = new FormControl('xxx');
  photo = new FormControl();

  fullUserForm = new FormGroup({
    name: this.name,
    surname: this.surname,
    age: this.age,
    profession: this.profession,
    photo: this.photo
  });

  simpleUserForm = new FormGroup({
    email: this.email,
    password: this.password,
    profile: this.fullUserForm
  });



  constructor(private userService: UserService) {}


  // saveUser(): void {
  //   this.formData = new FormData();
  //   if (this.fullInfoFlag) {
  //     for (const [key, value] of Object.entries(this.form.getRawValue())) {
  //       this.formData.append(key, String(value));
  //     }
  //     this.formData.set('photo', this.photoToUpload);
  //     this.userService.createUser(this.formData)
  //       .subscribe(response => window.alert('Created full user successfully!'),
  //                   error => this.error = error.error);
  //   } else {
  //     this.formData.append('email', this.form.getRawValue().email);
  //     this.formData.append('password', this.form.getRawValue().password);
  //
  //     this.userService.createUser(this.formData)
  //       .subscribe(response => window.alert('Created simple user successfully!'),
  //                   error => this.error = error.error);
  //   }
  // }

  saveUser(): void {
    this.shortData = this.simpleUserForm.getRawValue();
    this.shortData.profile.photo = this.photoToUpload;
    this.formData = new FormData();
    this.formData.append('email', this.shortData.email);
    this.formData.append('password', this.shortData.password);
    this.userProfile = this.shortData.profile;

    if (this.fullInfoFlag) {
      this.formData.append('profile', JSON.stringify(this.userProfile));
      this.userService.createUser(this.formData)
        .subscribe(response => window.alert('Created full user successfully!'),
                    error => this.error = error.error);
    } else {
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
