# from django.test import TestCase

# # Create your tests here.

# DELIMITER $$
# CREATE DEFINER=`root`@`localhost` PROCEDURE `User_Login`(
# OUT `ReturnMessage` VARCHAR(700),
# OUT `TradeCode` numeric(4, 0),
# OUT `ProjectCode` numeric(4, 0),
# OUT `BranchCode` numeric(4, 0),
# OUT `UserName` varchar(100),
# OUT `userType` varchar(50),
# IN  `thisComputer` varchar(100), 
# IN  `UserID` char(7),
# IN  `Location_ID` numeric(4, 0),
# IN  `Pass_Word` varchar(24)
# )
# Proc_Exit:BEGIN
# 	--
#     DECLARE CheckLogin varchar(100);
#    if (Select count(pc.`User_ID`)
# 		from `GenProcandFunctions`.`User_Locations` pc
# 		Where pc.`User_ID`=UserID and `Status`=True
# 		and pc.`Computer_Name`<>thisComputer)<>0 
#         or
#         (Select count(pc.`User_ID`)
# 		from `GenProcandFunctions`.`User_Locations` pc
# 		Where pc.`User_ID`=UserID and `Status`=True
# 		and pc.`Location_ID`<>Location_ID)<>0 
# 	    or
#         (Select count(pc.`User_ID`)
# 		from `GenProcandFunctions`.`User_Locations` pc
# 		Where pc.`User_ID`<>UserID and `Status`=True
# 		and pc.`Computer_Name`=thisComputer)<>0 
#         THEN
#         --
#         Set CheckLogin = (Select pc.`Computer_Name` from `GenProcandFunctions`.`User_Locations` pc where pc.`User_ID`=UserID);
#         Set ReturnMessage = CONCAT('User already loged in at computer  ',  `CheckLogin`, ' or computer  (', thisComputer, ') already in use by another user.');
#         if ReturnMessage is null then 
# 			Set ReturnMessage = CONCAT('Computer (', thisComputer, ') already in use by another user.');
#         End if;
# 		Leave Proc_Exit;
#    ELSEif (Select count(pc.`User_ID`) 
# 			from `GenProcandFunctions`.`User_Locations` pc
# 			Where pc.`User_ID`<>UserID and `Status`=True
# 			and pc.`Location_ID`=Location_ID)<>0 THEN
# 			--
# 		   (Select @un = usr.`User_Name`, @cn = pc.`Location_Name`
#             from `GenProcandFunctions`.`NHZ_Users` usr,
# 			`GenProcandFunctions`.`User_Locations` pc where usr.`User_ID`=pc.`User_ID` 
# 			and pc.`Location_ID`=Location_ID);
# 			--	
# 			Set ReturnMessage = CONCAT('Counter/POS  (', @cn ,') already used by  (',  @un, ') user.');
# 			Leave Proc_Exit;
#    END IF;
# 	--
#     if (Select count(usr.`User_ID`) from `GenProcandFunctions`.`NHZ_Users` usr
# 		Where 
# 		usr.`User_ID`=UserID and `Active`=True and usr.`Pass_Word`=Pass_Word)=0 Then
# 		--
#     	Set ReturnMessage ='Your user id or password is incorrect '; 
# 		Leave Proc_Exit;
# 	ELSE
# 		Update `GenProcandFunctions`.`User_Locations` pc Set pc.`User_ID`=UserID, 
#         pc.`Status`=True, pc.`Computer_Name`=thisComputer 
# 		Where pc.`Location_ID`=Location_ID;
# 		--
#         -- Set userType = (Select usr.`UserType` from `GenProcandFunctions`.`NHZ_Users` usr 
#         -- where usr.`User_ID`=UserID);
#         (
# 		 Select 
#           @userAuth = usr.`UserType`
#          ,@usrname = usr.`User_Name` 
#          ,@Trade_Code = usr.`Trade_Code`
#          ,@Project_Code = usr.`Project_Code`
#          ,@Branch_Code = usr.`Branch_Code`
# 		 from `GenProcandFunctions`.`NHZ_Users` usr 
#          where usr.`User_ID`=UserID
#          );
#         Set TradeCode = @Trade_Code;
#         Set ProjectCode = @Project_Code;
#         Set BranchCode = @Branch_Code;
#         Set userType = @userAuth;
#         Set UserName = @usrname;
#         Set ReturnMessage ='Login Succssed';
# 		--
# 	END IF;
# END$$
# DELIMITER ;




# CALL `genprocandfunctions`.`User_Login`(@ReturnMessage, @TradeCode, @ProjectCode, @BranchCode,@UserName,@userType, 'DESKTOP-GSN9BON', '123' , '123' , '123456');
