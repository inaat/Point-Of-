DELIMITER $$
drop procedure if exists `accounts`.`Account_List`;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Account_List`(

IN  `BranchCode` numeric(4,0),
IN  `BookCode` numeric(2,0)
)
Proc_Exit:BEGIN


Select concat(`accounts`.`chart_of_accounts`.`First_Title`,'::',substr(`accounts`.`chart_of_accounts`.`Acc_No`,12,6)) as `Acc_No`
from 
`accounts`.`chart_of_accounts`
Where
`accounts`.`chart_of_accounts`.`Branch_Code`=BranchCode and
`accounts`.`chart_of_accounts`.`Book_Code`= BookCode 
order by `accounts`.`chart_of_accounts`.`First_Title`  ;

End$$
DELIMITER ;
