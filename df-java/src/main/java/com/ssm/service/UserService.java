package com.ssm.service;

//import com.ssm.domain.User;
import com.ssm.domain.UserInfo;

public interface UserService {
    public UserInfo getUserById(int userId);
    public UserInfo Login_handle(String username, String password);
    public boolean isregistername_check(String username);
	public String Register_handle(UserInfo us,String cpwd,String allow);
	public String site_handle(UserInfo us);
}
