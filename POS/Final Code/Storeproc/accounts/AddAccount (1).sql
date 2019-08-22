DELIMITER $$
use accounts $$
DROP PROCEDURE IF EXISTS `AddAccount`;
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddAccount`(
OUT ReturnMessage varchar(150), 
IN TradeCode numeric(2, 0), 
IN ProjectCode numeric(4, 0), 
IN BranchCode numeric(4, 0), 
IN  `UserID` char(7),
IN BookCode numeric(2, 0), 
IN AccNO numeric(18, 0),
IN Title varchar(300), 
IN AccNature varchar(20), 
IN AccType varchar(50), 
IN `Active` varchar(10), 
IN SubofAcc numeric(18, 0)
)
Proc_Exit:BEGIN
	Declare AlAdded numeric(20, 0);
    Declare PrmID numeric(20, 0);
    Declare MakeID varchar(20);
    Declare AcNo numeric(18, 0);
    Declare SubofAccount numeric(18, 0);
    declare AcNature char(1);
	declare AcType char(50);
    declare AcInAc bit;
    Declare ChkSubAcc bit;
    --
    set AcType = AccType;
	If AccNo = 0 or AccNo is null then
		Set ReturnMessage = 'Account ID must be greater than  0';
		leave Proc_Exit;
	End if;
    --
    if 	AccType = 'Retain Earning' or 
		AccType = 'Income Summary' then
		if AccType = 'Retain Earning' then
			Set AlAdded = ( Select `Acc_No` 
            from `Accounts`.`TrialBalance` where 
			`Trade_Code`=TradeCode and 
            `Project_Code`=ProjectCode and 
            `Branch_Code`=BranchCode and 
            `Acc_Type`='REA' limit 1);
		Else 
			Set AlAdded = (Select `Acc_No` from 
            `Accounts`.`TrialBalance` where 
			`Trade_Code`=TradeCode and 
            `Project_Code`=ProjectCode and 
            `Branch_Cod`=BranchCode and	
            `Acc_Type`='SUM' limit 1);
		End if;
		--
   		If not AlAdded is null then
			Set ReturnMessage = 'Retain Earning or income Summary already added';
			leave Proc_Exit;
		End if;
	End if;
    --
    Set MakeID = (Select `Accounts`.`makeid`(TradeCode, ProjectCode, BranchCode, BookCode, AccNo));
	Set AcNo = MakeID;
    --
    -- Check in other tables
	if (Select count(`Accounts`.`chart_of_accounts`.`Acc_No`) 
		From `Accounts`.`chart_of_accounts`
		Where `Accounts`.`chart_of_accounts`.`Acc_No`=Acno and 
        `chart_of_accounts`.`Categ`<>'Gen')<>0 then
		Set ReturnMessage = 'Account ID Already exist';
		leave Proc_Exit;
	End if;
    --
    If not SubofAcc is null and SubofAcc <> 0 then
		Set MakeID = null;
		Set MakeID = (Select `Accounts`.`makeid` (
		TradeCode, ProjectCode, BranchCode, BookCode, SubofAcc)
		);
		Set SubofAccount  = MakeID;
	End if;
    --
    if AcNo = SubofAccount then
		Set ReturnMessage = 'Main and sub accounts are same';
		leave Proc_Exit;
	End if;
    --
    if (Select 
        count(`Accounts`.`chart_of_accounts`.`Acc_No`)
		From 
        `Accounts`.`chart_of_accounts`
		Where 
        `Accounts`.`chart_of_accounts`.`Acc_No` = AcNo
        and 
        not Sub_of_Account is null)<>0 
        and 
        (SubofAcc = 0 or SubofAcc is null) then 
		Set ReturnMessage = 
        concat(CAST(AcNo AS CHAR),'Already added as Sub-Account');
		leave Proc_Exit;
	End if;
     
    Set AcNature =
		Case AccNature
			When 'Assets' then 'A'
			when 'Equities' then 'O'
			when 'Liabilities' then 'L'
			when 'Income-Revenue' then 'R'
			when 'Expenses' then 'E'
		End;
    --
    If AcNature='A' then
		Begin
			Set AcType=
			Case AccType
				when 'Cash' then 'CAS'
				when 'Bank' then 'Ban'
				when 'Petty Cash' then 'PTC'
                when 'Accounts Receivable' then 'ACR'
                when 'Fixed Asset' then 'FIA'
                when 'Inventory' then 'INV'
                when 'Other Asset' then 'OTA'
                when 'Bad Dabts/Uncollectable' then 'BDS'
                when 'Depreciation' then 'DEP'
			End;
		End;
        End if;
     --
     If AcNature='O' then
		Begin
			Set AcType=
			Case AccType
				when 'Owner Equity' then 'OWE'
				when 'Owner Drawing' then 'OWD'
				when 'Retain Earning' then 'REA'
                when 'Income Summary' then 'SUM'
			End;
		End;
        End if;
	--
     If AcNature='L' then
		Begin
			Set AcType=
			Case AccType
				when 'Account Payable' then 'ACP'
				when 'Long Term' then 'LTL'
				when 'Other Liability' then 'OLI'
			End;
		End;
        End if;
   --
	If AcNature='R' then
		Begin
			Set AcType =
			Case AccType
				when 'Sales/Fee/Commission' then 'SFR'
				when 'Sales Return & Allowances' then 'SRT'
				when 'Sales/Cash Discount' then 'CDA'
				when 'Other Income' then 'OIN'	
			End;
		End;
	End if;
	--
    If AcType= 'SRT' or AcType= 'CDA' then
		Set AcNature = 'D';
	End if;
	--
	If AcNature ='E' then
		Begin
			Set AcType =
			Case AccType
				when 'General Exp.' then 'GEX'
				when 'Pre-Paid Exp.' then 'PEX'
				when 'Cost of Goods Sold' then 'COG'
				when 'Purchases Return & Allowances' then 'PRT'
				when 'Purchases/Cash discount' then 'CDR'
			End;
        End;
    End if;
    --
	If AcType = 'PEX' then
				Set AcNature = 'A';
    End If; 
    if AcType = 'PRT' or AcType = 'CDR' then
				Set AcNature = 'C';
    End if;
    --
	If not SubofAcc is null and SubofAcc <> 0 then
		Begin
            Set ChkSubAcc = 0;
			if ( Select Count(Acc_No) 
				From 
				`Accounts`.`TrialBalance` where 
				Acc_No = SubofAccount) <> 0 then
				Set ChkSubAcc = 1;
			ElseIf ( Select count(Acc_No) 
					From 
					`Accounts`.`SubAccounts` where 
                    Acc_No = SubofAccount) <> 0 then
					Set ChkSubAcc = 1;
		End if;
		--
		if ChkSubAcc = 0 then 
			Set ReturnMessage = 'Invalid Sub-Account';
		End if;
	  End;
	End if;
    --
	set AcInAc = (select `Accounts`.`AcInAcBit`(Active));
    --
     If SubofAcc = 0 or SubofAcc Is Null then
		Begin

			if (Select Count(Acc_No)
				from `accounts`.`trialbalance` where Acc_No = AcNo) = 0 then
                --
                Insert Into `Accounts`.`TrialBalance`
					(
					`Trade_Code`
					,`Project_Code` 
					,`Branch_Code`
					,`Book_Code`
					,`Acc_NO`
					,`Title`
					,`Acc_Nature`
					,`Acc_Type`
					,`Active`
					)
					Values
					(
					 TradeCode
					,ProjectCode 
					,BranchCode
					,BookCode
					,AcNo
					,Title
					,AcNature
					,AcType
					,AcInAc
					);
					Set ReturnMessage ='Save';
			Else 
				Begin
                  Update `Accounts`.`TrialBalance` 
					Set 
                     `Title`=Title
					,`Acc_Nature`=AcNature
					,`Acc_Type`=AcType
					,`Active` = AcInAc
					Where 
					`Accounts`.`TrialBalance`.`Acc_No`=AcNo;
                    Set ReturnMessage ='Account Updated ';
				End;
			End If;
            delete from SubHeadLinks where `SubofSub`=AcNo;
            -- and MainofsubAcc=SubAccount;
			delete from MainSubHeadLinks where `SubAcc`=AcNo;
            -- and MainAcc=SubAccount 
			Delete from `Accounts`.`SubAccounts` where `Acc_No`=AcNo;
        End;
     Else
		Begin
			if (Select count(`Acc_No`) from `Accounts`.`SubAccounts` 
				where `Acc_No`=AcNo) = 0 then
				Begin
					Insert Into `Accounts`.`SubAccounts` 
					(
                    `Acc_No`
					,`Title`
					,`Active`
					)
					Values
					(
                    AcNo
					,Title
					,AcInAc
					);
					Set ReturnMessage ='Save';
				End;
			Else
				Begin
					Update `Accounts`.`SubAccounts`
					Set `Title`=Title
					,`Active`=AcInAc
					Where 
					`Accounts`.`SubAccounts`.`Acc_No`=AcNo;
				End;
                delete from SubHeadLinks where `SubofSub`=AcNo and `MainofsubAcc`=SubofAccount;
				delete from MainSubHeadLinks where `SubAcc`=AcNo and `MainAcc`=SubofAccount; 
				Delete from `Accounts`.`TrialBalance` where `Acc_No`=AcNo;
			End if;
            if (Select count(`Acc_NO`) from `Accounts`.`TrialBalance` 
            where `Acc_No`=SubofAccount) <> 0 then
				Insert into MainSubHeadLinks values(AcNo, SubofAccount);
			Else
				insert into SubHeadLinks values(AcNo, SubofAccount);
			End if;
        End;
     End if;   
END$$
DELIMITER ;
-- select * from chart_of_Accounts;