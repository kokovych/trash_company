export class User {
  email: string;
  password: string;
  id: number;

}

export class UserLoginData {
  success: string;
  token: string;
}

export class UserRegistrationData{
  firstName: string;
  lastName: string;
  username: string;
  email: string;
  password: string;
  passwordConfirm: string;
}

