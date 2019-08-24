DELIMITER $$
use accounts $$
drop function if exists `Acc_ID`;
CREATE DEFINER=`root`@`localhost` FUNCTION `Acc_ID`(
TradeCode numeric(2, 0), 
ProjectCode numeric(4, 0), 
BranchCode numeric(4, 0), 
Ac_No numeric(9, 0)
) RETURNS varchar(25) 
    DETERMINISTIC
BEGIN
	Declare BookCode numeric(4, 0);
    Declare BookLength tinyint;
    Declare PrmidLength tinyint;
    Declare Chars nvarchar(20);
	--
	Set BookLength = (Select BookCode from `Accounts`.`LengthofCodes`);
	Set PrmidLength = (Select IDLength from `Accounts`.`LengthofCodes`);
	--
    Set Chars = Right(REPLICATE('0',BookLength) + convert(Ac_No,char),PrmidLength+BookLength);
	-- BookCode
	Set BookCode = LEFT(CONVERT(Ac_No, char),len(Ac_No)- PrmidLength);
	Set Ac_No = right(convert(Ac_No,char),PrmidLength);
	Set Chars = (Select `Accounts`.`MakeID`(TradeCode, ProjectCode, BranchCode, BookCode, Ac_No));
	Return Chars;	
	
END$$
DELIMITER ;
select `accounts`.`Acc_ID`(1,1,1,02);