package com.hyb.rabbbitmq.controller;

import com.rabbitmq.client.AMQP;
import org.springframework.amqp.core.Queue;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author hyb
 * @date 2018/12/3 10:33
 */
@Configuration
public class RabbitmqConfig {
    @Bean
    public Queue helloQueue(){
        // 创建一个队列
        return new Queue("hello");
    }
}
