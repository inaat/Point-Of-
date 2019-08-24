DELIMITER $$
use inventory $$
drop function if exists `GetZeroForNullValue`;
CREATE DEFINER=`root`@`localhost` FUNCTION `GetZeroForNullValue`(
Value varchar(25)
) RETURNS numeric(25, 4) 
    DETERMINISTIC
BEGIN
	Declare GetValue numeric(25, 4);
	if Value is null then
		Set GetValue = 0.00;
	Else
			Begin
				if (Select cast(Value as SIGNED)) <> 1 then
				Set GetValue = 0.00;
			
				else
					Set GetValue = Value;
				End if;
                End;
     End if;           
	Return GetValue;
END$$
DELIMITER ;
