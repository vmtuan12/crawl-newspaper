package org.example.utils;

public enum ETopic {
    NEWSPAPER("newspaper"),
    NEWS_2("news2"),
    NEWS_3("news3");;

    private final String topicName;

    ETopic(String topicName) {
        this.topicName = topicName;
    }

    public String getTopicName() {
        return topicName;
    }
}
