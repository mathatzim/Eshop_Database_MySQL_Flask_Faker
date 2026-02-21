-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ESHOP_Database
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ESHOP_Database
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ESHOP_Database` DEFAULT CHARACTER SET utf8 ;
USE `ESHOP_Database` ;

-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Categories` (
  `Product_CategoryID` INT NOT NULL AUTO_INCREMENT,
  `ProductCategory_Descrption` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Product_CategoryID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Brands`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Brands` (
  `BrandID` INT NOT NULL AUTO_INCREMENT,
  `Brand_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`BrandID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Products` (
  `ProductID` INT NOT NULL AUTO_INCREMENT,
  `Discontinued` TINYINT NOT NULL,
  `Product_Name` VARCHAR(45) NOT NULL,
  `Product_CategoryID` INT NOT NULL,
  `BrandID` INT NOT NULL,
  PRIMARY KEY (`ProductID`),
  INDEX `fk_Products_Product_Categories1_idx` (`Product_CategoryID` ASC) VISIBLE,
  INDEX `fk_Products_Brands1_idx` (`BrandID` ASC) VISIBLE,
  CONSTRAINT `fk_Products_Product_Categories1`
    FOREIGN KEY (`Product_CategoryID`)
    REFERENCES `ESHOP_Database`.`Product_Categories` (`Product_CategoryID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Products_Brands1`
    FOREIGN KEY (`BrandID`)
    REFERENCES `ESHOP_Database`.`Brands` (`BrandID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Shops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Shops` (
  `Shop_Name` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `Phone` INT NOT NULL,
  `Shop_Email` VARCHAR(45) NOT NULL,
  `ShopID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ShopID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Customers` (
  `Customer_FirstName` VARCHAR(45) NOT NULL,
  `Customer_LastName` VARCHAR(45) NOT NULL,
  `Customer_Email` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `CustomerID` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`CustomerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`CustomerOrders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`CustomerOrders` (
  `OrderDate` DATE NOT NULL,
  `Order_Country` VARCHAR(45) NOT NULL,
  `Order_City` VARCHAR(45) NOT NULL,
  `Order_Address` VARCHAR(45) NOT NULL,
  `PostalCode` VARCHAR(45) NOT NULL,
  `Shipment_Method` VARCHAR(45) NOT NULL,
  `Payment_Method` VARCHAR(45) NOT NULL,
  `CustomerID` INT NOT NULL,
  `Customer_OrderID` INT NOT NULL AUTO_INCREMENT,
  `Order_Address2` VARCHAR(45) NOT NULL,
  `Customer_Phone` INT NOT NULL,
  `Customer_Phone2` INT NULL,
  `ShopID` INT NOT NULL,
  INDEX `fk_CustomerOrder_Customer1_idx` (`CustomerID` ASC) VISIBLE,
  PRIMARY KEY (`Customer_OrderID`),
  INDEX `fk_CustomerOrders_Shops1_idx` (`ShopID` ASC) VISIBLE,
  CONSTRAINT `fk_CustomerOrder_Customer1`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `ESHOP_Database`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CustomerOrders_Shops1`
    FOREIGN KEY (`ShopID`)
    REFERENCES `ESHOP_Database`.`Shops` (`ShopID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Variation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Variation` (
  `Product_VariationID` INT NOT NULL AUTO_INCREMENT,
  `ProductID` INT NOT NULL,
  `Description` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Product_VariationID`),
  INDEX `fk_Product_Version_Products1_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Version_Products1`
    FOREIGN KEY (`ProductID`)
    REFERENCES `ESHOP_Database`.`Products` (`ProductID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Price`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Price` (
  `Product_PriceID` INT NOT NULL AUTO_INCREMENT,
  `Starting_ProductPrice` INT NOT NULL,
  `Discount_Percentage` INT NULL,
  `Current_ProductPrice` INT NOT NULL,
  PRIMARY KEY (`Product_PriceID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`OrderItems`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`OrderItems` (
  `Customer_OrderID` INT NOT NULL,
  `Order_ItemID` INT NOT NULL AUTO_INCREMENT,
  `Ordered_Quantity` INT NOT NULL,
  `Product_VariationID` INT NOT NULL,
  `Product_PriceID` INT NOT NULL,
  INDEX `fk_OrderItem_CustomerOrder1_idx` (`Customer_OrderID` ASC) VISIBLE,
  PRIMARY KEY (`Order_ItemID`),
  INDEX `fk_OrderItems_Product_Variation1_idx` (`Product_VariationID` ASC) VISIBLE,
  INDEX `fk_OrderItems_Product_Price1_idx` (`Product_PriceID` ASC) VISIBLE,
  CONSTRAINT `fk_OrderItem_CustomerOrder1`
    FOREIGN KEY (`Customer_OrderID`)
    REFERENCES `ESHOP_Database`.`CustomerOrders` (`Customer_OrderID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_OrderItems_Product_Variation1`
    FOREIGN KEY (`Product_VariationID`)
    REFERENCES `ESHOP_Database`.`Product_Variation` (`Product_VariationID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_OrderItems_Product_Price1`
    FOREIGN KEY (`Product_PriceID`)
    REFERENCES `ESHOP_Database`.`Product_Price` (`Product_PriceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Color`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Color` (
  `Product_ColorID` INT NOT NULL AUTO_INCREMENT,
  `Primary_Color` VARCHAR(45) NOT NULL,
  `Secondary_Color` VARCHAR(45) NULL,
  PRIMARY KEY (`Product_ColorID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Dimensions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Dimensions` (
  `Product_DimensionsID` INT NOT NULL AUTO_INCREMENT,
  `Product_Size` VARCHAR(45) NOT NULL,
  `Vertical_Dimension` INT NOT NULL,
  `Horizontal_Dimension` INT NOT NULL,
  PRIMARY KEY (`Product_DimensionsID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Options`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Options` (
  `Product_OptionsID` INT NOT NULL AUTO_INCREMENT,
  `Product_DimensionsID` INT NOT NULL,
  `Product_ColorID` INT NOT NULL,
  `Model_year` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Product_OptionsID`),
  INDEX `fk_Product_Options_Product_Color1_idx` (`Product_ColorID` ASC) VISIBLE,
  INDEX `fk_Product_Options_Product_Dimensions1_idx` (`Product_DimensionsID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Options_Product_Color1`
    FOREIGN KEY (`Product_ColorID`)
    REFERENCES `ESHOP_Database`.`Product_Color` (`Product_ColorID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Options_Product_Dimensions1`
    FOREIGN KEY (`Product_DimensionsID`)
    REFERENCES `ESHOP_Database`.`Product_Dimensions` (`Product_DimensionsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Variation_has_Product_Options`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Variation_has_Product_Options` (
  `Product_VariationID` INT NOT NULL,
  `Product_OptionsID` INT NOT NULL,
  PRIMARY KEY (`Product_VariationID`, `Product_OptionsID`),
  INDEX `fk_Product_Variation_has_Product_Options_Product_Options1_idx` (`Product_OptionsID` ASC) VISIBLE,
  INDEX `fk_Product_Variation_has_Product_Options_Product_Variation1_idx` (`Product_VariationID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Variation_has_Product_Options_Product_Variation1`
    FOREIGN KEY (`Product_VariationID`)
    REFERENCES `ESHOP_Database`.`Product_Variation` (`Product_VariationID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Variation_has_Product_Options_Product_Options1`
    FOREIGN KEY (`Product_OptionsID`)
    REFERENCES `ESHOP_Database`.`Product_Options` (`Product_OptionsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Options_has_Shops`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Options_has_Shops` (
  `Product_OptionsID` INT NOT NULL,
  `ShopID` INT NOT NULL,
  `Product_PriceID` INT NOT NULL,
  `ProductStock_Number` INT NOT NULL,
  PRIMARY KEY (`Product_OptionsID`, `ShopID`),
  INDEX `fk_Product_Options_has_Shops_Shops1_idx` (`ShopID` ASC) VISIBLE,
  INDEX `fk_Product_Options_has_Shops_Product_Options1_idx` (`Product_OptionsID` ASC) VISIBLE,
  INDEX `fk_Product_Options_has_Shops_Product_Price1_idx` (`Product_PriceID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Options_has_Shops_Product_Options1`
    FOREIGN KEY (`Product_OptionsID`)
    REFERENCES `ESHOP_Database`.`Product_Options` (`Product_OptionsID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Options_has_Shops_Shops1`
    FOREIGN KEY (`ShopID`)
    REFERENCES `ESHOP_Database`.`Shops` (`ShopID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Options_has_Shops_Product_Price1`
    FOREIGN KEY (`Product_PriceID`)
    REFERENCES `ESHOP_Database`.`Product_Price` (`Product_PriceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Product_Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Product_Comments` (
  `Product_CommentID` INT NOT NULL AUTO_INCREMENT,
  `pComment_Content` VARCHAR(45) NULL,
  `pComment_Rating` INT NOT NULL,
  `pComment_Date` DATE NOT NULL,
  `CustomerID` INT NOT NULL,
  `Product_VariationID` INT NOT NULL,
  PRIMARY KEY (`Product_CommentID`),
  INDEX `fk_Product_Comments_Customers1_idx` (`CustomerID` ASC) VISIBLE,
  INDEX `fk_Product_Comments_Product_Variation1_idx` (`Product_VariationID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Comments_Customers1`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `ESHOP_Database`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_Comments_Product_Variation1`
    FOREIGN KEY (`Product_VariationID`)
    REFERENCES `ESHOP_Database`.`Product_Variation` (`Product_VariationID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ESHOP_Database`.`Shop_Comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`Shop_Comments` (
  `Shop_CommentID` INT NOT NULL AUTO_INCREMENT,
  `sComment_Content` VARCHAR(45) NULL,
  `sComment_Rating` INT NOT NULL,
  `sComment_Date` DATE NOT NULL,
  `CustomerID` INT NOT NULL,
  `ShopID` INT NOT NULL,
  PRIMARY KEY (`Shop_CommentID`),
  INDEX `fk_Product_Comments_Customers1_idx` (`CustomerID` ASC) VISIBLE,
  INDEX `fk_Shop_Comments_Shops1_idx` (`ShopID` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Comments_Customers10`
    FOREIGN KEY (`CustomerID`)
    REFERENCES `ESHOP_Database`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Shop_Comments_Shops1`
    FOREIGN KEY (`ShopID`)
    REFERENCES `ESHOP_Database`.`Shops` (`ShopID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `ESHOP_Database` ;

-- -----------------------------------------------------
-- Placeholder table for view `ESHOP_Database`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ESHOP_Database`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `ESHOP_Database`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ESHOP_Database`.`view1`;
USE `ESHOP_Database`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
