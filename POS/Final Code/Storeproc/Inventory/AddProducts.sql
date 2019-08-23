DELIMITER $$
use inventory $$
drop  procedure if exists `ProductAdd`;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ProductAdd`(
Out ReturnMessage varchar(150) , 
IN Branch numeric(4, 0), 
IN Terminal numeric(4, 0), 
IN User char(7), 
IN TradeCode numeric(2, 0), 
IN ProjectCode numeric(4, 0), 
IN BranchCode numeric(4, 0), 
IN ProdCode numeric(18, 0), 
IN CategCode numeric(5, 0), 
IN ProdType varchar(20), 
IN Valuation varchar(10),
IN RackShelf numeric(6, 0),
IN Active varchar(10),
IN ProdImage varbinary(4000),
IN ProdName varchar(100), 
IN OuterUnits numeric(11, 4), 
IN InnerUnits numeric(11, 4), 
IN Packing varchar(50),
IN SalesDiscPer numeric(5, 2),
IN PurchaseDiscPer numeric(5, 2),
IN CommPer numeric(5, 2),
IN PurchasePrice numeric(13, 4),
IN ProfitPer numeric(8, 4),
IN SalesPrice numeric(18, 4),
IN DSTPrice numeric(13, 4),
IN WSPrice numeric(13, 4),
IN VendorID numeric(19, 0),
IN Old_Price varchar(200),
IN ReorderLevel numeric(5, 0),
IN OinnerOf numeric(18, 0),
IN InnerOf numeric(18, 0),
IN TradeName varchar(100), 
IN InventoryAC numeric(18, 0),
IN SalesAC numeric(18, 0),
IN COGSAC numeric(18, 0),
IN LocCode numeric(5, 0),
IN CompanyCode numeric(6, 0),
IN SchemeCode numeric(3, 0)
 )
BEGIN
	Declare AcInAc bit;
    Declare Prev_Valation varchar(20);
    Declare Cur_Date date;
	Declare Cost_Price numeric(17, 4); 
	Declare	Total_Units numeric(17, 4);
    Declare Last_inv numeric(10, 0);
	--
	IF LENGTH(ProdImage) = 1 or LENGTH(ProdImage) = 0 then 
		Set ProdImage = null;
	End IF;
	--
    IF(Select Count(`inventory`.`Stock_Locations`.`Loc_Code` )
		from 
		`inventory`.`Stock_Locations` 
         where
         Branch_Code=BranchCode and Loc_Code=LocCode) = 0 then
         Set ReturnMessage = 'Location code was not found, select location code please.';
	End If;
	--
    if InventoryAcc is null or SalesAcc is null or COGSAcc is null then
		Begin
			Set ReturnMessage = 'Inventory account(s) are required.';			
		End;
	End IF;
    --
    -- if(Select isnumeric(LEFT(ProdName, 1))) = 1 then
		-- begin
		-- set ReturnMessage = 'Product name must be start with character!';
		-- end;
	-- End IF;
		Set ReturnMessage = 'OK';
		If ProdCode = 0 or ProdCode is null then
			Begin
			Set ReturnMessage = 'Product code must be greater than  0';
			End;
		End IF;
            -- Error
            if Valuation <> 'AVCO' and (PurchasePrice is null or PurchasePrice=0) then
			Begin
			set ReturnMessage = 'Purchase price is required for FIFO or LIFO valuation.';
			End;
			End If;
            
            if not VendorID is null then
				Set VendorID = (Select `Accounts`.`Acc_ID`(TradeCode, ProjectCode, BranchCode, VendorID));
            End IF;
            
	-- Set @Valuation = 'AVCO';
	-- if @Profit_Per >0 
	-- Set @Sales_Price = CONVERT(numeric(18, 4),@Purchase_Price + (@Purchase_Price*@Profit_Per/100));
	-- if @Sales_Price = 0 or @Sales_Price is null Set @Sales_Price = @Purchase_Price;
	Set AcInAc  = (Select `accounts`.`AcInAcBit`(Active));
    -- Begin Transaction;
    If (Select Count(Prod_Code) from `Products`
       where Prod_Code=ProdCode) = 0 then
      Begin
			Insert Into Products
			(
			Categ_Code,
			Prod_Code,
			Prod_Type,
			Inner_Outer_Units,
			Inner_Units,
			Prod_Name,
			Schecme_Code,
			Prod_Image,
			Sales_Price,
			Purchase_Price,
			Sales_Disc_Per,
			Purchase_Disc_Per,
			DST_Price,
			WS_Price,
			Comm_Per,
			Company_code,
			Vendor_ID,
			Active,
			Profit_Per,
			Packing,
			Old_Prices,
			Oinner_Of,
			Inner_Of,
			Rack_Shelf,
			Trade_Name
			)
			Values
			(
			CategCode,
			ProdCode,
			ProdType,
			OuterUnits,
			InnerUnits,
			ProdName,
			SchemeCode,
			ProdImage,
			SalesPrice,
			PurchasePrice,
			SalesDiscPer,
			PurchaseDiscPer,
			DSTPrice,
			WSPrice,
			CommPer,
			CompanyCode,
			VendorID,
			AcInAc,
			ProfitPer,
			Packing,
			OldPrice,
			OinnerOf,
			InnerOf,
			RackShelf,
			TradeName
			);
			--
			Insert Into Location_Stock 
			( 
			Trade_Code,
			Project_Code, 
			Branch_Code,
            Loc_Code, 
			Prod_Code, 
			Inventory_Acc,
			COGS_Acc, 
			Sales_Acc,
			Valuation,
			Reorder_Level
			)
			Values 
            (
			TradeCode ,
			ProjectCode , 
			BranchCode , 
			LocCode ,
			ProCode ,
			InventoryAC, 
			COGSAC , 
			SalesAC , 
			Valuation ,
			ReorderLevel 
			);
			Set ReturnMessage ='Save';
		End;
Else
	Begin
		Update Products 
		Set Prod_Name=ProdName,
		Categ_Code=CategCode,
		Sales_Price=SalesPrice,
		Sales_Disc_Per=SalesDiscPer,
		Purchase_Price=PurchasePrice,
		Purchase_Disc_Per=PurchaseDiscPer,
		DST_Price=DSTPrice,
		WS_Price=WSPrice,
		Inner_Outer_Units=OuterUnits,
		Inner_Units=InnerUnits,
		Comm_Per=CommPer,
		Company_code=CompanyCode,
		Vendor_ID=VendorID,
		Active =AcInAc,
		Prod_Type=ProdType,
		Profit_Per=ProfitPer,
		Packing=Packing,
		Old_Prices=OldPrice,
		Oinner_Of=OinnerOf,
		Inner_Of=InnerOf,
		Schecme_Code=SchemeCode,
		Prod_Image=ProdImage, 
		Rack_Shelf=RackShelf,
		Trade_Name=TradeName
		Where Prod_Code=ProdCode;
	    --
        If 
            ( 
			Select Count(prod_Code)
            from Location_Stock 
			where Trade_Code=TradeCode and 
            Project_Code=ProjectCode and
            Branch_Code=BranchCode and 
            Loc_Code=LocCode  and
			Prod_Code=ProdCode)=0  then
			--
            Insert into Location_Stock 
			( 
			Trade_Code,
			Project_Code ,
			Branch_Code,
			Loc_Code ,
			Prod_Code ,
			Inventory_Acc,
			COGS_Acc ,
			Sales_Acc ,
			Valuation ,
			Reorder_Level
			)
			Values 
			(
			TradeCode,
			ProjectCode ,
		    BranchCode ,
			LocCode,
			ProdCode ,
			InventoryAC ,
			COGSAC ,
			SalesAC ,
			Valuation ,
			ReorderLevel
			);
        Else
			Begin
				Set Prev_Valation  = (
				Select Valuation 
                from
                Location_Stock 
                where
                Loc_Code=LocCode and 
                Prod_Code=ProdCode and
				Inventory_Acc is not null);
				--
				Update Location_Stock Set
				Inventory_Acc=InventoryAC, 
				COGS_Acc=COGSAC ,
				Sales_Acc=SalesAC, 
				Valuation=Valuation ,
				Reorder_Level=Reorder_Level
				where
				Trade_Code=TradeCode and
				Project_Code=ProjectCode and
				Branch_Code=BranchCode and
				Loc_Code=LocCode and
				Prod_Code=ProCode;
				--
			
               if Valuation <> Prev_Valation then
					Begin
						if Prev_Valation = 'AVCO' then
							Begin
							  Set Total_Units =(
								Select (`GetZeroForNullValue`(ls.Opening_Units)+
										`GetZeroForNullValue`(ls.Units_Purchased))-
										(`GetZeroForNullValue`(ls.Units_Sold_Prev)+
										`GetZeroForNullValue`(ls.Units_Sold))
											--
										from Location_Stock ls
										Where ls.Loc_Code=LocCode and 
                                        ls.Prod_Code=ProCode
									);
                                    if Total_Units <> 0 then
										Begin
                                        Set Cost_Price =(
										Select  (`GetZeroForNullValue`(ls.Openning_Purchases_Amount)+
												 `GetZeroForNullValue`(ls.Purchases_Amount))/
												(`GetZeroForNullValue`(ls.Opening_Units)+
												 `GetZeroForNullValue`(ls.Units_Purchased))
												--
												from Location_Stock ls
												Where ls.Loc_Code=LocCode and
                                                ls.Prod_Code=ProdCode and
												(`GetZeroForNullValue`(ls.Openning_Purchases_Amount)+
												 `GetZeroForNullValue`(ls.Purchases_Amount))>0 
												 and
												(`GetZeroForNullValue`(ls.Opening_Units)+
												 `GetZeroForNullValue`(ls.Units_Purchased))>0
										        );
										  --
										if Cost_Price is null or Cost_Price = 0 then
                                        -- Set Cost_Price = (Select top 1  `GetZeroForNullValue`(prd.Purchase_Price)-
											-- (`GetZeroForNullValue`(prd.Purchase_Price)*
											 -- `GetZeroForNullValue`(prd.Purchase_Disc_Per)/100) 
											-- from Products prd where Prod_Code=ProCode);
											--
										Set Last_inv = (select `GetZeroForNullValue`(max(LFInvoice_No))+1 
                                        from Lifo_Fifo_PrQty);
										Set Cur_Date = getdate();
										insert `Lifo_Fifo_PrQty` (Loc_Code, Prod_Code, LFInvoice_Date, LFInvoice_No, LFOuter_Units, LFPrice)
										Values(LocCode, ProCode, Cur_date, Last_inv, Total_Units, Cost_Price);
                                        End If;
                                        
                                        
                                        
                                        End;
									End IF;
                            
                            if Valuation = 'AVCO' then
									Delete from Lifo_Fifo_PrQty where Loc_Code=LocCode
                                    and Prod_Code=ProCode;
                            End If;        
                            
                            
                            End;
						End if ;   
                                       
                    
                    
                    
                    
                    
                    
                    End;
               End if;     
            
            
            
            
            
            End;
        
        
        
        
        
        
        
        End if;
      End;
    End IF;
    
	END$$
DELIMITER ;
