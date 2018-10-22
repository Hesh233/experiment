package com.ssm.service.impl;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import com.ssm.Dao.CartInfoMapper;
import com.ssm.service.CartService;



@Service("cartService")
public class CartServiceImpl implements CartService{
	@Resource
	private CartInfoMapper cart;
}
