package com.ssm.Dao;

import com.ssm.domain.CartInfo;

public interface CartInfoMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(CartInfo record);

    int insertSelective(CartInfo record);

    CartInfo selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(CartInfo record);

    int updateByPrimaryKey(CartInfo record);
}