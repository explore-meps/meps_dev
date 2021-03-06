from django.db import models


class HospitalInpatientStays18(models.Model):
    """ Defines the HospitalInpatientStays Model for 2018, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays18"

    DUID = models.CharField("PANEL # + ENCRYPTED DU IDENTIFIER", max_length=7)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=10)
    EVNTIDX = models.CharField("EVENT ID", max_length=16)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=16)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=1)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP18X = models.CharField("TOTAL EXP FOR EVENT (IPFXP18X+IPDXP18X)", max_length=9)
    IPTC18X = models.CharField("TOTAL CHG FOR EVENT (IPFTC18X+IPDTC18X)", max_length=10)
    IPFSF18X = models.CharField("FACILITY AMOUNT PAID, FAMILY (IMPUTED)", max_length=8)
    IPFMR18X = models.CharField("FACILITY AMOUNT PAID, MEDICARE (IMPUTED)", max_length=9)
    IPFMD18X = models.CharField("FACILITY AMOUNT PAID, MEDICAID (IMPUTED)", max_length=9)
    IPFPV18X = models.CharField("FACILITY AMOUNT PAID, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA18X = models.CharField("FACILITY AMOUNT PAID,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR18X = models.CharField("FACILITY AMOUNT PAID,TRICARE(IMPUTED)", max_length=8)
    IPFOF18X = models.CharField("FACILITY AMOUNT PAID, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL18X = models.CharField("FACILITY AMOUNT PAID, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC18X = models.CharField("FACILITY AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR18X = models.CharField("FACILITY AMOUNT PAID, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU18X = models.CharField("FACILITY AMOUNT PAID, OTH PUB (IMPUTED)", max_length=8)
    IPFOT18X = models.CharField("FACILITY AMOUNT PAID, OTH INSUR (IMPUTED)", max_length=9)
    IPFXP18X = models.CharField("FACILITY SUM PAYMENTS IPFSF18X-IPFOT18X", max_length=9)
    IPFTC18X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF18X = models.CharField("DOCTOR AMOUNT PAID, FAMILY (IMPUTED)", max_length=7)
    IPDMR18X = models.CharField("DOCTOR AMOUNT PAID, MEDICARE (IMPUTED)", max_length=7)
    IPDMD18X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV18X = models.CharField("DOCTOR AMOUNT PAID, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA18X = models.CharField("DOCTOR AMOUNT PAID,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPDTR18X = models.CharField("DOCTOR AMOUNT PAID,TRICARE(IMPUTED)", max_length=7)
    IPDOF18X = models.CharField("DOCTOR AMOUNT PAID, OTH FEDERAL (IMPUTED)", max_length=4)
    IPDSL18X = models.CharField("DOCTOR AMOUNT PAID, STATELOC GOV (IMPUTED)", max_length=6)
    IPDWC18X = models.CharField("DOCTOR AMOUNT PAID, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR18X = models.CharField("DOCTOR AMOUNT PAID, OTH PRIV (IMPUTED)", max_length=7)
    IPDOU18X = models.CharField("DOCTOR AMOUNT PAID, OTH PUB (IMPUTED)", max_length=7)
    IPDOT18X = models.CharField("DOCTOR AMOUNT PAID, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP18X = models.CharField("DOCTOR SUM PAYMENTS IPDSF18X-IPDOT18X", max_length=8)
    IPDTC18X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT18F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2018", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2018", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2018", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays18 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays17(models.Model):
    """ Defines the HospitalInpatientStays Model for 2017, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays17"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF17 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2017", max_length=2)
    FFTOT18 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2017", max_length=2)
    IPXP17X = models.CharField("TOT EXP FOR EVENT (IPFXP17X+IPDXP17X)", max_length=9)
    IPTC17X = models.CharField("TOTAL CHG FOR EVENT (IPFTC17X+IPDTC17X)", max_length=9)
    IPFSF17X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR17X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD17X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV17X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA17X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR17X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF17X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    IPFSL17X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC17X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR17X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU17X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT17X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP17X = models.CharField("FACILITY SUM PAYMENTS IPFSF17X-IPFOT17X", max_length=9)
    IPFTC17X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    IPDSF17X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR17X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD17X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    IPDPV17X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA17X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPDTR17X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF17X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    IPDSL17X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    IPDWC17X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR17X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    IPDOU17X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT17X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP17X = models.CharField("DOCTOR SUM PAYMENTS IPDSF17X-IPDOT17X", max_length=8)
    IPDTC17X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT17F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2017", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2017", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2017", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays17 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays16(models.Model):
    """ Defines the HospitalInpatientStays Model for 2016, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays16"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=3)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP16X = models.CharField("TOT EXP FOR EVENT (IPFXP16X+IPDXP16X)", max_length=9)
    IPTC16X = models.CharField("TOTAL CHG FOR EVENT (IPFTC16X+IPDTC16X)", max_length=10)
    IPFSF16X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR16X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD16X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV16X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA16X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR16X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF16X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL16X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC16X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR16X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU16X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT16X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=9)
    IPFXP16X = models.CharField("FACILITY SUM PAYMENTS IPFSF16X-IPFOT16X", max_length=9)
    IPFTC16X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF16X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR16X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD16X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    IPDPV16X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA16X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR16X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF16X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=4)
    IPDSL16X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    IPDWC16X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR16X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    IPDOU16X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT16X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP16X = models.CharField("DOCTOR SUM PAYMENTS IPDSF16X-IPDOT16X", max_length=8)
    IPDTC16X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT16F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2016", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2016", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2016", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays16 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays15(models.Model):
    """ Defines the HospitalInpatientStays Model for 2015, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays15"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=5)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP15X = models.CharField("TOT EXP FOR EVENT (IPFXP15X+IPDXP15X)", max_length=9)
    IPTC15X = models.CharField("TOTAL CHG FOR EVENT (IPFTC15X+IPDTC15X)", max_length=9)
    IPFSF15X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR15X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD15X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV15X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA15X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR15X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF15X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL15X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC15X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR15X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=9)
    IPFOU15X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT15X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=9)
    IPFXP15X = models.CharField("FACILITY SUM PAYMENTS IPFSF15X-IPFOT15X", max_length=9)
    IPFTC15X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    IPDSF15X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR15X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD15X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    IPDPV15X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA15X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR15X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF15X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    IPDSL15X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=6)
    IPDWC15X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR15X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU15X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT15X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP15X = models.CharField("DOCTOR SUM PAYMENTS IPDSF15X-IPDOT15X", max_length=8)
    IPDTC15X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT15F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2015", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2015", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2015", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays15 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays14(models.Model):
    """ Defines the HospitalInpatientStays Model for 2014, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays14"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF14 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2014", max_length=2)
    IPXP14X = models.CharField("TOT EXP FOR EVENT (IPFXP14X+IPDXP14X)", max_length=9)
    IPTC14X = models.CharField("TOTAL CHG FOR EVENT (IPFTC14X+IPDTC14X)", max_length=10)
    IPFSF14X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR14X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD14X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV14X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA14X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPFTR14X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF14X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL14X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC14X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR14X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=9)
    IPFOU14X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=9)
    IPFOT14X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=9)
    IPFXP14X = models.CharField("FACILITY SUM PAYMENTS IPFSF14X-IPFOT14X", max_length=9)
    IPFTC14X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF14X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR14X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD14X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=7)
    IPDPV14X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA14X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR14X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF14X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=5)
    IPDSL14X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC14X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR14X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU14X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT14X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP14X = models.CharField("DOCTOR SUM PAYMENTS IPDSF14X-IPDOT14X", max_length=8)
    IPDTC14X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT14F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2014", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2014", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2014", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays14 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays13(models.Model):
    """ Defines the HospitalInpatientStays Model for 2013, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays13"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFTOT14 = models.CharField("TOTAL # OF VISITS IN FF AFTER 2013", max_length=2)
    IPXP13X = models.CharField("TOT EXP FOR EVENT (IPFXP13X+IPDXP13X)", max_length=9)
    IPTC13X = models.CharField("TOTAL CHG FOR EVENT (IPFTC13X+IPDTC13X)", max_length=10)
    IPFSF13X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR13X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD13X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV13X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA13X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR13X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=9)
    IPFOF13X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    IPFSL13X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC13X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR13X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU13X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=9)
    IPFOT13X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP13X = models.CharField("FACILITY SUM PAYMENTS IPFSF13X-IPFOT13X", max_length=9)
    IPFTC13X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF13X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR13X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD13X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV13X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA13X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR13X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPDOF13X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=5)
    IPDSL13X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC13X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR13X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU13X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT13X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP13X = models.CharField("DOCTOR SUM PAYMENTS IPDSF13X-IPDOT13X", max_length=8)
    IPDTC13X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT13F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2013", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2013", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2013", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays13 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays12(models.Model):
    """ Defines the HospitalInpatientStays Model for 2012, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays12"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=5)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=3)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    EPIDURAL = models.CharField("RECEIVE AN EPIDURAL OR SPINAL FOR PAIN", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP12X = models.CharField("TOT EXP FOR EVENT (IPFXP12X+IPDXP12X)", max_length=9)
    IPTC12X = models.CharField("TOTAL CHG FOR EVENT (IPFTC12X+IPDTC12X)", max_length=10)
    IPFSF12X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=9)
    IPFMR12X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD12X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV12X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA12X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=9)
    IPFTR12X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF12X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    IPFSL12X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC12X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR12X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU12X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT12X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP12X = models.CharField("FACILITY SUM PAYMENTS IPFSF12X-IPFOT12X", max_length=9)
    IPFTC12X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF12X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=8)
    IPDMR12X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD12X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV12X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA12X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR12X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF12X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=4)
    IPDSL12X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPDWC12X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=7)
    IPDOR12X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    IPDOU12X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT12X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP12X = models.CharField("DOCTOR SUM PAYMENTS IPDSF12X-IPDOT12X", max_length=8)
    IPDTC12X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT12F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2012", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2012", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2012", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays12 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays11(models.Model):
    """ Defines the HospitalInpatientStays Model for 2011, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays11"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=5)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    EPIDURAL = models.CharField("RECEIVE AN EPIDURAL OR SPINAL FOR PAIN", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP11X = models.CharField("TOT EXP FOR EVENT (IPFXP11X+IPDXP11X)", max_length=9)
    IPTC11X = models.CharField("TOTAL CHG FOR EVENT (IPFTC11X+IPDTC11X)", max_length=10)
    IPFSF11X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR11X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD11X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV11X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA11X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPFTR11X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF11X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL11X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC11X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=9)
    IPFOR11X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=9)
    IPFOU11X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT11X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP11X = models.CharField("FACILITY SUM PAYMENTS IPFSF11X-IPFOT11X", max_length=9)
    IPFTC11X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF11X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=8)
    IPDMR11X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD11X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV11X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA11X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR11X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPDOF11X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=4)
    IPDSL11X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC11X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR11X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU11X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT11X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP11X = models.CharField("DOCTOR SUM PAYMENTS IPDSF11X-IPDOT11X", max_length=8)
    IPDTC11X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT11F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2011", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2011", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2011", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays11 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays10(models.Model):
    """ Defines the HospitalInpatientStays Model for 2010, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays10"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=5)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    EPIDURAL = models.CharField("RECEIVE AN EPIDURAL OR SPINAL FOR PAIN", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP10X = models.CharField("TOT EXP FOR EVENT (IPFXP10X+IPDXP10X)", max_length=9)
    IPTC10X = models.CharField("TOTAL CHG FOR EVENT (IPFTC10X+IPDTC10X)", max_length=9)
    IPFSF10X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR10X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD10X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV10X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA10X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPFTR10X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF10X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL10X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC10X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR10X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU10X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT10X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP10X = models.CharField("FACILITY SUM PAYMENTS IPFSF10X-IPFOT10X", max_length=9)
    IPFTC10X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    IPDSF10X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=8)
    IPDMR10X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD10X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV10X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA10X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR10X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF10X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=4)
    IPDSL10X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC10X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR10X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU10X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT10X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP10X = models.CharField("DOCTOR SUM PAYMENTS IPDSF10X-IPDOT10X", max_length=8)
    IPDTC10X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT10F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2010", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2010", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2010", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays10 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays09(models.Model):
    """ Defines the HospitalInpatientStays Model for 2009, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays09"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    EPIDURAL = models.CharField("RECEIVE AN EPIDURAL OR SPINAL FOR PAIN", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP09X = models.CharField("TOT EXP FOR EVENT (IPFXP09X+IPDXP09X)", max_length=9)
    IPTC09X = models.CharField("TOTAL CHG FOR EVENT (IPFTC09X+IPDTC09X)", max_length=9)
    IPFSF09X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR09X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD09X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV09X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA09X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPFTR09X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF09X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL09X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=9)
    IPFWC09X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR09X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU09X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=9)
    IPFOT09X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP09X = models.CharField("FACILITY SUM PAYMENTS IPFSF09X-IPFOT09X", max_length=9)
    IPFTC09X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=9)
    IPDSF09X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR09X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD09X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV09X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA09X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR09X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF09X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    IPDSL09X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC09X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR09X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU09X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPDOT09X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP09X = models.CharField("DOCTOR SUM PAYMENTS IPDSF09X-IPDOT09X", max_length=8)
    IPDTC09X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT09F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2009", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2009", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2009", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays09 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays08(models.Model):
    """ Defines the HospitalInpatientStays Model for 2008, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays08"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    DLVRTYPE = models.CharField("VAGINAL OR CAESAREAN DELIVERY", max_length=2)
    EPIDURAL = models.CharField("RECEIVE AN EPIDURAL OR SPINAL FOR PAIN", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP08X = models.CharField("TOT EXP FOR EVENT (IPFXP08X+IPDXP08X)", max_length=9)
    IPTC08X = models.CharField("TOTAL CHG FOR EVENT (IPFTC08X+IPDTC08X)", max_length=10)
    IPFSF08X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR08X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=8)
    IPFMD08X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV08X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA08X = models.CharField("FAC AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=8)
    IPFTR08X = models.CharField("FACILITY AMT PD,TRICARE(IMPUTED)", max_length=8)
    IPFOF08X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL08X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC08X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR08X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=9)
    IPFOU08X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT08X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP08X = models.CharField("FACILITY SUM PAYMENTS IPFSF08X-IPFOT08X", max_length=9)
    IPFTC08X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF08X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR08X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD08X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV08X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA08X = models.CharField("DR AMT PD,VETERANSCHAMPVA(IMPUTED)", max_length=7)
    IPDTR08X = models.CharField("DOCTOR AMT PD,TRICARE(IMPUTED)", max_length=7)
    IPDOF08X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=7)
    IPDSL08X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC08X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR08X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU08X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT08X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP08X = models.CharField("DOCTOR SUM PAYMENTS IPDSF08X-IPDOT08X", max_length=8)
    IPDTC08X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT08F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2008", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2008", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2008", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays08 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays07(models.Model):
    """ Defines the HospitalInpatientStays Model for 2007, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays07"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    IPXP07X = models.CharField("TOT EXP FOR EVENT (IPFXP07X+IPDXP07X)", max_length=9)
    IPTC07X = models.CharField("TOTAL CHG FOR EVENT (IPFTC07X+IPDTC07X)", max_length=10)
    IPFSF07X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR07X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD07X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV07X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA07X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=8)
    IPFTR07X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=8)
    IPFOF07X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL07X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC07X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR07X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU07X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=9)
    IPFOT07X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=9)
    IPFXP07X = models.CharField("FACILITY SUM PAYMENTS IPFSF07X-IPFOT07X", max_length=9)
    IPFTC07X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF07X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR07X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD07X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV07X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA07X = models.CharField("DOCTOR AMOUNT PD, VETERANS (IMPUTED)", max_length=6)
    IPDTR07X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=7)
    IPDOF07X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=5)
    IPDSL07X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC07X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR07X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU07X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT07X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPDXP07X = models.CharField("DOCTOR SUM PAYMENTS IPDSF07X-IPDOT07X", max_length=8)
    IPDTC07X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT07F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2007", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2007", max_length=4)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2007", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays07 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays06(models.Model):
    """ Defines the HospitalInpatientStays Model for 2006, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays06"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=10)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    FFBEF06 = models.CharField("TOTAL # OF VISITS IN FF BEFORE 2006", max_length=2)
    IPXP06X = models.CharField("TOT EXP FOR EVENT (IPFXP06X+IPDXP06X)", max_length=9)
    IPTC06X = models.CharField("TOTAL CHG FOR EVENT (IPFTC06X+IPDTC06X)", max_length=10)
    IPFSF06X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR06X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD06X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV06X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA06X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=9)
    IPFTR06X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=8)
    IPFOF06X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL06X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC06X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR06X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=8)
    IPFOU06X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT06X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP06X = models.CharField("FACILITY SUM PAYMENTS IPFSF06X-IPFOT06X", max_length=9)
    IPFTC06X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF06X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR06X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD06X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV06X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA06X = models.CharField("DOCTOR AMOUNT PD, VETERANS (IMPUTED)", max_length=7)
    IPDTR06X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=7)
    IPDOF06X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    IPDSL06X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC06X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR06X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=8)
    IPDOU06X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT06X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP06X = models.CharField("DOCTOR SUM PAYMENTS IPDSF06X-IPDOT06X", max_length=8)
    IPDTC06X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=8)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT06F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2006", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2006", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2006", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays06 object"""
        return f"{self.DUPERSID}"


class HospitalInpatientStays05(models.Model):
    """ Defines the HospitalInpatientStays Model for 2005, derived from the model class. """

    # Metadata
    class Meta:
        """ Set parameters for admin app"""

        ordering = ["DUPERSID"]
        verbose_name_plural = "HospitalInpatientStays05"

    DUID = models.CharField("DWELLING UNIT ID", max_length=5)
    PID = models.CharField("PERSON NUMBER", max_length=3)
    DUPERSID = models.CharField("PERSON ID (DUID + PID)", max_length=8)
    EVNTIDX = models.CharField("EVENT ID", max_length=12)
    EVENTRN = models.CharField("EVENT ROUND NUMBER", max_length=1)
    ERHEVIDX = models.CharField("EVENT ID FOR CORRESPONDING EMER RM VISIT", max_length=12)
    FFEEIDX = models.CharField("FLAT FEE ID", max_length=5)
    PANEL = models.CharField("PANEL NUMBER", max_length=2)
    MPCDATA = models.CharField("MPC DATA FLAG", max_length=1)
    IPBEGYR = models.CharField("EVENT START DATE - YEAR", max_length=4)
    IPBEGMM = models.CharField("EVENT START DATE - MONTH", max_length=2)
    IPBEGDD = models.CharField("EVENT START DATE - DAY", max_length=2)
    IPENDYR = models.CharField("EVENT END DATE - YEAR", max_length=4)
    IPENDMM = models.CharField("EVENT END DATE - MONTH", max_length=2)
    IPENDDD = models.CharField("EVENT END DATE - DAY", max_length=2)
    NUMNIGHX = models.CharField("# OF NIGHTS IN HOSPITAL - EDITEDIMPUTED", max_length=3)
    NUMNIGHT = models.CharField("NUMBER OF NIGHTS STAYED AT PROVIDER", max_length=2)
    EMERROOM = models.CharField("DID STAY BEGIN WITH EMERGENCY ROOM VISIT", max_length=2)
    SPECCOND = models.CharField("HOSPITAL STAY RELATED TO CONDITION", max_length=2)
    RSNINHOS = models.CharField("REASON ENTERED HOSPITAL", max_length=2)
    ANYOPER = models.CharField("ANY OPERATIONS OR SURGERIES PERFORMED", max_length=2)
    VAPLACE = models.CharField("VA FACILITY FLAG", max_length=1)
    IPICD1X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD2X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD3X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPICD4X = models.CharField("3-DIGIT ICD-9-CM CONDITION CODE", max_length=3)
    IPPRO1X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPPRO2X = models.CharField("2-DIGIT ICD-9-CM PROCEDURE CODE", max_length=2)
    IPCCC1X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC2X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC3X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    IPCCC4X = models.CharField("MODIFIED CLINICAL CLASSIFICATION CODE", max_length=3)
    DSCHPMED = models.CharField("MEDICINES PRESCRIBED AT DISCHARGE", max_length=2)
    FFIPTYPE = models.CharField("FLAT FEE BUNDLE", max_length=2)
    IPXP05X = models.CharField("TOT EXP FOR EVENT (IPFXP05X+IPDXP05X)", max_length=9)
    IPTC05X = models.CharField("TOTAL CHG FOR EVENT (IPFTC05X+IPDTC05X)", max_length=10)
    IPFSF05X = models.CharField("FACILITY AMT PD, FAMILY (IMPUTED)", max_length=8)
    IPFMR05X = models.CharField("FACILITY AMT PD, MEDICARE (IMPUTED)", max_length=9)
    IPFMD05X = models.CharField("FACILITY AMT PD, MEDICAID (IMPUTED)", max_length=9)
    IPFPV05X = models.CharField("FACILITY AMT PD, PRIV INSUR (IMPUTED)", max_length=9)
    IPFVA05X = models.CharField("FACILITY AMT PD, VETERANS (IMPUTED)", max_length=8)
    IPFTR05X = models.CharField("FACILITY AMT PD,TRICARECHAMPVA(IMPUTED)", max_length=8)
    IPFOF05X = models.CharField("FACILITY AMT PD, OTH FEDERAL (IMPUTED)", max_length=8)
    IPFSL05X = models.CharField("FACILITY AMT PD, STATELOC GOV (IMPUTED)", max_length=8)
    IPFWC05X = models.CharField("FACILITY AMT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPFOR05X = models.CharField("FACILITY AMT PD, OTH PRIV (IMPUTED)", max_length=9)
    IPFOU05X = models.CharField("FACILITY AMT PD, OTH PUB (IMPUTED)", max_length=8)
    IPFOT05X = models.CharField("FACILITY AMT PD, OTH INSUR (IMPUTED)", max_length=8)
    IPFXP05X = models.CharField("FACILITY SUM PAYMENTS IPFSF05X-IPFOT05X", max_length=9)
    IPFTC05X = models.CharField("TOTAL FACILITY CHARGE (IMPUTED)", max_length=10)
    IPDSF05X = models.CharField("DOCTOR AMOUNT PD, FAMILY (IMPUTED)", max_length=7)
    IPDMR05X = models.CharField("DOCTOR AMOUNT PD, MEDICARE (IMPUTED)", max_length=8)
    IPDMD05X = models.CharField("DOCTOR AMOUNT PAID, MEDICAID (IMPUTED)", max_length=8)
    IPDPV05X = models.CharField("DOCTOR AMT PD, PRIV INSUR (IMPUTED)", max_length=8)
    IPDVA05X = models.CharField("DOCTOR AMOUNT PD, VETERANS (IMPUTED)", max_length=7)
    IPDTR05X = models.CharField("DOCTOR AMT PD, TRICARECHAMPVA (IMPUTED)", max_length=7)
    IPDOF05X = models.CharField("DOCTOR AMT PD, OTH FEDERAL (IMPUTED)", max_length=6)
    IPDSL05X = models.CharField("DOCTOR AMT PD, STATELOC GOV (IMPUTED)", max_length=7)
    IPDWC05X = models.CharField("DOCTOR AMOUNT PD, WORKERS COMP (IMPUTED)", max_length=8)
    IPDOR05X = models.CharField("DOCTOR AMT PD, OTH PRIVATE (IMPUTED)", max_length=7)
    IPDOU05X = models.CharField("DOCTOR AMT PD, OTH PUB (IMPUTED)", max_length=7)
    IPDOT05X = models.CharField("DOCTOR AMT PD, OTH INSUR (IMPUTED)", max_length=7)
    IPDXP05X = models.CharField("DOCTOR SUM PAYMENTS IPDSF05X-IPDOT05X", max_length=8)
    IPDTC05X = models.CharField("TOTAL DOCTOR CHARGE (IMPUTED)", max_length=9)
    IMPFLAG = models.CharField("IMPUTATION STATUS", max_length=1)
    PERWT05F = models.CharField("EXPENDITURE FILE PERSON WEIGHT, 2005", max_length=12)
    VARSTR = models.CharField("VARIANCE ESTIMATION STRATUM, 2005", max_length=3)
    VARPSU = models.CharField("VARIANCE ESTIMATION PSU, 2005", max_length=1)

    # Methods
    def __str__(self):
        """String for representing a HospitalInpatientStays05 object"""
        return f"{self.DUPERSID}"
