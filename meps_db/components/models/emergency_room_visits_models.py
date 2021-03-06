from django.db import models


class EmergencyRoomVisits18(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits18"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    EVNTIDX = models.CharField("EVENT ID", max_length=16)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=16)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VISIT DT", max_length=2)
    VSTRELCN = models.CharField("THIS VISIT RELATED TO SPEC CONDITION", max_length=2)
    LABTEST_M18 = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM_M18 = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS_M18 = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG_M18 = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI_M18 = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG_M18 = models.CharField("THIS VISIT DID P HAVE AN EKG, EEG OR ECG", max_length=2)
    RCVVAC_M18 = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP18X = models.CharField("TOTAL EXP FOR EVENT (ERFXP18X + ERDXP18X)", max_length=8)
    ERTC18X = models.CharField("TOTAL CHG FOR EVENT (ERFTC18X+ERDTC18X)", max_length=9)
    ERFSF18X = models.CharField("FACILITY AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERFMR18X = models.CharField("FACILITY AMOUNT PAID, MEDICARE (IMPUTED)", max_length=8)
    ERFMD18X = models.CharField("FACILITY AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERFPV18X = models.CharField("FACILITY AMOUNT PAID, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA18X = models.CharField("FACILITY AMOUNT PAID,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR18X = models.CharField("FACILITY AMOUNT PAID,TRICARE(IMPUTED)", max_length=7)
    ERFOF18X = models.CharField("FACILITY AMOUNT PAID, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL18X = models.CharField("FACILITY AMOUNT PAID, STATELOC GOV (IMPUTED)", max_length=8)
    ERFWC18X = models.CharField("FACILITY AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    ERFOR18X = models.CharField("FACILITY AMOUNT PAID, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU18X = models.CharField("FACILITY AMOUNT PAID, OTH PUB (IMPUTED)", max_length=7)
    ERFOT18X = models.CharField("FACILITY AMOUNT PAID, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP18X = models.CharField("FACILITY SUM PAYMENTS ERFSF18X-ERFOT18X", max_length=8)
    ERFTC18X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF18X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR18X = models.CharField("DOCTOR AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    ERDMD18X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV18X = models.CharField("DOCTOR AMOUNT PAID, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA18X = models.CharField("DOCTOR AMOUNT PAID,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR18X = models.CharField("DOCTOR AMOUNT PAID,TRICARE(IMPUTED)", max_length=7)
    ERDOF18X = models.CharField("DOCTOR AMOUNT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL18X = models.CharField("DOCTOR AMOUNT PAID, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC18X = models.CharField("DOCTOR AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR18X = models.CharField("DOCTOR AMOUNT PAID, OTH PRIV (IMPUTED)", max_length=7)
    ERDOU18X = models.CharField("DOCTOR AMOUNT PAID, OTH PUB (IMPUTED)", max_length=6)
    ERDOT18X = models.CharField("DOCTOR AMOUNT PAID, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP18X = models.CharField("DOCTOR SUM PAYMENTS ERDSF18X - ERDOT18X", max_length=7)
    ERDTC18X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits18 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits17(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits17"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG, EEG OR ECG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP17X = models.CharField("TOT EXP FOR EVENT (ERFXP17X + ERDXP17X)", max_length=8)
    ERTC17X = models.CharField("TOTAL CHG FOR EVENT (ERFTC17X+ERDTC17X)", max_length=9)
    ERFSF17X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=7)
    ERFMR17X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD17X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV17X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA17X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    ERFTR17X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF17X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL17X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC17X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    ERFOR17X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU17X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT17X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP17X = models.CharField("FACILITY SUM PAYMENTS ERFSF17X-ERFOT17X", max_length=8)
    ERFTC17X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF17X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR17X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD17X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV17X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA17X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR17X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERDOF17X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL17X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC17X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR17X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU17X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT17X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP17X = models.CharField("DOCTOR SUM PAYMENTS ERDSF17X - ERDOT17X", max_length=7)
    ERDTC17X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits17 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits16(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits16"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF16 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2016", max_length=2)
    ERXP16X = models.CharField("TOT EXP FOR EVENT (ERFXP16X + ERDXP16X)", max_length=9)
    ERTC16X = models.CharField("TOTAL CHG FOR EVENT (ERFTC16X+ERDTC16X)", max_length=9)
    ERFSF16X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR16X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD16X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV16X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    ERFVA16X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    ERFTR16X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF16X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL16X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC16X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR16X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    ERFOU16X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT16X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP16X = models.CharField("FACILITY SUM PAYMENTS ERFSF16X-ERFOT16X", max_length=9)
    ERFTC16X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF16X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR16X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD16X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV16X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA16X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR16X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF16X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL16X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC16X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR16X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU16X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT16X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP16X = models.CharField("DOCTOR SUM PAYMENTS ERDSF16X - ERDOT16X", max_length=7)
    ERDTC16X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits16 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits15(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits15"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFTOT16 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2015", max_length=2)
    ERXP15X = models.CharField("TOT EXP FOR EVENT (ERFXP15X + ERDXP15X)", max_length=8)
    ERTC15X = models.CharField("TOTAL CHG FOR EVENT (ERFTC15X+ERDTC15X)", max_length=9)
    ERFSF15X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR15X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD15X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV15X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA15X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR15X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF15X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL15X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC15X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR15X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    ERFOU15X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT15X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP15X = models.CharField("FACILITY SUM PAYMENTS ERFSF15X-ERFOT15X", max_length=8)
    ERFTC15X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF15X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR15X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD15X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV15X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA15X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=6)
    ERDTR15X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF15X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL15X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=5)
    ERDWC15X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR15X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU15X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERDOT15X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP15X = models.CharField("DOCTOR SUM PAYMENTS ERDSF15X - ERDOT15X", max_length=7)
    ERDTC15X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits15 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits14(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits14"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP14X = models.CharField("TOT EXP FOR EVENT (ERFXP14X + ERDXP14X)", max_length=9)
    ERTC14X = models.CharField("TOTAL CHG FOR EVENT (ERFTC14X+ERDTC14X)", max_length=9)
    ERFSF14X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR14X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD14X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV14X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    ERFVA14X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR14X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF14X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    ERFSL14X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC14X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR14X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    ERFOU14X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    ERFOT14X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP14X = models.CharField("FACILITY SUM PAYMENTS ERFSF14X-ERFOT14X", max_length=9)
    ERFTC14X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF14X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR14X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    ERDMD14X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV14X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERDVA14X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR14X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF14X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL14X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC14X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR14X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU14X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT14X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP14X = models.CharField("DOCTOR SUM PAYMENTS ERDSF14X - ERDOT14X", max_length=8)
    ERDTC14X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits14 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits13(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits13"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP13X = models.CharField("TOT EXP FOR EVENT (ERFXP13X + ERDXP13X)", max_length=8)
    ERTC13X = models.CharField("TOTAL CHG FOR EVENT (ERFTC13X+ERDTC13X)", max_length=9)
    ERFSF13X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=7)
    ERFMR13X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD13X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV13X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA13X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR13X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF13X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL13X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    ERFWC13X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR13X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU13X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT13X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP13X = models.CharField("FACILITY SUM PAYMENTS ERFSF13X-ERFOT13X", max_length=8)
    ERFTC13X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF13X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR13X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD13X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV13X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA13X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR13X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERDOF13X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL13X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC13X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR13X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU13X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT13X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=6)
    ERDXP13X = models.CharField("DOCTOR SUM PAYMENTS ERDSF13X - ERDOT13X", max_length=7)
    ERDTC13X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits13 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits12(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits12"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF12 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2012", max_length=2)
    ERXP12X = models.CharField("TOT EXP FOR EVENT (ERFXP12X + ERDXP12X)", max_length=8)
    ERTC12X = models.CharField("TOTAL CHG FOR EVENT (ERFTC12X+ERDTC12X)", max_length=9)
    ERFSF12X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR12X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD12X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV12X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA12X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    ERFTR12X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF12X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL12X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC12X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR12X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU12X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    ERFOT12X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP12X = models.CharField("FACILITY SUM PAYMENTS ERFSF12X-ERFOT12X", max_length=8)
    ERFTC12X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF12X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR12X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD12X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV12X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA12X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=6)
    ERDTR12X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERDOF12X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL12X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC12X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR12X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU12X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERDOT12X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=6)
    ERDXP12X = models.CharField("DOCTOR SUM PAYMENTS ERDSF12X - ERDOT12X", max_length=7)
    ERDTC12X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits12 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits11(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits11"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP11X = models.CharField("TOT EXP FOR EVENT (ERFXP11X + ERDXP11X)", max_length=8)
    ERTC11X = models.CharField("TOTAL CHG FOR EVENT (ERFTC11X+ERDTC11X)", max_length=9)
    ERFSF11X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR11X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD11X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV11X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA11X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR11X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF11X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL11X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC11X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    ERFOR11X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    ERFOU11X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    ERFOT11X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP11X = models.CharField("FACILITY SUM PAYMENTS ERFSF11X-ERFOT11X", max_length=8)
    ERFTC11X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF11X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR11X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD11X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV11X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA11X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=6)
    ERDTR11X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF11X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL11X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERDWC11X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=6)
    ERDOR11X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU11X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT11X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP11X = models.CharField("DOCTOR SUM PAYMENTS ERDSF11X - ERDOT11X", max_length=7)
    ERDTC11X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits11 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits10(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits10"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP10X = models.CharField("TOT EXP FOR EVENT (ERFXP10X + ERDXP10X)", max_length=8)
    ERTC10X = models.CharField("TOTAL CHG FOR EVENT (ERFTC10X+ERDTC10X)", max_length=9)
    ERFSF10X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR10X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD10X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV10X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA10X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR10X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF10X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    ERFSL10X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    ERFWC10X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    ERFOR10X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU10X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT10X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP10X = models.CharField("FACILITY SUM PAYMENTS ERFSF10X-ERFOT10X", max_length=8)
    ERFTC10X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF10X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR10X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD10X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    ERDPV10X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA10X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERDTR10X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF10X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL10X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC10X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=6)
    ERDOR10X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU10X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT10X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP10X = models.CharField("DOCTOR SUM PAYMENTS ERDSF10X - ERDOT10X", max_length=8)
    ERDTC10X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits10 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits09(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits09"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP09X = models.CharField("TOT EXP FOR EVENT (ERFXP09X + ERDXP09X)", max_length=8)
    ERTC09X = models.CharField("TOTAL CHG FOR EVENT (ERFTC09X+ERDTC09X)", max_length=9)
    ERFSF09X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR09X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD09X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=8)
    ERFPV09X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA09X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR09X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF09X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL09X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC09X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR09X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU09X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT09X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    ERFXP09X = models.CharField("FACILITY SUM PAYMENTS ERFSF09X-ERFOT09X", max_length=8)
    ERFTC09X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    ERDSF09X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR09X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD09X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV09X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA09X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=6)
    ERDTR09X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERDOF09X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    ERDSL09X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERDWC09X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR09X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU09X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT09X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP09X = models.CharField("DOCTOR SUM PAYMENTS ERDSF09X - ERDOT09X", max_length=7)
    ERDTC09X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits09 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits08(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits08"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    THRTSWAB = models.CharField("THIS VISIT DID P HAVE A THROAT SWAB", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP08X = models.CharField("TOT EXP FOR EVENT (ERFXP08X + ERDXP08X)", max_length=9)
    ERTC08X = models.CharField("TOTAL CHG FOR EVENT (ERFTC08X+ERDTC08X)", max_length=9)
    ERFSF08X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR08X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    ERFMD08X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=7)
    ERFPV08X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA08X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    ERFTR08X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=7)
    ERFOF08X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL08X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC08X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR08X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    ERFOU08X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT08X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP08X = models.CharField("FACILITY SUM PAYMENTS ERFSF08X-ERFOT08X", max_length=9)
    ERFTC08X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=8)
    ERDSF08X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR08X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD08X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV08X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA08X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=6)
    ERDTR08X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=6)
    ERDOF08X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=5)
    ERDSL08X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC08X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR08X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU08X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT08X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP08X = models.CharField("DOCTOR SUM PAYMENTS ERDSF08X - ERDOT08X", max_length=7)
    ERDTC08X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits08 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits07(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits07"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP07X = models.CharField("TOT EXP FOR EVENT (ERFXP07X + ERDXP07X)", max_length=8)
    ERTC07X = models.CharField("TOTAL CHG FOR EVENT (ERFTC07X+ERDTC07X)", max_length=9)
    ERFSF07X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR07X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD07X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=7)
    ERFPV07X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA07X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=7)
    ERFTR07X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=7)
    ERFOF07X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL07X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC07X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR07X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU07X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    ERFOT07X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP07X = models.CharField("FACILITY SUM PAYMENTS ERFSF07X-ERFOT07X", max_length=8)
    ERFTC07X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=8)
    ERDSF07X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR07X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD07X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV07X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA07X = models.CharField("DOCTOR AMOUNT PAID, VETERANS (IMPUTED)", max_length=6)
    ERDTR07X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=6)
    ERDOF07X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=5)
    ERDSL07X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC07X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERDOR07X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU07X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT07X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=6)
    ERDXP07X = models.CharField("DOCTOR SUM PAYMENTS ERDSF07X - ERDOT07X", max_length=7)
    ERDTC07X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=7)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits07 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits06(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits06"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF06 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2006", max_length=2)
    FFTOT07 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2006", max_length=2)
    ERXP06X = models.CharField("TOT EXP FOR EVENT (ERFXP06X + ERDXP06X)", max_length=8)
    ERTC06X = models.CharField("TOTAL CHG FOR EVENT (ERFTC06X+ERDTC06X)", max_length=8)
    ERFSF06X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=7)
    ERFMR06X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    ERFMD06X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=7)
    ERFPV06X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA06X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=8)
    ERFTR06X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=7)
    ERFOF06X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL06X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC06X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR06X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU06X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT06X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP06X = models.CharField("FACILITY SUM PAYMENTS ERFSF06X-ERFOT06X", max_length=8)
    ERFTC06X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=8)
    ERDSF06X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR06X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=7)
    ERDMD06X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV06X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA06X = models.CharField("DOCTOR AMOUNT PAID, VETERANS (IMPUTED)", max_length=6)
    ERDTR06X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=6)
    ERDOF06X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=5)
    ERDSL06X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC06X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=6)
    ERDOR06X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU06X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERDOT06X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=6)
    ERDXP06X = models.CharField("DOCTOR SUM PAYMENTS ERDSF06X - ERDOT06X", max_length=7)
    ERDTC06X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits06 object"""
        return f"{self.DUPERSID}"


class EmergencyRoomVisits05(models.Model):
    """ Defines the EmergencyRoomVisits Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "EmergencyRoomVisits05"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING HOSPITAL STAY", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    ERDATEYR = models.CharField("EVENT DATE - YEAR", max_length=4)
    ERDATEMM = models.CharField("EVENT DATE - MONTH", max_length=2)
    ERDATEDD = models.CharField("EVENT DATE - DAY", max_length=2)
    SEEDOC = models.CharField("DID P TALK TO MD THIS VISIT", max_length=2)
    VSTCTGRY = models.CharField("BEST CATEGORY FOR CARE P RECV ON VST DT", max_length=2)
    VSTRELCN = models.CharField("THIS VST RELATED TO SPEC CONDITION", max_length=2)
    LABTEST = models.CharField("THIS VISIT DID P HAVE LAB TESTS", max_length=2)
    SONOGRAM = models.CharField("THIS VISIT DID P HAVE SONOGRAM OR ULTRSD", max_length=2)
    XRAYS = models.CharField("THIS VISIT DID P HAVE X-RAYS", max_length=2)
    MAMMOG = models.CharField("THIS VISIT DID P HAVE A MAMMOGRAM", max_length=2)
    MRI = models.CharField("THIS VISIT DID P HAVE AN MRICATSCAN", max_length=2)
    EKG = models.CharField("THIS VISIT DID P HAVE AN EKG OR ECG", max_length=2)
    EEG = models.CharField("THIS VISIT DID P HAVE AN EEG", max_length=2)
    RCVVAC = models.CharField("THIS VISIT DID P RECEIVE A VACCINATION", max_length=2)
    ANESTH = models.CharField("THIS VISIT DID P RECEIVE ANESTHESIA", max_length=2)
    OTHSVCE = models.CharField("THIS VISIT DID P HAVE OTH DIAG TESTEXAM", max_length=2)
    SURGPROC = models.CharField("WAS SURG PROC PERFORMED ON P THIS VISIT", max_length=2)
    MEDPRESC = models.CharField("ANY MEDICINE PRESCRIBED FOR P THIS VISIT", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    ERICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    ERPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    ERCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    ERCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    FFERTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    ERXP05X = models.CharField("TOT EXP FOR EVENT (ERFXP05X + ERDXP05X)", max_length=8)
    ERTC05X = models.CharField("TOTAL CHG FOR EVENT (ERFTC05X+ERDTC05X)", max_length=8)
    ERFSF05X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    ERFMR05X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=7)
    ERFMD05X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=7)
    ERFPV05X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    ERFVA05X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=7)
    ERFTR05X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=8)
    ERFOF05X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    ERFSL05X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    ERFWC05X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=7)
    ERFOR05X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=7)
    ERFOU05X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=7)
    ERFOT05X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERFXP05X = models.CharField("FACILITY SUM PAYMENTS ERFSF05X-ERFOT05X", max_length=8)
    ERFTC05X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=8)
    ERDSF05X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    ERDMR05X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=6)
    ERDMD05X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    ERDPV05X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=7)
    ERDVA05X = models.CharField("DOCTOR AMOUNT PAID, VETERANS (IMPUTED)", max_length=6)
    ERDTR05X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=6)
    ERDOF05X = models.CharField("DOCTOR AMT PAID, OTH FEDERAL (IMPUTED)", max_length=6)
    ERDSL05X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    ERDWC05X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=6)
    ERDOR05X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    ERDOU05X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=6)
    ERDOT05X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    ERDXP05X = models.CharField("DOCTOR SUM PAYMENTS ERDSF05X - ERDOT05X", max_length=7)
    ERDTC05X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a EmergencyRoomVisits05 object"""
        return f"{self.DUPERSID}"
