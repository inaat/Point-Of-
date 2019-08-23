DELIMITER $$
use accounts $$
drop procedure if exists `accounts`.`Account_List_By_Type`;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Account_List_By_Type`(
IN TradeCode numeric(4, 0),
IN ProjectCode numeric(4, 0),
IN  `BranchCode` numeric(4,0),
IN  `AcType` varchar(50)
)
Proc_Exit:BEGIN


Select concat(`accounts`.`chart_of_accounts`.`First_Title`,'::',substr(`accounts`.`chart_of_accounts`.`Acc_No`,12,6)) as `Acc_No`
from 
`accounts`.`chart_of_accounts`
Where
`accounts`.`chart_of_accounts`.`Trade_Code`=TradeCode and
`accounts`.`chart_of_accounts`.`Project_Code`= ProjectCode and
 `accounts`.`chart_of_accounts`.`Branch_Code`= BranchCode and
 `accounts`.`chart_of_accounts`.`Acc_Type`= AcType
order by `accounts`.`chart_of_accounts`.`First_Title` ;

End$$
DELIMITER ;
call Account_List_By_Type(001,001,001,'INV');