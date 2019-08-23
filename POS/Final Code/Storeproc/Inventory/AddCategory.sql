DELIMITER $$
use inventory $$
drop procedure if exists `AddCategory`;
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddCategory`(
OUT ReturnMessage varchar(150),
IN User_ID varchar(7), 
IN CategCode numeric(2, 0),
IN NameTitle varchar(50), 
Active varchar(10)
)
Proc_Exit:BEGIN
		declare AcInAc bit;
		If CategCode = 0 or CategCode is null then
				Begin
						Set ReturnMessage = 'Trade Code must greater than  0';
						leave Proc_Exit;
				End ;
        end if;
      If (Select count(`Prod_Category`.`Categ_Name`)from `inventory`.`Prod_Category`
	where`Prod_Category`.`Categ_Name`=NameTitle and`Prod_Category`.`Categ_Code`<>CategCode) then
    Set ReturnMessage = '(' + NameTitle + ') Category Name already exist';
    end if;
    set AcInAc = (select `Accounts`.`AcInAcBit`(Active));
    If (Select Count(Categ_Code) from `inventory`.`Prod_Category` Where Categ_Code=CategCode) = 0 then
         Begin
			Insert `inventory`.`Prod_Category` (Categ_Name, Categ_Code, Active)
			Values(NameTitle, CategCode, AcInAc);
			
		End ;
	Else
		Begin
			if ReturnMessage <> 'OK' then
				leave Proc_Exit;
			End If;
		-- Update department
			Update `inventory`.`Prod_Category`
			Set Categ_Name=NameTitle, Active=AcInAc 
			Where Categ_Code=CategCode;
            
		End;
	end if;
END$$
DELIMITER ;
