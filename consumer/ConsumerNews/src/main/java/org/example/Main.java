package org.example;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.example.properties.KafkaProperties;
import org.example.utils.ETopic;
import org.example.utils.StringHandler;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.time.Duration;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        JSONParser parser = new JSONParser();
        try (Consumer<String, String> consumer = new KafkaConsumer<>(KafkaProperties.getInstance())) {
            consumer.subscribe(Arrays.asList(ETopic.NEWSPAPER.getTopicName(), ETopic.NEWS_2.getTopicName(), ETopic.NEWS_3.getTopicName()));

            try {
                while (true) {
                    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));

                    for (ConsumerRecord<String, String> record : records) {
                        JSONObject jsonObject = (JSONObject) parser.parse(record.value());

                        String title = (String) jsonObject.get("title");
                        String content = (String) jsonObject.get("content");
                        String date = (String) jsonObject.get("date");
                        String url = (String) jsonObject.get("url");

                        if (!StringHandler.emptyString(content)) {
                            content = StringHandler.simpleConvertHtmlToText(content);
                        } else {
                            content = "None";
                        }

                        System.out.println("Offset: " + record.offset());
                        System.out.println("Topic: " + record.topic());
                        System.out.println("Title: " + (title != null ? title : "None"));
                        System.out.println("Content: " + content);
                        System.out.println("Date: " + (date != null ? date : "None"));
                        System.out.println("Url: " + (url != null ? url : "None"));
                        System.out.println("-------------------------------------------------------------------");
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}