//import javax.annotation.Resource;
//
//import org.apache.log4j.Logger;
//import org.junit.Before;
//import org.junit.Test;
//import org.junit.runner.RunWith;
//import org.springframework.context.ApplicationContext;
//import org.springframework.context.support.ClassPathXmlApplicationContext;
//import org.springframework.test.context.ContextConfiguration;
//import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
//
//import com.alibaba.fastjson.JSON;
//import com.ssm.domain.User;
//import com.ssm.service.UserService1;
// 
//@RunWith(SpringJUnit4ClassRunner.class)		//��ʾ�̳���SpringJUnit4ClassRunner��
//@ContextConfiguration(locations = {"classpath:spring-mybatis.xml"})
// 
//public class TestMybatis {
//    private static Logger logger = Logger.getLogger(TestMybatis.class);
//     // private ApplicationContext ac = null;
//    @Resource
//    private UserService1 userService1 = null;
//
////  @Before
////  public void before() {
////      ac = new ClassPathXmlApplicationContext("applicationContext.xml");
////      userService = (UserService) ac.getBean("userService");
////  }
//
//    @Test
//    public void test1() {
//        User user = userService1.getUserById(1);
//        // System.out.println(user.getUserName());
//        // logger.info("ֵ��"+user.getUserName());
//        logger.info(JSON.toJSONString(user));
//    }
//}
