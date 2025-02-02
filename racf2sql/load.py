import sqlite3
import click

def load_racf(unload, db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    with open(unload, encoding="utf8", errors='ignore') as fp:
        for line in fp:
            process(line, c)
    conn.commit()
    conn.close()

def process(l, c):
    if len(l) < 4:
        click.secho(f"WARN: Unexpected short line:\n\t{l}", fg='red')
        return

    record_type = l[0:4]

    if record_type ==   "0100":
        process_gpbd(l, c)
    elif record_type == "0101":
        process_gpsgrp(l, c)
    elif record_type == "0102":
        process_gpmem(l, c)
    elif record_type == "0103":
        process_gpinstd(l, c)
    elif record_type == "0110":
        process_gpdfp(l, c)
    elif record_type == "0120":
        process_gpomvs(l, c)
    elif record_type == "0130":
        process_gpovm(l, c)
    elif record_type == "0141":
        process_gptme(l, c)
    elif record_type == "0151":
        process_gpcsd(l, c)
    elif record_type == "0200":
        process_usbd(l, c)
    elif record_type == "0201":
        process_uscat(l, c)
    elif record_type == "0202":
        process_uscla(l, c)
    elif record_type == "0203":
        process_usgcon(l, c)
    elif record_type == "0204":
        process_usinstd(l, c)
    elif record_type == "0205":
        process_uscon(l, c)
    elif record_type == "0206":
        process_usrsf(l, c)
    elif record_type == "0207":
        process_uscert(l, c)
    elif record_type == "0208":
        process_usnmap(l, c)
    elif record_type == "0209":
        process_usdmap(l, c)
    elif record_type == "020A":
        process_usmfa(l, c)
    elif record_type == "020B":
        process_usmpol(l, c)
    elif record_type == "0210":
        process_usdfp(l, c)
    elif record_type == "0220":
        process_ustso(l, c)
    elif record_type == "0230":
        process_uscics(l, c)
    elif record_type == "0231":
        process_uscopc(l, c)
    elif record_type == "0232":
        process_uscrsl(l, c)
    elif record_type == "0233":
        process_usctsl(l, c)
    elif record_type == "0240":
        process_uslan(l, c)
    elif record_type == "0250":
        process_usopr(l, c)
    elif record_type == "0251":
        process_usoprp(l, c)
    elif record_type == "0260":
        process_uswrk(l, c)
    elif record_type == "0270":
        process_usomvs(l, c)
    elif record_type == "0280":
        process_usnetv(l, c)
    elif record_type == "0281":
        process_usnopc(l, c)
    elif record_type == "0282":
        process_usndom(l, c)
    elif record_type == "0290":
        process_usdce(l, c)
    elif record_type == "02A0":
        process_usovm(l, c)
    elif record_type == "02B0":
        process_uslnot(l, c)
    elif record_type == "02C0":
        process_usnds(l, c)
    elif record_type == "02D0":
        process_uskerb(l, c)
    elif record_type == "02E0":
        process_usproxy(l, c)
    elif record_type == "02F0":
        process_useim(l, c)
    elif record_type == "02G1":
        process_uscsd(l, c)
    elif record_type == "1210":
        process_usmfac(l, c)
    elif record_type == "0400":
        process_dsbd(l, c)
    elif record_type == "0401":
        process_dscat(l, c)
    elif record_type == "0402":
        process_dscacc(l, c)
    elif record_type == "0403":
        process_dsvol(l, c)
    elif record_type == "0404":
        process_dsacc(l, c)
    elif record_type == "0405":
        process_dsinstd(l, c)
    elif record_type == "0410":
        process_dsdfp(l, c)
    elif record_type == "0421":
        process_dstme(l, c)
    elif record_type == "0500":
        process_grbd(l, c)
    elif record_type == "0501":
        process_grtvol(l, c)
    elif record_type == "0502":
        process_grcat(l, c)
    elif record_type == "0503":
        process_grmem(l, c)
    elif record_type == "0504":
        process_grvol(l, c)
    elif record_type == "0505":
        process_gracc(l, c)
    elif record_type == "0506":
        process_grinstd(l, c)
    elif record_type == "0507":
        process_grcacc(l, c)
    elif record_type == "0508":
        process_grfltr(l, c)
    elif record_type == "0509":
        process_grdmap(l, c)
    elif record_type == "0510":
        process_grses(l, c)
    elif record_type == "0511":
        process_grsese(l, c)
    elif record_type == "0520":
        process_grdlf(l, c)
    elif record_type == "0521":
        process_grdlfj(l, c)
    elif record_type == "0530":
        process_grsign(l, c)
    elif record_type == "0540":
        process_grst(l, c)
    elif record_type == "0550":
        process_grsv(l, c)
    elif record_type == "0560":
        process_grcert(l, c)
    elif record_type == "0561":
        process_certr(l, c)
    elif record_type == "0562":
        process_keyr(l, c)
    elif record_type == "0570":
        process_grtme(l, c)
    elif record_type == "0571":
        process_grtmec(l, c)
    elif record_type == "0572":
        process_grtmer(l, c)
    elif record_type == "0573":
        process_grtmeg(l, c)
    elif record_type == "0574":
        process_grtmee(l, c)
    elif record_type == "0580":
        process_grkerb(l, c)
    elif record_type == "0590":
        process_grproxy(l, c)
    elif record_type == "05A0":
        process_greim(l, c)
    elif record_type == "05B0":
        process_gralias(l, c)
    elif record_type == "05C0":
        process_grcdt(l, c)
    elif record_type == "05D0":
        process_grictx(l, c)
    elif record_type == "05E0":
        process_grcfdef(l, c)
    elif record_type == "05F0":
        process_grsig(l, c)
    elif record_type == "05G0":
        process_grcsf(l, c)
    elif record_type == "05G1":
        process_grcsfk(l, c)
    elif record_type == "05G2":
        process_grcsfc(l, c)
    elif record_type == "05H0":
        process_grmfa(l, c)
    elif record_type == "05I0":
        process_grmfp(l, c)
    elif record_type == "05I1":
        process_grmpf(l, c)
    elif record_type == "05J1":
        process_grcsd(l, c)
    elif record_type == "05K0" or record_type == "05k0":    #IBM's documentation has a lowercase K in places, which we might as well handle.
        process_gridtp(l, c)
    elif record_type == "05L0":
        process_grjes(l, c)
    elif record_type == "1560":
        process_certn(l, c)
    else:
        click.secho(f"WARN: Uncategorised/unknown line:\n\t{l}", fg='red')

def process_gpbd(l, c):
    v = (
        l[5:13].strip(),        #GPBD_NAME:         Group name as taken from the profile name.
        l[14:22].strip(),       #GPBD_SUPGRP_ID:    Name of the superior group to this group.
        l[23:33].strip(),       #GPBD_CREATE_DATE:  Date that the group was defined.
        l[34:42].strip(),       #GPBD_OWNER_ID:     The user ID or group name which owns the profile.
        l[43:51].strip(),       #GPBD_UACC:         The default universal access. Valid values are NONE for all groups other than the IBM®-defined VSAMDSET group which has CREATE.
        l[52:56].strip(),       #GPBD_NOTERMUACC:   Indicates if the group must be specifically authorized to use a particular terminal through the use of the PERMIT command.
        l[57:312].strip(),      #GPBD_INSTALL_DATA: Installation-defined data.
        l[313:357].strip(),     #GPBD_MODEL:        Data set profile that is used as a model for this group.
        l[358:362].strip(),     #GPBD_UNIVERSAL:    Indicates if the group has the UNIVERSAL attribute.
    )
    c.execute("INSERT INTO gpbd VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0100) Group Basic Data Record processed.")

def process_gpsgrp(l, c):
    v = (
        l[5:13].strip(),        #GPSGRP_NAME:       Group name as taken from the profile name.
        l[14:22].strip(),       #GPSGRP_SUBGRP_ID:  The name of a subgroup within the group.
    )
    c.execute("INSERT INTO gpsgrp VALUES (?, ?)", v)
    print("INFO: (0101) Group Subgroups Record processed.")

def process_gpmem(l, c):
    v = (
        l[5:13].strip(),        #GPMEM_NAME:        Group name as taken from the profile name.
        l[14:22].strip(),       #GPMEM_MEMBER_ID:   A user ID within the group.
        l[23:31].strip(),       #GPMEM_AUTH:        Indicates the authority that the user ID has within the group. Valid values are USE, CONNECT, JOIN, and CREATE.
    )
    c.execute("INSERT INTO gpmem VALUES (?, ?, ?)", v)
    print("INFO: (0102) Group Members Record processed.")

def process_gpinstd(l, c):
    v = (
        l[5:13].strip(),        #GPINSTD_NAME:      Group name as taken from the profile name.
        l[14:22].strip(),       #GPINSTD_USR_NAME:  The name of the installation-defined field.
        l[23:278].strip(),      #GPINSTD_USR_DATA:  The data for the installation-defined field.
        l[279:287].strip(),     #GPINSTD_USR_FLAG:  The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO gpinstd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0103) Group Installation Data Record processed.")

def process_gpdfp(l, c):
    v = (
        l[5:13].strip(),        #GPDFP_NAME         Group name as taken from the profile name.
        l[14:22].strip(),       #GPDFP_DATAAPPL     Default application name for the group.
        l[23:31].strip(),       #GPDFP_DATACLAS     Default data class for the group.
        l[32:40].strip(),       #GPDFP_MGMTCLAS     Default management class for the group.
        l[41:49].strip(),       #GPDFP_STORCLAS     Default storage class for the group.
    )
    c.execute("INSERT INTO gpdfp VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0110) Group DFP Data Record processed.")

def process_gpomvs(l, c):
    v = (
        l[5:13].strip(),        #GPOMVS_NAME        Group name as taken from the profile name.
        l[14:24].strip(),       #GPOMVS_GID         OMVS z/OS UNIX group identifier (GID) associated with the group name from the profile.
    )
    c.execute("INSERT INTO gpomvs VALUES(?, ?)", v)
    print("INFO: (0120) Group OMVS Data Record processed.")

def process_gpovm(l, c):
    v = (
        l[5:13].strip(),        #GPOVM_NAME         Group name as taken from the profile name.
        l[14:24].strip(),       #GPOVM_GID          OpenExtensions group identifier (GID) associated with the group name from the profile.
    )
    c.execute("INSERT INTO gpovm VALUES(?, ?)", v)
    print("INFO: (0130) Group OVM Data Record processed.")

def process_gptme(l, c):
    v = (
        l[5:13].strip(),        #GPTME_NAME         Group name as taken from the profile name.
        l[14:260].strip(),      #GPTME_ROLE         Role profile name.
    )
    c.execute("INSERT INTO gptme VALUES(?, ?)", v)
    print("INFO: (0141) Group TME Record processed.")

def process_gpcsd(l, c):
    v = (
        l[5:13].strip(),        #GPCSD_NAME         Group name.
        l[14:18].strip(),       #GPCSD_TYPE         Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[19:51].strip(),       #GPCSD_KEY          Custom field keyword; maximum length = 8.
        l[52:1152].strip(),     #GPCSD_VALUE        Custom field value.
    )
    c.execute("INSERT INTO gpcsd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0151) Group CSDATA Custom Fields Record processed.")

def process_usbd(l, c):
    v = (
        l[5:13].strip(),        #USBD_NAME          User ID as taken from the profile name.
        l[14:24].strip(),       #USBD_CREATE_DATE   The date that the profile was created.
        l[25:33].strip(),       #USBD_OWNER_ID      The user ID or group name that owns the profile.
        l[34:38].strip(),       #USBD_ADSP          Does the user have the ADSP attribute?
        l[39:43].strip(),       #USBD_SPECIAL       Does the user have the SPECIAL attribute?
        l[44:48].strip(),       #USBD_OPER          Does the user have the OPERATIONS attribute?
        l[49:53].strip(),       #USBD_REVOKE        Is the user REVOKEd?
        l[54:58].strip(),       #USBD_GRPACC        Does the user have the GRPACC attribute?
        l[59:62].strip(),       #USBD_PWD_INTERVAL  The number of days that the user's password can be used.
        l[63:73].strip(),       #USBD_PWD_DATE      The date that the password was last changed.
        l[74:94].strip(),       #USBD_PROGRAMMER    The name associated with the user ID.
        l[95:103].strip(),      #USBD_DEFGRP_ID     The default group associated with the user.
        l[104:112].strip(),     #USBD_LASTJOB_TIME  The last recorded time that the user entered the system.
        l[113:123].strip(),     #USBD_LASTJOB_DATE  The last recorded date that the user entered the system.
        l[124:379].strip(),     #USBD_INSTALL_DATA  Installation-defined data.
        l[380:384].strip(),     #USBD_UAUDIT        Do all RACHECK and RACDEF SVCs cause logging?
        l[385:389].strip(),     #USBD_AUDITOR       Does this user have the AUDITOR attribute?
        l[390:394].strip(),     #USBD_NOPWD         "YES" indicates that this user ID can log on without a password using OID card. "NO" indicates that this user must specify a password. "PRO" indicates a protected user ID. "PHR" indicates that the user has a password phrase. See also z/OS Security Server RACF Security Administrator's Guide.
        l[395:399].strip(),     #USBD_OIDCARD       Does this user have OIDCARD data?
        l[400:403].strip(),     #USBD_PWD_GEN       The current password generation number.
        l[404:407].strip(),     #USBD_REVOKE_CNT    The number of unsuccessful logon attempts.
        l[408:452].strip(),     #USBD_MODEL         The data set model profile name.
        l[453:456].strip(),     #USBD_SECLEVEL      The user's security level.
        l[457:467].strip(),     #USBD_REVOKE_DATE   The date that the user will be revoked.
        l[468:478].strip(),     #USBD_RESUME_DATE   The date that the user will be resumed.
        l[479:483].strip(),     #USBD_ACCESS_SUN    Can the user access the system on Sunday?
        l[484:488].strip(),     #USBD_ACCESS_MON    Can the user access the system on Monday?
        l[489:493].strip(),     #USBD_ACCESS_TUE    Can the user access the system on Tuesday?
        l[494:498].strip(),     #USBD_ACCESS_WED    Can the user access the system on Wednesday?
        l[499:503].strip(),     #USBD_ACCESS_THU    Can the user access the system on Thursday?
        l[504:508].strip(),     #USBD_ACCESS_FRI    Can the user access the system on Friday?
        l[509:513].strip(),     #USBD_ACCESS_SAT    Can the user access the system on Saturday?
        l[514:522].strip(),     #USBD_START_TIME    After what time can the user log on?
        l[523:531].strip(),     #USBD_END_TIME      After what time can the user not log on?
        l[532:540].strip(),     #USBD_SECLABEL      The user's default security label.
        l[541:549].strip(),     #USBD_ATTRIBS       Other user attributes (RSTD for users with RESTRICTED attribute).
        l[550:554].strip(),     #USBD_PWDENV_EXISTS Has a PKCS#7 envelope been created for the user's current password?
        l[555:559].strip(),     #USBD_PWD_ASIS      Should the password be evaluated in the case entered?
        l[560:570].strip(),     #USBD_PHR_DATE      The date the password phrase was last changed.
        l[571:574].strip(),     #USBD_PHR_GEN       The current password phrase generation number.
        l[575:585].strip(),     #USBD_CERT_SEQN     Sequence number that is incremented whenever a certificate for the user is added, deleted, or altered. The starting value might not be 0.
        l[586:590].strip(),     #USBD_PPHENV_EXISTS Has the user's current password phrase been PKCS#7 enveloped for possible retrieval?
    )
    c.execute("INSERT INTO usbd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0200) User Basic Data Record processed.")

def process_uscat(l, c):
    v = (
        l[5:13].strip(),        #USCAT_NAME         User ID as taken from the profile name.
        l[14:19].strip(),       #USCAT_CATEGORY     Category to which the user has access.
    )
    c.execute("INSERT INTO uscat VALUES(?, ?)", v)
    print("INFO: (0201) User Categories Record processed.")

def process_uscla(l, c):
    v = (
        l[5:13].strip(),        #USCLA_NAME         User ID as taken from the profile name.
        l[14:22].strip(),       #USCLA_CLASS        A class in which the user is allowed to define profiles.
    )
    c.execute("INSERT INTO uscla VALUES(?, ?)", v)
    print("INFO: (0202) User Classes Record processed.")

def process_usgcon(l, c):
    v = (
        l[5:13].strip(),        #USGCON_NAME        User ID as taken from the profile name.
        l[14:22].strip(),       #USGCON_GRP_ID      The group with which the user is associated.
    )
    c.execute("INSERT INTO usgcon VALUES(?, ?)", v)
    print("INFO: (0203) User Group Connections Record processed.")

def process_usinstd(l, c):
    v = (
        l[5:13].strip(),        #USINSTD_NAME       User ID as taken from the profile name.
        l[14:22].strip(),       #USINSTD_USR_NAME   The name of the installation-defined field.
        l[23:278].strip(),      #USINSTD_USR_DATA   The data for the installation-defined field.
        l[279:287].strip(),     #USINSTD_USR_FLAG   The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO usinstd VALUES(?, ?, ?, ?)", v)
    print("INFO: (0204) User Installation Data Record processed.")

def process_uscon(l, c):
    v = (
        l[5:13].strip(),        #USCON_NAME         User ID as taken from the profile name.
        l[14:22].strip(),       #USCON_GRP_ID       The group name.
        l[23:33].strip(),       #USCON_CONNECT_DATE The date that the user was connected.
        l[34:42].strip(),       #USCON_OWNER_ID     The owner of the user-group connection.
        l[43:51].strip(),       #USCON_LASTCON_TIME Time that the user last connected to this group.
        l[52:62].strip(),       #USCON_LASTCON_DATE Date that the user last connected to this group.
        l[63:71].strip(),       #USCON_UACC         The default universal access authority for all new resources the user defines while connected to the specified group. Valid values are NONE, READ, UPDATE, CONTROL, and ALTER.
        l[72:77].strip(),       #USCON_INIT_CNT     The number of RACINITs issued for this user/group combination.
        l[78:82].strip(),       #USCON_GRP_ADSP     Does this user have the ADSP attribute in this group?
        l[83:87].strip(),       #USCON_GRP_SPECIAL  Does this user have GROUP-SPECIAL in this group?
        l[88:92].strip(),       #USCON_GRP_OPER     Does this user have GROUP-OPERATIONS in this group?
        l[93:97].strip(),       #USCON_REVOKE       Is this user revoked?
        l[98:102].strip(),      #USCON_GRP_ACC      Does this user have the GRPACC attribute?
        l[103:107].strip(),     #USCON_NOTERMUACC   Does this user have the NOTERMUACC attribute in this group?
        l[108:112].strip(),     #USCON_GRP_AUDIT    Does this user have the GROUP-AUDITOR attribute in this group?
        l[113:123].strip(),     #USCON_REVOKE_DATE  The date that the user's connection to the group will be revoked.
        l[123:134].strip(),     #USCON_RESUME_DATE  The date that the user's connection to the group will be resumed.
    )
    c.execute("INSERT INTO uscon VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0205) User Connect Data Record processed.")

def process_usrsf(l, c):
    v = (
        l[5:13].strip(),        #USRSF_NAME         User ID as taken from the profile name.
        l[14:22].strip(),       #USRSF_TARG_NODE    Target node name.
        l[23:31].strip(),       #USRSF_TARG_USER_ID Target user ID.
        l[32:35].strip(),       #USRSF_VERSION      Version of this record.
        l[36:40].strip(),       #USRSF_PEER         Is this a peer user ID?
        l[41:45].strip(),       #USRSF_MANAGING     Is USRSF_NAME managing this ID?
        l[46:50].strip(),       #USRSF_MANAGED      Is USRSF_NAME being managed by this ID?
        l[51:55].strip(),       #USRSF_REMOTE_PEND  Is this remote RACF association pending?
        l[56:60].strip(),       #USRSF_LOCAL_PEND   Is this local RACF association pending?
        l[61:65].strip(),       #USRSF_PWD_SYNC     Is there password synchronization with this user ID?
        l[66:70].strip(),       #USRSF_REM_REFUSAL  Was a system error encountered on the remote system?
        l[71:81].strip(),       #USRSF_DEFINE_DATE  GMT date stamp for when this record was defined.
        l[82:97].strip(),       #USRSF_DEFINE_TIME  GMT time stamp for when this record was defined.
        l[98:108].strip(),      #USRSF_ACCEPT_DATE  GMT date stamp when this association was approved or refused. Based on the REMOTE_REFUSAL bit setting.
        l[109:124].strip(),     #USRSF_ACCEPT_TIME  GMT time stamp when this association was approved or refused. Based on the REMOTE_REFUSAL bit setting.
        l[125:133].strip(),     #USRSF_CREATOR_ID   User ID who created this entry.
    )
    c.execute("INSERT INTO usrsf VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0206) User RRSF Data Record processed.")

def process_uscert(l, c):
    v = (
        l[5:13].strip(),        #USCERT_NAME        User ID as taken from the profile name.
        l[14:260].strip(),      #USCERT_CERT_NAME   Digital certificate name.
        l[261:293].strip(),     #USCERT_CERTLABL    Digital certificate label.
    )
    c.execute("INSERT INTO uscert VALUES(?, ?, ?)", v)
    print("INFO: (0207) User Certificate Name Record processed.")

def process_usnmap(l, c):
    v = (
        l[5:13].strip(),        #USNMAP_NAME        User ID as taken from the profile name.
        l[14:46].strip(),       #USNMAP_LABEL       The label associated with this mapping.
        l[47:293].strip(),      #USNMAP_MAP_NAME    The name of the DIGTNMAP profile associated with this user.
    )
    c.execute("INSERT INTO usnmap VALUES(?, ?, ?)", v)
    print("INFO: (0208) User Associated Mappings Record processed.")

def process_usdmap(l, c):
    v = (
        l[5:13].strip(),        #USDMAP_NAME        User ID as taken from the profile name.
        l[14:46].strip(),       #USDMAP_LABEL       The label associated with this mapping.
        l[47:293].strip(),      #USDMAP_MAP_NAME    The name of the IDIDMAP profile associated with this user. Note: This value is stored in the RACF database in UTF-8 format. If possible, database unload changes this value to the EBCDIC format. If not possible, hexadecimal values are produced.
    )
    c.execute("INSERT INTO usdmap VALUES(?, ?, ?)", v)
    print("INFO: (0209) User Associated Distributed Mappings Record processed.")

def process_usmfa(l, c):
    v = (
        l[5:13].strip(),        #USMFA_NAME         User ID as taken from the profile name.
        l[14:34].strip(),       #USMFA_FACTOR_NAME  Factor name.
        l[35:54].strip(),       #USMFA_FACTOR_ACTIVE  Factor active date. Will be blank if factor is not ACTIVE.
    )
    c.execute("INSERT INTO usmfa VALUES(?, ?, ?)", v)
    print("INFO: (020A) User MFA Factor Data Record processed.")

def process_usmpol(l, c):
    v = (
        l[5:13].strip(),        #USMPOL_NAME        User ID as taken from the profile name.
        l[14:34].strip(),       #USMPOL_POLICY_NAME MFA Policy name.
    )
    c.execute("INSERT INTO usmpol VALUES(?, ?)", v)
    print("INFO: (020B) User MFA Policies Record processed.")

def process_usdfp(l, c):
    v = (
        l[5:13].strip(),        #USDFP_NAME         User ID as taken from the profile name.
        l[14:22].strip(),       #USDFP_DATAAPPL     Default application name for the user.
        l[23:31].strip(),       #USDFP_DATACLAS     Default data class for the user.
        l[32:40].strip(),       #USDFP_MGMTCLAS     Default management class for the user.
        l[41:49].strip(),       #USDFP_STORCLAS     Default storage class for the user.
    )
    c.execute("INSERT INTO usdfp VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0210) User DFP Data Record processed.")

def process_ustso(l, c):
    v = (
        l[5:13].strip(),        #USTSO_NAME         User ID as taken from the profile name.
        l[14:54].strip(),       #USTSO_ACCOUNT      The default account number.
        l[55:135].strip(),      #USTSO_COMMAND      The command issued at LOGON.
        l[136:144].strip(),     #USTSO_DEST         The default destination identifier.
        l[145:146].strip(),     #USTSO_HOLD_CLASS   The default hold class.
        l[147:148].strip(),     #USTSO_JOB_CLASS    The default job class.
        l[149:157].strip(),     #USTSO_LOGON_PROC   The default logon procedure.
        l[158:168].strip(),     #USTSO_LOGON_SIZE   The default logon region size.
        l[169:170].strip(),     #USTSO_MSG_CLASS    The default message class.
        l[171:181].strip(),     #USTSO_LOGON_MAX    The maximum logon region size.
        l[182:192].strip(),     #USTSO_PERF_GROUP   The performance group associated with the user.
        l[193:194].strip(),     #USTSO_SYSOUT_CLASS The default sysout class.
        l[195:203].strip(),     #USTSO_USER_DATA    The TSO user data, in hexadecimal in the form X<cccc>.
        l[204:212].strip(),     #USTSO_UNIT_NAME    The default SYSDA device.
        l[213:221].strip(),     #USTSO_SECLABEL     The default logon security label.
    )
    c.execute("INSERT INTO ustso VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0220) User TSO Data Record processed.")

def process_uscics(l, c):
    v = (
        l[5:13].strip(),        #USCICS_NAME        User ID as taken from the profile name.
        l[14:17].strip(),       #USCICS_OPIDENT     The CICS operator identifier.
        l[18:23].strip(),       #USCICS_OPPRTY      The CICS operator priority.
        l[24:28].strip(),       #USCICS_NOFORCE     Is the extended recovery facility (XRF) NOFORCE option in effect?
        l[29:34].strip(),       #USCICS_TIMEOUT     The terminal time-out value. Expressed in hh:mm
    )
    c.execute("INSERT INTO uscics VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0230) User CICS Data Record processed.")

def process_uscopc(l, c):
    v = (
        l[5:13].strip(),        #USCOPC_NAME        User ID as taken from the profile name.
        l[14:17].strip(),       #USCOPC_OPCLASS     The class associated with the CICS operator.
    )
    c.execute("INSERT INTO uscopc VALUES(?, ?)", v)
    print("INFO: (0231) User CICS Operator Classes Record processed.")

def process_uscrsl(l, c):
    v = (
        l[5:13].strip(),        #USCRSL_NAME        User ID as taken from the profile name.
        l[14:19].strip(),       #USCRSL_KEY         RSL key number.
    )
    c.execute("INSERT INTO uscrsl VALUES(?, ?)", v)
    print("INFO: (0232) User CICS RSL Keys Record processed.")

def process_usctsl(l, c):
    v = (
        l[5:13].strip(),        #USCTSL_NAME        User ID as taken from the profile name.
        l[14:19].strip(),       #USCTSL_KEY         TSL key number.
    )
    c.execute("INSERT INTO usctsl VALUES(?, ?)", v)
    print("INFO: (0233) User CICS TSL Keys Record processed.")

def process_uslan(l, c):
    v = (
        l[5:13].strip(),        #USLAN_NAME         User ID as taken from the profile name.
        l[14:17].strip(),       #USLAN_PRIMARY      The primary language for the user.
        l[18:21].strip(),       #USLAN_SECONDARY    The secondary language for the user.
    )
    c.execute("INSERT INTO uslan VALUES(?, ?, ?)", v)
    print("INFO: (0240) User Language Data Record processed.")

def process_usopr(l, c):
    v = (
        l[5:13].strip(),        #USOPR_NAME         User ID as taken from the profile name.
        l[14:19].strip(),       #USOPR_STORAGE      The number of megabytes of storage that can be used for message queuing.
        l[20:24].strip(),       #USOPR_MASTERAUTH   Does this user have MASTER console authority?
        l[25:29].strip(),       #USOPR_ALLAUTH      Does this user have ALL console authority?
        l[30:34].strip(),       #USOPR_SYSAUTH      Does this user have SYSAUTH console authority?
        l[35:39].strip(),       #USOPR_IOAUTH       Does this user have I/O console authority?
        l[40:44].strip(),       #USOPR_CONSAUTH     Does this user have CONS console authority?
        l[45:49].strip(),       #USOPR_INFOAUTH     Does this user have INFO console authority?
        l[50:54].strip(),       #USOPR_TIMESTAMP    Do console messages contain a timestamp?
        l[55:59].strip(),       #USOPR_SYSTEMID     Do console messages contain a system ID?
        l[60:64].strip(),       #USOPR_JOBID        Do console messages contain a job ID?
        l[65:69].strip(),       #USOPR_MSGID        Do console messages contain a message ID?
        l[70:74].strip(),       #USOPR_X            Are the job name and system name to be suppressed for messages issued from the JES3 global processor?
        l[75:79].strip(),       #USOPR_WTOR         Does the console receive WTOR messages?
        l[80:84].strip(),       #USOPR_IMMEDIATE    Does the console receive immediate messages?
        l[85:89].strip(),       #USOPR_CRITICAL     Does the console receive critical event messages?
        l[90:94].strip(),       #USOPR_EVENTUAL     Does the console receive eventual event messages?
        l[95:99].strip(),       #USOPR_INFO         Does the console receive informational messages?
        l[100:104].strip(),     #USOPR_NOBRODCAST   Are broadcast messages to this console suppressed?
        l[105:109].strip(),     #USOPR_ALL          Does the console receive all messages?
        l[110:114].strip(),     #USOPR_JOBNAMES     Are job names monitored?
        l[115:119].strip(),     #USOPR_JOBNAMEST    Are job names monitored with timestamps displayed?
        l[120:124].strip(),     #USOPR_SESS         Are user IDs displayed with each TSO initiation and termination?
        l[125:129].strip(),     #USOPR_SESST        Are user IDs and timestamps displayed with each TSO initiation and termination?
        l[130:134].strip(),     #USOPR_STATUS       Are data set names and dispositions displayed with each data set that is freed?
        l[135:139].strip(),     #USOPR_ROUTECODE001 Is this console enabled for route code 001
        l[140:144].strip(),     #USOPR_ROUTECODE002 Is this console enabled for route code 002
        l[145:149].strip(),     #USOPR_ROUTECODE003 Is this console enabled for route code 003
        l[150:154].strip(),     #USOPR_ROUTECODE004 Is this console enabled for route code 004
        l[155:159].strip(),     #USOPR_ROUTECODE005 Is this console enabled for route code 005
        l[160:164].strip(),     #USOPR_ROUTECODE006 Is this console enabled for route code 006
        l[165:169].strip(),     #USOPR_ROUTECODE007 Is this console enabled for route code 007
        l[170:174].strip(),     #USOPR_ROUTECODE008 Is this console enabled for route code 008
        l[175:179].strip(),     #USOPR_ROUTECODE009 Is this console enabled for route code 009
        l[180:184].strip(),     #USOPR_ROUTECODE010 Is this console enabled for route code 010
        l[185:189].strip(),     #USOPR_ROUTECODE011 Is this console enabled for route code 011
        l[190:194].strip(),     #USOPR_ROUTECODE012 Is this console enabled for route code 012
        l[195:199].strip(),     #USOPR_ROUTECODE013 Is this console enabled for route code 013
        l[200:204].strip(),     #USOPR_ROUTECODE014 Is this console enabled for route code 014
        l[205:209].strip(),     #USOPR_ROUTECODE015 Is this console enabled for route code 015
        l[210:214].strip(),     #USOPR_ROUTECODE016 Is this console enabled for route code 016
        l[215:219].strip(),     #USOPR_ROUTECODE017 Is this console enabled for route code 017
        l[220:224].strip(),     #USOPR_ROUTECODE018 Is this console enabled for route code 018
        l[225:229].strip(),     #USOPR_ROUTECODE019 Is this console enabled for route code 019
        l[230:234].strip(),     #USOPR_ROUTECODE020 Is this console enabled for route code 020
        l[235:239].strip(),     #USOPR_ROUTECODE021 Is this console enabled for route code 021
        l[240:244].strip(),     #USOPR_ROUTECODE022 Is this console enabled for route code 022
        l[245:249].strip(),     #USOPR_ROUTECODE023 Is this console enabled for route code 023
        l[250:254].strip(),     #USOPR_ROUTECODE024 Is this console enabled for route code 024
        l[255:259].strip(),     #USOPR_ROUTECODE025 Is this console enabled for route code 025
        l[260:264].strip(),     #USOPR_ROUTECODE026 Is this console enabled for route code 026
        l[265:269].strip(),     #USOPR_ROUTECODE027 Is this console enabled for route code 027
        l[270:274].strip(),     #USOPR_ROUTECODE028 Is this console enabled for route code 028
        l[275:279].strip(),     #USOPR_ROUTECODE029 Is this console enabled for route code 029
        l[280:284].strip(),     #USOPR_ROUTECODE030 Is this console enabled for route code 030
        l[285:289].strip(),     #USOPR_ROUTECODE031 Is this console enabled for route code 031
        l[290:294].strip(),     #USOPR_ROUTECODE032 Is this console enabled for route code 032
        l[295:299].strip(),     #USOPR_ROUTECODE033 Is this console enabled for route code 033
        l[300:304].strip(),     #USOPR_ROUTECODE034 Is this console enabled for route code 034
        l[305:309].strip(),     #USOPR_ROUTECODE035 Is this console enabled for route code 035
        l[310:314].strip(),     #USOPR_ROUTECODE036 Is this console enabled for route code 036
        l[315:319].strip(),     #USOPR_ROUTECODE037 Is this console enabled for route code 037
        l[320:324].strip(),     #USOPR_ROUTECODE038 Is this console enabled for route code 038
        l[325:329].strip(),     #USOPR_ROUTECODE039 Is this console enabled for route code 039
        l[330:334].strip(),     #USOPR_ROUTECODE040 Is this console enabled for route code 040
        l[335:339].strip(),     #USOPR_ROUTECODE041 Is this console enabled for route code 041
        l[340:344].strip(),     #USOPR_ROUTECODE042 Is this console enabled for route code 042
        l[345:349].strip(),     #USOPR_ROUTECODE043 Is this console enabled for route code 043
        l[350:354].strip(),     #USOPR_ROUTECODE044 Is this console enabled for route code 044
        l[355:359].strip(),     #USOPR_ROUTECODE045 Is this console enabled for route code 045
        l[360:364].strip(),     #USOPR_ROUTECODE046 Is this console enabled for route code 046
        l[365:369].strip(),     #USOPR_ROUTECODE047 Is this console enabled for route code 047
        l[370:374].strip(),     #USOPR_ROUTECODE048 Is this console enabled for route code 048
        l[375:379].strip(),     #USOPR_ROUTECODE049 Is this console enabled for route code 049
        l[380:384].strip(),     #USOPR_ROUTECODE050 Is this console enabled for route code 050
        l[385:389].strip(),     #USOPR_ROUTECODE051 Is this console enabled for route code 051
        l[390:394].strip(),     #USOPR_ROUTECODE052 Is this console enabled for route code 052
        l[395:399].strip(),     #USOPR_ROUTECODE053 Is this console enabled for route code 053
        l[400:404].strip(),     #USOPR_ROUTECODE054 Is this console enabled for route code 054
        l[405:409].strip(),     #USOPR_ROUTECODE055 Is this console enabled for route code 055
        l[410:414].strip(),     #USOPR_ROUTECODE056 Is this console enabled for route code 056
        l[415:419].strip(),     #USOPR_ROUTECODE057 Is this console enabled for route code 057
        l[420:424].strip(),     #USOPR_ROUTECODE058 Is this console enabled for route code 058
        l[425:429].strip(),     #USOPR_ROUTECODE059 Is this console enabled for route code 059
        l[430:434].strip(),     #USOPR_ROUTECODE060 Is this console enabled for route code 060
        l[435:439].strip(),     #USOPR_ROUTECODE061 Is this console enabled for route code 061
        l[440:444].strip(),     #USOPR_ROUTECODE062 Is this console enabled for route code 062
        l[445:449].strip(),     #USOPR_ROUTECODE063 Is this console enabled for route code 063
        l[450:454].strip(),     #USOPR_ROUTECODE064 Is this console enabled for route code 064
        l[455:459].strip(),     #USOPR_ROUTECODE065 Is this console enabled for route code 065
        l[460:464].strip(),     #USOPR_ROUTECODE066 Is this console enabled for route code 066
        l[465:469].strip(),     #USOPR_ROUTECODE067 Is this console enabled for route code 067
        l[470:474].strip(),     #USOPR_ROUTECODE068 Is this console enabled for route code 068
        l[475:479].strip(),     #USOPR_ROUTECODE069 Is this console enabled for route code 069
        l[480:484].strip(),     #USOPR_ROUTECODE070 Is this console enabled for route code 070
        l[485:489].strip(),     #USOPR_ROUTECODE071 Is this console enabled for route code 071
        l[490:494].strip(),     #USOPR_ROUTECODE072 Is this console enabled for route code 072
        l[495:499].strip(),     #USOPR_ROUTECODE073 Is this console enabled for route code 073
        l[500:504].strip(),     #USOPR_ROUTECODE074 Is this console enabled for route code 074
        l[505:509].strip(),     #USOPR_ROUTECODE075 Is this console enabled for route code 075
        l[510:514].strip(),     #USOPR_ROUTECODE076 Is this console enabled for route code 076
        l[515:519].strip(),     #USOPR_ROUTECODE077 Is this console enabled for route code 077
        l[520:524].strip(),     #USOPR_ROUTECODE078 Is this console enabled for route code 078
        l[525:529].strip(),     #USOPR_ROUTECODE079 Is this console enabled for route code 079
        l[530:534].strip(),     #USOPR_ROUTECODE080 Is this console enabled for route code 080
        l[535:539].strip(),     #USOPR_ROUTECODE081 Is this console enabled for route code 081
        l[540:544].strip(),     #USOPR_ROUTECODE082 Is this console enabled for route code 082
        l[545:549].strip(),     #USOPR_ROUTECODE083 Is this console enabled for route code 083
        l[550:554].strip(),     #USOPR_ROUTECODE084 Is this console enabled for route code 084
        l[555:559].strip(),     #USOPR_ROUTECODE085 Is this console enabled for route code 085
        l[560:564].strip(),     #USOPR_ROUTECODE086 Is this console enabled for route code 086
        l[565:569].strip(),     #USOPR_ROUTECODE087 Is this console enabled for route code 087
        l[570:574].strip(),     #USOPR_ROUTECODE088 Is this console enabled for route code 088
        l[575:579].strip(),     #USOPR_ROUTECODE089 Is this console enabled for route code 089
        l[580:584].strip(),     #USOPR_ROUTECODE090 Is this console enabled for route code 090
        l[585:589].strip(),     #USOPR_ROUTECODE091 Is this console enabled for route code 091
        l[590:594].strip(),     #USOPR_ROUTECODE092 Is this console enabled for route code 092
        l[595:599].strip(),     #USOPR_ROUTECODE093 Is this console enabled for route code 093
        l[600:604].strip(),     #USOPR_ROUTECODE094 Is this console enabled for route code 094
        l[605:609].strip(),     #USOPR_ROUTECODE095 Is this console enabled for route code 095
        l[610:614].strip(),     #USOPR_ROUTECODE096 Is this console enabled for route code 096
        l[615:619].strip(),     #USOPR_ROUTECODE097 Is this console enabled for route code 097
        l[620:624].strip(),     #USOPR_ROUTECODE098 Is this console enabled for route code 098
        l[625:629].strip(),     #USOPR_ROUTECODE099 Is this console enabled for route code 099
        l[630:634].strip(),     #USOPR_ROUTECODE100 Is this console enabled for route code 100
        l[635:639].strip(),     #USOPR_ROUTECODE101 Is this console enabled for route code 101
        l[640:644].strip(),     #USOPR_ROUTECODE102 Is this console enabled for route code 102
        l[645:649].strip(),     #USOPR_ROUTECODE103 Is this console enabled for route code 103
        l[650:654].strip(),     #USOPR_ROUTECODE104 Is this console enabled for route code 104
        l[655:659].strip(),     #USOPR_ROUTECODE105 Is this console enabled for route code 105
        l[660:664].strip(),     #USOPR_ROUTECODE106 Is this console enabled for route code 106
        l[665:669].strip(),     #USOPR_ROUTECODE107 Is this console enabled for route code 107
        l[670:674].strip(),     #USOPR_ROUTECODE108 Is this console enabled for route code 108
        l[675:679].strip(),     #USOPR_ROUTECODE109 Is this console enabled for route code 109
        l[680:684].strip(),     #USOPR_ROUTECODE110 Is this console enabled for route code 110
        l[685:689].strip(),     #USOPR_ROUTECODE111 Is this console enabled for route code 111
        l[690:694].strip(),     #USOPR_ROUTECODE112 Is this console enabled for route code 112
        l[695:699].strip(),     #USOPR_ROUTECODE113 Is this console enabled for route code 113
        l[700:704].strip(),     #USOPR_ROUTECODE114 Is this console enabled for route code 114
        l[705:709].strip(),     #USOPR_ROUTECODE115 Is this console enabled for route code 115
        l[710:714].strip(),     #USOPR_ROUTECODE116 Is this console enabled for route code 116
        l[715:719].strip(),     #USOPR_ROUTECODE117 Is this console enabled for route code 117
        l[720:724].strip(),     #USOPR_ROUTECODE118 Is this console enabled for route code 118
        l[725:729].strip(),     #USOPR_ROUTECODE119 Is this console enabled for route code 119
        l[730:734].strip(),     #USOPR_ROUTECODE120 Is this console enabled for route code 120
        l[735:739].strip(),     #USOPR_ROUTECODE121 Is this console enabled for route code 121
        l[740:744].strip(),     #USOPR_ROUTECODE122 Is this console enabled for route code 122
        l[745:749].strip(),     #USOPR_ROUTECODE123 Is this console enabled for route code 123
        l[750:754].strip(),     #USOPR_ROUTECODE124 Is this console enabled for route code 124
        l[755:759].strip(),     #USOPR_ROUTECODE125 Is this console enabled for route code 125
        l[760:764].strip(),     #USOPR_ROUTECODE126 Is this console enabled for route code 126
        l[765:769].strip(),     #USOPR_ROUTECODE127 Is this console enabled for route code 127
        l[770:774].strip(),     #USOPR_ROUTECODE128 Is this console enabled for route code 128
        l[775:783].strip(),     #USOPR_LOGCMDRESP   Specifies the logging of command responses received by the extended operator. Valid values are SYSTEM, NO, and blank.
        l[784:788].strip(),     #USOPR_MIGRATIONID  Is this extended operator to receive a migration ID?
        l[789:797].strip(),     #USOPR_DELOPERMSG   Does this extended operator receive delete operator messages? Valid values are NORMAL, ALL, and NONE.
        l[798:806].strip(),     #USOPR_RETRIEVE_KEY Specifies a retrieval key used for searching. A null value is indicated by NONE.
        l[807:815].strip(),     #USOPR_CMDSYS       The name of the system that the extended operator is connected to for command processing.
        l[816:820].strip(),     #USOPR_UD           Is this operator to receive undeliverable messages?
        l[821:829].strip(),     #USOPR_ALTGRP_ID    The default group associated with this operator.
        l[830:834].strip(),     #USOPR_AUTO         Is this operator to receive messages automated within the sysplex?
        l[835:839].strip(),     #USOPR_HC           Is this operator to receive messages that are directed to hardcopy?
        l[840:844].strip(),     #USOPR_INT          Is this operator to receive messages that are directed to console ID zero?
        l[845:849].strip(),     #USOPR_UNKN         Is this operator to receive messages which are directed to unknown console IDs?
    )
    c.execute("INSERT INTO usopr VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0250) User OPERPARM Data Record processed.")

def process_usoprp(l, c):
    v = (
        l[5:13].strip(),        #USOPRP_NAME        User ID as taken from the profile name.
        l[14:22].strip(),       #USOPRP_SYSTEM      System name.
    )
    c.execute("INSERT INTO usoprp VALUES(?, ?)", v)
    print("INFO: (0251) User OPERPARM Scope Record processed.")

def process_uswrk(l, c):
    v = (
        l[5:13].strip(),        #USWRK_NAME         User ID as taken from the profile name.
        l[14:74].strip(),       #USWRK_AREA_NAME    Area for delivery.
        l[75:135].strip(),      #USWRK_BUILDING     Building for delivery.
        l[136:196].strip(),     #USWRK_DEPARTMENT   Department for delivery.
        l[197:257].strip(),     #USWRK_ROOM         Room for delivery.
        l[258:318].strip(),     #USWRK_ADDR_LINE1   Address line 1.
        l[319:379].strip(),     #USWRK_ADDR_LINE2   Address line 2.
        l[380:440].strip(),     #USWRK_ADDR_LINE3   Address line 3.
        l[441:501].strip(),     #USWRK_ADDR_LINE4   Address line 4.
        l[502:757].strip(),     #USWRK_ACCOUNT      Account number.
    )
    c.execute("INSERT INTO uswrk VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0260) User WORKATTR Data Record processed.")

def process_usomvs(l, c):
    v = (
        l[5:13].strip(),        #USOMVS_NAME        User name as taken from the profile name.
        l[14:24].strip(),       #USOMVS_UID         z/OS UNIX user identifier (UID) associated with the user name from the profile.
        l[25:1048].strip(),     #USOMVS_HOME_PATH   HOME PATH associated with the z/OS UNIX user identifier (UID).
        l[1049:2072].strip(),   #USOMVS_PROGRAM     Default Program associated with the z/OS UNIX user identifier (UID).
        l[2073:2083].strip(),   #USOMVS_CPUTIMEMAX  Maximum CPU time associated with the UID.
        l[2084:2094].strip(),   #USOMVS_ASSIZEMAX   Maximum address space size associated with the UID.
        l[2095:2105].strip(),   #USOMVS_FILEPROCMAX Maximum active or open files associated with the UID.
        l[2106:2116].strip(),   #USOMVS_PROCUSERMAX Maximum number of processes associated with the UID.
        l[2117:2127].strip(),   #USOMVS_THREADSMAX  Maximum number of threads associated with the UID.
        l[2128:2138].strip(),   #USOMVS_MMAPAREAMAX Maximum mappable storage amount associated with the UID.
        l[2139:2148].strip(),   #USOMVS_MEMLIMIT    Maximum size of non-shared memory
        l[2149:2158].strip(),   #USOMVS_SHMEMAX     Maximum size of shared memory
    )
    c.execute("INSERT INTO usomvs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0270) User OMVS Data Record processed.")

def process_usnetv(l, c):
    v = (
        l[5:13].strip(),        #USNETV_NAME        User ID as taken from profile name
        l[14:269].strip(),      #USNETV_IC          Command list processed at logon
        l[270:278].strip(),     #USNETV_CONSNAME    Default console name
        l[279:287].strip(),     #USNETV_CTL         CTL value: GENERAL, GLOBAL, or SPECIFIC
        l[288:292].strip(),     #USNETV_MSGRECVR    Eligible to receive unsolicited messages?
        l[293:297].strip(),     #USNETV_NGMFADMN    Authorized to NetView graphic monitoring facility?
        l[299:306].strip(),     #USNETV_NGMFVSPN    Value of view span options
    )
    c.execute("INSERT INTO usnetv VALUES (?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0280) User NETVIEW Segment Record processed.")

def process_usnopc(l, c):
    v = (
        l[5:13].strip(),        #USNOPC_NAME        User ID as taken from the profile name
        l[14:19].strip(),       #USNOPC_OPCLASS     OPCLASS value from 1 to 2040
    )
    c.execute("INSERT INTO usnopc VALUES (?, ?)", v)
    print("INFO: (0281) User OPCLASS Record processed.")

def process_usndom(l, c):
    v = (
        l[5:13].strip(),        #USNDOM_NAME        User ID as taken from the profile name
        l[14:19].strip(),       #USNDOM_DOMAINS     DOMAIN value.
    )
    c.execute("INSERT INTO usndom VALUES (?, ?)", v)
    print("INFO: (0282) User DOMAINS Record processed.")

def process_usdce(l, c):
    v = (
        l[5:13].strip(),        #USDCE_NAME         RACF user name as taken from the profile name.
        l[14:50].strip(),       #USDCE_UUID         DCE UUID associated with the user name from the profile.
        l[51:1074].strip(),     #USDCE_DCE_NAME     DCE principal name associated with this user.
        l[1075:2098].strip(),   #USDCE_HOMECELL     Home cell name.
        l[2099:2135].strip(),   #USDCE_HOMEUUID     Home cell UUID.
        l[2136:2140].strip(),   #USDCE_AUTOLOGIN    Is this user eligible for an automatic DCE login?
    )
    c.execute("INSERT INTO usdce VALUES (?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0290) User DCE Data Record processed.")

def process_usovm(l, c):
    v = (
        l[5:13].strip(),        #USOVM_NAME         User name as taken from the profile name.
        l[14:24].strip(),       #USOVM_UID          User identifier (UID) associated with the user name from the profile.
        l[25:1048].strip(),     #USOVM_HOME_PATH    Home path associated with the user identifier (UID).
        l[1049:2072].strip(),   #USOVM_PROGRAM      Default program associated with the user identifier (UID).
        l[2073:3096].strip(),   #USOVM_FSROOT       File system root for this user.
    )
    c.execute("INSERT INTO usovm VALUES (?, ?, ?, ?, ?)", v)
    print("INFO: (02A0) User OVM Data Record processed.")

def process_uslnot(l, c):
    v = (
        l[5:13].strip(),        #USLNOT_NAME        User ID as taken from the profile name.
        l[14:78].strip(),       #USLNOT_SNAME       LNOTES short name associated with the user ID.
    )
    c.execute("INSERT INTO uslnot VALUES(?, ?)", v)
    print("INFO: (02B0) User LNOTES Data Record processed.")

def process_usnds(l, c):
    v = (
        l[5:13].strip(),        #USNDS_NAME         User ID as taken from the profile name.
        l[14:260].strip(),      #USNDS_UNAME        NDS user name associated with the user ID.
    )
    c.execute("INSERT INTO usnds VALUES(?, ?)", v)
    print("INFO: (02C0) User NDS Data Record processed.")

def process_uskerb(l, c):
    v = (
        l[5:13].strip(),        #USKERB_NAME        RACF user name as taken from the profile.
        l[14:254].strip(),      #USKERB_KERBNAME    The Kerberos principal name.
        l[255:265].strip(),     #USKERB_MAX_LIFE    Maximum ticket life.
        l[266:269].strip(),     #USKERB_KEY_VERS    Current key version.
        l[270:274].strip(),     #USKERB_ENCRYPT_DES Is key encryption using DES enabled?
        l[275:279].strip(),     #USKERB_ENCRYPT_DES3  Is key encryption using DES3 enabled?
        l[280:284].strip(),     #USKERB_ENCRYPT_DESD  Is key encryption using DES with derivation enabled?
        l[285:289].strip(),     #USKERB_ENCRPT_A128 Is key encryption using AES128 enabled?
        l[290:294].strip(),     #USKERB_ENCRPT_A256 Is key encryption using AES256 enabled?
        l[350:358].strip(),     #USKERB_KEY_FROM    Key source. Valid values are PASSWORD or PHRASE.
    )
    c.execute("INSERT INTO uskerb VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (02D0) User KERB Data Record processed.")

def process_usproxy(l, c):
    v = (
        l[5:13].strip(),        #USPROXY_NAME       RACF user name as taken from the profile name.
        l[14:1037].strip(),     #USPROXY_LDAP_HOST  LDAP server URL.
        l[1038:2061].strip(),   #USPROXY_BIND_DN    LDAP BIND distinguished name.
    )
    c.execute("INSERT INTO usproxy VALUES(?, ?, ?)", v)
    print("INFO: (02E0) User PROXY Record processed.")

def process_useim(l, c):
    v = (
        l[5:13].strip(),        #USEIM_NAME         User name.
        l[14:260].strip(),      #USEIM_LDAPPROF     EIM LDAPBIND profile name.
    )
    c.execute("INSERT INTO useim VALUES(?, ?)", v)
    print("INFO: (02F0) User EIM Data Record processed.")

def process_uscsd(l, c):
    v = (
        l[5:13].strip(),        #USCSD_NAME         User name.
        l[14:18].strip(),       #USCSD_TYPE         Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[19:51].strip(),       #USCSD_KEY          Custom field keyword; maximum length = 8.
        l[52:1152].strip(),     #USCSD_VALUE        Custom field value.
    )
    c.execute("INSERT INTO uscsd VALUES(?, ?, ?, ?)", v)
    print("INFO: (02G1) User CSDATA Custom Fields Record processed.")

def process_usmfac(l, c):
    v = (
        l[5, 13],     #USMFAC_NAME        User ID as taken from the profile name.
        l[14:34].strip(),       #USMFAC_FACTOR_NAME Factor name.
        l[35:55].strip(),       #USMFAC_TAG_NAME    The tag name associated with the factor.
        l[56:1080].strip(),     #USMFAC_TAG_VALUE   Tag value associated with the tag name.
    )
    c.execute("INSERT INTO usmfac VALUES (?, ?, ?, ?)", v)
    print("INFO: (1210) User MFA Factor Tags Data Record processed.")

def process_dsbd(l, c):
    v = (
        l[5:49].strip(),        #DSBD_NAME          Data set name as taken from the profile name.
        l[50:56].strip(),       #DSBD_VOL           Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:61].strip(),       #DSBD_GENERIC       Is this a generic profile?
        l[62:72].strip(),       #DSBD_CREATE_DATE   Date the profile was created.
        l[73:81].strip(),       #DSBD_OWNER_ID      The user ID or group name that owns the profile.
        l[82:92].strip(),       #DSBD_LASTREF_DATE  The date that the data set was last referenced.
        l[93:103].strip(),      #DSBD_LASTCHG_DATE  The date that the data set was last changed.
        l[104:109].strip(),     #DSBD_ALTER_CNT     The number of times that the data set was accessed with ALTER authority.
        l[110:115].strip(),     #DSBD_CONTROL_CNT   The number of times that the data set was accessed with CONTROL authority.
        l[116:121].strip(),     #DSBD_UPDATE_CNT    The number of times that the data set was accessed with UPDATE authority.
        l[122:127].strip(),     #DSBD_READ_CNT      The number of times that the data set was accessed with READ authority.
        l[128:136].strip(),     #DSBD_UACC          The universal access of this data set. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[137:141].strip(),     #DSBD_GRPDS         Is this a group data set?
        l[142:150].strip(),     #DSBD_AUDIT_LEVEL   Indicates the level of resource-owner-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[151:159].strip(),     #DSBD_GRP_ID        The connect group of the user who created this data set.
        l[160:168].strip(),     #DSBD_DS_TYPE       The type of the data set. Valid values are VSAM, NONVSAM, TAPE, and MODEL.
        l[169:172].strip(),     #DSBD_LEVEL         The level of the data set.
        l[173:181].strip(),     #DSBD_DEVICE_NAME   The EBCDIC name of the device type on which the data set resides.
        l[182:190].strip(),     #DSBD_GAUDIT_LEVEL  Indicates the level of auditor-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[191:446].strip(),     #DSBD_INSTALL_DATA  Installation-defined data.
        l[447:455].strip(),     #DSBD_AUDIT_OKQUAL  The resource-owner-specified successful access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[456:464].strip(),     #DSBD_AUDIT_FAQUAL  The resource-owner-specified failing access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[465:473].strip(),     #DSBD_GAUDIT_OKQUAL The auditor-specified successful access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[474:482].strip(),     #DSBD_GAUDIT_FAQUAL The auditor-specified failing access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[483:487].strip(),     #DSBD_WARNING       Does this data set have the WARNING attribute?
        l[488:491].strip(),     #DSBD_SECLEVEL      The data set security level.
        l[492:500].strip(),     #DSBD_NOTIFY_ID     User ID that is notified when violations occur.
        l[501:506].strip(),     #DSBD_RETENTION     Retention period of the data set.
        l[507:511].strip(),     #DSBD_ERASE         For a DASD data set, is this data set scratched when the data set is deleted?
        l[512:520].strip(),     #DSBD_SECLABEL      Security label of the data set.
    )
    c.execute("INSERT INTO dsbd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0400) Data Set Basic Data Record processed.")

def process_dscat(l, c):
    v = (
        l[5:49].strip(),        #DSCAT_NAME         Data set name as taken from the profile name.
        l[50:56].strip(),       #DSCAT_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:62].strip(),       #DSCAT_CATEGORY     Category associated with this data set.
    )
    c.execute("INSERT INTO dscat VALUES(?, ?, ?)", v)
    print("INFO: (0401) Data Set Categories Record processed.")

def process_dscacc(l, c):
    v = (
        l[5:49].strip(),        #DSCACC_NAME        Data set name as taken from the profile name.
        l[50:56].strip(),       #DSCACC_VOL         Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65].strip(),       #DSCACC_CATYPE      The type of conditional access checking that is being performed. Valid values are APPCPORT, PROGRAM, CONSOLE, TERMINAL, JESINPUT, and SERVAUTH.
        l[66:74].strip(),       #DSCACC_CANAME      The name of a conditional access element that is permitted access.
        l[75:83].strip(),       #DSCACC_AUTH_ID     The user ID or group name that is authorized to the data set.
        l[84:92].strip(),       #DSCACC_ACCESS      The access of the conditional access element/user combination. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[93:98].strip(),       #DSCACC_ACCESS_CNT  The number of times that the data set was accessed.
        l[99:107].strip(),      #DSCACC_NET_ID      The network name when DSCACC_CATYPE is APPCPORT.
        l[108:352].strip(),     #DSCACC_CACRITERIA  The IP name when DSCACC_CATYPE is SERVAUTH.
    )
    c.execute("INSERT INTO dscacc VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0402) Data Set Conditional Access Record processed.")

def process_dsvol(l, c):
    v = (
        l[5:49].strip(),        #DSVOL_NAME         Data set name as taken from the profile name.
        l[50:56].strip(),       #DSVOL_VOL          Volume upon which this data set resides.
        l[57:63].strip(),       #DSVOL_VOL_NAME     A volume upon which the data set resides.
    )
    c.execute("INSERT INTO dsvol VALUES(?, ?, ?)", v)
    print("INFO: (0403) Data Set Volumes Record processed.")

def process_dsacc(l, c):
    v = (
        l[5:49].strip(),        #DSACC_NAME         Data set name as taken from the profile name.
        l[50:56].strip(),       #DSACC_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65].strip(),       #DSACC_AUTH_ID      The user ID or group name that is authorized to the data set.
        l[66:74].strip(),       #DSACC_ACCESS       The access allowed to the user. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[75:80].strip(),       #DSACC_ACCESS_CNT   The number of times that the data set was accessed.
    )
    c.execute("INSERT INTO dsacc VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0404) Data Set Access Record processed.")

def process_dsinstd(l, c):
    v = (
        l[5:49].strip(),        #DSINSTD_NAME       Data set name as taken from the profile name.
        l[50:56].strip(),       #DSINSTD_VOL        Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65].strip(),       #DSINSTD_USR_NAME   The name of the installation-defined field.
        l[66:321].strip(),      #DSINSTD_USR_DATA   The data for the installation-defined field.
        l[322:330].strip(),     #DSINSTD_USR_FLAG   The flag for the installation-defined field in the form X<cc>.
    )
    c.execute("INSERT INTO dsinstd VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0405) Data Set Installation Data Record processed.")

def process_dsdfp(l, c):
    v = (
        l[5:49].strip(),        #DSDFP_NAME         Data set name as taken from the profile name.
        l[50:56].strip(),       #DSDFP_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:65].strip(),       #DSDFP_RESOWNER_ID  The resource owner of the data set.
        l[66:130].strip(),      #DSDFP_DATAKEY      The label of the ICSF key that is used to encrypt the data of any newly allocated data set.
    )
    c.execute("INSERT INTO dsdfp VALUES(?, ?, ?, ?)", v)
    print("INFO: (0410) Data Set DFP Data Record processed.")

def process_dstme(l, c):
    v = (
        l[5:49].strip(),        #DSTME_NAME         Data set name as taken from the profile name.
        l[50:56].strip(),       #DSTME_VOL          Volume upon which this data set resides. Blank if the profile is generic, and *MODEL if the profile is a model profile.
        l[57:303].strip(),      #DSTME_ROLE_NAME    Role profile name.
        l[304:312].strip(),     #DSTME_ACCESS_AUTH  Access permission to this resource as defined by the role.
        l[313:321].strip(),     #DSTME_COND_CLASS   Class name for conditional access.
        l[322, 568],  #DSTME_COND_PROF    Resource profile for conditional access.
    )
    c.execute("INSERT INTO dstme VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0421) Data Set TME Role Record processed.")

def process_grbd(l, c):
    v = (
        l[5:251].strip(),       #GRBD_NAME          General resource name as taken from the profile name.
        l[252:260].strip(),     #GRBD_CLASS_NAME    Name of the class to which the general resource profile belongs.
        l[261:265].strip(),     #GRBD_GENERIC       Is this a generic profile? Valid Values include "Yes" and "No".
        l[266:269].strip(),     #GRBD_CLASS         The class number of the profile.
        l[270:280].strip(),     #GRBD_CREATE_DATE   Date the profile was created.
        l[281:289].strip(),     #GRBD_OWNER_ID      The user ID or group name which owns the profile.
        l[290:300].strip(),     #GRBD_LASTREF_DATE  The date that the resource was last referenced.
        l[301:311].strip(),     #GRBD_LASTCHG_DATE  The date that the resource was last changed.
        l[312:317].strip(),     #GRBD_ALTER_CNT     The number of times that the resource was accessed with ALTER authority.
        l[318:323].strip(),     #GRBD_CONTROL_CNT   The number of times that the resource was accessed with CONTROL authority.
        l[324:329].strip(),     #GRBD_UPDATE_CNT    The number of times that the resource was accessed with UPDATE authority.
        l[330:335].strip(),     #GRBD_READ_CNT      The number of times that the resource was accessed with READ authority.
        l[336:344].strip(),     #GRBD_UACC          The universal access of this resource. For profiles in classes other than DIGTCERT, the valid values are NONE, READ, EXECUTE, UPDATE, CONTROL, and ALTER. For DIGTCERT profiles, the valid values are TRUST, NOTRUST, and HIGHTRST.
        l[345:353].strip(),     #GRBD_AUDIT_LEVEL   Indicates the level of resource-owner-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[354:357].strip(),     #GRBD_LEVEL         The level of the resource.
        l[358:366].strip(),     #GRBD_GAUDIT_LEVEL  Indicates the level of auditor-specified auditing that is performed. Valid values are ALL, SUCCESS, FAIL, and NONE.
        l[367:622].strip(),     #GRBD_INSTALL_DATA  Installation-defined data.
        l[623:631].strip(),     #GRBD_AUDIT_OKQUAL  The resource-owner-specified successful access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[632:640].strip(),     #GRBD_AUDIT_FAQUAL  The resource-owner-specified failing access audit qualifier. This is set to blanks if AUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[641:649].strip(),     #GRBD_GAUDIT_OKQUAL The auditor-specified successful access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[650:658].strip(),     #GRBD_GAUDIT_FAQUAL The auditor-specified failing access audit qualifier. This is set to blanks if GAUDIT_LEVEL is NONE. Otherwise, it is set to either READ, UPDATE, CONTROL, or ALTER.
        l[659:663].strip(),     #GRBD_WARNING       Does this resource have the WARNING attribute? Valid Values include "Yes" and "No".
        l[664:668].strip(),     #GRBD_SINGLEDS      If this is a TAPEVOL profile, is there only one data set on this tape? Valid Values include "Yes" and "No".
        l[669:673].strip(),     #GRBD_AUTO          If this is a TAPEVOL profile, is the TAPEVOL protection automatic? Valid Values include "Yes" and "No".
        l[674:678].strip(),     #GRBD_TVTOC         If this is a TAPEVOL profile, is there a tape volume table of contents on this tape? Valid Values include "Yes" and "No".
        l[679:687].strip(),     #GRBD_NOTIFY_ID     User ID that is notified when violations occur.
        l[688:692].strip(),     #GRBD_ACCESS_SUN    Can the terminal be used on Sunday? Valid Values include "Yes" and "No".
        l[693:697].strip(),     #GRBD_ACCESS_MON    Can the terminal be used on Monday? Valid Values include "Yes" and "No".
        l[698:702].strip(),     #GRBD_ACCESS_TUE    Can the terminal be used on Tuesday? Valid Values include "Yes" and "No".
        l[703:707].strip(),     #GRBD_ACCESS_WED    Can the terminal be used on Wednesday? Valid Values include "Yes" and "No".
        l[708:712].strip(),     #GRBD_ACCESS_THU    Can the terminal be used on Thursday? Valid Values include "Yes" and "No".
        l[713:717].strip(),     #GRBD_ACCESS_FRI    Can the terminal be used on Friday? Valid Values include "Yes" and "No".
        l[718:722].strip(),     #GRBD_ACCESS_SAT    Can the terminal be used on Saturday? Valid Values include "Yes" and "No".
        l[723:731].strip(),     #GRBD_START_TIME    After what time can a user logon from this terminal?
        l[732:740].strip(),     #GRBD_END_TIME      After what time can a user not logon from this terminal?
        l[741:746].strip(),     #GRBD_ZONE_OFFSET   Time zone in which the terminal is located. Expressed as hh:mm. Blank if the time zone has not been specified.
        l[747:748].strip(),     #GRBD_ZONE_DIRECT   The direction of the time zone shift. Valid values are E(east), W(west), and blank.
        l[749:752].strip(),     #GRBD_SECLEVEL      The security level of the general resource.
        l[753:1008].strip(),    #GRBD_APPL_DATA     Installation-defined data.
        l[1009:1017].strip(),   #GRBD_SECLABEL      The security label for the general resource.
    )
    c.execute("INSERT INTO grbd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0500) General Resource Basic Data Record processed.")

def process_grtvol(l, c):
    v = (
        l[5:251].strip(),       #GRTVOL_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTVOL_CLASS_NAME  Name of the class to which the general resource profile belongs, namely TAPEVOL.
        l[261:266].strip(),     #GRTVOL_SEQUENCE    The file sequence number of the tape data set.
        l[267:277].strip(),     #GRTVOL_CREATE_DATE Creation date of the tape data set.
        l[278:282].strip(),     #GRTVOL_DISCRETE    Does a discrete profile exist? Valid Values include "Yes" and "No".
        l[283:327].strip(),     #GRTVOL_INTERN_NAME The RACF internal data set name.
        l[328:583].strip(),     #GRTVOL_INTERN_VOLS The volumes upon which the data set resides.
        l[584:628].strip(),     #GRTVOL_CREATE_NAME The data set name used when creating the data set.
    )
    c.execute("INSERT INTO grtvol VALUES(?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0501) General Resource Tape Volume Data Record processed.")

def process_grcat(l,c):
    v = (
        l[5:251].strip(),       #GRCAT_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCAT_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:266].strip(),     #GRCAT_CATEGORY     Category to which this general resource belongs.
    )
    c.execute("INSERT INTO grcat VALUES(?, ?, ?)", v)
    print("INFO: (0502) General Resource Categories Record processed.")

def process_grmem(l, c):
    v = (
        l[5:251].strip(),       #GRMEM_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRMEM_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:516].strip(),     #GRMEM_MEMBER       Member value for this general resource.
        l[517:525].strip(),     #GRMEM_GLOBAL_ACC   If this is a GLOBAL profile, this is the access that is allowed. Valid values are NONE, READ, UPDATE, CONTROL, and ALTER.
        l[526:534].strip(),     #GRMEM_PADS_DATA    If this is a PROGRAM profile, this field contains the Program Access to Data Set (PADS) information for the profile. Valid values are PADCHK and NOPADCHK.
        l[535:541].strip(),     #GRMEM_VOL_NAME     If this is a PROGRAM profile, this field defines the volume upon which the program resides.
        l[542:547].strip(),     #GRMEM_VMEVENT_DATA If this is a VMXEVENT profile, this field defines the level of auditing that is being performed. Valid values are CTL, AUDIT, and NOCTL.
        l[548:553].strip(),     #GRMEM_SECLEVEL     If this is a SECLEVEL profile in the SECDATA class, this is the numeric security level that is associated with the SECLEVEL.
        l[554:559].strip(),     #GRMEM_CATEGORY     If this is a CATEGORY profile in the SECDATA class, this is the numeric category that is associated with the CATEGORY.
    )
    c.execute("INSERT INTO grmem VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0503) General Resource Members Record processed.")

def process_grvol(l, c):
    v = (
        l[5:251].strip(),       #GRVOL_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRVOL_CLASS_NAME   Name of the class to which the general resource profile belongs, namely TAPEVOL.
        l[261:267].strip(),     #GRVOL_VOL_NAME     Name of a volume in a tape volume set.
    )
    c.execute("INSERT INTO grvol VALUES(?, ?, ?)", v)
    print("INFO: (0504) General Resource Volumes Record processed.")

def process_gracc(l, c):
    v = (
        l[5:251].strip(),       #GRACC_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRACC_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:269].strip(),     #GRACC_AUTH_ID      User ID or group name which is authorized to use the general resource.
        l[270:278].strip(),     #GRACC_ACCESS       The authority that the user or group has over the resource. Valid values are NONE, EXECUTE, READ, UPDATE, CONTROL, and ALTER.
        l[279:284].strip(),     #GRACC_ACCESS_CNT   The number of times that the resource was accessed.
    )
    c.execute("INSERT INTO gracc VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0505) General Resource Access Record processed.")

def process_grinstd(l, c):
    v = (
        l[5:251].strip(),       #GRINSTD_NAME       General resource name as taken from the profile name.
        l[252:260].strip(),     #GRINSTD_CLASS_NAME Name of the class to which the general resource profile belongs.
        l[261:269].strip(),     #GRINSTD_USR_NAME   The name of the installation-defined field.
        l[270:525].strip(),     #GRINSTD_USR_DATA   The data for the installation-defined field.
        l[256:534].strip(),     #GRINSTD_USR_FLAG   The flag for the installation-defined field in the form X<nn>.
    )
    c.execute("INSERT INTO grinstd VALUES (?, ?, ?, ?, ?)", v)
    print("INFO: (0506) General Resource Installation Data Record processed.")

def process_grcacc(l, c):
    v = (
        l[5:251].strip(),       #GRCACC_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCACC_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:269].strip(),     #GRCACC_CATYPE      The type of conditional access checking that is being performed. Valid values are CONSOLE, TERMINAL, JESINPUT, SYSID, APPCPORT, SERVAUTH, PROGRAM, and CRITERIA.
        l[270:278].strip(),     #GRCACC_CANAME      The name of a conditional access element which is permitted access.
        l[279:287].strip(),     #GRCACC_AUTH_ID     The user ID or group name which has authority to the general resource.
        l[288:296].strip(),     #GRCACC_ACCESS      The authority of the conditional access element/user combination. Valid values are NONE, READ, UPDATE, CONTROL, and ALTER.
        l[297:302].strip(),     #GRCACC_ACCESS_CNT  The number of times that the general resource was accessed.
        l[303:311].strip(),     #GRCACC_NET_ID      The network name when GRCACC_CATYPE is APPCPORT.
        l[312:556].strip(),     #GRCACC_CACRITERIA  Access criteria or SERVAUTH IP data.
    )
    c.execute("INSERT INTO grcacc VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0507) General Resource Conditional Access Record processed.")

def process_grfltr(l, c):
    v = (
        l[5:251].strip(),       #GRFLTR_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRFLTR_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:293].strip(),     #GRFLTR_LABEL       The label associated with this filter.
        l[294:302].strip(),     #GRFLTR_STATUS      The status of this filter (TRUST) for filters that are trusted.
        l[303:549].strip(),     #GRFLTR_USER        The user ID or criteria profile name associated with this filter.
        l[550:1061].strip(),    #GRFLTR_CREATE_NAME The issuer's or subject's name, or both, used to create this profile.
    )
    c.execute("INSERT INTO grfltr VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0508) General Resource Filter Data Record processed.")

def process_grdmap(l, c):
    v = (
        l[5:251].strip(),       #GRDMAP_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRDMAP_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:293].strip(),     #GRDMAP_LABEL       The label associated with this mapping.
        l[294:302].strip(),     #GRDMAP_USER        The RACF user ID associated with this mapping.
        l[303:558].strip(),     #GRDMAP_DIDREG      The registry name value associated with this mapping.
    )
    c.execute("INSERT INTO grdmap VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (0509) General Resource Distributed Identity Mapping Data Record processed.")

def process_grses(l, c):
    v = (
        l[5:251].strip(),       #GRSES_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRSES_CLASS_NAME   Name of the class to which the general resource profile belongs, namely APPCLU.
        l[261:269].strip(),     #GRSES_SESSION_KEY  The key associated with the APPC session.
        l[270:274].strip(),     #GRSES_LOCKED       Is the profile locked? Valid Values include "Yes" and "No".
        l[275:285].strip(),     #GRSES_KEY_DATE     Last date that the session key was changed.
        l[286:291].strip(),     #GRSES_KEY_INTERVAL Number of days that the key is valid.
        l[292:297].strip(),     #GRSES_SLS_FAIL     Current number of failed attempts.
        l[298:303].strip(),     #GRSES_MAX_FAIL     Number of failed attempts before lockout.
        l[304:312].strip(),     #GRSES_CONVSEC      Specifies the security checking performed when sessions are established. Valid values are NONE, CONVSEC, PERSISTV, ALREADYV, and AVPV.
    )
    c.execute("INSERT INTO grses VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0510) General Resource Session Data Record processed.")

def process_grsese(l, c):
    v = (
        l[5:251].strip(),       #GRSESE_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRSESE_CLASS_NAME  Name of the class to which the general resource profile belongs, namely APPCLU.
        l[261:296].strip(),     #GRSESE_ENTITY_NAME Entity name.
        l[297:302].strip(),     #GRSESE_FAIL_CNT    The number of failed session attempts.
    )
    c.execute("INSERT INTO grsese VALUES(?, ?, ?, ?)", v)
    print("INFO: (0511) General Resource Session Entities Record processed.")

def process_grdlf(l, c):
    v = (
        l[5:251].strip(),       #GRDLF_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRDLF_CLASS_NAME   Name of the class to which the general resource profile belongs, namely DLFCLASS.
        l[261:265].strip(),     #GRDLF_RETAIN       Is this a retained resource? Valid Values include "Yes" and "No".
    )
    c.execute("INSERT INTO grdlf VALUES(?, ?, ?)", v)
    print("INFO: (0520) General Resource DLF Data Record processed.")

def process_grdlfj(l, c):
    v = (
        l[5:251].strip(),       #GRDLFJ_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRDLFJ_CLASS_NAME  Name of the class to which the general resource profile belongs, namely DLFCLASS.
        l[261:269].strip(),     #GRDLFJ_JOB_NAME    The job name associated with the general resource.
    )
    c.execute("INSERT INTO grdlfj VALUES(?, ?, ?)", v)
    print("INFO: (0521) General Resource DLF Job Names Record processed.")

def process_grsign(l, c):
    v = (
        l[5:251].strip(),       #GRSIGN_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRSIGN_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:325].strip(),     #GRSIGN_PROTECTION  Method of protection for the encryption key.
    )
    c.execute("INSERT INTO grsign VALUES(?, ?, ?)", v)
    print("INFO: (0530) General Resource SSIGNON Data Record processed.")

def process_grst(l, c):
    v = (
        l[5:251].strip(),       #GRST_NAME          Profile name.
        l[252:260].strip(),     #GRST_CLASS_NAME    The class name, STARTED.
        l[261:269].strip(),     #GRST_USER_ID       User ID assigned.
        l[270:278].strip(),     #GRST_GROUP_ID      Group name assigned.
        l[279:283].strip(),     #GRST_TRUSTED       Is process to run trusted? Valid Values include "Yes" and "No".
        l[284:288].strip(),     #GRST_PRIVILEGED    Is process to run privileged? Valid Values include "Yes" and "No".
        l[289:293].strip(),     #GRST_TRACE         Is entry to be traced? Valid Values include "Yes" and "No".
    )
    c.execute("INSERT INTO grst VALUES(?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0540) General Resource Started Task Data Record processed.")

def process_grsv(l, c):
    v = (
        l[5:251].strip(),       #GRSV_NAME          Profile name.
        l[252:260].strip(),     #GRSV_CLASS_NAME    Class name, SYSMVIEW.
        l[261:269].strip(),     #GRSV_SCRIPT_NAME   Logon script name for the application.
        l[270:278].strip(),     #GRSV_PARM_NAME     Parameter list name for the application.
    )
    c.execute("INSERT INTO grsv VALUES(?, ?, ?, ?)", v)
    print("INFO: (0550) General Resource SystemView Data Record processed.")

def process_grcert(l, c):
    v = (
        l[5:251].strip(),       #GRCERT_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCERT_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:271].strip(),     #GRCERT_START_DATE  The date from which this certificate is valid.
        l[272:280].strip(),     #GRCERT_START_TIME  The time from which this certificate is valid.
        l[281:291].strip(),     #GRCERT_END_DATE    The date after which this certificate is no longer valid.
        l[292:300].strip(),     #GRCERT_END_TIME    The time after which this certificate is no longer valid.
        l[301:309].strip(),     #GRCERT_KEY_TYPE    The type of key associated with the certificate. Valid values: BPECC, BPECCTKN, BPECTKNT, DSA, ICSFTOKN, NTECC, NTECCTKN, NTECTKNT, PCICCTKN, PKCSDER, PUBTOKEN, RSATKNT, or all blanks indicating no private key. The value PUBTOKEN indicates that the public key (without the private key) is stored in ICSF.
        l[310:320].strip(),     #GRCERT_KEY_SIZE    The size of private key associated with the certificate, expressed in bits.
        l[321:337].strip(),     #GRCERT_LAST_SERIAL The hexadecimal representation of the low-order eight bytes of the serial number of the last certificate signed with this key.
        l[338:348].strip(),     #GRCERT_RING_SEQN   A sequence number for certificates within the ring.
        l[349:353].strip(),     #GRCERT_GEN_REQ     Indicator to show if the certificate is used to generate a request. Valid Values include "Yes" and "No".
    )
    c.execute("INSERT INTO grcert VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0560) General Resource Certificate Data Record processed.")

def process_certr(l, c):
    v = (
        l[5:251].strip(),       #CERTR_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #CERTR_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:507].strip(),     #CERTR_RING_NAME    The name of the profile which represents a key ring with which this certificate is associated.
    )
    c.execute("INSERT INTO certr VALUES(?, ?, ?)", v)
    print("INFO: (0561) General Resource Certificate References Record processed.")

def process_keyr(l, c):
    v = (
        l[5:251].strip(),       #KEYR_NAME          General resource name as taken from the profile name.
        l[252:260].strip(),     #KEYR_CLASS_NAME    Name of the class to which the general resource profile belongs.
        l[261:507].strip(),     #KEYR_CERT_NAME     The name of the profile which contains the certificate which is in this key ring.
        l[508:516].strip(),     #KEYR_CERT_USAGE    The usage of the certificate within the ring. Valid values are PERSONAL, SITE, and CERTAUTH.
        l[517:521].strip(),     #KEYR_CERT_DEFAULT  Is this certificate the default certificate within the ring? Valid Values include "Yes" and "No".
        l[522:554].strip(),     #KEYR_CERT_LABEL    The label associated with the certificate.
    )
    c.execute("INSERT INTO keyr VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0562) General Resource Key Ring Data Record processed.")

def process_grtme(l, c):
    v = (
        l[5:251].strip(),       #GRTME_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTME_CLASS_NAME   Name of the class to which the general resource belongs.
        l[261:507].strip(),     #GRTME_PARENT       Parent role.
    )
    c.execute("INSERT INTO grtme VALUES(?, ?, ?)", v)
    print("INFO: (0570) General Resource TME Data Record processed.")

def process_grtmec(l, c):
    v = (
        l[5:251].strip(),       #GRTMEC_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTMEC_CLASS_NAME  Name of the class to which the general resource belongs.
        l[261:507].strip(),     #GRTMEC_CHILD       Child role.
    )
    c.execute("INSERT INTO grtmec VALUES(?, ?, ?)", v)
    print("INFO: (0571) General Resource TME Child Record processed.")

def process_grtmer(l, c):
    v = (
        l[5:251].strip(),       #GRTMER_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTMER_CLASS_NAME  Name of the class to which the general resource belongs.
        l[261:507].strip(),     #GRTMER_ORIGIN_ROLE Role profile from which resource access is inherited.
        l[508:516].strip(),     #GRTMER_PROF_CLASS  Class name of the origin-role resource.
        l[517:763].strip(),     #GRTMER_PROF_NAME   Resource name defined in the origin role.
        l[764:772].strip(),     #GRTMER_ACCESS_AUTH Access permission to the resource.
        l[773:781].strip(),     #GRTMER_COND_CLASS  Class name for conditional access.
        l[782:1028].strip(),    #GRTMER_COND_PROF   Resource profile for conditional access.
    )
    c.execute("INSERT INTO grtmer VALUES(?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0572) General Resource TME Resource Record processed.")

def process_grtmeg(l, c):
    v = (
        l[5:251].strip(),       #GRTMEG_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTMEG_CLASS_NAME  Name of the class to which the general resource belongs.
        l[261:269].strip(),     #GRTMEG_GROUP       Group name defined to the role.
    )
    c.execute("INSERT INTO grtmeg VALUES(?, ?, ?)", v)
    print("INFO: (0573) General Resource TME Group Record processed.")

def process_grtmee(l, c):
    v = (
        l[5:251].strip(),       #GRTMEE_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRTMEE_CLASS_NAME  Name of the class to which the general resource belongs.
        l[261:507].strip(),     #GRTMEE_ROLE_NAME   Role profile name.
        l[508:516].strip(),     #GRTMEE_ACCESS_AUTH Access permission to this resource as defined by the role.
        l[517:525].strip(),     #GRTMEE_COND_CLASS  Class name for conditional access.
        l[526:772].strip(),     #GRTMEE_COND_PROF   Resource profile for conditional access.
    )
    c.execute("INSERT INTO grtmee VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0574) General Resource TME Role Record processed.")

def process_grkerb(l, c):
    v = (
        l[5:251].strip(),       #GRKERB_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRKERB_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:501].strip(),     #GRKERB_KERBNAME    The Kerberos realm name.
        l[502:512].strip(),     #GRKERB_MIN_LIFE    Minimum ticket life.
        l[513:523].strip(),     #GRKERB_MAX_LIFE    Maximum ticket life.
        l[524:534].strip(),     #GRKERB_DEF_LIFE    Default ticket life.
        l[535:538].strip(),     #GRKERB_KEY_VERS    Current key version.
        l[539:543].strip(),     #GRKERB_ENCRYPT_DES Is key encryption using DES enabled? Valid Values include "Yes" and "No".
        l[544:548].strip(),     #GRKERB_ENCRYPT_DES3  Is key encryption using DES3 enabled? Valid Values include "Yes" and "No".
        l[549:553].strip(),     #GRKERB_ENCRYPT_DESD  Is key encryption using DES with derivation enabled? Valid Values include "Yes" and "No".
        l[554:558].strip(),     #GRKERB_ENCRPT_A128 Is key encryption using AES128 enabled? Valid Values include "Yes" and "No".
        l[559:563].strip(),     #GRKERB_ENCRPT_A256 Is key encryption using AES256 enabled? Valid Values include "Yes" and "No".
        l[564:568].strip(),     #GRKERB_ENCRPT_A128SHA2   Is key encryption using AES128 SHA2 enabled? Valid Values include "Yes" and "No".
        l[569:573].strip(),     #GRKERB_ENCRPT_A256SHA2   Is key encryption using AES256 SHA2 enabled? Valid Values include "Yes" and "No".
        l[619:623].strip(),     #GRKERB_CHKADDRS    Should the Kerberos server check addresses in tickets? Valid Values include "Yes" and "No".
    )
    c.execute("INSERT INTO grkerb VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (0580) General Resource KERB Data Record processed.")

def process_grproxy(l, c):
    v = (
        l[5:251].strip(),       #GRPROXY_NAME       General resource name as taken from the profile name.
        l[252:260].strip(),     #GRPROXY_CLASS_NAME Name of the class to which the general resource belongs.
        l[261:1284].strip(),    #GRPROXY_LDAP_HOST  LDAP server URL.
        l[1285:2308].strip(),   #GRPROXY_BIND_DN    LDAP BIND distinguished name.
    )
    c.execute("INSERT INTO grproxy VALUES(?, ?, ?, ?)", v)
    print("INFO: (0590) General Resource PROXY Record processed.")

def process_greim(l, c):
    v = (
        l[5:251].strip(),       #GREIM_NAME         Profile name.
        l[252:260].strip(),     #GREIM_CLASS_NAME   Class name.
        l[261:1284].strip(),    #GREIM_DOMAIN_DN    EIM domain name.
        l[1285:1289].strip(),   #GREIM_ENABLE       EIM Enable option. Valid Values include "Yes" and "No".
        l[1365:1620].strip(),   #GREIM_LOCAL_REG    EIM LDAP local registry name.
        l[1621:1876].strip(),   #GREIM_KERBREG      EIM Kerberos Registry Name
        l[1877:2132].strip(),   #GREIM_X509REG      EIM X.509 Registry name
    )
    c.execute("INSERT INTO greim VALUES(?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05A0) General Resource EIM Record processed.")

def process_gralias(l, c):
    v = (
        l[5:251].strip(),       #GRALIAS_NAME       General resource name as taken from the profile.
        l[252:260].strip(),     #GRALIAS_CLASS_NAME Name of the class to which the general resource belongs.
        l[261:293].strip(),     #GRALIAS_IPLOOK     IP lookup value in SERVAUTH class.
    )
    c.execute("INSERT INTO gralias VALUES(?, ?, ?)", v)
    print("INFO: (05B0) General Resource Alias Data Record processed.")

def process_grcdt(l, c):
    v = (
        l[5:251].strip(),       #GRCDT_NAME         General resource name as taken from the profile.
        l[252:260].strip(),     #GRCDT_CLASS_NAME   Name of the class to which the general resource belongs, namely CDT.
        l[261:271].strip(),     #GRCDT_POSIT        POSIT number for class.
        l[272:275].strip(),     #GRCDT_MAXLENGTH    Maximum length of profile names when using ENTITYX.
        l[276:286].strip(),     #GRCDT_MAXLENX      Maximum length of profile names when using ENTITYX.
        l[187:290].strip(),     #GRCDT_DEFAULTRC    Default return code.
        l[291:301].strip(),     #GRCDT_KEYQUALIFIER Number of key qualifiers.
        l[302:310].strip(),     #GRCDT_GROUP        Resource grouping class name.
        l[311:319].strip(),     #GRCDT_MEMBER       Member class name.
        l[320:324].strip(),     #GRCDT_FIRST_ALPHA  Is an alphabetic character allowed in the first character of a profile name? Valid Values include "Yes" and "No".
        l[325:329].strip(),     #GRCDT_FIRST_NATL   Is a national character allowed in the first character of a profile name? Valid Values include "Yes" and "No".
        l[330:334].strip(),     #GRCDT_FIRST_NUM    Is a numeric character allowed in the first character of a profile name? Valid Values include "Yes" and "No".
        l[335:339].strip(),     #GRCDT_FIRST_SPEC   Is a special character allowed in the first character of a profile name? Valid Values include "Yes" and "No".
        l[340:344].strip(),     #GRCDT_OTHER_ALPHA  Is an alphabetic character allowed in other characters of a profile name? Valid Values include "Yes" and "No".
        l[345:349].strip(),     #GRCDT_OTHER_NATL   Is a national character allowed in other characters of a profile name? Valid Values include "Yes" and "No".
        l[350:354].strip(),     #GRCDT_OTHER_NUM    Is a numeric character allowed in other characters of a profile name? Valid Values include "Yes" and "No".
        l[355:359].strip(),     #GRCDT_OTHER_SPEC   Is a special character allowed in other characters of a profile name? Valid Values include "Yes" and "No".
        l[360:364].strip(),     #GRCDT_OPER         Is OPERATIONS attribute to be considered? Valid Values include "Yes" and "No".
        l[365:373].strip(),     #GRCDT_DEFAULTUACC  Default universal access. Valid values are ACEE, ALTER, CONTROL, UPDATE, READ, EXECUTE, NONE.
        l[374:384].strip(),     #GRCDT_RACLIST      RACLIST setting. Valid values are ALLOWED, DISALLOWED, REQUIRED.
        l[385:395].strip(),     #GRCDT_GENLIST      GENLIST setting. Valid values are ALLOWED, DISALLOWED.
        l[396:400].strip(),     #GRCDT_PROF_ALLOW   Are profiles allowed in the class? Valid Values include "Yes" and "No".
        l[401:405].strip(),     #GRCDT_SECL_REQ     Are security labels required for the class when MLACTIVE is on? Valid Values include "Yes" and "No".
        l[406:414].strip(),     #GRCDT_MACPROCESS   Type of mandatory access check processing. Valid values are EQUAL, NORMAL, REVERSE.
        l[415:419].strip(),     #GRCDT_SIGNAL       Is ENF signal to be sent? Valid Values include "Yes" and "No".
        l[420:428].strip(),     #GRCDT_CASE         Case of profile names. Valid values are ASIS, UPPER.
        l[429:439].strip(),     #GRCDT_GENERIC      GENERIC setting. Valid values are ALLOWED and DISALLOWED.
    )
    c.execute("INSERT INTO grcdt VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05C0) General Resource CDTINFO Data Record processed.")

def process_grictx(l, c):
    v = (
        l[5:251].strip(),       #GRICTX_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRICTX_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:265].strip(),     #GRICTX_USEMAP      Should the identity cache store an application provided identity mapping? Valid Values include "Yes" and "No".
        l[266:270].strip(),     #GRICTX_DOMAP       Should the identity cache determine and store the identity mapping? Valid Values include "Yes" and "No".
        l[271:275].strip(),     #GRICTX_MAPREQ      Is an identity mapping required? Valid Values include "Yes" and "No".
        l[276:281].strip(),     #GRICTX_MAP_TIMEOUT How long the identity cache should store an identity mapping.
    )
    c.execute("INSERT INTO grictx VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05D0) General Resource ICTX Data Record processed.")

def process_grcfdef(l, c):
    v = (
        l[5:251].strip(),       #GRCFDEF_NAME       General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCFDEF_CLASS      Name of the class to which the general resource belongs, namely CFIELD.
        l[261:265].strip(),     #GRCFDEF_TYPE       Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[266:276].strip(),     #GRCFDEF_MAXLEN     Maximum length of the custom field.
        l[277:287].strip(),     #GRCFDEF_MAXVAL     Maximum value of the custom field.
        l[288:298].strip(),     #GRCFDEF_MINVAL     Minimum value of the custom field.
        l[299:307].strip(),     #GRCFDEF_FIRST      Character restriction for the first character. Valid values are ALPHA, ALPHANUM, ANY, NONATABC, NONATNUM, NUMERIC.
        l[308:316].strip(),     #GRCFDEF_OTHER      Character restriction for other characters. Valid values are ALPHA, ALPHANUM, ANY, NONATABC, NONATNUM, NUMERIC.
        l[317:321].strip(),     #GRCFDEF_MIXED      Is mixed case allowed in the field? Valid Values include "Yes" and "No".
        l[322:577].strip(),     #GRCFDEF_HELP       Help text for the custom field.
        l[578:618].strip(),     #GRCFDEF_LISTHEAD   List heading for the custom field.
        l[619:627].strip(),     #GRCFDEF_VALREXX    Name of the REXX exec to validate the custom field value.
    )
    c.execute("INSERT INTO grcfdef VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05E0) General Resource CFDEF Data Record processed.")

def process_grsig(l, c):
    v = (
        l[5:251].strip(),       #GRSIG_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRSIG_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:265].strip(),     #GRSIG_SIGREQUIRED  Signature required. Valid Values include "Yes" and "No".
        l[266:276].strip(),     #GRSIG_FAILLOAD     Condition for which load should fail. Valid values are NEVER, BADSIGONLY, and ANYBAD.
        l[277:287].strip(),     #GRSIG_AUDIT        Condition for which RACF should audit. Valid values are NONE, ALL, SUCCESS, BADSIGONLY, and ANYBAD.
    )
    c.execute("INSERT INTO grsig VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (05F0) General Resource SIGVER Data Record processed.")

def process_grcsf(l, c):
    v = (
        l[5:251].strip(),       #GRCSF_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCSF_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:273].strip(),     #GRCSF_EXPORTABLE   Is the symmetric key exportable? Valid values are: BYNONE, BYLIST, and BYANY.
        l[274:529].strip(),     #GRCSF_USAGE        Allowable uses of the asymmetric key. Valid values are: HANDSHAKE, NOHANDSHAKE, SECUREEXPORT, and NOSECUREEXPORT.
        l[530:533].strip(),     #GRCSF_CPACF_WRAP   Specifies whether the encrypted symmetric key is eligible to be rewrapped by CP Assist for Cryptographic Function (CPACF). Valid Values include "Yes" and "No".
        l[534:537].strip(),     #GRCSF_CPACF_RET    Specifies whether the encrypted symmetric keys that are rewrapped by CP Assist for Cryptographic Function (CPACF) are eligible to be returned to an authorized caller.
    )
    c.execute("INSERT INTO grcsf VALUES(?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05G0) General Resource ICSF Record processed.")

def process_grcsfk(l, c):
    v = (
        l[5:251].strip(),       #GRCSFK_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCSFK_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:325].strip(),     #GRCSFK_LABEL       ICSF key label of a public key that can be used to export this symmetric key.
    )
    c.execute("INSERT INTO grcsfk VALUES(?, ?, ?)", v)
    print("INFO: (05G1) General Resource ICSF Key Label Record processed.")

def process_grcsfc(l, c):
    v = (
        l[5:251].strip(),       #GRCSFC_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCSFC_CLASS_NAME  Name of the class to which the general resource profile belongs.
        l[261:358].strip(),     #GRCSFC_LABEL       Certificate identifier of a public key that can be used to export this symmetric key.
    )
    c.execute("INSERT INTO grcsfc VALUES(?, ?, ?)", v)
    print("INFO: (05G2) General Resource ICSF Certificate Identifier Record processed.")

def process_grmfa(l, c):
    v = (
        l[5:251].strip(),       #GRMFA_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRMFA_CLASS_NAME   Name of the class to which the general resource profile belongs, namely MFADEF.
        l[261:266].strip(),     #GRMFA_FACTOR_DATA_LEN  Length of factor data.
    )
    c.execute("INSERT INTO grmfa VALUES(?, ?, ?)", v)
    print("INFO: (05H0) General Resource MFA Factor Definition Record processed.")

def process_grmfp(l, c):
    v = (
        l[5:251].strip(),       #GRMFP_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRMFP_CLASS_NAME   Name of the class to which the general resource profile belongs, namely MFADEF.
        l[261:271].strip(),     #GRMFP_TOKEN_TIMEOUT    MFA token timeout setting.
        l[272:275].strip(),     #GRMFP_REUSE        MFA token reuse setting.
    )
    c.execute("INSERT INTO grmfp VALUES(?, ?, ?, ?)", v)
    print("INFO: (05I0) General Resource MFPOLICY Definition Record processed.")

def process_grmpf(l, c):
    v = (
        l[5:251].strip(),       #GRMPF_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRMPF_CLASS_NAME   Name of the class to which the general resource profile belongs, namely MFADEF.
        l[261:281].strip(),     #GRMPF_POL_FACTOR   Policy factor name.
    )
    c.execute("INSERT INTO grmpf VALUES(?, ?, ?)", v)
    print("INFO: (05I1) General Resource MFA Policy Factors Record processed.")

def process_grcsd(l, c):
    v = (
        l[5:251].strip(),       #GRCSD_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRCSD_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:265].strip(),     #GRCSD_TYPE         Data type for the custom field. Valid values are CHAR, FLAG, HEX, NUM.
        l[266:298].strip(),     #GRCSD_KEY          Custom field keyword; maximum length = 8.
        l[299:1399].strip(),    #GRCSD_VALUE        Custom field value.
    )
    c.execute("INSERT INTO grcsd VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (05J1) General Resource CSDATA Record processed.")

def process_gridtp(l, c):
    v = (
        l[5:251].strip(),       #GRIDTP_NAME        General resource name as taken from the profile name.
        l[252:260].strip(),     #GRIDTP_CLASS_NAME  Name of the class to which the general resource profile belongs, namely IDTDATA.
        l[261:293].strip(),     #GRIDTP_SIG_TOKEN_NAME      The ICSF PKCS#11 token name.
        l[294:302].strip(),     #GRIDTP_SIG_SEQ_NUM The ICSF PKCS#11 sequence number.
        l[303:307].strip(),     #GRIDTP_SIG_CA      The ICSF PKCS#11 category.
        l[308:340].strip(),     #GRIDTP_SIG_ALG     The signature algorithm.
        l[341:351].strip(),     #GRIDTP_TIMEOUT     IDT timeout setting.
        l[352:355].strip(),     #GRIDTP_ANYAPPL     Is the IDT allowed for any application? Valid values include "Yes" and "No".
    )
    c.execute("INSERT INTO gridtp VALUES(?, ?, ?, ?, ?, ?, ?, ?)", v)
    print("INFO: (05K0) General Resource IDTPARMS Definition Record processed.")

def process_grjes(l, c):
    v = (
        l[5:251].strip(),       #GRJES_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #GRJES_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:325].strip(),     #GRJES_KEYLABEL     The label of the ICSF key that is used to encrypt the JES spool data.
    )
    c.execute("INSERT INTO grjes VALUES(?, ?, ?)", v)
    print("INFO: (05L0) General Resource JES Data Record processed.")

def process_certn(l, c):
    v = (
        l[5:251].strip(),       #CERTN_NAME         General resource name as taken from the profile name.
        l[252:260].strip(),     #CERTN_CLASS_NAME   Name of the class to which the general resource profile belongs.
        l[261:1285].strip(),    #CERTN_ISSUER_DN    Issuers distinguished name.
        l[1286:2310].strip(),   #CERTN_SUBJECT_DN   Subjects distinguished name.
        l[2311:2327].strip(),   #CERTN_SIG_ALG      Certificate signature algorithm. Valid values are md2RSA, md5RSA, sha1RSA, sha1DSA, sha256RSA, sha224RSA, sha384RSA, sha512RSA, sha1ECDSA, sha256ECDSA, sha224ECDSA, sha384ECDSA, sha512ECDSA, and UNKNOWN.
    )
    c.execute("INSERT INTO certn VALUES(?, ?, ?, ?, ?)", v)
    print("INFO: (1560) General Resource Certificate Information Record processed.")