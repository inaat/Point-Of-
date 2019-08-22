DELIMITER $$
USE `accounts`$$
DROP Function IF EXISTS `MakeID`;
Create FUNCTION `Accounts`.`MakeID` 
(
TradeCode numeric(2, 0), 
ProjectCode numeric(4, 0), 
BranchCode numeric(4, 0), 
BookCode numeric(2, 0),
AccNo numeric(18, 0)
)
RETURNS varchar(20)
DETERMINISTIC
BEGIN
	-- TradeCode
	Set @Chars = right(concat(Repeat('0', 2), convert(TradeCode, char)), 2);
	-- ProjectCode
	Set @Chars = concat(@chars, 
	right(concat(Repeat('0', 4), convert(ProjectCode, char)), 4)
	);
	-- BranchCode
	Set @Chars = concat(@chars, 
	right(concat(Repeat('0', 4), convert(BranchCode, char)), 4)
	);
	-- BookCode
	Set @Chars = concat(@chars, 
	right(concat(Repeat('0', 2), convert(BookCode, char)), 2)
	);
	-- Account ID
	Set @Chars = concat(@chars, 
	right(concat(Repeat('0', 6), convert(AccNo, char)), 6)
	);
	Return @Chars;
END$$
DELIMITER ;
