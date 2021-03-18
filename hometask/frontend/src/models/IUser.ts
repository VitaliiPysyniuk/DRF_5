export interface IUser {
  id: number;
  email: string;
  password: string;
  is_active: boolean;
  is_staff: boolean;
  is_superuser: boolean;
  profile_id: number;
}
