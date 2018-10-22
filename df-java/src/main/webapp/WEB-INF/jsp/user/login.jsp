<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
 <%@ include file="../header.jsp" %>
 	<script>
$(function(){
	name_error = false;
	pwd_error = false;
	
	 if ("${error_login}" !=""){
//	if ("${error_login}" == "1") {
//		$('.user_error').html('用户名错误').show();
//	}
	if ("${error_login}" == "2"){
		$('.user_error').html('请先登录').show();
	}
	if ("${error_login}" == "3") {
		$('.user_error').html('用户名或密码错误').show();//pwd_error
	}
	if ("${error_login}" == "4") {
		alert("注册成功");
	//	$('.user_error').html('注册成功').show();//pwd_error
	}
}
});
</script>
</head>
<body>
<div class="login_top clearfix">
		<a href="index.html" class="login_logo"><img src="${pageContext.request.contextPath}/static/images/logo02.png"></a>	
	</div>
	<div class="login_form_bg">
		<div class="login_form_wrap clearfix">
			<div class="login_banner fl"></div>
			<div class="slogan fl">日夜兼程 · 急速送达</div>
			<div class="login_form fr">
				<div class="login_title clearfix">
					<h1>用户登录</h1>
					<a href="${pageContext.request.contextPath}/user/register">立即注册</a>
				</div>
				<div class="form_input">
					<form action="login_handle" method="POST" >
						<input type="text" name="uname" class="name_input" placeholder="请输入用户名">
						<div class="user_error">输入错误</div>
						<input type="password" name="upwd" class="pass_input" placeholder="请输入密码">
						<div class="pwd_error">输入错误</div>
						<div class="more_input clearfix">
							<input type="checkbox" name="">
							<label>记住用户名</label>
							<a href="#">忘记密码</a>
						</div>
						<input type="submit" name="" value="登录" class="input_submit">
					</form>
				</div>
			</div>
		</div>
	</div>	
 <%@ include file="../footer.jsp" %>
</body>
</html>