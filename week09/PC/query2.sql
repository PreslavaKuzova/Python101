SELECT PRODUCT.MAKER, AVG(SCREEN) as average_screen
    FROM LAPTOP
    JOIN PRODUCT
        ON LAPTOP.MODEL = PRODUCT.MODEL
GROUP BY PRODUCT.MAKER;