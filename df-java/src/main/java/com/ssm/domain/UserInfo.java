package com.ssm.domain;

public class UserInfo {
    private Integer id;

    private String uname;

    private String upwd;

    private String uemail;

    private String ushou;

    private String uphone;

    private String uaddress;

    private String uyoubian;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getUname() {
        return uname;
    }

    public void setUname(String uname) {
        this.uname = uname == null ? null : uname.trim();
    }

    public String getUpwd() {
        return upwd;
    }

    public void setUpwd(String upwd) {
        this.upwd = upwd == null ? null : upwd.trim();
    }

    public String getUemail() {
        return uemail;
    }

    public void setUemail(String uemail) {
        this.uemail = uemail == null ? null : uemail.trim();
    }

    public String getUshou() {
        return ushou;
    }

    public void setUshou(String ushou) {
        this.ushou = ushou == null ? null : ushou.trim();
    }

    public String getUphone() {
        return uphone;
    }

    public void setUphone(String uphone) {
        this.uphone = uphone == null ? null : uphone.trim();
    }

    public String getUaddress() {
        return uaddress;
    }

    public void setUaddress(String uaddress) {
        this.uaddress = uaddress == null ? null : uaddress.trim();
    }

    public String getUyoubian() {
        return uyoubian;
    }

    public void setUyoubian(String uyoubian) {
        this.uyoubian = uyoubian == null ? null : uyoubian.trim();
    }
}