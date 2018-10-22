package com.ssm.service.impl;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import com.ssm.Dao.GoodsInfoMapper;
import com.ssm.service.GoodsService;



@Service("goodsService")
public class GoodsServiceImpl implements GoodsService{
	@Resource
	private GoodsInfoMapper goods;
}
