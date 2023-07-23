package com.codepoet.website.pojo;

import lombok.Data;

import java.sql.Date;

@Data
public class Person {
    private String personId;
    private String name;
    private Date birthDay;
    private String dreamCar;
    private String hobby;
}
