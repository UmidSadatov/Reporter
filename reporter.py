from abc import ABC, abstractmethod


class PrimaryReportUnitData:
    """
    unit data of primary report

    distributor :str, distributor's name;
    name :str, name of drug or medication;
    region :str|tuple<str>, region where the medication was sold;
    balance_beginning: int;
    incomes: int;
    sells: int;
    balance_end: int;
    """

    def __init__(
            self,
            distributor: str,
            name: str,
            region: str | list[str],
            balance_beginning: int = 0,
            incomes: int = 0,
            balance_end: int = 0,
    ):
        self.distributor = distributor
        self.name = name
        self.region = region
        self.balance_beginning = balance_beginning
        self.incomes = incomes
        self.sells = balance_beginning + incomes - balance_end
        self.balance_end = balance_end

    def __repr__(self):
        return f"distributor: {self.distributor}" \
               f"name: {self.name}" \
               f"region: {self.region}" \
               f"balance_beginning:{self.balance_beginning}\n" \
               f"incomes:{self.incomes}\n" \
               f"sells:{self.sells}\n" \
               f"balance_end:{self.balance_end}"

    def __add__(self, other):
        if isinstance(other, PrimaryReportUnitData):
            return PrimaryReportUnitData(
                self.distributor,
                self.name,
                self.region,
                balance_beginning=
                self.balance_beginning + other.balance_beginning,
                incomes=self.incomes + other.incomes,
                balance_end=self.balance_end + other.balance_end,
            )
        else:
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, PrimaryReportUnitData):
            return PrimaryReportUnitData(
                self.distributor,
                self.name,
                self.region,
                balance_beginning=
                self.balance_beginning - other.balance_beginning,
                incomes=self.incomes - other.incomes,
                balance_end=self.balance_end - other.balance_end,
            )
        else:
            raise ValueError


