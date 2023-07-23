package com.codepoet.website.mapper;

import com.codepoet.website.pojo.Person;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface PersonMapper {
    List<Person> findAll();
}
