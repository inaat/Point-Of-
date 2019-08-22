DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Account_Find`(
IN `TradeCode` numeric(4, 0), 
IN `ProjectCode` numeric(4, 0), 
IN `BranchCode` numeric(4, 0), 
IN `BookCode` numeric(2, 0), 
IN  `AccNo` numeric(18,0)

)
Proc_Exit:BEGIN
Declare MakeID varchar(20);
Set MakeID = (Select `Accounts`.`makeid`(TradeCode, ProjectCode, BranchCode, BookCode, AccNo));

Select `accounts`.`trialbalance`.`Title`,
`accounts`.`GET_AccountNature_Account_Type`(`accounts`.`trialbalance`.`Acc_Type`, `accounts`.`trialbalance`.`Acc_Nature`,'Nature') as `Acc_Nature`,
`accounts`.`GET_AccountNature_Account_Type`(`accounts`.`trialbalance`.`Acc_Type`, `accounts`.`trialbalance`.`Acc_Nature`,'AccType') as `Acc_Type` ,
 AcinAcTxt(`accounts`.`trialbalance`.`Active`) as `Status`
from 
`accounts`.`trialbalance`
Where

`accounts`.`trialbalance`.`Acc_No`=MakeID ;


End$$
DELIMITER ;
