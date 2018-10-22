package com.ssm.service.impl;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import com.ssm.Dao.TypeInfoMapper;
import com.ssm.service.TypeService;



@Service("typeService")
public class TypeServiceImpl implements TypeService{
	@Resource
	private TypeInfoMapper type;
}
