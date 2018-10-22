package com.ssm.Dao;

import org.apache.ibatis.annotations.Param;


import com.ssm.domain.UserInfo;

public interface UserInfoMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(UserInfo record);

    int insertSelective(UserInfo record);

    UserInfo selectByPrimaryKey(Integer id);
    
    public UserInfo getUserByName(@Param(value="username")String username);

    int updateByPrimaryKeySelective(UserInfo record);

    int updateByPrimaryKey(UserInfo record);
}