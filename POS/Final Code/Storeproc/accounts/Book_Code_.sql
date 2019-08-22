DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Book_Code_`(

IN  `BranchCode` varchar(24)
)
Proc_Exit:BEGIN

select concat(`accountbooks`.`Book_Name`,'::',repeat(0,1),convert(`accountbooks`.`Book_Code`,char)) from accountbooks where Branch_Code= BranchCode;
END$$
DELIMITER ;
