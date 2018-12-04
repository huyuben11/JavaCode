package com.hyb.rabbbitmq.controller;

import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Date;

/**
 * @author hyb
 * @date 2018/12/3 10:25
 */
@Component
public class Sender {
    @Autowired
    private AmqpTemplate amqpTemplate;

    public void send(){
        String context ="hellorabbitmq";
        System.out.println("sender:" + context);
        //把context放入到队列之中
        this.amqpTemplate.convertAndSend("hello",context);
    }
}
