package com.codepoet.website.controller;

import com.codepoet.website.pojo.Person;
import com.codepoet.website.service.PersonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class PersonController {
    private final PersonService personService;
    @Autowired
    public PersonController(PersonService personService) {
        this.personService = personService;
    }

    @RequestMapping("/introduce")
    public List<Person> introduce() {
        return personService.findAllPerson();
    }
}
