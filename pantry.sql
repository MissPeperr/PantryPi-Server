CREATE TABLE Category (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL
);

CREATE TABLE Food (
    `id` TEXT NOT NULL PRIMARY KEY,
    `name` TEXT NOT NULL,
    `quantity` INTEGER NOT NULL,
    `barcode` TEXT NOT NULL,
    `on_grocery_list` INTEGER NOT NULL,
    `category_id` INTEGER NOT NULL,
    FOREIGN KEY(`category_id`) REFERENCES `Category`(`id`)
);

INSERT INTO Category VALUES (1, "Default");
INSERT INTO Category VALUES (2, "Sweets");
INSERT INTO Category VALUES (3, "Snacks");
INSERT INTO Category VALUES (4, "Breads");
INSERT INTO Category VALUES (5, "Vegetables");
DELETE FROM Category;

INSERT INTO Food VALUES ("food_bn5ga70bfcre8eaft1zptb3ri979", "NABISCO, OREO, MILK'S FAVORITE SANDWICH COOKIES, CHOCOLATE", 1, "044000032029", 1, 1);
INSERT INTO Food VALUES ("food_adq4r9la7hrqf2b3zqpmxbg73go2", "SANDWICH POTATO BREAD", 1, "075185007007", 0, 3);
INSERT INTO Food VALUES ("food_bk64133bt6s1gwb2ltlfibzx8fxr", "ICE CREAM, VANILLA", 1, "853149008006", 0, 1);
INSERT INTO Food VALUES ("food_bhgjeekag1cntnb3ty89ib5dgsf5", "SHARP WHITE CHEDDAR CHEESE", 2, "072830000956", 1, 1);
INSERT INTO Food VALUES ("food_ajgf5dvbu2abvqbcb2c3iauhehne", "Sweetened With Stevia", 2, "858982001306", 1, 1);
DELETE FROM Food WHERE barcode = "858982001306";
DELETE FROM Food WHERE barcode = "%20858982001306";
DELETE FROM Food;