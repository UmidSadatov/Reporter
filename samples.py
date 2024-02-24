class PrimaryReportSample:
    def __init__(
            self,
            name_column: str,
            balance_beginning_column: str,
            incomes_column: str,
            sells_column: str,
            balance_end_column: str,
            start_row: int
    ):
        self.name_column = name_column
        self.balance_beginning_column = balance_beginning_column
        self.incomes_column = incomes_column
        self.sells_column = sells_column
        self.balance_end_column = balance_end_column,
        self.start_row = start_row


class SecondaryReportSample:
    def __init__(
            self,
            name_column: str,
            sells_column: str,
            start_row: int,
            max_row: int,
            region1_column=None,
            region1_cell=None,
            region2_column=None,
            region2_cell=None,
    ):
        self.name_column = name_column
        self.sells_column = sells_column
        self.start_row = start_row
        self.max_row = max_row
        self.region1_column = region1_column
        self.region1_cell = region1_cell
        self.region2_column = region2_column
        self.region2_cell = region2_cell


sample = SecondaryReportSample(
    name_column='A',
    sells_column='D',
    start_row=7,
    max_row=10,
    region1_cell='D5'
)