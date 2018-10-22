
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">  
<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8" %> 
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<meta http-equiv="content-language" content="zh-CN" />
	<title>天天生鲜-${title}</title>
	<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/static/css/reset.css">
	<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/static/css/main.css">
	<script src ="${pageContext.request.contextPath}/static/js/jquery-1.12.4.min.js"></script> 
	<rapid:block name="import"></rapid:block>  
</head>
<body>

<rapid:block name="body"></rapid:block>  
<rapid:block name="footer">
	<div class="footer no-mp">
		<div class="foot_link">
			<a href="#">关于我们</a>
			<span>|</span>
			<a href="#">联系我们</a>
			<span>|</span>
			<a href="#">招聘人才</a>
			<span>|</span>
			<a href="#">友情链接</a>		
		</div>
		<p>CopyRight © 2016 北京天天生鲜信息技术有限公司 All Rights Reserved</p>
		<p>电话：010-****888    京ICP备*******8号</p>
	</div>
</rapid:block>  
</body>
</html>