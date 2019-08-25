DELIMITER $$
use inventory $$
drop function if exists `GetNullforZeroValue`;
CREATE DEFINER=`root`@`localhost` FUNCTION `GetNullforZeroValue`(
Value numeric(25, 4)
) RETURNS numeric(25, 4) 
    DETERMINISTIC
BEGIN
	Declare GetValue numeric(25, 4);
	if Value = 0 then
		Set GetValue = Null;
	Else
		Set GetValue = Value;
    End if;    
	Return GetValue;
END$$
DELIMITER ;
select `inventory`.`GetZeroForNullValue`(null);