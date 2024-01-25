create table website
(
    id       int auto_increment
        primary key,
    domain   varchar(100) null,
    category json         null
);

create table x_path_category
(
    id         int auto_increment
        primary key,
    website_id int          null,
    x_path     varchar(500) null,
    constraint x_path_to_website
        foreign key (website_id) references website (id)
);

create table x_path_content
(
    id         int auto_increment
        primary key,
    website_id int          null,
    title      varchar(500) null,
    content    text         null,
    date       varchar(500) null,
    constraint x_path_content_to_website
        foreign key (website_id) references website (id)
);

insert into newspaper.website (id, domain, category)
values  (1, 'https://vietnamnet.vn/', '["thoi-su/", "kinh-doanh/", "giai-tri/", "the-gioi/"]'),
        (2, 'https://nhandan.vn/', '["moi-truong/", "y-te/", "khoahoc-congnghe/"]');

insert into newspaper.x_path_category (id, website_id, x_path)
values  (1, 1, '//div[@class=''main'']//div[@class=''container__left'']'),
        (2, 2, '//*[@class=''site-body'']//div[contains(@class, ''content-col'')]//div[contains(@class, ''content-list'')]');

insert into newspaper.x_path_content (id, website_id, title, content, date)
values  (1, 1, '//h1[@class=''content-detail-title'']', '//*[@id="maincontent"]', '//div[@class=''main-v1 bg-white'']//div[@class=''bread-crumb-detail__time'']'),
        (2, 2, '//*[@class=''site-body'']//div[contains(@class, ''main-content'')]/h1', '//*[@class=''site-body'']//div[contains(@class, ''main-content'')]//div[contains(@class, ''content-col'')]/div[contains(@class, ''body'')]', '//*[@class=''site-body'']//div[contains(@class, ''main-content'')]//div[contains(@class, ''content-col'')]//*[@datetime]');

