DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `Branches_Code_`(

IN  `ProjectCode` varchar(24)
)
Proc_Exit:BEGIN
select concat(`br`.`Branch_Name`,'::', repeat(0,3),convert(`br`.`Branch_Code`,char))
from branches br 
join branchesprojects `bp` on
bp.branch_code=br.branch_code
where bp.project_code=projectcode;
END$$
DELIMITER ;
