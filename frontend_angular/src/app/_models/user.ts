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

export class UserData{
  firstName: string;
  lastName: string;
  username: string;
  email: string;
  personal_account_number: string;
  city: string;
  street: string;
  house: string;
  flat: string;
}

