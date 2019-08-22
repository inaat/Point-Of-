DELIMITER $$
Use accounts $$
DROP Function IF EXISTS `GET_AccountNature_Account_Type`;
CREATE DEFINER=`root`@`localhost` FUNCTION `GET_AccountNature_Account_Type`
(
AccType varchar(50),
AccNature varchar(50),
Gets varchar(50)

) 
RETURNS varchar(50)
 DETERMINISTIC
BEGIN
  
  declare AcType varchar(50);
  declare AcNature varchar(50);
  
  -- set Actype = 'get type';
  -- set AcNature = 'get nat';
   If AccNature='A' then
       
       If AccType = 'PEX' then
				Set AcNature = 'Expenses';
        else 
			
				Set AcNature = 'Assests';
    End If; 
   
		Begin
			Set AcType=
			Case AccType
				when 'CAS' then 'Cash'
				when 'Ban' then 'Bank' 
				when 'PTC' then 'Petty Cash'
                when 'ACR' then 'Accounts Receivable' 
                when 'FIA' then 'Fixed Asset'
                when 'INV' then 'Inventory'  
                when 'OTA' then 'Other Asset'
                when 'BDS' then 'Bad Dabts/Uncollectable'
                when 'DEP' then 'Depreciation'
			End;
            
            
		End;
   Elseif AccNature = 'O' then
         set AcNature = 'Equities';
          Begin
			Set AcType=
				Case AccType
					when 'OWE' then 'Owner Equity'
					when 'OWD' then 'Owner Drawing' 
					when 'REA' then 'Retain Earning' 
					when 'SUM' then 'Income Summary'
				End;
		   End;
	ElseIf AccNature = 'L' then
           Set AcNature = 'Liabilities';
				Begin
					Set AcType=
						Case AccType
						when 'ACP'  then 'Account Payable'
						when  'LTL'  then 'Long Term'
						when 'OLI' then  'Other Liability' 
						End;
				End;
		ElseIf AccNature = 'R'  or AccNature = 'D' then
         set AcNature = 'Income-Revenue';
			Begin
				Set AcType =
				Case AccType
					when 'SFR' then 'Sales/Fee/Commission'
					when 'SRT' then 'Sales Return & Allowances'
					when 'CDA' then 'Sales/Cash Discount' 
					when 'OIN'	 then 'Other Income' 
				End;
			End;
		ElseIf AccNature ='E' or AccNature = 'C'  then
        
       set AcNature = 'Expenses' ;
		Begin
			Set AcType =
			Case AccType
				when 'GEX' then 'General Exp.'
				when 'PEX' then 'Pre-Paid Exp.' 
				when 'COG' then 'Cost of Goods Sold' 
				when 'PRT' then 'Purchases Return & Allowances'
				when 'CDR' then 'Purchases/Cash discount' 
			End;
        End;
   End if;   
 
 
 if Gets = 'AccType' then
		return AcType;
  else
     Return AcNature;
  end if;
END$$
DELIMITER ;


Select `GET_AccountNature_Account_Type`('srt', 'D', 'acctyp'); 