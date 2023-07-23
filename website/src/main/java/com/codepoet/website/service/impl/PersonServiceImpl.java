package com.codepoet.website.service.impl;

import com.codepoet.website.mapper.PersonMapper;
import com.codepoet.website.pojo.Person;
import com.codepoet.website.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("PersonService")
public class PersonServiceImpl implements PersonService {

    private final PersonMapper personMapper;

    @Autowired
    public PersonServiceImpl(PersonMapper personMapper) {
        this.personMapper = personMapper;
    }

    @Override
    public List<Person> findAllPerson() {
        List<Person> personList = personMapper.findAll();
        personList.forEach(person -> {
            String hobby = person.getHobby();
            person.setHobby(hobby.replace("|", "、"));
        });
        return personList;
    }
}
