__author__ = 'gaa8664'

FIND_GRN_DETAILS = '''
    exec sgrhsp_HMS_GRNITEMS_SearchDetails '', '',%s,'','','',%s,'','','',-987654321, -987654321,''

'''

OPENING_STOCK = '''
    Select
	A.BATCHNO,
	A.EXPIRYDATE,
	A.MRP,
	A.QTY as GRNQTY,
	B.FVALUE TotalValue,
	B.ITEM,
	B.RATE ItemRate,
	B.OPTNo AS GRNNo,
	(
	    SELECT
	        OPTSTORE
	    FROM
	        HMS_OPENINGSTOCK (NOLOCK)
	    WHERE 1=1
	        AND OPTNO = B.OPTNo
	) AS Store,
	(
	    SELECT
	        OPTDate
	    FROM
	        HMS_OPENINGSTOCK (NOLOCK)
	    WHERE 1=1
	        AND OPTNO = B.OPTNo
	) AS GRNDate
From
	HMS_OPTBATCH (NOLOCK) A,
	HMS_OPTSTOCKITEMS (NOLOCK) B
 Where 1=1
	AND A.OPENINGSTOCKITEM=B.ID AND
	B.ITEM = %s AND
	BatchNo = %s
'''

OPENING_STOCK_GRN = '''
    Select
	A.BATCHNO,
	A.EXPIRYDATE,
	A.MRP,
	A.QTY as GRNQTY,
	B.FVALUE TotalValue,
	B.ITEM,
	B.RATE ItemRate,
	B.OPTNo AS GRNNo,
	(
	    SELECT
	        OPTSTORE
	    FROM
	        HMS_OPENINGSTOCK (NOLOCK)
	    WHERE 1=1
	        AND OPTNO = B.OPTNo
	) AS Store,
	(
	    SELECT
	        OPTDate
	    FROM
	        HMS_OPENINGSTOCK (NOLOCK)
	    WHERE 1=1
	        AND OPTNO = B.OPTNo
	) AS GRNDate
From
	HMS_OPTBATCH (NOLOCK) A,
	HMS_OPTSTOCKITEMS (NOLOCK) B
 Where 1=1
	AND A.OPENINGSTOCKITEM=B.ID AND
	B.ITEM = %s AND
	B.OPTNo = %s
'''

PO = '''
	exec
	sgrhsp_HMS_PurchaseOrderTran_ConsignmentPOBreakup
	%s, -- from_po_date,
	%s, -- to_po_date,
	'',
	'',
	'',
	'',
	''
'''

UPLOAD_DATA = '''
	INSERT INTO
'''

