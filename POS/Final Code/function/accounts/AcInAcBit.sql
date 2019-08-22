DELIMITER $$
USE `accounts`$$
DROP Function IF EXISTS `AcInAcBit`;
Create FUNCTION `Accounts`.`AcInAcBit` 
(
BitTxt varchar(20)
)
RETURNS bit
DETERMINISTIC
BEGIN
    declare AccStatus bit;
    if BitTxt = 'Active' then
		Set AccStatus = True;
    else
		Set AccStatus = False;
    End if;
	Return AccStatus;
END$$
DELIMITER ;
