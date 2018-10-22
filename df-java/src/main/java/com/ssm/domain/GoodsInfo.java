package com.ssm.domain;

import java.math.BigDecimal;

public class GoodsInfo {
    private Integer id;

    private String gtitle;

    private String gpic;

    private BigDecimal gprice;

    private String gunit;

    private Integer gclick;

    private String gjianjie;

    private Integer gkucun;

    private Boolean isdelete;

    private Integer gtypeId;

    private String gcontent;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getGtitle() {
        return gtitle;
    }

    public void setGtitle(String gtitle) {
        this.gtitle = gtitle == null ? null : gtitle.trim();
    }

    public String getGpic() {
        return gpic;
    }

    public void setGpic(String gpic) {
        this.gpic = gpic == null ? null : gpic.trim();
    }

    public BigDecimal getGprice() {
        return gprice;
    }

    public void setGprice(BigDecimal gprice) {
        this.gprice = gprice;
    }

    public String getGunit() {
        return gunit;
    }

    public void setGunit(String gunit) {
        this.gunit = gunit == null ? null : gunit.trim();
    }

    public Integer getGclick() {
        return gclick;
    }

    public void setGclick(Integer gclick) {
        this.gclick = gclick;
    }

    public String getGjianjie() {
        return gjianjie;
    }

    public void setGjianjie(String gjianjie) {
        this.gjianjie = gjianjie == null ? null : gjianjie.trim();
    }

    public Integer getGkucun() {
        return gkucun;
    }

    public void setGkucun(Integer gkucun) {
        this.gkucun = gkucun;
    }

    public Boolean getIsdelete() {
        return isdelete;
    }

    public void setIsdelete(Boolean isdelete) {
        this.isdelete = isdelete;
    }

    public Integer getGtypeId() {
        return gtypeId;
    }

    public void setGtypeId(Integer gtypeId) {
        this.gtypeId = gtypeId;
    }

    public String getGcontent() {
        return gcontent;
    }

    public void setGcontent(String gcontent) {
        this.gcontent = gcontent == null ? null : gcontent.trim();
    }
}