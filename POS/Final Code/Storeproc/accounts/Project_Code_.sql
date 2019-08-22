DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Project_Code_`(

IN  `TradeCode` varchar(24)
)
Proc_Exit:BEGIN
select concat(`projects`.`Project_Name`,'::', repeat(0, 3), convert(`projects`.`Project_Code`, char)) from projects where Trade_Code= TradeCode;
END$$
DELIMITER ;
