package com.ssm.service.impl;
import java.util.regex.*;
import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import com.ssm.Dao.UserInfoMapper;
//import com.ssm.Dao.UserMapper;
//import com.ssm.domain.User;
import com.ssm.domain.UserInfo;
import com.ssm.service.UserService;
import com.ssm.util.GetSha1;



@Service("userService")
public class UserServiceImpl implements UserService{
	@Resource
	private UserInfoMapper userdao;
//	@Resource
//	private UserMapper userda;

	public UserInfo getUserById(int userId) {
		UserInfo user = userdao.selectByPrimaryKey(userId);
		return user;
	}

	public UserInfo Login_handle(String username, String password) {
//		User use = userda.selectByPrimaryKey(1);
//		System.out.println(use.getId());          
		UserInfo user = userdao.getUserByName(username);
		//System.out.println(GetSha1.getSha1(password));
		//System.out.println(user);// 测试成功返回正常
		if (user != null && user.getUpwd().equals(GetSha1.getSha1(password))) {
			System.out.println(GetSha1.getSha1(password));
			return user;
		} else {
			return null;
		}
	}
	public boolean isregistername_check(String username) {
		UserInfo user = userdao.getUserByName(username);
		if (user != null) {
			return true;
		}
		return false;
	}
	public String site_handle(UserInfo us) {
		userdao.updateByPrimaryKeySelective(us);
		return null;
	}
	public String Register_handle(UserInfo us,String cpwd,String allow) {
		//System.out.println(us.getUname()+""+us.getUemail());
		UserInfo user = userdao.getUserByName(us.getUname());
		if (user == null) {
			if (us.getUemail() != "" && us.getUpwd() != "" &&us.getUname()!= "") {
				if (us.getUpwd().equals(cpwd)) {
					if (allow.equals("on")) {
						us.setUpwd(GetSha1.getSha1(us.getUpwd()));
						userdao.insert(us);
						return null;
					} else {
						return "请先同意协议";
					}
				} else {
					return "密码不一致";
				}
			} else {
				return "输入内容不能为空";
			}
		} else {
			return "用户名已注册";
		}	
	}

}
