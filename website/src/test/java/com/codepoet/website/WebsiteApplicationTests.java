package com.codepoet.website;

import com.codepoet.website.mapper.PersonMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class WebsiteApplicationTests {

    @Autowired
    private PersonMapper personMapper;

    @Test
    public void testFindAll() {
        System.out.println(personMapper.findAll());
    }

}
