package org.example.utils;

public class StringHandler {

    public static String simpleConvertHtmlToText(String html) {

        html = html.trim();

        // replace tags
        html = html.replaceAll("<[^>]*>", "");

        // replace nextlines and tabs
        html = html.replaceAll("\n", "");
        html = html.replaceAll("\r", "");

        // fix whitespace
        html = html.replaceAll(" {2,}", " ");

        return html;
    }

    public static boolean emptyString(String s) {
        return s == null || s.length() == 0;
    }
}
