DELIMITER $$
USE `accounts`$$
DROP Function IF EXISTS `AcInAcTxt`;
Create FUNCTION `Accounts`.`AcInAcTxt` 
(
BitValue bit
)
RETURNS varchar(20)
DETERMINISTIC
BEGIN
    declare AccStatus varchar(20);
    if BitValue= True then
		Set AccStatus = 'Active';
    else
		Set AccStatus = 'In-Active';
    End if;
	Return AccStatus;
END$$
DELIMITER ;
