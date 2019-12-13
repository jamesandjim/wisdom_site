#ifndef __JB_NV_SDK_H__
#define __JB_NV_SDK_H__

#include <MMSYSTEM.H>
/************************************************************************/
/*  Error Code Define                                                   */
/************************************************************************/
#define JB_SUCCESS                          0x00000000
#define JBERR_BASE							0x10000000
#define	JBERR_PASSWORD_UNMATCH				(JBERR_BASE+0x03)			//���벻ƥ��
#define	JBERR_TIME_OVER						(JBERR_BASE+0x04)			//������ʱ
#define	JBERR_INVALID_PARAM					(JBERR_BASE+0x05)			//��Ч����
#define	JBERR_MAX_LINK						(JBERR_BASE+0x06)			//�������������
#define	JBERR_INVALID_HANDLE				(JBERR_BASE+0x07)			//����Ƿ������
#define	JBERR_INVALID_COMMAND				(JBERR_BASE+0x08)			//�������ܵ�����
#define	JBERR_SENDCMD_FAILD					(JBERR_BASE+0x09)			//������������ʧ��
#define	JBERR_GETCONFIG_FAILD				(JBERR_BASE+0x0A)			//ȡ����������ʧ��
#define	JBERR_NO_LOGON						(JBERR_BASE+0x0B)			//û�е�¼
#define	JBERR_ALLOC_FAILD					(JBERR_BASE+0x0C)			//�����ڴ�ʧ��
#define	JBERR_INVALID_NETADDRESS			(JBERR_BASE+0x0D)			//��Ч�Ļ��޷������������ַ	
#define	JBERR_FILE_CRC32					(JBERR_BASE+0x0E)			//�ļ�У���
#define JBERR_SOFTVER_ERR					(JBERR_BASE+0x10)			//����汾���ͣ��޷�У�������ļ�
#define	JBERR_CPUTYPE_ERR					(JBERR_BASE+0x11)			//�����ļ��������ڴ�CPU���͵�����
#define	JBERR_ERROR_10054					(JBERR_BASE+0x12)			//���ӱ�������ǿ�ȹر�!
#define	JBERR_ERROR_10061					(JBERR_BASE+0x13)			//������û����ָ���˿ڴ򿪷���!
#define	JBERR_ERROR_10060					(JBERR_BASE+0x14)			//û�з���ָ��IP�ķ�����!
#define	JBERR_ERROR_10065					(JBERR_BASE+0x15)			//����δ׼����!
#define	JBERR_INITSURFACE					(JBERR_BASE+0x16)			//��ʼ����ʾ�������
#define	JBERR_UNSUPPORT						(JBERR_BASE+0x17)			//��������֧�ִ˹���
#define JBERR_TALK_REJECTED					(JBERR_BASE+0x18)			//�Խ����󱻷������ܾ�
#define JBERR_TALK_INITAUDIO				(JBERR_BASE+0x19)			//�����Խ�ʱ��Ƶ��ʼ��ʧ��
#define JBERR_OPEN_FILE						(JBERR_BASE+0x1A)			//���ļ���
#define JBERR_BIND_PORT						(JBERR_BASE+0x1B)			//�󶨱��ض˿�ʧ��
#define JBERR_NO_FILE						(JBERR_BASE+0x21)			//û���ҵ��ļ�
#define JBERR_NOMORE_FILE					(JBERR_BASE+0x22)			//û�и����ļ�
#define	JBERR_FILE_FINDING					(JBERR_BASE+0x23)			//���ڲ���
#define JBERR_DISK_NOTEXIST					(JBERR_BASE+0x24)			//��ʽ��/������Ӳ�̲�����
#define JBERR_FILE_ERROR					(JBERR_BASE+0x25)			//�ļ�����ȷ���߲�ƥ��˷�����
#define JBERR_UNINITOBJ						(JBERR_BASE+0x26)			//����û�г�ʼ�����Ժ�����
#define JBERR_UNKNOW_SERVER					(JBERR_BASE+0x27)			//�������޷�ʶ��
#define JBERR_CHANNEL_NOT_OPEN				(JBERR_BASE+0x28)			//ͨ��û�д򿪣�����ʧ��
#define JBERR_INVALID_FILE					(JBERR_BASE+0x29)			//
#define JBERR_ENCRYPT_IC_NO_FIND			(JBERR_BASE+0x2A)			//������û���ҵ�����IC
#define JBERR_ENCRYPT_IC_NO_MATCH			(JBERR_BASE+0x2B)			//����IC��ƥ��
#define JBERR_RTSP_GET_DESCRIBE				(JBERR_BASE+0xB0)			//��ȡRTSP����ʧ��
#define	JBERR_RTSP_SETUPAUDIO				(JBERR_BASE+0xB1)			//RTSP������Ƶʧ��
#define	JBERR_RTSP_SETUPVIDIO				(JBERR_BASE+0xB2)			//RTSP������Ƶʧ��
#define	JBERR_RTSP_NOSTREAM					(JBERR_BASE+0xB3)			//RTSPû��������
#define	JBERR_RTSP_PLAY						(JBERR_BASE+0xB4)			//RTSP��������ʧ��
#define JBERR_IP_ERROR						(JBERR_BASE+0xB5)			//����IP���󣬲�������ָ��������
#define JBERR_SERVER_UPDATAING				(JBERR_BASE+0xB6)			//���������������������ܿͻ��˵����Ӳ���
#define JBERR_ERROR_10051					(JBERR_BASE+0xB7)			//���������޷�����Ŀ���豸�����粻�ɴ�
#define JBERR_LATEST_VERSION      			(JBERR_BASE+0x2C)           //��ǰ�������°汾
#define JBERR_UPGRADING      				(JBERR_BASE+0x2D)           //������

/************************************************************************/
/* ��Ϣ����		                                                        */
/************************************************************************/
#define  JB_MSG_VIDEOLOST					0x20000001  //��Ƶ��ʧ
#define  JB_MSG_MOVEDETECT                  0x20000002  //�ƶ�����
#define  JB_MSG_SENSOR_ALARM                0x20000003  //̽ͷ����
#define  JB_MSG_RESETSERVER                 0x20000004  //��������ΪĳЩ�������ı䣬��Ҫ��������
#define  JB_MSG_JPEGSNAP                    0x20000005  //JPEGץͼ
#define  JB_MSG_UPGRADE                     0x20000006  //��������֪ͨ
#define  JB_MSG_CRCERROR                    0x20000007  //����CRC��
#define  JB_MSG_SERVER_BUSY                 0x20000008  //������æ������ʧ��

//��Ϊ�������¿ͻ��˿��������ٷ������������Ϣ��ֱ����Ӧ�ò��ѯ״̬����������ʽ
//#define  JB_MSG_SERVER_BREAK                0x20000009  //�������ж�����
//#define  JB_MSG_CHANNEL_BREAK               0x2000000A  //ͨ���ж�����
#define  JB_MSG_TALK_REQUEST				0x2000000B	//Զ�̷���������Խ�
#define  JB_MSG_UPGRADEOK            		0x2000000C  //�������
#define	 JB_MSG_VIDEORESUME					0x2000000D	//��Ƶ�ָ�
#define	 JB_MSG_COMDATA						0x2000000E	//��������
#define	 JB_MSG_USERDATA					0x2000000F	//�û�����
#define	 JB_MSG_DISK_REMOVE					0x20000010	//���̱�̽�����Ƴ�
#define  JB_MSG_ALARM_SNAP					0x20000011 
#define	 JB_MSG_FILE_DATA					0x20000012	//ǰ�˷��ص��ļ������ӽṹΪ��JBNV_DVR_FILE_DATA
#define	 JB_MSG_DISK_ERROR					0x20000013	//���̴��ļ����ɶ�д��
#define  JB_MSG_TEL_ALARM					0x20000014	//�绰�澯����

//Add 2009-02-24
#define  JB_MSG_TEMPHUM_LOST_ALARM			0x20000015	//TempHum Device is Off
#define  JB_MSG_TEMPHUM_TEMP_LOWER			0x20000016	//TempHum Temp is Lower
#define  JB_MSG_TEMPHUM_TEMP_UPPER			0x20000017	//TempHum Temp is Upper
#define  JB_MSG_TEMPHUM_HUM_LOWER			0x20000018	//TempHum Hum is Lower
#define  JB_MSG_TEMPHUM_HUM_UPPER			0x20000019	//TempHum Hum is Upper
#define	 JB_MSG_POWER_220V_OFF				0x2000001A	//220V Power is Off
#define	 JB_MSG_POWER_48V_OFF				0x2000001B	//220V Power is Off
#define	 JB_MSG_POWER_DEVICE_LOST			0x2000001C  //Power Device is Off

#define  JB_MSG_FILE_NAME_DATA				0x2000001D //ǰ�˷��ص��ļ���  ���ӽṹ��JBNV_FILE_DATA_INFO
#define	 JB_MSG_ERROR_DEVICE				0x2000001E //��֧�ֵ�ǰ���豸

#define	 JB_MSG_IVS_DATA					0x2000001F //�̻𱨾�
#define	 JB_MSG_SENSOR_RESUME				0x20000020 //̽ͷ�����ָ�
#define	 JB_MSG_SERVER_LINK_OK              0x20000021 //���������ӳɹ�

#define JB_MSG_UPDATE_FILE					0x20000022	//�����ļ����ͽ���
#define JB_MSG_HSR_ALARM					0x20000023	//���α���
#define JB_MSG_HSR_ALARM_C					0x20000024	//���α������
#define JB_MSG_HFC_ALARM					0x20000025	//����ץ��
#define JB_MSG_FACE_RECOGNIZE				0x20000026
#define JB_MSG_LPR_ALARM                    0x20000027  //����ץ��

#define JB_MSG_DOWNLOAD_FRIM			    0x20000033  //������
#define JB_MSG_DOWNLOAD_FRIMOK			    0x20000034  //�������

#define ICE_HSD_MAX_OUTPUT_NUM	16



typedef struct tagrect_t
{
	int x;            //!< letf x
	int y;             //!< top y
	int w;           //!< right x
	int h;          //!< bottom y
} rect_t;

typedef struct
{
	int score;
	rect_t rect;
} human_info_s;

typedef struct
{
	int num;                           // ������Ŀ
	human_info_s human[50]; // ��������
} ICE_HSR_RESULT_S;

typedef struct
{
	DWORD x; /**< ���Ͻ�x���� */
	DWORD y; /**< ���Ͻ�y���� */
	DWORD w; /**< ���ο�� */
	DWORD h; /**< ���θ߶� */
} DMS_RECT_V2_S;


typedef struct tagDMS_FR_CMP_RET
{
    DWORD dwSize;				//�ṹ���С
    unsigned int id;            //����ID���㷨�����
    char uuid[36];				//UUID
    char name[32];				//����
    int  age;					//����
    char sex;					//�Ա� ��F��/��M��
    char role;					//1-������ 2-������ ...
    char identity_num[30];	    //���֤�� 18λ��
    int  score;					//���Ŷ�	
    DMS_RECT_V2_S rect;         //����λ��
    int  recognized;            //�ȶ�״̬: 0-�����ȶ� -1-δ���ȶ�
    int valid_time_type;        //��Ч������ 0:ÿ��(һ����ʼ����-һ���������) 1:����(0-6/������-������) 2:����(��ʼ����ʱ���-��������ʱ���)
    unsigned int start_time;    //��ʼʱ��
    unsigned int expire_time;   //����ʱ��
    int ndepartmentid;          //����ID
    int nworkid;                //Ա��ID
    int nHostelID;              //¥��ID
    char department_name[24];   //��������
    long devicetm;
    char csReserved[52];		//�����ֶ�

    char age2;                  // 0-N/A; ����-age;
    char gender;                // 0-N/A; 'M'-male; 'F'-female;
    char glasses;               // 0-N/A; 1-none; 2-glasses; 3-sunglasses;
    char mask;                  // 0-N/A; 1-none; 2-mask;
    char race;                  // 0-N/A; 1-yellow; 2-black; 3-white;
    char beard;                 // 0-N/A; 1-none 2-beard;
    char expression;            // 0-N/A; 1-angry; 2-calm; 3-happy; 4-sad; 5-surprised;
    char hat;                   // 0-N/A; 1-none; 2-hat;
	char hair;                  // 0-N/A; 1-short; 2-long; 3-bald;
	char hold_object;           // 0-N/A; 1-not hold object; 2-hold object;
	char upper_clothing;        // 0-N/A; 1-short level; 2-long level;
    char reserved2[5];

    unsigned int face_bg_data_len; //�����������ݳ���
    unsigned int snap_len;		// ץ�ĵ����ݳ���
    unsigned int src_len;		// ����ͼ���ݳ���
    unsigned int feature_data_len;
} DMS_FR_CMP_RET;



typedef struct
{
	unsigned int struct_size;	// �ṹ���С
	int id;
	int score;
	DMS_RECT_V2_S rect;         // ����λ��
	unsigned int face_data_len; // ��������ͼ���ݳ���
	unsigned int bg_data_len;   // ��������ͼ���ݳ���
} DMS_NET_FACE_CAPTURE_RESULT_S;


#define JB_MSG_CHANNEL_RECONN_SUCCESS		0x21000000

//FTP�ϴ�ʱ�����ܳ��ֵĴ���š�
#define JBERR_FTP_INVALID_PARAM					0x32000001
#define JBERR_FTP_CONNECT						0x32000002
#define JBERR_FTP_USERPASS						0x32000003
#define JBERR_FTP_NOSUPPORT						0x32000004
#define JBERR_FTP_CHANGEDIR						0x32000005
#define JBERR_FTP_PASVMODE						0x32000006
#define JBERR_FTP_DATACONNECT					0x32000007
#define JBERR_FTP_ALLOCSPACE					0x32000008
#define JBERR_FTP_STORFILE						0x32000009
#define JBERR_FTP_SENDDATA						0x3200000A
#define JBERR_FTP_MKDIR							0x3200000B

//����EMAILʱ�����ܳ��ֵĴ���
#define JBERR_EMAIL_INVALID_SERVER_ADDRESS		0x33000001
#define JBERR_EMAIL_CONNECT_FAILED				0x33000002
#define JBERR_EMAIL_SEND_LOGIN					0x33000003
#define JBERR_EMAIL_SEND_USERNAME				0x33000004
#define JBERR_EMAIL_SEND_PASSWORD				0x33000005
#define JBERR_EMAIL_GET_HOSTNAME				0x33000006
#define JBERR_EMAIL_SERVER_REJECT				0x33000007
//��дǰ�˴���ʱ�����ܳ��ֵĴ���
#define	JBERR_RECORD_DISK_READONLY				0x34000001	//���̴��ļ����ɶ�д��
/************************************************************************/
/* ��ָ̨��                                                             */
/************************************************************************/

#define PTZ_CMD_UP				1
#define	PTZ_CMD_DOWN			2
#define	PTZ_CMD_LEFT			3
#define	PTZ_CMD_RIGHT			4
#define	PTZ_CMD_FOCUS_SUB		5		//Focus Far
#define	PTZ_CMD_FOCUS_ADD		6		//Focus Near
#define	PTZ_CMD_ZOOM_SUB		7		//Zoom Wide
#define	PTZ_CMD_ZOOM_ADD		8		//Zoom Tele
#define	PTZ_CMD_IRIS_SUB		9		//Iris Close
#define	PTZ_CMD_IRIS_ADD		10		//Iris Open
#define	PTZ_CMD_STOP			11
#define	PTZ_CMD_PRESET			12		//Ԥ��
#define	PTZ_CMD_CALL			13		//����

#define	PTZ_CMD_AUTO_STRAT		14		//�Զ�
#define	PTZ_CMD_AUTO_STOP		15
#define	PTZ_CMD_LIGHT_OPEN		16		//�ƹ�
#define	PTZ_CMD_LIGHT_CLOSE		17		
#define	PTZ_CMD_BRUSH_START		18		//��ˢ
#define	PTZ_CMD_BRUSH_STOP		19		
#define	PTZ_CMD_TRACK_START		20		//�켣
#define	PTZ_CMD_TRACK_STOP		21
#define	PTZ_CMD_TRACK_RUN		22

#define DMS_PTZ_CMD_UP_LEFT			31
#define DMS_PTZ_CMD_UP_RIGHT		32
#define DMS_PTZ_CMD_DOWN_LEFT		33
#define DMS_PTZ_CMD_DOWN_RIGHT		34


#define DMS_PTZ_CMD_LEFT_RIGHT      35
#define DMS_PTZ_CMD_UP_DOWN         36

#define PTZCMD_UP				1
#define	PTZCMD_DOWN			    2
#define	PTZCMD_LEFT				3
#define	PTZCMD_RIGHT			4
#define	PTZCMD_FOCUS_SUB			5
#define	PTZCMD_FOCUS_ADD			6
#define	PTZCMD_ZOOM_SUB			7
#define	PTZCMD_ZOOM_ADD			8
#define	PTZCMD_IRIS_SUB			9
#define	PTZCMD_IRIS_ADD			10
#define	PTZCMD_LMAP			11
#define	PTZCMD_BRUSH			12
#define	PTZCMD_PRESET			13
#define	PTZCMD_CALL				14
#define	PTZCMD_AUTO			15
#define	PTZCMD_STOP				16
#define	PTZCMD_TRACK_CALL		17
#define	PTZCMD_KEYFN			18
#define	PTZCMD_AUTOSTOP			19
#define	PTZCMD_LIGHT			20
#define	PTZCMD_RAIN				21
#define	PTZCMD_TRACK_START		22
#define	PTZCMD_TRACK_STOP		23
#define	PTZCMD_TRACK_RUN			24
#define	PTZCMD_IO				25
#define	PTZCMD_IO_STOP			26



/************************************************************************/
/* �ṹ����			                                                    */
/************************************************************************/
// ��Ϣ�ṹ      
typedef struct tagJB_SERVER_MSG{
	DWORD		dwMsg;		//��Ϣ���ʹ���
	DWORD		dwChannel;	//ͨ��
	SYSTEMTIME	st;			//������ʱ��
	DWORD		cbSize;		//�������ݳ���
}JB_SERVER_MSG,*PJB_SERVER_MSG;

/************************************************************************/
/* ������Ƶ��������������                                               */
/************************************************************************/
#define		CMD_REBOOT					0x00000001		//Param:
#define		CMD_RESTORE					0x00000002		//Param:
#define		CMD_UPDATEFLASH				0x00000003		//Param:
#define		CMD_SNAPSHOT				0x00000004		//Param:int
#define		CMD_SETSYSTIME				0x00000005		//Param:SYSTEMTIME
#define		CMD_SET_OSDINFO				0x00000006		//Param:JB_CHANNEL_OSDINFO
#define		CMD_SET_SHELTER				0x00000007		//Param:JB_CHANNEL_SHELTER
#define		CMD_SET_LOGO				0x00000008		//Param:JB_CHANNEL_LOGO
#define		CMD_SET_CHANNEL_CONFIG		0x00000009		//Param:JB_CHANNEL_CONFIG
#define		CMD_SET_COLOR				0x0000000A		//Param:JB_CHANNEL_COLOR
#define		CMD_SET_MOTION_DETECT		0x0000000B		//Param:JB_CHANNEL_MOTION_DETECT
#define		CMD_SET_SENSOR_ALARM		0x0000000C		//Param:JB_SENSOR_ALARM
#define		CMD_SET_VIDEO_LOST			0x0000000D		//Param:JB_CHANNEL_VIDEO_LOST
#define		CMD_SET_COMINFO				0x0000000E		//Param:JB_SERVER_COMINFO
#define		CMD_SET_USERINFO			0x0000000F		//Param:JB_SERVER_USER
#define		CMD_SET_NETWORK				0x00000010		//Param:JB_SERVER_NETWORK
#define		CMD_UPLOAD_PTZ_PROTOCOL		0x00000011		//Param:JB_UPLOAD_PTZ_PROTOCOL
#define		CMD_SEND_COMDATA			0x00000012		//Param:JB_COM_DATA
#define		CMD_SET_FTPUPDATA_PARAM		0x00000013		//Param:JB_FTPUPDATA_PARAM
#define		CMD_CLEAR_ALARM_OUT			0x00000014		//Param:
 
#define		CMD_SET_ALARM_OUT			0x00000016		//Param:JBNV_ALARM_OUT_INFO
#define		CMD_SET_NOTIFY_SERVER		0x00000017		//Param:JB_NOTIFY_SERVER
#define		CMD_SET_PPPOE_DDNS			0x00000018		//Param:JB_PPPOE_DDNS_CONFIG
#define		CMD_SET_SENSOR_STATE		0x00000019		//Param:JBNV_SENSOR_STATE
//Add 2007-08-30
#define		CMD_SET_SERVER_RECORD		0x00000020		//Param:JB_SERVER_RECORD_SET
#define		CMD_RECORD_BEGIN			0x00000021		//Param:
#define		CMD_RECORD_STOP				0x00000022		//Param:
//Add 2007-09-17
#define		CMD_SET_CENTER_INFO			0x00000023		//Param:JB_CENTER_INFO
#define		CMD_UPDATE_CENTER_LICENCE	0x00000024
//Add 2008-01-14
#define		CMD_SET_CHANNEL_ALARM_CONFIG 0x00000025		//Param:JB_CHANNEL_ALARM_CONFIG
//Add 2008-05-14
#define		CMD_SET_EMAIL_PARAM			0x00000026		//Param:JBNV_EMAIL_PARAM
//Add 2008-07-07
#define		CMD_SET_COMMODE				0x00000027		//Param:JBNV_SERVER_COMMODE
#define		CMD_SET_3322DDNS			0x00000028		//Param:JBNV_3322DDNS_CONFIG
#define		CMD_STOP_FILE_DOWNLOAD		0x00000029
//Add 2008-08-20	
#define		CMD_SET_NVD_SENSOR_ALARM	0x0000002A		//Param:JB_NVD_SENSOR_ALARM_SET

//Add 2008-11-25
#define     CMD_SET_WIFI				0x00000046		//Param:JB_WIFI_CONFIG
#define     CMD_SET_TDSCDMA				0x00000047		//Param:JB_TDSCDMA_CONFIG
#define		CMD_SET_PERIPH_CONFIG		0x00000048		//Param:JB_PERIPH_CONFIG
#define		CMD_SET_TEL_ALARM			0x00000049		//Param:JB_TEL_ALARM_SET
//Add 2009-02-24
#define		CMD_SET_TEMPHUM_SENSOR		0x0000004A		//Param:JB_TEMP_HUM_SENSOR_CONFIG
#define		CMD_SET_POWER_DEVICE		0x0000004B		//Param:JB_POWER_DEVICE_CONFIG

#define		CMD_SET_RECORD_CONFIG		0x0000004C		//Param:JB_SERVER_RECORD_CONFIG
#define  	CMD_SET_UPNP				0x0000004D  	//Param:JB_UPNP_CONFIG
#define		CMD_SET_PLAYBACK_NAME		0x0000004E		//Param: char *csPlayBackFileName
#define		CMD_SET_PLAYBACK_TIME		0x0000004F		//Param:JBNV_TIME
#define		CMD_PLAYBACK_VODACTION		0x00000050		//Param:JBNV
#define		CMD_SET_MOBILE_CENTER		0x00000051		//Param:JB_MOBILE_CENTER_INFO
#define		CMD_SET_CHANNEL_SUBSTREAM_CONFIG 0x00000052	//Param:JB_CHANNEL_CONFIG

#define		CMD_FDISK_DISK				0x00000061		//Param:JBNV_FDISK_DISK
#define		CMD_FORMAT_DISK				0x00000062		//Param:JBNV_FORMAT_DISK

//Added 2011-12-20
#define CMD_REQUEST_IFRAME				0x00000063 //Param:JB_CHANNEL_FRAMEREQ

#define CMD_SET_CENTER_INFO_EX			0x00000064 //Param:JBNV_NXSIGHT_SERVER_ADDR_EX
#define CMD_GET_CENTER_INFO_EX			0x00000065 //Param:JBNV_NXSIGHT_SERVER_ADDR_EX

#define CMD_SET_AUDIO_PARA				0x00000066 //Param:HI_CFG_AUDIO_ATTR_S
#define CMD_GET_AUDIO_PARA				0x00000067 //Param:HI_CFG_AUDIO_ATTR_S

#define CMD_FORMAT_DISK_NEW				0x00000068 //Param:HI_HDI_FORMAT

#define		CMD_SET_FR_VOICE			0x00000071  //

#define  CMD_MOUSE_CHECK                0x00000080  //Զ�����棬�����Ϣ JBNV_MOUSE_MESSAGE
// �����ȶ��������ݿ����
#define  	CMD_FR_ADD_SAMPLE			0xA0100050 // �������� DMS_FR_SAMPLE_S
#define  	CMD_FR_DEL_SAMPLE			0xA0100051 // ɾ������ DMS_FR_SAMPLE_S
#define  	CMD_FR_UPDATE_SAMPLE		0xA0100052 // �������� DMS_FR_SAMPLE_S
#define  	CMD_FR_QUERY_SAMPLE			0xA0100053 // ��������ѯ���� ����DMS_FR_SAMPLE_QUERY_COND_S, ����DMS_FR_SAMPLE_QUERY_RES_S
#define  	CMD_FR_REQ_SAMPLE_PIC		0xA0100054 // ����ָ��ID��ͼƬ���� DMS_FR_SAMPLE_S

#define     DMS_NET_CMD_FR_GET_PARA     0xA0100055  //DMS_FACE_RECG_ATTR_S	
#define     DMS_NET_CMD_FR_SET_PARA     0xA0100056
#define     CMD_FR_SET_VERSION          0xA0100057 // ��ѯ������汾        DMS_FR_VERSION_QUERY
#define     CMD_FR_GET_VERSION          0xA0100058 // ����������汾        DMS_FR_VERSION_QUERY
#define DMS_NET_CMD_FR_RESET_SAMPLE_DB  0xA0100059 // �����������ݿ�    ɾ����������������������

#define DMS_NET_CMD_FR_QUERY_HISTORY            0xA010005B // ��ѯ�ȶԼ�¼ ����DMS_FR_RECORD_QUERY_COND_S, ����DMS_FR_RECORD_QUERY_RES_S
#define DMS_NET_CMD_FR_QUERY_HISTORY_PIC        0xA010005C // ����ָ��ID��ͼƬ����  DMS_FR_RECORD_S 
#define DMS_NET_CMD_FR_QUERY_HISTORY_BY_TIME    0xA010005D // ��ѯ��ֹʱ���ڵıȶԼ�¼  DMS_FR_RECORD_QUERY_BY_TIME_REQ_S, ����DMS_FR_RECORD_QUERY_RES_S

// �������
#define DMS_NET_CMD_FD_GET_PARA        0xA0100060 // DMS_FACE_DETECT_ATTR_S
#define DMS_NET_CMD_FD_SET_PARA        0xA0100061

// ����ץ��
#define DMS_NET_CMD_FC_GET_PARA        0xA0100070 // DMS_FACE_CAPTURE_ATTR_S
#define DMS_NET_CMD_FC_SET_PARA        0xA0100071
#define DMS_NET_CMD_FC_SRV_GET_PARA    0xA0100072 // DMS_FACE_SERVER_S
#define DMS_NET_CMD_FC_SRV_SET_PARA    0xA0100073

//ӭ�����ӿ�
#define DMS_NET_CMD_WELCOME_GET_PARA   0xA0100080   //DMS_WELCOME_ATTR_S
#define DMS_NET_CMD_WELCOME_SET_PARA   0xA0100081   //DMS_WELCOME_ATTR_S

#define DMS_NET_CMD_FR_GET_ATTANDENCE_DB    0xA0100090  //��ȡ��������

#define DMS_NET_CMD_FR_UPDATE_MODEL_DATA    0xA0100091  //�����������ģ������  JBNV_VFR_MODEL_DATA
#define DMS_NET_CMD_FR_GET_MODEL_CRC_VALUE  0xA0100092  //��ȡģ�͵�CRCֵ       JBNV_VFR_MODEL_INFO

#define DMS_NET_CMD_SET_FR_ALARM_PARA	0xA01000A0  //DMS_FR_ALARM_ATTR_S
#define DMS_NET_CMD_GET_FR_ALARM_PARA	0xA01000A1  //DMS_FR_ALARM_ATTR_S

#define DMS_NET_CMD_SET_LPR_PARAM	0xA01000C0  //JB_LPR_PARAM
#define DMS_NET_CMD_GET_LPR_PARAM	0xA01000C1  //JB_LPR_PARAM

 

/************************************************************************/
/*��ȡ��������Ϣ                                                        */
/************************************************************************/
#define		CMD_GET_SYSTIME				0x10000000		//Param:SYSTEMTIME
#define		CMD_GET_OSDINFO				0x10000001		//Param:JB_CHANNEL_OSDINFO
#define		CMD_GET_CHANNEL_CONFIG		0x10000002		//Param:JB_CHANNEL_CONFIG
#define		CMD_GET_COLOR				0x10000003		//Param:JB_CHANNEL_COLOR
#define		CMD_GET_MOTION_DETECT		0x10000004		//Param:JB_CHANNEL_MOTION_DETECT
#define		CMD_GET_SENSOR_ALARM		0x10000005		//Param:JB_SENSOR_ALARM
#define		CMD_GET_VIDEO_LOST			0x10000006		//Param:JB_CHANNEL_VIDEO_LOST
#define		CMD_GET_COMINFO				0x10000007		//Param:JB_SERVER_COMINFO
#define		CMD_GET_USERINFO			0x10000008		//Param:JB_SERVER_USER
#define		CMD_GET_NETWORK				0x10000009		//Param:JB_SERVER_NETWORK
#define		CMD_GET_FTPUPDATA_PARAM		0x1000000A		//Param:JB_FTPUPDATA_PARAM
 
 
#define		CMD_GET_ALARM_OUT			0x1000000D		//Param:JBNV_ALARM_OUT_INFO
#define		CMD_GET_NOTIFY_SERVER		0x1000000E		//Param:JB_NOTIFY_SERVER
#define		CMD_GET_PPPOE_DDNS			0x1000000F		//Param:JB_PPPOE_DDNS_CONFIG
#define		CMD_GET_SENSOR_STATE		0x10000010		//Param:JBNV_SENSOR_STATE
//Add 2007-08-30
#define		CMD_GET_SERVER_RECORD_SET	0x10000011		//Param:JB_SERVER_RECORD_SET
#define		CMD_GET_SERVER_RECORD_STATE	0x10000012		//Param:JB_SERVER_RECORD_STATE
#define		CMD_UNLOAD_DISK				0x10000013		//Param:
//Add 2007-09-17
#define		CMD_GET_CENTER_INFO			0x10000014		//Param:JB_CENTER_INFO

//Add 2008-01-14
#define		CMD_GET_CHANNEL_ALARM_CONFIG	0x10000015	//Param:JB_CHANNEL_ALARM_CONFIG
#define		CMD_GET_CENTER_LICENCE		0x10000016		
//Add 2008-05-04
#define		CMD_GET_SERVER_STATUS		0x11000001		//Param:JB_SERVER_STATE	
//Add 2008-05-14
#define		CMD_GET_EMAIL_PARAM			0x10000017		//Param:JBNV_EMAIL_PARAM
//Add 2008-07-07
#define		CMD_GET_COMMODE				0x10000018		//Param:JBNV_SERVER_COMMODE
#define		CMD_GET_3322DDNS			0x10000019		//Param:JBNV_3322DDNS_CONFIG
//Add 2008-07-28
#define		CMD_GET_DIRECT_LIST			0x1000001A		//Param:JBNV_DIRECTORY_LIST
#define		CMD_GET_FILE_DATA			0x1000001B		//Param:char[64]
//Add 2008-08-20	
#define		CMD_GET_NVD_SENSOR_ALARM	0x1000001C		//Param:JB_NVD_SENSOR_ALARM_SET
//Add 2008-11-25
#define     CMD_GET_WIFI				0x10000046		//Param:JB_WIFI_CONFIG
#define     CMD_GET_TDSCDMA				0x10000047		//Param:JB_TDSCDMA_CONFIG
//Add 2008-12-22
#define		CMD_GET_PERIPH_CONFIG		0x10000048		//Param:JB_PERIPH_CONFIG
#define		CMD_GET_TEL_ALARM			0x10000049		//Param:JB_TEL_ALARM_SET
//Add 2009-02-24
#define		CMD_GET_TEMPHUM_SENSOR		0x1000004A		//Param:JB_TEMP_HUM_SENSOR_CONFIG
#define		CMD_GET_POWER_DEVICE		0x1000004B		//Param:JB_POWER_DEVICE_CONFIG

#define		CMD_GET_RECORD_CONFIG		0x1000004C		//Param:JB_SERVER_RECORD_CONFIG
#define		CMD_GET_UPNP				0x1000004D		//Param:JB_UPNP_CONFIG
#define		CMD_GET_FILELIST			0x1000004E		//Param:JBNV_FIND_FILE_RESP
#define		CMD_GET_MOBILE_CENTER		0x10000051		//Param:JB_MOBILE_CENTER_INFO
#define		CMD_GET_CHANNEL_SUBSTREAM_CONFIG 0x10000052	//Param:JB_CHANNEL_CONFIG

#define		CMD_GET_DISK_INFO			0x10000060			//Param:JBNV_DISK_INFO
#define		CMD_GET_FORMAT_STATE		0x10000061			//Param:JBNV_FORMAT_STATUS


#define  	NETCMD_SET_ALARM_VOICE      0x00000070

#define		CMD_SET_DVR_CONFIG			0x000000A0			
#define		CMD_GET_DVR_CONFIG			0x100000A0	

#define		CMD_GET_SYSTEM_INFOR		0x10001001		//Param:JB_SYSTEM_INFOR


typedef struct tagJB_SYSTEM_INFOR
{
    char DeviceModel[24];   //�豸�ͺ�,����M1
    char DeviceNumber[24];  //�豸��ţ����к�
    char KernelVer[64];		//�ں˰汾
    char ServerVer[24];		//�������汾���豸����汾
    char WebVer[24];		//��ҳ�汾������eg:V2.3.4-20190117
    char PluginVer[24];		//����汾������eg:6.0.0.8
    char csReserved[512];
}JB_SYSTEM_INFOR,*LPJB_SYSTEM_INFOR;

typedef struct tagWH_WCMDA_DIAL_PARAM{
    DWORD   dwSize;
    char    csAPN[32];          //3gnet     
    char    csUsername[32];     //card     
    char    csPassword[32];     //card    
    char    csDialNumber[32];   //*99#
    int     bDefault;           //�Ƿ�ΪĬ�ϲ�����1ΪϵͳĬ�ϣ�0Ϊ�û��޸�
    char    bEth0IsOnline;
    char    bWifiIsOnline;
    char    csReserved[60];
}WH_WCMDA_DIAL_PARAM;

typedef struct tagDMS_WELCOME_ATTR_S
{
    int dwSize;
    int channel;
    int enable;     // ʹ�ܿ���
    int duration;   // ����ʱ��(��λ: ��)
    int name_pos;   // 0-�ƺ���ǰ 1-�ƺ��ں�
    char text[256]; // �Զ��延ӭ��
    char reserved[256];
}DMS_WELCOME_ATTR_S;

//2014-10-23 17:08:25 Ѧ���� 
#define     CMD_SET_WCDMA_DIAL          0x01000062          //����3G����
#define     CMD_GET_WCDMA_DIAL          0x10000062          //��ȡ3G���Ų���
/************************************************************************/
/* ����ͨ��SDK��ȡ�ķ�������Ϣ                                          */
/************************************************************************/
//�û�Ȩ�޶���
#define		USER_RIGHT_PTZ			0x0001		//����̨
#define		USER_RIGHT_SETUP		0x0002		//����
#define		USER_RIGHT_UPDATE		0x0004		//����
//#define		USER_RIGHT_SETUP		0x80000000

/************************************************************************/
/* ���������ܶ���                                                       */
/************************************************************************/
#define DMS_SYS_FLAG_ALARM_IN           0x0001
#define DMS_SYS_FLAG_ALARM_OUT          0x0002
#define DMS_SYS_FLAG_ALARM_PERSON       0x0004
#define DMS_SYS_FLAG_ALARM_FACE         0x0008        //֧������ץ��
#define DMS_SYS_FLAG_PTZ                0x0010
#define DMS_SYS_FLAG_WIFI               0x0020
#define DMS_SYS_FLAG_DDNS               0x0040
#define DMS_SYS_FLAG_FACE_ANALYZE       0x0080       //֧�������ȶ�
#define DMS_SYS_FLAG_LPR                0x0100        //֧�ֳ�����ȡ


/************************************************************************/
/* ���������Ͷ���                                                       */
/************************************************************************/
#define JB_NVS_FLAG			100001	//������Ƶ������
#define JB_NVD_FLAG			100002	//������Ƶ������
#define JB_DVR_FLAG			100003	//������Ƶ����������Ӳ�̣�
#define DMS_IPCAM_FLAG		100004	//


//������������Ϣ
typedef struct tagJBNV_SERVER_INFO
{
	DWORD		dwSize;				//�ṹ��С
	DWORD		dwServerFlag;		//����������
	DWORD		dwServerIp;			//������IP(������ʾ��ʽ)
	char		szServerIp[16];		//������IP(�ַ�����ʾ��ʽ)
	WORD		wServerPort;		//�������˿�
	WORD		wChannelNum;		//ͨ������
	DWORD		dwVersionNum;		//�汾
	char		szServerName[32];	//����������
	DWORD		dwServerCPUType;	//��ǰCPU����
	BYTE		bServerSerial[48];	//���������кţ�����Ψһ��ʶ����
	BYTE		byMACAddr[6];		//�������������ַ
	DWORD		dwAlarmInCount;
	DWORD		dwAlarmOutCount;
	DWORD		dwSysFlags;			//ϵͳ֧�ֵĹ���
	DWORD		dwUserRight;		//��ǰ�û�Ȩ��
	DWORD		dwNetPriviewRight;	//����ۿ�Ȩ��
	DWORD		dwCompany;
	char		csP2PID[32];
	DWORD		dwStatus;
    DWORD       image_flags;        //ͼ��֧��ģʽ
    char        image_type;           //0: ir 1: white light 2: double light
	char        image_switch_type;    //0: ircut switch mode 1: soft switch mode
	char		cReserved[18];
}JBNV_SERVER_INFO,*PJBNV_SERVER_INFO;


#define DMS_FR_QUERY_MAX_NUM 50

// ������������
typedef struct tagDMS_FR_SAMPLE_S
{
	DWORD dwSize;				// �ṹ���С
	DWORD id;					// ���ݿ�ΨһID
	char uuid[36];				// UUID
	char name[32];				// ����
	int	 age;					// ����
	char sex;					// �Ա� ��F��/��M��
	char role;					// 0,���У�1-������ 2-��������3��VIP��4,İ����
	char identity_num[30];		// ���֤�� 18λ��
	char csOther[64];
    char csICCard[32];          //IC��
    char csTel[16];             //�绰����  
    unsigned short x;           //����ͼƬ�У�����λ��
    unsigned short y;
    unsigned short w;
    unsigned short h;
    int valid_time_type;        // ��Ч������ 0:ÿ��(һ����ʼ����-һ���������) 1:����(0-6/������-������) 2:����(��ʼ����ʱ���-��������ʱ���)
    unsigned int start_time;    // ��ʼʱ��
    unsigned int expire_time;   // ����ʱ��
    int nClassID;               //����ID
    int nworkid;                //Ա��ID
    int nHostelID;              //¥��ID
    char department_name[24];   //��������
	char reserved[88];	        //����
	unsigned int feature_len;	// ����ֵ����
	unsigned int data_len;		// ����ͼ���ݳ���
} DMS_FR_SAMPLE_S;

// ��ѯ����
typedef struct tagDMS_FR_SAMPLE_QUERY_COND_S
{
	int struct_size;   	// �ṹ���С
	int page_size;      // ÿҳ��ʾ��������¼
	int page_index;     // ҳ�� 0,1,2,3
	int role;           // �������� 0-����, ����ͬDMS_FR_SAMPLE_S��role
    char csName[32];    // ����
    char csReserved[64];//
} DMS_FR_SAMPLE_QUERY_COND_S;

// ��ѯ���
typedef struct
{
	int struct_size;    // �ṹ���С
	int total_size;     // ���ݿ��ܵļ�¼��
	int query_size;     // ��ǰ��ѯ����ļ�¼��
	DMS_FR_SAMPLE_S sample[DMS_FR_QUERY_MAX_NUM]; // ����ͼƬ���ݡ�����ֵ
} DMS_FR_SAMPLE_QUERY_RES_S;

typedef struct
{
    int struct_size;
    int nFrTotal;       //��������  (R)
    int nVersion;       //�汾      (RW)
    char csReserved[128];
} DMS_FR_VERSION_QUERY;

typedef struct
{
	int struct_size;
	int channel;
	int threshold;      // �ȶԵ÷���ֵ ���ȶԵ÷ִ��ڴ�ֵ,����Ϊ�ȶԳɹ�,����ȶ�ʧ��
	char reserved[256];
} DMS_FACE_RECG_ATTR_S;


typedef struct
{
	int hour;
	int minute;
	int second;
} DMS_TIME_S;

typedef struct
{
	int enable;
	DMS_TIME_S begin1;
	DMS_TIME_S end1;
	DMS_TIME_S begin2;
	DMS_TIME_S end2;
} DMS_SCHEDULE_S;

/******************** ���������� ***************************/
typedef struct
{
	int struct_size;
	int channel;
	int enable;      // �Ƿ�ʹ��
	short size_min;    // ��С�����ߴ�
	short sensitivity; // ������(0~100) ԽСԽ����
	int rect_num;    // ����������
	DMS_RECT_V2_S rect[4]; // ��������
	DMS_SCHEDULE_S schedule[8];// ����ʱ��
	int show_face;   // ��ƵԤ���Ƿ���ʾ������
    int  live_detect;
	char reserved[256 - 4];
} DMS_FACE_DETECT_ATTR_S;


/******************** ����ץ�Ĳ��� ***************************/
typedef enum
{
	DMS_FACE_CAP_MODE_LEAVE = 0,    // ���뿪��ץ�ģ�ÿ�δ����������¼���ʼ�����������뿪�¼�������ץȡһ����������ֵ��ѵ�ͼƬ
	DMS_FACE_CAP_MODE_REALTIME = 1, // ʵʱץ��: �����������¼���ʼ, �����ַ���ץ������������ʱ, ��������ץ��, �Һ���������������ץ��
	DMS_FACE_CAP_MODE_INTERVAL = 2, // ���ץ��: ������������뼰�뿪�¼�, ���ڼ�������ڼ�⵽����ʱ, �����õ�ץ��ʱ����, �����Ե��ϴ�������������ץ��ͼƬ��
	DMS_FACE_CAP_MODE_BUTT,
} DMS_FACE_CAP_MODE_E;

typedef struct
{
	int struct_size;
	int channel;
	DMS_FACE_CAP_MODE_E mode; // ץ��ģʽ 0-���뿪��ץ�� 1-ʵʱץ�� 2-���ץ��
	int threshold; // �ȶ���ֵ, �������ж��ȶԳɹ�
	int interval;  // ץ�ļ��, ����ץ��ģʽΪDMS_FACE_CAP_MODE_INTERVALʱ��Ч (��λ:��)
	int pic_type;  // 0-��������ͼ 1-��������ͼ+ԭͼ
	char reserved[256];
} DMS_FACE_CAPTURE_ATTR_S;

typedef struct
{
	int  enable;
	char host[16];
	int  port;
} DMS_HTTP_SERVER_S;

typedef struct
{
	int  enable;
	char host[16];
	int  port;
	char user[32];
	char pwd[32];
	char path[64];
} DMS_FTP_SERVER_S;

typedef struct
{
	int  struct_size;
	int  channel;
	DMS_HTTP_SERVER_S http_server;
	DMS_FTP_SERVER_S  ftp_server;
	int  pic_upload_type; // 0:����ͼƬ 1:����ͼƬ+ԭͼ
	char reserved[256];
} DMS_FACE_SERVER_S;


//��Ƶ��������
#define	 WAVE_FORMAT_ALAW						0x0006 
#define  WAVE_FORMAT_MPEGLAYER3                 0x0055
#define	 WAVE_FORMAT_G722_ADPCM					0x0065
#define	 WAVE_FORMAT_G711A						0x003E
#define	 WAVE_FORMAT_G711U						0x003F
#define	 WAVE_FORMAT_ADPCM						0x0002
#define	 WAVE_FORMAT_G726_ADPCM					0x0064		//��˼�����ADPCM
//����������Ϣ
typedef struct tagJBNV_CHANNEL_INFO
{
    DWORD   dwSize;
    DWORD   dwStream1Height;	//��Ƶ��(1)
    DWORD   dwStream1Width;		//��Ƶ��
	DWORD   dwStream1CodecID;	//��Ƶ�������ͺţ�H264,4;H265,8;JPEG,5��
    DWORD   dwStream2Height;	//��Ƶ��(2)
    DWORD   dwStream2Width;		//��Ƶ��
    DWORD   dwStream2CodecID;	//��Ƶ�������ͺţ�H264,4;H265,8;JPEG,5��
    DWORD   dwAudioChannels;	//��Ƶͨ����
    DWORD   dwAudioBits;		//��Ƶ������
    DWORD   dwAudioSamples;		//��Ƶ������
    DWORD   dwWaveFormatTag;	//��Ƶ�������ͺ�
	char	csChannelName[32];	//ͨ������
}JBNV_CHANNEL_INFO,*PJBNV_CHANNEL_INFO;

#define MAX_SENSOR_IN	16
#define MAX_SENSOR_OUT	16
#define MAX_SENSOR_INOUT	(MAX_SENSOR_IN +MAX_SENSOR_OUT)

//̽ͷ��������
//̽ͷ�����б�
//0x0001 �������̽ͷ
//0x0002 ����̽ͷ
//0x0003 ����̽ͷ
//0x0004 �Ŵ�̽ͷ
//0x0005 ���������Ӧ
//0x0006 ���ߺ���̽ͷ
//0x0007 ��̤����
//0x0008 �̸�̽ͷ
//0x0009 �ְ�����
//0x000A ��Ƶ����̽ͷ

//������ࣺ
//0x0001 �Զ�������
//0x0002 ������
//0x0003 �ƾ߿���
//0x0004 ��е����
typedef struct tagJBNV_SENSOR_INFO
{
	DWORD	dwSize;
	DWORD	dwIndex;				//̽ͷ����
	DWORD	dwSensorType;			//̽ͷ����
	char	csSensorName[32];		//̽ͷ����
}JBNV_SENSOR_INFO,*PJBNV_SENSOR_INFO;

//������״̬
typedef struct tagJB_SERVER_STATE
{
	DWORD	dwSize;
	DWORD	dwAlarmInState;			//�澯����״̬
	DWORD	dwAlarmOutState;		//�澯���״̬
	DWORD	dwVideoState;			//��Ƶ״̬
	DWORD	dwServerError;			//������������Ϣ
	DWORD	dwLinkNum;				//�ͻ������ӵĸ���
	DWORD	dwClientIP[10];			//�ͻ��˵�IP��ַ
}JB_SERVER_STATE,*LPJB_SERVER_STATE;
/************************************************************************/
/* ������������Ϣ�ṹ                                                   */
/************************************************************************/

/*--------------------------ͨ�����ýṹ--------------------------------*/
//ͨ��OSD��ʾ�Լ�ͨ����������
typedef struct tagJB_CHANNEL_OSDINFO
{
	DWORD	dwSize;
	DWORD	dwChannel;
    BYTE    bShowWeek;            //�Ƿ���ʾ���� (0-��ʾ 1-����ʾ)
    BYTE    bShowFaceStatistic;   //�Ƿ���ʾ������ͳ�� (0-��ʾ 1-����ʾ)
    BYTE    reserve1[2];
	DWORD	dwTimeFormat;
			/*
			0 XXXX-XX-XX (������)
			1 XX-XX-XXXX (������)
			2 XXXX��XX��XX��
			3 XX��XX��XXXX��
			4 XX-XX-XXXX ������
			5 XX��XX��XXXX��
			*/
	DWORD	dwReserved2;			 
	DWORD	dwOsdPos;			//0 left top;1 left bottom; 2 right top; 3 right bottom; 
	DWORD	dwTimePos;			
	char	csString[80];		//�û������ַ���
}JB_CHANNEL_OSDINFO,*LPJB_CHANNEL_OSDINFO;

//ͨ�����á�
typedef struct tagJB_CHANNEL_CONFIG
{
	DWORD	dwSize;
	DWORD	dwChannel;			//ͨ����
	DWORD	nFrameRate;			//֡�� (1-25/30) PALΪ25��NTSCΪ30
	DWORD	nStandard; 			//��ʽ (0ΪNTSC��,1ΪPAL��)
	DWORD	dwRateType;			//��ģʽ(0Ϊ��������1Ϊ������)
	DWORD	dwStreamFormat;		//��ʽ (0ΪCIF,1ΪD1,2ΪHALF-D1,3ΪQCIF)
	DWORD	dwBitRate;			//���� (16000-4096000)
	DWORD	dwImageQuality;		//��������(0-4),0Ϊ���
	DWORD	nMaxKeyInterval;	//�ؼ�֡���(1-100)
	BOOL	bEncodeAudio;		//�Ƿ������Ƶ
	char	csChannelName[32];	//ͨ������
}JB_CHANNEL_CONFIG,*LPJB_CHANNEL_CONFIG;

//ͨ����ɫ����
typedef struct tagJB_CHANNEL_COLOR
{
	DWORD	dwSize;
	DWORD	dwChannel;
	DWORD	dwSetFlag;		//0,���õ�������;1,�������;2,�ָ���һ�α����
	DWORD	dwHue;			//ɫ��
	DWORD	dwColor;		//ɫ��
	DWORD	dwContrast;		//�Աȶ�
	DWORD	dwBrightness;	//����
	DWORD	dwDefinition;	//������
}JB_CHANNEL_COLOR,*PJB_CHANNEL_COLOR;

//���������ṹֻ֧������
//LOGO��������
//LOGO�����ݲ�֧��
#pragma warning( disable:4200 )
typedef struct tagJB_CHANNEL_LOGO
{
	DWORD	dwSize;
	DWORD	dwChannel;
	BOOL	bEnable;		//�Ƿ�����LOGO��ʾ
	DWORD	dwLogox;		//LOGO��ʾ��ʼλ�ã���D1Ϊ׼
	DWORD	dwLogoy;
	BYTE	bLogoData[];	//��LOGO���ݿ��Ե���...��á��������Ϊ40K
}JB_CHANNEL_LOGO;
#pragma warning( default:4200 )

//�ڵ���������
typedef struct tagJB_CHANNEL_SHELTER
{
	DWORD	dwSize;
	DWORD	dwChannel;
	BOOL	bEnable;		//�Ƿ���������ڵ�
	RECT	rcShelter[5];	//�ڵ��������֧��5��������ڵ���RECT��D1Ϊ׼
}JB_CHANNEL_SHELTER,*PJB_CHANNEL_SHELTER;

//����ؼ�֡
typedef struct tagJB_CHANNEL_FRAMEREQ
{
	DWORD	dwSize;
	DWORD	dwChannel;
	DWORD	dwStreamType;
	DWORD	dwFrameType;		// 0 - I�����ౣ��
}JB_CHANNEL_FRAMEREQ, *PJB_CHANNEL_FRAMEREQ;

//�澯��ؽṹ��
typedef struct tagJB_SET_TIME{
	WORD	wHour;				//(0-23)
	WORD	wMinute;			//(0-59)
}JB_SET_TIME;

//����ʱ���
typedef struct tagJB_SCHED_TIME
{
	BOOL		bEnable;		//�Ƿ����ø�ʱ���
	JB_SET_TIME	BeginTime1;		//ʱ���1
	JB_SET_TIME	EndTime1;
	JB_SET_TIME	BeginTime2;		//ʱ���2
	JB_SET_TIME	EndTime2;
}JB_SCHED_TIME;

//���и澯��ͼ��ץ�ľ��Զ��ϴ����ͻ��ˣ�����Ҫ�������á�
//��Ƶ�ƶ��澯
typedef struct tagJB_CHANNEL_MOTION_DETECT{
	DWORD			dwSize;
	DWORD			dwChannel;				//ͨ����
	BOOL			bEnable;				//�Ƿ���в���
	DWORD			nDuration;				//����IO�˿��������ʱ��(��)
	BOOL			bShotSnap;				//�Ƿ��Զ�ץͼ
	BOOL			bAlarmIOOut[4];			//̽ͷ���
	DWORD			dwSensitive;			//������
	JB_SCHED_TIME	jbScheduleTime[8];		//����ʱ��Σ�����һ�������졢ÿ�ա�
	RECT	        rectMotion[4];
	BOOL            bLight;					// �׹�����
	int             bVoice;					// ��������,0��ɶ��������1�����¼������ & ������ź�
	WORD			wVoiceCount;			// ����
	WORD            wVoiceIndex;			// ѡ�еģ��Զ��� 0xFFFF
	int				bVoiceCustom;			//�Ƿ�ʹ���Զ�����Ƶ
	BOOL            bShowHuman; 
	RECT	        rectHumanMin;
	RECT	        rectHumanMax;
    DWORD           direction;              // 0:˫�� 1:���� 2:�뿪
	BYTE          	reserve[216 - 4];
}JB_CHANNEL_MOTION_DETECT,*PJB_CHANNEL_MOTION_DETECT;

typedef struct tagJB_PRESET_CHANNEL{
	WORD	wPresetPoint1;
	WORD	wPresetPoint2;
}JB_PRESET_CHANNEL;

//̽ͷ����澯
typedef struct tagJB_SENSOR_ALARM
{
	DWORD			dwSize;
	int				nSensorID;				//̽ͷ����
	DWORD			dwSensorType;			//̽ͷ����
	char			szSensorName[32];		//̽ͷ����
	BOOL			bEnable;				//�Ƿ���в���
	int				nDuration;				//����IO�˿��������ʱ��(��)
	BOOL			bAlarmIOOut[4];			//̽ͷ�������
	JB_PRESET_CHANNEL PresetChannel[4];	//�������澯ʱ���Ƿ������̨Ԥ�õ�1����
	JB_SCHED_TIME	jbScheduleTime[8];		//����ʱ��
	BOOL			bSnapShot;				//�����澯ʱ���Ƿ�ץͼ
	int				nCaptureChannel;		//����ʱ������ץͼ������ͨ��
	BOOL			bReQuestTalkback;		//�Ƿ�����Խ�
}JB_SENSOR_ALARM,*PJB_SENSER_ALARM;

typedef struct tagJBNV_ALARM_OUT
{
    BYTE    AlarmOutDelay;                  //�澯�����ʱ
    char    reserve[3];
	char	szAlarmOutName[32];				//�澯�������
}JBNV_ALARM_OUT,*PJBNV_ALARM_OUT;

//�澯���
typedef struct tagJBNV_ALARM_OUT_INFO{
	DWORD	dwSize;
	JBNV_ALARM_OUT jbao[4];					//�澯���������̽ͷ��������������ö���
}JBNV_ALARM_OUT_INFO,*PJBNV_ALARM_OUT_INFO;

//��Ƶ��ʧ��������
typedef struct tagJB_CHANNEL_VIDEO_LOST
{
	DWORD			dwSize;
	DWORD			dwChannel;					//ͨ����
	BOOL			bEnable;					//�Ƿ���в���
	int				nDuration;					//����IO�˿��������ʱ��(��)
	BOOL	        bAlarmIOOut[4];				//����IO���
	JB_SCHED_TIME   jbScheduleTime[8];			//����ʱ���
}JB_CHANNEL_VIDEO_LOST,*PJB_CHANNEL_VIDEO_LOST;

/*--------------------------�������������ýṹ------------------------------*/
//������485�ߵ�COM����
typedef struct tagJB_SERVER_COMINFO
{
	DWORD		dwSize;
	DWORD		dwChannel;		//ͨ����
	DWORD		dwBaudRate;		//������
				/*1200,2400,4800,9600,19200,38400,43000,56000,57600,115200*/
	int			nDataBits;		//����λ
	int			nStopBits;		//ֹͣλ
	int			nParity;		//У��λ
	int			nStreamControl;	//������

    BOOL        bEanble485Out;  //0 disable,1 enable
    int         n485DeviceType; //0 ptz,1 485 Mode1,2 485 Mode2
    
    BOOL        bEnableWeiGen;  //0 disable,1 enable
    int         WeiGenType;     //0 26 ;1 34

    int			nPrePos;		//��̨Ԥ��λ
    int			nCruise;		//��̨Ѳ��
    int			nTrack;			//��̨�켣
    int			nPTZSpeed;		//��̨�ٶ�
	int			nAddress;		//��̨��ַ

    char        csReserved[64];
}JB_SERVER_COMINFO,*PJB_SERVER_COMINFO;


typedef struct tagJBNV_MOUSE_MESSAGE
{
    //��1080P����X,Y
    int x;
    int y;
    int nType;  //0,Left Down;1,Right Down;2,Left Double Down;
    int nReserved[9];
}JBNV_MOUSE_MESSAGE;

 
#pragma warning( disable :4200 )
//ֱ��ͨ��COM���շ�����
typedef struct tagJB_COM_DATA
{
	DWORD		dwSize;
	DWORD		dwChannel;
	BOOL		bIs485;					//485 or 232
	char		DataBuf[];				//���128
}JB_COM_DATA;
#pragma warning( default:4200 )

//�����ַ
typedef struct tagJB_SERVER_NETWORK
{
	DWORD		dwSize;
	DWORD		dwNetIpAddr;			//IP��ַ
	DWORD       dwNetMask;				//����
	DWORD       dwGateway;				//����
	BYTE		bEnableDHCP;			//
	BYTE		bSetDNS;
    BYTE		no_instant_effect;		//�Ƿ�������Ч
	BYTE		bVideoStandard;			//0 - NTSC, 1 - PAL
	DWORD       dwHttpPort;				//Http�˿�
	DWORD       dwDataPort;				//���ݶ˿�
	DWORD		dwDNSServer;			//DNS������
	DWORD		dwP2PStatus;			//p2p״̬			
	char        szMacAddr[6];			//����MAC��ַ
	char		szServerName[32];		//����������
}JB_SERVER_NETWORK,*PJB_SERVER_NETWORK;



//�û�����
typedef struct tagJB_SERVER_USER{
	DWORD		dwSize;
	DWORD		dwIndex;			//���5���û�����һ��Ĭ������ΪAdmin.
	BOOL		bEnable;			//�Ƿ�����
	char		csUserName[32];
	char		csPassword[32];
	DWORD		dwUserRight;		/* Ȩ�� */
									//0x01: ������̨
									//0x02: ���ò���
									//0x04: ��������ʽ��
	DWORD		dwNetPreviewRight;	//Զ�̿���Ԥ����ͨ�� bit0 -- channel 1
	DWORD		dwUserIP;			//�û�IP��ַ(Ϊ0ʱ��ʾ�����κε�ַ) 
	BYTE		byMACAddr[6];		//�����ַ
}JB_SERVER_USER,*PJB_SERVER_USER;

/* ftp�ϴ�����*/
typedef struct tagJB_FTPUPDATA_PARAM
{
	DWORD	dwSize;
	DWORD	dwEnableFTP;			/*�Ƿ�����ftp�ϴ�����*/
	char	csFTPIpAddress[32];		/*ftp ������*/
	DWORD	dwFTPPort;				/*ftp�˿�*/
	BYTE	sUserName[32];			/*�û���*/
	BYTE	sPassword[32];			/*����*/
	WORD 	wTopDirMode;			/*0x0 = ʹ���豸ip��ַ,0x1 = ʹ���豸��,0x2 = OFF*/
	WORD 	wSubDirMode;			/*0x0 = ʹ��ͨ���� ,0x1 = ʹ��ͨ����,0x2 = OFF*/
	BOOL	bAutoUpData;			//�Ƿ������Զ��ϴ�ͼƬ����
	DWORD	dwAutoTime;				//�Զ���ʱ�ϴ�ʱ��
	DWORD	dwChannel;				//Ҫ�ϴ���ͨ��
	BYTE	reservedData[16];		//����
}JB_FTPUPDATA_PARAM, *LPJB_FTPUPDATA_PARAM;

//����֪ͨ����
typedef struct tagJB_NOTIFY_SERVER
{
	DWORD		dwSize;
	BOOL		bEnable;			//�������Ƿ�ʱ����������Ϣ��Ŀ������
	DWORD		dwTimeDelay;		//����������������Ϣ�ļ��ʱ��
	DWORD		dwPort;				//���շ�����������Ϣ��Ŀ�������˿�
	char        szDNS[128];			//���շ�����������Ϣ��Ŀ����������
}JB_NOTIFY_SERVER,*PJB_NOTIFY_SERVER;

typedef struct tagJB_PPPOE_DDNS_CONFIG
{
	DWORD	dwSize;
	BOOL	bEnablePPPOE;				//0-������,1-����
	char	csPPPoEUserName[32];		//PPPoE�û���
	char	csPPPoEPassword[32];		//PPPoE����
	DWORD	dwPPPoEIP;					//PPPoE IP��ַ(ֻ��)
	BOOL	bEnableDDNS;				//�Ƿ�����DDNS
	CHAR	csDDNSUsername[32];
	CHAR	csDDNSPassword[32];
	char	csDDNSDomain[32];			//�ڷ�����ע���DDNS����
	char	csDNSAddress[32];			//DNS��������ַ
	DWORD	dwDNSPort;					//DNS�������˿ڣ�Ĭ��Ϊ6500
}JB_PPPOE_DDNS_CONFIG,*PJB_PPPOE_DDNS_CONFIG;

typedef struct tagJB_ALARM_VOICE_CONFIG{
	DWORD	dwSize;		//�ṹ��С
	WORD    wFormatTag; // DMS_PT_G711A ���̶�
	WORD    wFileSize;
	BYTE    byData[64*1024];
}JB_ALARM_VOICE_CONFIG;

//�澯�������
#define		SENSOR_OUT_1			0x0001		//̽ͷ1�����
#define		SENSOR_OUT_2			0x0002		//̽ͷ2�����
#define		SENSOR_OUT_3			0x0004		//̽ͷ3�����
#define		SENSOR_OUT_4			0x0008		//̽ͷ4�����
typedef struct tagJBNV_SENSOR_STATE{
	DWORD	dwSize;
	DWORD	dwSensorID;					//̽ͷID
	DWORD	dwSensorOut;				//̽ͷ���״̬
}JBNV_SENSOR_STATE;

typedef struct tagJBNV_VFR_MODEL_INFO{
    DWORD   dwSize;
    DWORD   dwModelCompany; //0 ���ģ�1����
    DWORD   dwModelCRC32;   //�ļ�CRCֵ
    DWORD   dwModelFileLen; //�ļ���
    char    csFileName[32];
    char    csReserved[200]; //����
}JBNV_VFR_MODEL_INFO;

typedef struct tagJBNV_VFR_MODEL_DATA{
    DWORD   dwSize;
    DWORD   dwModelCompany; //ģ���ļ��ṩ��˾
    DWORD   dwModelFileLen; //ģ���ļ��ܳ���
    DWORD   dwPackStart;    //������ļ�������λ��
    DWORD   dwPackLength;   //���η��͵����ݳ���
    DWORD   dwFileCRC;
    char    csFileName[32]; //�ļ���
}JBNV_VFR_MODEL_DATA;

enum JBNV_NetStatus{
	NetStatus_Ok,
	NetStatus_Break,
	NetStatus_Update,
};

typedef struct tagJBNV_NETWORK_STATUS{	
	JBNV_NetStatus	dwServerStatus;
	JBNV_NetStatus	dwChannelStatus[64][3];	//3����
}JBNV_NETWORK_STATUS;

typedef int	(CALLBACK *StreamCallBack)(
					HANDLE hServer,			//���������
					DWORD dwClientIndex,	//�ͻ������������ͻ��Զ���
					DWORD dwChannelNo,		//������ͨ���ţ���0��ʼ
					PBYTE pbDataBuffer,		//�ṹ����Ϊ JB_DATAPACK
					DWORD dwUser);			//�û�����

typedef void (CALLBACK *DrawOSD)(
					HDC hDC,				//�ص����صĻ�ͼDC
					SIZE *pImageSize,		//�����С
					SIZE *pDCSize,			//DC�����С
					DWORD dwUser);			//�û�����

//��Ƶ��������
#define		VIDEO_MODE_YUY2		1
#define		VIDEO_MODE_YV12		2
#define		VIDEO_MODE_UYVY		3

typedef void (CALLBACK *VideoCallBack)(
					HANDLE hHandle,
					DWORD dwVideoMode,		//��Ƶ��������
					DWORD dwWidth,			//��ǰ��Ƶ�Ŀ�
					DWORD dwHeight,			//��ǰ��Ƶ�ĸ�
					BYTE *lpData,			//��Ƶ����
					DWORD dwLineLength,		//�г�
					DWORD dwUser);			//�û�����


typedef void (CALLBACK *AudioCallBack)(
				    HANDLE hHandle,
				    DWORD dwAudioMode,		//��Ƶ��������
				    BYTE *lpData,			//��Ƶ����
				    DWORD dwDataLength,		//��Ƶ���ݳ���
					DWORD dwUser);			//�û�����


typedef void(CALLBACK *VoiceDataCallBack)(
					DWORD dwAudioFormat,	//��Ƶ��������
					BYTE *lpEncode,			//����������
					int nELength,			//���������ݳ���
					BYTE *lpPCMWave,		//PCM��Ƶ����
					int nPCMLength,			//PCM��Ƶ���ݳ���
					DWORD dwUser);			//�û�����


typedef void(CALLBACK *SnapShotCallBack)(
					HANDLE hServer,
					DWORD dwChannel,
					BYTE *bPicBuffer,
					DWORD dwPicSize,
					DWORD dwUser);

typedef void(CALLBACK *fStreamCallBackEx)(
					HANDLE hHandle,
					DWORD dwDataType,		// 0(ʵʱԤ��) :JB_DATAPACK�ṹ���� 1(�ļ��ط�):JB_STREAM_BUFFER�ṹ����
					BYTE *pBuffer,
					DWORD dwBufSize,		//pBuffer �ܳ���
					DWORD dwUser);

typedef void(CALLBACK *TestResultCallBack)(
				  HANDLE hHandle,
				  BYTE *pBuffer,
				  DWORD dwBufSize,		//pBuffer �ܳ���
				  DWORD dwUser);


DWORD WINAPI JBNV_OpenServer(LPCSTR lpServerDNS,WORD wServerPort,
				LPCSTR lpszUserName,LPCSTR lpszPassword,LPVOID *lpHandle);
DWORD WINAPI JBNV_SetHDPreviewOptim(HANDLE hServer, BOOL enable);

DWORD WINAPI JBNV_CloseServer(HANDLE hServer);		//�رշ�����
DWORD WINAPI JBNV_GetServerInfo(HANDLE hServer,JBNV_SERVER_INFO *lpsi);	//��ȡ��������Ϣ
DWORD WINAPI JBNV_SetMessage(HANDLE hServer,HWND hMsgWnd,UINT nMessage);//������Ϣ�ص�
DWORD WINAPI JBNV_SetStreamCallBack(HANDLE hServer,StreamCallBack lpscb,DWORD dwUser);//�����������ص�
DWORD WINAPI JBNV_SetSecondSurface(HANDLE hServer,DWORD dwChannelNo,HWND hDisPlayWnd,DrawOSD pOSD,DWORD dwUser, DWORD dwStreamType);

DWORD WINAPI JBNV_UnSetSecondSurface(HANDLE hServer,DWORD dwChannelNo,HWND hDisPlayWnd,DWORD dwStreamType);

DWORD WINAPI JBNV_PTZControl(HANDLE hServer,DWORD dwChannelNo,DWORD dwPTZCmd,DWORD dwValue);// ��̨����
DWORD WINAPI JBNV_PTZControlEx(HANDLE hServer,DWORD dwChannelNo,DWORD dwPTZCmd,DWORD dwSpeed,DWORD dwValue);// ��̨���� dwSpeed�ֶ�δʹ��
DWORD WINAPI JBNV_SetServerConfig(HANDLE hServer,DWORD dwCmd,LPVOID lpData,DWORD dwSize);// ���÷���������
DWORD WINAPI JBNV_GetServerConfig(HANDLE hServer,DWORD dwCmd,LPVOID lpData,DWORD dwSize);// ��ȡ����������
DWORD WINAPI JBNV_GetChannelInfo(HANDLE hServer,DWORD dwChannelNo,JBNV_CHANNEL_INFO *lpStreamInfo);//�õ�����Ϣ
DWORD WINAPI JBNV_GetSensorInfo(HANDLE hServer,DWORD dwSensorID,	//����Ϊ 0,1,...,15,���Ϊ16,17,...31
								JBNV_SENSOR_INFO *lpSensor);
DWORD WINAPI JBNV_UpdateServer(HANDLE hServer,LPCSTR lpszFileName);
DWORD WINAPI JBNV_SetTestCommand(HANDLE hServer,DWORD dwCmd,LPVOID lpData,DWORD dwSize);// �����Զ���������
DWORD WINAPI JBNV_SetTestResultCallBack(HANDLE hServer,TestResultCallBack pTestResult,DWORD dwUser);// ���ò��Խ�����ջص�

DWORD WINAPI JBNV_GetServerNetStatus(HANDLE hServer,JBNV_NETWORK_STATUS *lpStatus);

DWORD WINAPI JBNV_GetChannelNetStatus(HANDLE hChannel,JBNV_NetStatus *lpStatus);
//Ԥ����������
DWORD WINAPI JBNV_OpenChannel(HANDLE hServer,DWORD dwChannelNo,//��������ͨ��
				DWORD dwClientIndex,	//�ͻ������������ͻ��Զ���
				DWORD dwNetProtocol,	//����Э��
				DWORD dwStreamType,		//�������ͣ�����������С����
				HWND  hDispWnd,			//��ʾ����
				BOOL  bUserDecode,		//�ͻ��Լ�����
				DWORD dwShowMode,		//��ʾģʽ��0ΪOVERLAY��ʾģʽ��1Ϊ��OVERLAY��ʾģʽ��
				LPVOID *lpHandle);		//����ͨ���ɹ���lpHandle��������ͨ�����
DWORD WINAPI JBNV_CloseChannel(HANDLE hChannel);
DWORD WINAPI JBNV_GetRecvCount(HANDLE hChannel,DWORD *pdwRecvCount);//�õ��������ݽ�����
DWORD WINAPI JBNV_GetSafePlayer(HANDLE hChannel,HANDLE *lphPlayer);

#define LANGID_EN_US		MAKELANGID(LANG_ENGLISH,SUBLANG_DEFAULT)
#define	LANGID_CH			0x00000804
#define LANGID_CHTW			0x00000404
//�ֽ�֧�����ĺ�Ӣ�ģ�0��0x0804Ϊ���ģ�1��LANGID_EN_USΪӢ��
DWORD WINAPI JBNV_GetErrorMessage(DWORD dwErrorID,
								  LPSTR lpBuffer,		// message buffer
								  DWORD nSize,			// maximum size of message buffer
								  DWORD dwLanguageId);	// language identifier 0x0 China,

DWORD WINAPI JBNV_Mute(HANDLE hChannel,BOOL bMute);		//��������
DWORD WINAPI JBNV_SetVolume(HANDLE hChannel,DWORD dwValume);
//���ز�׽ͼ�󣬵�����������ʱ������ʹ�ô˺�����׽���һ֡��ͼ�����ݡ����ΪBMPͼƬ���ݣ�����ֱ�ӱ���
DWORD WINAPI JBNV_CaptureBitmap(HANDLE hChannel,BYTE *in_Buffer,DWORD *nSize);	
//��ȡ�����ñ��ز��Ż���
DWORD WINAPI JBNV_GetStreamBufferSize(HANDLE hChannel,DWORD *lpMin,DWORD *lpMax,DWORD *lpCurrent);	
DWORD WINAPI JBNV_SetStreamBufferSize(HANDLE hChannel,DWORD dwMin,DWORD dwMax);
//������ʾ����
DWORD WINAPI JBNV_SetDisplayRect(HANDLE hChannel,RECT *lpRect);
//����ͼƬ
DWORD WINAPI JBNV_UpdataImage(HANDLE hChannel,RECT *lpRect);
//����OSD�ص�������ͨ���˻ص��ڻ�����ʵ�ֻ��߻���������ȹ���
DWORD WINAPI JBNV_SetOSDCallback(HANDLE hChannel,DrawOSD pOSD,DWORD dwUser);
//������ʾ����
DWORD WINAPI JBNV_SetDisplayhWnd(HANDLE hChannel,HWND hDisplayWnd);

//������ʾ�Ƿ���Ƶ�������е���
DWORD WINAPI JBNV_ShowToScale(HANDLE hChannel,BOOL bEnable);

//������Ƶ���ݻص����ص�������ΪYUV422
DWORD WINAPI JBNV_SetVideoCallback(HANDLE hChannel,VideoCallBack pvideocallback,DWORD dwUser);

//������Ƶ�Ƿ��͵����������н��룬��������ʾ��ʱ�򣬲��ٷ��͵�������
//���Խ���CPU��Դռ��
DWORD WINAPI JBNV_SetVideoStatic(HANDLE hChannel,BOOL bShowVideo);
 

DWORD WINAPI JBNV_SetStreamCallBackEx(HANDLE hChannel,fStreamCallBackEx cbStreamCallBackEx,DWORD dwUser);//����ͨ�������ص�

//¼���������
//����Ԥ¼��ʱ�䳤�ȣ��60��
DWORD WINAPI JBNV_SetPreRecord(HANDLE hChannel,DWORD dwSeconds);
DWORD WINAPI JBNV_StartRecord(HANDLE hChannel,LPCSTR lpszFile,
							DWORD dwFileType);	//0 ΪASF���ֽ�֧��1�ָ�ʽ
DWORD WINAPI JBNV_GetRecorded(HANDLE hChannel,DWORD *lpdwWrited);
DWORD WINAPI JBNV_StopRecord(HANDLE hChannel);
DWORD WINAPI JBNV_StartAlarmRecord(HANDLE hChannel,LPCSTR lpszFile,	DWORD dwFileType);
DWORD WINAPI JBNV_StopAlarmRecord(HANDLE hChannel);

//�Խ�
DWORD WINAPI JBNV_TalkOpen(LPCSTR lpszServerIP,WORD wServerPort);
DWORD WINAPI JBNV_TalkOpenEx(HANDLE hServer, LPCSTR lpszServerIP,WORD wServerPort);
DWORD WINAPI JBNV_TalkWith(LPCSTR lpServerA,WORD wServerPortA,LPCSTR lpServerB,WORD wServerPortB,BOOL bBreak);
//����ָ��������������
DWORD WINAPI JBNV_TalkListen(LPCSTR lpServer,WORD nServerPort);
DWORD WINAPI JBNV_TalkClose();
DWORD WINAPI JBNV_TalkStartRecord(LPCSTR lpszFileName);
DWORD WINAPI JBNV_TalkStopRecord();


/*��Ƶ�Խ�͸������*/
DWORD WINAPI JBNV_StartVoiceCom(LPCSTR lpszServerIP,WORD wServerPort, VoiceDataCallBack lpVideoData, DWORD dwUser, LONG *lpHandle);
DWORD WINAPI JBNV_StopVoiceCom();
DWORD WINAPI JBNV_VoiceComSendData (LONG  lVoiceComHandle, int nVoiceType, char  *pSendBuf, DWORD  dwBufSize);

/*Զ��ץ��*/
DWORD WINAPI JBNV_SnapShotCallBack(HANDLE hServer, SnapShotCallBack lpSnapShotData, DWORD dwUser);
DWORD WINAPI JBNV_CapturePicture(HANDLE hServer,DWORD dwChannel,LPCSTR lpPicFileName,BYTE *bPicBuffer,LPDWORD lpSizeReturned);
DWORD WINAPI JBNV_Capture(HANDLE hChannel,LPCSTR lpPicFileName);

DWORD WINAPI JBNV_SetConnectTime(DWORD dwWaitTime, DWORD dwTryTimes);		//dwWaitTime��λ���룬ȡֵ��Χ[3000,75000]
DWORD WINAPI JBNV_SetReconnect(DWORD dwInterval,BOOL bEnableRecon = FALSE);	//dwInterval�����������λ:���� [30*1000,X]

//��������
typedef struct tagJBNV_SERVER_PACK
{
	char	szIp[16];			//������Ip
	WORD	wMediaPort;			//���˿�
	WORD	wWebPort;			//Http�˿ں�
	WORD	wChannelCount;		//ͨ������
	char	szServerName[32];	//��������
    WORD    wReserved1;
	DWORD	dwDeviceType;		//����������
	DWORD	dwServerVersion;	//�������汾
	WORD	wReserved2;		    //wChannelStatic ͨ��״̬(�Ƿ���Ƶ��ʧ)
	WORD	wSensorStatic;		//̽ͷ״̬
	WORD	wAlarmOutStatic;	//�������״̬
    WORD    wReserved3;
    BYTE	bMac[6];
    WORD    wReserved4;
    BOOL	bEnableDHCP;	
    BOOL	bEnableDNS;
    DWORD	dwNetMask;
    DWORD	dwGateway;
    DWORD	dwDNS;
    DWORD	dwComputerIP;	
	DWORD	dwSupportFunc;

	DWORD   bP2PStatus; //Old Name:dwCenterIpAddress
	WORD    wStreamWidth;//Old Name:dwCenterPort
    WORD    wStreamHeight;
    char    csP2Pid[52]; //Old Name:csServerNo
    DWORD   ipAutoStatus;//IP��ַ����Ӧ״̬
    WORD    wSubStreamW;
    WORD    wSubStreamH;
    WORD    wMainStreamType;//2 - H264,8 H265,
    WORD    wSubStreamType; //2 - H264,8 H265,
    int     bEncodeAudio;
	char    csCenterIpAddress[64];
}JBNV_SERVER_PACK;

 
 
typedef struct tagJBNV_SERVER_MSG_DATA_EX
{
	DWORD					dwSize;
	DWORD					dwPackFlag; // == SERVER_PACK_FLAG
	JBNV_SERVER_PACK		jbServerPack;
}JBNV_SERVER_MSG_DATA;

typedef struct tagJBNV_MC_PACK{
	DWORD	dwFlag;
	DWORD	dwServerIpaddr;
	WORD	wServerPort;
	WORD	wBufSize;
	DWORD	dwCommand;
	DWORD	dwChannel;
}JBNV_MC_PACK;


DWORD WINAPI JBNV_SearchServer(HWND hWnd,DWORD dwMsg);
DWORD WINAPI JBNV_ModifyNewWork(JB_SERVER_NETWORK* pServerMsgData, BOOL bManualModify);
DWORD WINAPI JBNV_SetAlarmRecv(HWND hWnd,DWORD dwMsg,WORD wPort);

//��������
//��������ļ���Ϣ
DWORD WINAPI JBNV_GetUpgradeFileInfo(HANDLE hServer,LPCSTR lpFile,DWORD *lpFileVer,DWORD *lpFileLen,LPSTR lpDes);
DWORD WINAPI GetDataCRC (LPVOID lpData,DWORD dwSize);		//�������CRC32ֵ������ֵΪCRCֵ
DWORD WINAPI GetWindowsMacInfo(BYTE *lpMac,DWORD *lpdwSize);//��õ�ǰ�������MAC��ַ
DWORD WINAPI GetWindowsIpAddressInfo(DWORD *lpIpAddress,DWORD *lpdwSize);//��õ�ǰ�������IP��ַ�б�
//֡ͷ�ṹ
typedef struct tagJB_FRAME_HEADER
{
	WORD	wMotionDetect;			//�˶���
	WORD	wFrameIndex;			//֡����
	DWORD	nVideoSize;				//��Ƶ��С
	DWORD	nTimeTick;				//ʱ���
	WORD	nAudioSize;				//��Ƶ��С
	BYTE	bKeyFrame;				//�Ƿ�ؼ�֡
	BYTE	nPackIndex;				//������
}JB_FRAME_HEADER,*PJB_FRAME_HEADER;

#define MAX_STREAM_BUFF_SIZE (1024 * 1000) // 500 *1024

typedef struct tagJB_FRAME_DATA
{
	JB_FRAME_HEADER		jbFrameHeader;
	BYTE				*lpStreamData;
	DWORD				dwStreamSize;	//MAX_STREAM_BUFF_SIZE
}JB_FRAME_DATA,*PJB_FRAME_DATA;

#define JB_PACKDATA_SIZE	(32 * 1024)
typedef struct tagJB_DATAPACK
{
	WORD				IsSampleHead;
	WORD				BufSize;			// Buf ���ж��ٿ���
	JB_FRAME_HEADER		jbFrameHeader;
	BYTE				PackData[JB_PACKDATA_SIZE];
}JB_DATAPACK, *PJB_DATAPACK;

//��������
#define		JB_PLAY_CMD_PLAY			1
#define		JB_PLAY_CMD_PLAYPREV		2
#define		JB_PLAY_CMD_STEPIN			3
#define		JB_PLAY_CMD_STEPOUT			4
#define		JB_PLAY_CMD_PAUSE			5
#define		JB_PLAY_CMD_RESUME			6
#define		JB_PLAY_CMD_FASTPLAY		7
#define		JB_PLAY_CMD_FASTBACK		8
#define		JB_PLAY_CMD_STOP			9
#define		JB_PLAY_CMD_SLOWPLAY		10

#define		JB_PLAY_CMD_FIRST			11			/*��λ���ļ�ͷ*/
#define		JB_PLAY_CMD_LAST			12			/*��λ���ļ�ĩβ*/
#define		JB_PLAY_CMD_SEEK			13			/*��λ����*/

#define		JB_PLAY_CMD_SOUND			14

#define		VIDEO_FORMAT_MPEG4		0
#define		VIDEO_FORMAT_H264		1
#define		VIDEO_FORMAT_MP4A		2

enum
{
	DOWNLOAD_WAITING,		// �ȴ�����
	DOWNLOAD_DOING,			// ��������
	DOWNLOAD_COMPLETE,		// �������
};

typedef struct tagJB_STREAM_PLAY_INFO{
	DWORD	dwPlayState;		//����״̬
	DWORD	dwTimeLength;		//����ʱ�䳤���룩
	DWORD	dwPlayedTime;		//�Ѳ���ʱ��
	DWORD	dwImageWidth;
	DWORD	dwImageHeight;
	DWORD	dwFileLength;		// 2010-11-25���ļ��ܳ��ȣ����ֽ���
	DWORD	dwVideoCode;
	DWORD	dwAudioCode;
	BOOL	m_bAudioPlay;		//�Ƿ񲥷���Ƶ
	BOOL	m_bLoopPlay;		//�Ƿ�ѭ������
	DWORD	dwDownloadTime;		//�����ص�ʱ��	// 2010-11-25�����¶���Ϊ�����ص��ֽ���
	DWORD	dwDownloadStatus;	//����״̬		0 �ȴ�����	1 ��������	2 �������
}JB_STREAM_PLAY_INFO,*PJB_STREAM_PLAY_INFO;

DWORD WINAPI JBPlay_OpenFile(LPCSTR lpFile,DWORD dwFileNumber,HWND hVideoWnd,BOOL bUseOverlay,HANDLE *lpHandle);
DWORD WINAPI JBPlay_OpenStream(DWORD dwVideoFormat,HWND hVideoWnd,BOOL bUseOverlay,HANDLE *lpHandle);
DWORD WINAPI JBPlay_OpenStreamEx(DWORD dwVideoFormat,HWND hVideoWnd,BOOL bUseOverlay,int nVideoWidth,int nVideoHeight,HANDLE *lpHandle);
DWORD WINAPI JBPlay_PlayCommand(HANDLE hPlayer,DWORD dwPlayCmd);
DWORD WINAPI JBPlay_PlayCommandEx(HANDLE hPlayer,DWORD dwPlayCmd,DWORD dwValue);
DWORD WINAPI JBPlay_GetPlayInfo(HANDLE hPlayer,JB_STREAM_PLAY_INFO *lpInfo);
DWORD WINAPI JBPlay_SetAudio(HANDLE hPlayer,BOOL bEnabled);
DWORD WINAPI JBPlay_UpdateBound(HANDLE hPlayer);
DWORD WINAPI JBPlay_SetDisplayRect(HANDLE hPlayer,RECT *Rect);
DWORD WINAPI JBPlay_SetDisplayWnd(HANDLE hPlayer,HWND hDisplayWnd);
DWORD WINAPI JBPlay_SetOSDCallback(HANDLE hPlayer,DrawOSD pOSD,DWORD dwUser);
DWORD WINAPI JBPlay_SetVideoCallback(HANDLE hPlayer,VideoCallBack pvideocallback,DWORD dwUser);
DWORD WINAPI JBPlay_SetVolume(HANDLE hPlayer,DWORD dwValume);
DWORD WINAPI JBPlay_CapturePicture(HANDLE hPlayer,LPCSTR lpFile);
DWORD WINAPI JBPlay_SetImagePos(HANDLE hPlayer,RECT *lprc);

DWORD WINAPI JBPlay_SetSecondSurface(HANDLE hPlayer,HWND hVideoWnd,DrawOSD pOSD,DWORD dwUser);

DWORD WINAPI JBPlay_Release(HANDLE hPlayer);

//�����ĸ�����������ļ�����
DWORD WINAPI JBPlay_SeekToSecond(HANDLE hPlayer,DWORD dwSecond);
DWORD WINAPI JBPlay_SetPlayLoop(HANDLE hPlayer,BOOL m_bLoopPlay);
DWORD WINAPI JBPlay_SaveStreamData(HANDLE hPlayer,DWORD dwSaveFormat,DWORD dwStartSecond,DWORD dwEndSecond,LPCSTR lpFileName);
DWORD WINAPI JBPlay_SetMessage(HANDLE hPlayer,HWND hMsgWnd,DWORD dwMessageID);

//�����������������������
DWORD WINAPI JBPlay_InputDataPack(HANDLE hPlayer,JB_DATAPACK *lpData);
DWORD WINAPI JBPlay_InputFrame(HANDLE hPlayer,JB_FRAME_DATA *lpFrame);
DWORD WINAPI JBPlay_SetAudioFormat(HANDLE hPlayer,WAVEFORMATEX *lpwfx);
DWORD WINAPI JBPlay_StartRecord(HANDLE hPlayer,LPCSTR lpszFile,DWORD dwFileType);
DWORD WINAPI JBPlay_GetRecorded(HANDLE hPlayer,DWORD *lpdwWrited);
DWORD WINAPI JBPlay_StopRecord(HANDLE hPlayer);

DWORD WINAPI JBPlay_SetStreamBufferSize(HANDLE hPlayer,DWORD dwMin,DWORD dwMax);

DWORD WINAPI JBPlay_SetAudioCallBack(HANDLE hPlayer,BOOL bDecode, AudioCallBack pAudioCallback,DWORD dwUser);

DWORD WINAPI JBPlay_SetStreamCallback(HANDLE hPlayer,fStreamCallBackEx pStreamCallBackEx,DWORD dwUser);

//Add 2007-08-30

//¼������
typedef struct tagJB_SERVER_RECORD_SET{
	DWORD	dwSize;
	DWORD	dwLocalRecordMode;			//¼��ģʽ��0 ��¼��1��ȫʵʱ¼��2����ʵʱ¼��3���澯¼��
	BOOL	bAutoDeleteFile;			//�Ƿ��Զ�ɾ���ļ�
}JB_SERVER_RECORD_SET;


typedef struct tagJB_SERVER_RECORD_CONFIG{
	DWORD	dwSize;
	BOOL	bTimeControl;		
	BOOL	bSizeControl;		
	DWORD	dwRecordTime;		
	DWORD	dwRecordSize;	
}JB_SERVER_RECORD_CONFIG;

//¼��״̬
typedef struct tagJB_SERVER_RECORD_STATE{
	DWORD	dwSize;
	DWORD	dwChannelRecordState;		//��ǰͨ��¼��״̬
	DWORD	dwServerSpace;				//��MΪ��λ
	DWORD	dwSpaceFree;				//���ɿռ�
}JB_SERVER_RECORD_STATE;


//Add 2007-09-17
typedef struct tagJB_CENTER_INFO{
	DWORD	dwSize;
	BOOL	bEnable;
	DWORD	dwCenterIp;					//����IP
	DWORD	dwCenterPort;				//���Ķ˿�
	char	csServerNo[64];				//���������к�
}JB_CENTER_INFO;

typedef struct tagJB_CENTER_INFO_EX{
	DWORD dwSize;
	char  csCenterid[32];
	char  csUsername[32];
	char  csUserpass[32];
	char csReserver[64];
}JBNV_NXSIGHT_SERVER_ADDR_EX;

typedef struct tagJB_CENTER_INFO_V2{
	DWORD	dwSize;
	BOOL	bEnable;
	DWORD	dwCenterIp; //�����ã�Ϊ��֮ǰ�汾���ݹʱ�����
	DWORD	dwCenterPort;
	char	csServerNo[64];
	char	csCenterIP[64];
}JBNV_NXSIGHT_SERVER_ADDR_V2;


//Add 2007-10-25 ����������
//��������Ϣ����
/************************************************************************/
/*	������Ƶ��������������												*/
/************************************************************************/

#define		CMD_NVD_ALONE_SET_CHANNELINFO	0x01000001		//���õ�·������Ϣ��	���Ӳ���:DVS_DECODER_CHANNEL_INFO
#define		CMD_NVD_ALONE_STOP				0x01000002		//ֹͣ��·����
#define		CMD_NVD_ALONE_START				0x01000003		//��ʼ��·����
#define		CMD_NVD_CYCLE_STOP				0x01000004		//ֹͣѭ��
#define		CMD_NVD_CYCLE_START				0x01000005		//��ʼѭ��
#define		CMD_NVD_CYCLE_SET_INFO			0x01000006		//����ѭ��������Ϣ
#define		CMD_NVD_AUDIO_SET				0x01000007		//������Ƶ���أ�		���Ӳ���:int
#define		CMD_NVD_VIDEO_MODE_SET			0x01000008		//������Ƶ�����ʽ		���Ӳ���:int
#define		CMD_NVD_TALK_BACK_SET			0x01000009		//���öԽ�����			���Ӳ���:int
#define		CMD_NVD_LANGUAGE_SET			0x0100000A		//��������				���Ӳ���:int
#define		CMD_NVD_SET_SYSTEM				0x0100000B		//ϵͳ����
#define		CMD_NVD_SET_NETWORK				0x0100000C		//��������
#define		CMD_NVD_ALONE_AUTO_CON_SET		0x0100000D		//���õ�·�Զ�����		���Ӳ���:int
#define		CMD_NVD_CYCLE_AUTO_CON_SET		0x0100000E		//����ѭ���Զ�����		���Ӳ���:int
#define		CMD_NVD_MENU_SET				0x0100000F		//���ò˵�				���Ӳ���:int
#define		CMD_NVD_SET_SENSOR_ALARM_INFO	0x01000020		//���ø澯���			���Ӳ���:DVS_DECODER_SENSOR_ALARM_INFO
#define		CMD_NVD_SET_SENSOR_STATE		0x01000021		//����̽ͷ״̬

#define		CMD_NVD_SET_COM485				0x01000022		//����485����			���Ӳ���:JB_NVD_COM485_SET
#define		CMD_NVD_SET_BUFFER				0x01000023		//���ò��Ż���
#define		CMD_NVD_SET_AUDIO_CHANNEL		0x01000024		//���ý�����Ƶͨ��

#define		CMD_NVD_CYCLE_GET_INFO			0x02000000		//���ѭ��������Ϣ
#define		CMD_NVD_ALONE_GET_CHANNELINFO	0x02000001		//��ȡ��ǰ���Ӳ���		���Ӳ���:DVS_DECODER_CHANNEL_INFO
#define		CMD_NVD_GET_NETWORK				0x02000002		//��ȡ����
#define		CMD_NVD_GET_SERVER_STATE		0x02000003		//��������ǰ״̬		���Ӳ���:DVS_DECODER_SERVER_INFO
#define		CMD_NVD_GET_SYSTEM				0x02000004		//��ȡϵͳ����
#define		CMD_NVD_GET_SENSOR_ALARM_INFO	0x02000005		//��ø澯�������		���Ӳ���:DVS_DECODER_SENSOR_ALARM_INFO
#define		CMD_NVD_GET_SENSOR_STATE		0x02000006		//���̽ͷ״̬

#define		CMD_NVD_GET_COM485				0x02000007		//���485����			���Ӳ���:JB_NVD_COM485_SET
#define		CMD_NVD_GET_BUFFER				0x02000008		//��ò��Ż���
#define		CMD_NVD_GET_AUDIO_CHANNEL		0x02000009		//���ý�����Ƶͨ��
/************************************************************************/
/* �������ýṹ                                                         */
/************************************************************************/

typedef enum {
	nvd_nowork = 0,
	nvd_alone,
	nvd_cycle,
}NVD_CUR_STATE;

typedef enum {
	nvd_menu_Hide = 0,
	nvd_menu_Show,
	nvd_menu_Lock,
	nvd_menu_UnLock,
}NVD_MENU_STATE;

typedef struct tagNVD_DECODER_PARAM{
	BOOL			bAudioOpen;		//��Ƶ�Ƿ��Ѿ���
	DWORD			dwVideoMode;	//0ΪPAL,1ΪNTSC
	DWORD			dwLanguage;		//����
	DWORD			bAloneAutoCon;	//�Ƿ�·�Զ�����
	DWORD			bCycleAutoCon;	//ѭ�������Զ�����
}NVD_DECODER_PARAM,*PNVD_DECODER_PARAM;

//������ϵͳ��Ϣ
typedef struct tagNVD_DECODER_SERVER_INFO
{
	NVD_CUR_STATE	ServerState;	//������״̬
	BOOL			bAudioOpen;		//��Ƶ�Ƿ��Ѿ���
	DWORD			bTalkback;		//�Ƿ��ڶԽ�
	DWORD			dwVideoMode;	//1ΪNTSC��0ΪPAL
	DWORD			dwLanguage;		//����
	/*
	DWORD			bAloneAutoCon;	//�Ƿ�·�Զ�����
	DWORD			bCycleAutoCon;	//ѭ�������Զ�����
	*/
	BOOL			bAloneAutoCon;	//�Ƿ�·�Զ�����
	BOOL			bCycleAutoCon;	//ѭ�������Զ�����
}NVD_DECODER_SERVER_INFO;

typedef struct tagNVD_DECODER_NETWORK_INFO
{
	DWORD			dwServerIp;
	DWORD			dwServerMask;
	DWORD			dwGateway;
	DWORD			dwDNS;
	DWORD			dwServerPort;
}NVD_DECODER_NETWORK_INFO;

typedef struct tagNVD_DECODER_SYSTEM_SET
{
	DWORD			DeviceNo;		//�豸��
	DWORD			dwMenuliveTime;	//�˵�����ʱ��
}NVD_DECODER_SYSTEM_SET;

typedef struct tagNVD_DECODER_SENSOR_ALARM_INFO
{
	BYTE			bEnableAlarm;		//�Ƿ�ʹ��
	BYTE			dwSensitive;		//������
	WORD			dwKeepTime;			//����ʱ��
	DWORD			dwSensorOut[4];		//̽ͷ�澯���
	DWORD			dwMontionDec;		//��Ƶ�ƶ��澯���
	DWORD			dwVideoLost;		//��Ƶ��ʧ�澯���
}NVD_DECODER_SENSOR_ALARM_INFO;

//������ͨ��������Ϣ
typedef struct tagNVD_DECODER_CHANNEL_INFO
{ /*
	BYTE   bChannelIndex;			//ͨ��ID����������Ҫ�����·��Ƶʱ��Ҫ�˲���
	BYTE   nChannel;				//Ҫ���ӵķ�����ͨ��
	WORD   nProt;					//�˿�
	DWORD  dwNetPoc;				//����Э��
	DWORD  bConnectMode;			//���ӷ�ʽ����IP�������� 0 Ϊ IP
	DWORD  dwIpaddress;				//Ip ��ַ	
	char   szChannelName[16];		//ͨ������
	char   szUserName[24];			//�û���
	char   szPassword[24];			//����
    char   DomainAddress[128];		//����
	*/

	
	WORD	bEnable;	         	//�Ƿ����
	WORD	nDelayTime;             //ͣ��ʱ��
	BYTE   	bIndexChannel;		    //ͨ���±�
	BYTE   	nChannel;               //ͨ��
	WORD   	nProt;                  //�˿�
	DWORD	ConnectProtocol;		// 0 TCP 1 UDP 2 MultiBrocast 
	DWORD   AddressType;            //address type 0x00 IP address  0x01 domemain
	DWORD   IPAddress; 		        //ip��ַ    
	char   	szChannelName[16];      //ͨ������
	char   	szUserName[24];         //�û���
	char   	szPassword[24];		    //�û�����						
	char   	DomainAddress[128];     //����
}NVD_DECODER_CHANNEL_INFO, *PNVD_DECODER_CHANNEL_INFO;

typedef struct tagJB_NVD_COM485_SET{
	DWORD		dwSize;
	DWORD		dwBaudRate;		//������
	int			nDataBits;		//����λ
	int			nStopBits;		//ֹͣλ
	int			nParity;		//У��λ
	int			nStreamControl;	//������
	BOOL		bTransferState;	//͸������
	DWORD		dwReserve[4];	//����
}JB_NVD_COM485_SET;

typedef struct tagNVD_SNAP_IMAGE{
	BOOL	bEnable;
	DWORD	dwChannel;
	DWORD	dwSnapMode;
	DWORD	dwSnapNum;
	DWORD	dwIntervalTime;
}NVD_SNAP_IMAGE;

DWORD WINAPI JBNV_SendStreamToNVD(HANDLE hServer,int nChannel,JB_DATAPACK *lpData);
DWORD WINAPI JBNV_SendStreamToNVDx(HANDLE hServer,int nChannel,JB_FRAME_DATA *lpFrame);

//Add 2008-01-14
//ͨ���澯��������
typedef struct tagJB_CHANNEL_ALARM_CONFIG
{
	DWORD	dwSize;
	DWORD	dwChannel;			//ͨ����
	BOOL	bEnable;
	DWORD	nFrameRate;			//֡�� (1-25/30) PALΪ25��NTSCΪ30
	DWORD	dwRateType;			//��ģʽ(0Ϊ��������1Ϊ������)
	DWORD	dwStreamFormat;		//��ʽ (0ΪCIF,1ΪD1,2ΪHALF-D1,3ΪQCIF)
	DWORD	dwBitRate;			//���� (16000-4096000)
	DWORD	dwImageQuality;		//��������(0-4),0Ϊ���
	DWORD	nMaxKeyInterval;	//�ؼ�֡���(1-100)
	BOOL	bEncodeAudio;		//�Ƿ������Ƶ
}JB_CHANNEL_ALARM_CONFIG,*LPJB_CHANNEL_ALARM_CONFIG;

//Add 2008-05-14
typedef struct tagJBNV_EMAIL_PARAM
{
	DWORD	dwSize;
	BOOL	bEnableEmail;
	BOOL	bAttachPicture;
	char	csEmailServer[64];
	char	csEMailUser[32];
	char	csEmailPass[32];
	char	csEmailFrom[64];
	char	csEmailTo[128];
	char	csEmailCopy[128];
	char	csEmailBCopy[128];
	char	csReserved[32];
}JBNV_EMAIL_PARAM, *PJBNV_EMAIL_PARAM;

//Add 2008-07-07
typedef struct tagJBNV_SERVER_COMMODE{
	DWORD dwSize;
	DWORD dwChannel;
	DWORD dwComMode;		//0 WriteOnly; 1 ReadOnly ; 2 Read after Write.
	DWORD dwInterval;
	DWORD dwReserved[4];	//����
}JBNV_SERVER_COMMODE;

typedef struct tagJBNV_3322DDNS_CONFIG
{
	DWORD	dwSize;
	BOOL	bEnableDDNS;			//0-������,1-����
	char	csDDNSUserName[32];		//�û���
	char	csDDNSPassword[32];		//����
	char	csDNSDomain[64];		//DDNS����
	int		updateTime;             //ˢ��������ʱ��
	char	reserved[32];           //����
}JBNV_3322DDNS_CONFIG,*PJBNV_3322DDNS_CONFIG;
/*
typedef enum
{
    DDNS_ZK = 0,
    DDNS_3322,
    DDNS_SELF,
    DDNS_DYDNS
}e_ddns_t;
*/

typedef struct
{
	DWORD	dwSize;
	BYTE byEnableDDNS;
	BYTE byDdnsType;
	char resv[2];
	char	csDDNSUserName[32];		
	char	csDDNSPassword[32];		
	char	csDNSDomain[64];		
	int	updateTime;
    DWORD dwIsMaped;
	char	reserved[28];
}JB_DDNS_CONFIG,*PJB_DDNS_CONFIG;

DWORD JBNV_TalkStartRecordEx(LPCSTR lpServer, WORD wServerPort,LPCSTR lpFile);
DWORD JBNV_TalkStopRecordEx(LPCSTR lpServer, WORD wServerPort);


typedef struct tagJBNV_TRANSMIT_ITEM{
	char	csServerDNS[64];	//��������ַ
	DWORD	dwServerPort;		//�������˿�
	BOOL	bEnableSetup;		//�������Ƿ�����ת����������
	DWORD	dwTransMitChannel;	//������Ҫת����ͨ����-1Ϊ����ͨ��
				//0x0001 Ϊͨ��1��0x0002Ϊͨ��2��0x0004Ϊͨ��3��0x0008Ϊͨ��4
}JBNV_TRANSMIT_ITEM;

typedef struct tagJBNV_TRANSMIT_VERIFY{
	char	csUserName[32];
	char	csPassword[32];
	DWORD	dwPreviewCount;		//���û�����������û��ܹ����ķ�����������-1Ϊ���з�����
	JBNV_TRANSMIT_ITEM *lpItem; //���û��ܹ����ķ��������б�
}JBNV_TRANSMIT_VERIFY;

typedef struct tagJBNV_CONNECT_LIST{
	char	csUserName[32];			//����ʹ�õ��û���
	DWORD	dwPriviewChannel;		//���ڿ���ͼ��
	DWORD	dwRemoteIPAddress;		//����ʹ�õ�IP��ַ
	DWORD	dwRemotePort;			//����ʹ�õĶ˿�
	DWORD	dwDataTransMit;			//ת����������,��λK Bit
	tagJBNV_CONNECT_LIST *lpNext;
}JBNV_CONNECT_LIST;

//��ʼ����ת������,���ͻ��������������ݺͶϿ��Ȳ�������������
//�ᷢ����Ϣ��Ӧ�ó���Ӧ�ó�����Խ��б�����־�ȹ���
DWORD WINAPI JBNV_TM_StartServer(HWND hMessageWnd,DWORD dwMessage,WORD wServerPort,HANDLE *lpHandle);
//�����û�������У����Ϣ,��������ô˽ӿڣ�Ĭ��ʹ��admin����
//�û��������飬��������û����йۿ�������Ȩ��
DWORD WINAPI JBNV_TM_SetVerifyInfo(HANDLE hServer,JBNV_TRANSMIT_VERIFY *lpVerify);
//������ת������Ƶ�������б�
DWORD WINAPI JBNV_TM_InsertItem(HANDLE hServer,JBNV_TRANSMIT_ITEM *lpItem);
//��������ϵ��û��б�
DWORD WINAPI JBNV_TM_GetConnectList(HANDLE hServer,JBNV_CONNECT_LIST *lpConnectList);
//ֹͣת������
DWORD WINAPI JBNV_TM_CloseServer(HANDLE hServer);

typedef struct tagJBNV_SERVER_ITEM{
	char	csServerDNS[64];
	DWORD	dwServerPort;
	char	csUserName[32];
	char	csPassword[32];
}JBNV_SERVER_ITEM;

DWORD WINAPI JBNV_OpenServerByTransMit(JBNV_SERVER_ITEM *lpTMServer,//ת��������
	JBNV_SERVER_ITEM *lpServer,	/*��Ҫ���ӵķ�����*/LPVOID *lpHandle);
DWORD WINAPI JBNV_TM_OpenServer(JBNV_SERVER_ITEM *lpTMServer,LPVOID *lpHandle);
DWORD WINAPI JBNV_TM_GetServerList(HANDLE hTMServer,JBNV_SERVER_ITEM *lpServer,DWORD *lpdwServerCount);
DWORD WINAPI JBNV_TM_CloseHandle(HANDLE hTMServer);

//Add 2008-07-28
typedef struct tagJBNV_DIRECTORY_LIST{
	DWORD	dwSize;
	char	csDirectory[64];
	char	csBuffer[0x8000];	//JBNV_FILE_INFO[];
}JBNV_DIRECTORY_LIST;

typedef struct tagJBNV_FILE_INFO{
	char	csFileName[16];
	DWORD	bIsDir;
	DWORD	dwFileSize;
}JBNV_FILE_INFO;

typedef struct tagJBNV_DVR_FILE_DATA{
	DWORD	dwFileLength;			//�ļ�����
	DWORD	dwDataIndex;			//������
	DWORD	dwDataLength;			//���ݳ���
	DWORD	dwReserved;				//����
	char	csFileName[64];
	BYTE	bFileData[64 * 1024];
}JBNV_DVR_FILE_DATA;

//Add 2008-08-08 ��������
typedef struct tagJBNV_BROADCAST_DATA
{
	DWORD				CommandType;
	DWORD				dwServerType;
	DWORD				dwServerIp;
	WORD				wServerDataPort;
	WORD				wServerWebPort;	
	char				csServerName[32];
	BYTE				bServerMac[8];
	BYTE				bChannelCount;
	BYTE				bAlarmInCount;
	BYTE				bAlarmOutCount;
	BYTE				bChanneNo;
	DWORD				dwReserve[6];
	DWORD				dwRemoteIp;
	WORD				wRemotePort;
}JBNV_BROADCAST_DATA;

//����������������������з��������ӣ�SDK����ͻ�����Message,
//����wParam Ϊ JBNV_BROADCAST_DATA �ṹ��ָ��
//		JBNV_BROADCAST_DATA *lpData = (JBNV_BROADCAST_DATA *)wParam;

//�������ӷ�����ʱ����Ҫʹ�ýӿ�JBNV_OpenServerByBackConnect
//����dwServerIpAddress Ϊ lpData->dwRemoteIp;
//����wServerPort		Ϊ lpData->wRemotePort;
DWORD WINAPI JBNV_StartBackConnectListen(HWND  hMsgWnd,DWORD dwMsgID,WORD wLocalPort);
DWORD WINAPI JBNV_StopBackConnectListen();

DWORD WINAPI JBNV_OpenServerByBackConnect(DWORD dwServerIpAddress,WORD wServerPort,
		LPCSTR lpszUserName,LPCSTR lpszPassword,LPVOID *lpHandle);
DWORD WINAPI JBNV_OpenRTSPChannel(LPCSTR lpUrl,HWND hShowWnd,LPCSTR lpUserName,LPCSTR lpPassword,HANDLE *lpHandle);
//Add 2008-08-20
typedef struct tagJB_NVD_SENSOR_ALARM_SET
{
	DWORD			dwSize;
	BOOL			bEnableAlarm;		//�Ƿ�ʹ��
	DWORD			dwKeepTime;			//����ʱ��
	DWORD			dwSensorOut[4];		//̽ͷ�澯���
	DWORD			dwMontionDec;		//��Ƶ�ƶ��澯���
	DWORD			dwVideoLost;		//��Ƶ��ʧ�澯���
	DWORD			dwReserved[2];
}JB_NVD_SENSOR_ALARM_SET;

#define WIRELESS_WIFI           0x01
#define WIRELESS_TDSCDMA_ZX     0x02
#define WIRELESS_EVDO_HUAWEI    0x03
#define WIRELESS_WCDMA			0x04
//Add 2008-11-25
typedef struct tagJB_TDSCDMA_CONFIG
{
	DWORD			dwSize;
	BYTE			bCdmaEnable;
	BYTE			byDevType;              //SIM������
	BYTE			byStatus;               //3G״̬
	BYTE			byReserve;              //�ź�ǿ��
	DWORD		    dwNetIpAddr;			//IP  (wifi enable)
}JB_TDSCDMA_CONFIG;


typedef struct tagJB_WIFI_CONFIG
{
	DWORD		dwSize;
	int         bWifiEnable; // 0: disable, 1:static ip address, 2:dhcp
	DWORD		dwNetIpAddr;
	DWORD       dwNetMask;
	DWORD       dwGateway;
	DWORD		dwDNSServer;
	char		szEssid[32];
	unsigned char         nSecurity;  //0: none,1:web 64  assii,
                                      //2:web 64  hex,
                                      //3:web 128 assii
						 	          // 4:web 128 hex
                                      //5 WPAPSK-TKIP 
                                      //6 WPAPSK-AES
                                      //7 WPA2PSK-TKIP
                                      //8 WPA2PSK-AES   
    unsigned char byMode;  // 1. managed 2. ad-hoc
	BYTE          byStatus; //	0:	�ɹ�,����ֵ�Ǵ�����
	BYTE          byRes;  // 1:wps����
    char		  szWebKey[32];
}JB_WIFI_CONFIG;


typedef struct tagJBPeriphSensorConfig{
	BOOL		bEnable;
	DWORD		nAddress;
	BOOL		bOSDVideo;
	BOOL		bAlarmRecord;
	DWORD		nLinkVideoChn; //bit 
	DWORD		nStatus; //the current status identify
} JB_PERIPH_SENSOR_CONFIG;

typedef struct tagJBPeriphConfig{
	DWORD		dwSize;
	BOOL 		bEnable;
	char      	csDevName[32];
	DWORD		nComID; // 0:485, 1:232
	DWORD 		nEnableDevNO;	
	JB_PERIPH_SENSOR_CONFIG SensorCfg[16]; //MAX 16 device 
} JB_PERIPH_CONFIG;

//Add 2009-01-06
typedef struct tagJB_TEL_ALARM_SET{
	DWORD		dwSize;
	char		csTelNo[9][20];
	DWORD		dwBeepTime;
	BOOL		bArming;
	BOOL		bEnableVideoLost;
	BOOL		bEnableMotionDetect;
	BYTE		bPrepos[8];
	DWORD		dwReserved[2];
}JB_TEL_ALARM_SET;


typedef struct tagJB_TEMP_HUM_SENSOR_CONFIG{
	DWORD		dwSize;
	BOOL		bEnableDevice;
	BOOL		bEnableDeviceLostAlarm;
	BOOL		bEnableDeviceLimitAlarm;
	BOOL		bEnableShowDataOnVideo;
	DWORD		dwDeviceNo;
	char		csDeviceName[32];
	BOOL		bDeviceIsOnline;
	float       fTempUpperLimit;
	float       fTempLowerLimit;
	float       fTempValue;
	float       fHumUpperLimit;
	float       fHumLowerLimit;
	float       fHumValue;
	DWORD		dwRecved[4];
}JB_TEMP_HUM_SENSOR_CONFIG;

typedef struct tagJB_POWER_DEVICE_CONFIG{
	DWORD		dwSize;
	BOOL		bEnableDevice;
	BOOL		bDeviceIsOnline;
	BOOL		bEnableDeviceLostAlarm;
	BOOL		bEnableShowDataOnVideo;
	DWORD		dwDeviceNo;
	char		csDeviceName[32];
	DWORD		dwPower220VState;		//0 off,1 on
	DWORD		dwPower48VState;		//0 oof,1 on
	DWORD		dwRecved[4];
}JB_POWER_DEVICE_CONFIG;

//Add 2009-04-07
//��Ӵ˺������ͻ�ʹ�ã��˻ص�����ͬJBNV_SetMessage������
typedef int (CALLBACK *MessageCallBack)
( HANDLE hServer,				//���������
 JB_SERVER_MSG *lpmsg,			//��Ϣ
 DWORD dwUser);					//�û�����
DWORD WINAPI JBNV_SetMessageEx(HANDLE hServer,MessageCallBack lpMessagecb,DWORD dwUser);

#include <WINSOCK2.H>

//��������������
typedef int (CALLBACK *SearchServerCallBack)(JBNV_SERVER_MSG_DATA *lpServerMsgData,	//���������ص���Ϣ
											 sockaddr_in *lpRemote,DWORD dwUser);				//��������ַ
DWORD WINAPI JBNV_SearchServerEx(SearchServerCallBack lpSearchServer,DWORD dwUser);
//���ڷ�������
typedef int (CALLBACK *BackConnectCallBack)(JBNV_BROADCAST_DATA *lpData,DWORD dwUser);		//����������Ϣ
DWORD WINAPI JBNV_StartBackConnectListenEx(BackConnectCallBack lpBackConnect,DWORD dwUser,WORD wLocalPort);



#define CMD_NVD_SET_TVSIZE 0x01000010 //���ý�������Ƶ�����С
#define CMD_NVD_GET_TVSIZE 0x02000010 //��ý�������Ƶ�����С

typedef struct tagNVD_DECODER_CHANNEL_TV
{
	DWORD dwSize;
	DWORD dwChannel;	//ͨ����
	DWORD dwTop;        //�ϱ߾�
	DWORD dwLeft;		//��߾�
	DWORD dwRight;		//�ұ߾�
	DWORD dwBottom;		//�±߾�
}NVD_DECODER_CHANNEL_TV; 


DWORD WINAPI JBNV_TalkOpenByBackConnect(DWORD dwServerIpAddress,WORD wServerPort);
DWORD WINAPI JBNV_TalkOpenByBackConnectEx(HANDLE hServer, DWORD dwServerIpAddress,WORD wServerPort);



typedef struct tagJBNV_TIME{
	DWORD dwYear;	
	DWORD dwMonth;
	DWORD dwDay;
	DWORD dwHour;
	DWORD dwMinute;
	DWORD dwSecond;	
}JBNV_TIME;

typedef struct tagJBNV_FindFileReq{		//��ѯ����
	DWORD		dwSize;
	DWORD		nChannel;				//0xff��ȫ��ͨ����0��1��2 ......
	DWORD		nFileType;				//�ļ����� ��0xff �� ȫ����0 �� ��ʱ¼��1 - �ƶ���⣬2 �� ����������3  �� �ֶ�¼��
	JBNV_TIME	BeginTime;				//
	JBNV_TIME	EndTime;				//StartTime StopTime ��ֵ��Ϊ0000-00-00 00:00:00��ʾ��������ʱ��
}JBNV_FIND_FILE_REQ;


typedef struct tagJBNV_FILE_DATA_INFO{
	char		sFileName[256];			//�ļ���
	JBNV_TIME	BeginTime;				//
	JBNV_TIME	EndTime;
	DWORD		nChannel;
	DWORD		nFileSize;				//�ļ��Ĵ�С
	DWORD		nState;					//�ļ�ת��״̬
}JBNV_FILE_DATA_INFO;

typedef struct tagJBNV_FindFileResp{
	DWORD		dwSize;
	DWORD		nResult;		//0:success ;1:find file error ; 2:the number of file more than the memory size, and the result contains part of the data
	DWORD		nCount;
	DWORD		dwReserved[3];
}JBNV_FIND_FILE_RESP;


DWORD WINAPI JBPlay_PlayBackByName(HANDLE	hServer ,					//JBNV_OPENSERVER �ķ���ֵ
								  LPCSTR	lpszFileName,				//Ҫ�طŵ��ļ���
								  DWORD		dwImageIndex,				//�طŴ������
								  HWND  	hWnd,						//�ط��ļ��Ĵ��ھ��
								  JB_STREAM_PLAY_INFO *lpInfo,
								  LPVOID	*lpHandle
								  );


DWORD WINAPI JBPlay_PlayBackByTime(HANDLE	hServer ,			//JBNV_OPENSERVER �ķ���ֵ
								  DWORD		lChannel,			//ͨ����
								  JBNV_TIME	lpBeginTime, 		//��ʼʱ��
								  JBNV_TIME	lpEndTime , 		//����ʱ��
								  DWORD dwImageIndex,
								  HWND hWnd,				//Ҫ���ŵĴ��ھ��
								  JB_STREAM_PLAY_INFO *lpInfo,
								  LPVOID *lpHandle);

DWORD WINAPI JBPlay_StopPlay(HANDLE hPlayHandle);		//���ž����JBNV_PlayBackByName//����JBNV_PlayBackByTime�ķ���


DWORD WINAPI JBPlay_RemotePlayCommand(HANDLE hPlayHandle ,
									 DWORD  dwControlCode,		//����¼��ط�״̬����
									 DWORD  dwInValue			//�����ļ��طŵĽ���(JBNV_PLAYSETPOS)ʱ,�˲�����ʾ����ֵ��
									 );

DWORD WINAPI JBPlay_RemoteDownloadStart(HANDLE hServer, LPCSTR	lpszRemoteFileName,  LPCSTR	lpszSaveFileName, LPVOID *lpHandle);//�����б��ڵ��ļ�
DWORD WINAPI JBPlay_RemoteDownloadStop(HANDLE hHandle);//ֹͣ�����б��ڵ��ļ�


DWORD WINAPI JBPlay_GetRemotePlayInfo(HANDLE hPlayHandle,JB_STREAM_PLAY_INFO *lpInfo); //��ȡ������Ϣ
DWORD WINAPI JBPlay_RemoteSetMessage(HANDLE hServer,HWND hMsgWnd,UINT nMessage);//������Ϣ�ص�
DWORD WINAPI JBPlay_RemoteCapturePicture(HANDLE hPlayHandle,LPCSTR lpFileName); //Զ��ץ��ͼƬ

typedef struct tagJBUPnPConfig
{
	DWORD dwSize;
	BOOL bEnable; /*�Ƿ�����upnp*/
	DWORD dwMode; /*upnp������ʽ.0Ϊ�Զ��˿�ӳ�䣬1Ϊָ���˿�ӳ��*/
	DWORD dwLineMode; /*upnp����������ʽ.0Ϊ��������,1Ϊ��������*/
	char csServerIp[32]; /*upnpӳ������.������·����IP*/
	DWORD dwDataPort; /*upnpӳ�����ݶ˿�*/
	DWORD dwWebPort; /*upnpӳ������˿�*/
	DWORD dwMobilePort;         /*upnpӳ���ֻ��˿�*/  
	DWORD dwDataPort1; /*upnp��ӳ��ɹ������ݶ˿�*/
	DWORD dwWebPort1; /*upnp��ӳ��ɹ�������˿�*/
	DWORD dwMobilePort1;      /*upnpӳ��ɹ����ֻ��˿�*/  
}JB_UPNP_CONFIG; 


#define MAX_DISK_NUM	64

typedef struct tagJBNV_DISK_ITEM{
	DWORD	dwDiskID;			//��Itemָ���ǵڼ���Ӳ���ϵ�
	DWORD	dwDiskType;			//��������
	DWORD	dwPartitionIndex; 
	DWORD	dwPartitionType;
	DWORD	dwPartitionState;	//����״̬
	DWORD	dwPartitionSize;	//��������,��MΪ��λ
	DWORD	dwPartitionFree;	//����ʣ��ռ�
}JBNV_DISK_ITEM;

typedef struct tagJBNV_DISK_INFO{
	DWORD	dwSize;
	DWORD	dwItemCount;
	JBNV_DISK_ITEM DiskItem[MAX_DISK_NUM];
}JBNV_DISK_INFO;

typedef struct tagJBNV_FDISK_DISK{
	DWORD	dwSize;
	DWORD	dwDiskID;			//Ҫ�����Ĵ���ID
	DWORD	dwPartitionSize;	//��ʽ������С(G)
	DWORD	dwRecvParam[8];
}JBNV_FDISK_DISK;

typedef struct tagJBNV_FORMAT_DISK{
	DWORD	dwSize;
	DWORD	dwDiskID;			//����ID
	DWORD	dwPartitionIndex;	//Ҫ��ʽ���Ĵ���
	BOOL	bFastFormat;		//�Ƿ���п��ٸ�ʽ��
	DWORD	dwClusterSize;		//��ʽ���ش�С
	DWORD	dwRecvParam[8];
}JBNV_FORMAT_DISK;

#define JBNV_STOP_RECORDING			0x1000
#define JBNV_STOP_RECORDSUCCESS		0x1001
#define JBNV_FDISK_RUNING			0x1002
#define	JBNV_FDISK_SUCCESS			0x1003
#define JBNV_FDISK_ERROR_NODISK		0x1004
#define JBNV_FDISK_ERROR_NOFIND		0x1005
#define JBNV_FORMAT_RUNING			0x1006
#define JBNV_FORMAT_SUCCESS			0x1007
#define JBNV_FORMAT_ERROR_NODISK	0x1008
#define JBNV_FORMAT_ERROR_FAILED	0x1009

typedef struct tagJBNV_FORMAT_STATUS{
	DWORD dwSize;
	DWORD dwDiskID;
	DWORD dwPartitionIndex;
	DWORD dwFormatState;
	DWORD dwParam1;
	DWORD dwParam2;
}JBNV_FORMAT_STATUS;


typedef struct tagJB_MOBILE_CONFIG
{
	unsigned long		dwSize; 
	unsigned short      wPort;
	char				reserved[128];
}JB_MOBILE_CONFIG,*PJB_MOBILE_CONFIG; 


#define CMD_SET_MOBILE                0x00000051
#define CMD_GET_MOBILE                0x10000051

typedef struct tagJB_MOBILE_CENTER_INFO{
	DWORD	dwSize;
	BOOL	bEnable;
	char	szIp[64];					//������Ip
	DWORD	dwCenterPort;				//���Ķ˿�
	char	csServerNo[64];				//���������к�
	DWORD	dwStatus;					//����������״̬ 0Ϊδ���� 1Ϊ������ 2���ӳɹ�
	char	csUserName[32];				//�û���
	char	csPassWord[32];				//����
	BYTE	byAlarmPush;
	BYTE	breservedData[3];
	DWORD	reservedData;				//����
}JB_MOBILE_CENTER_INFO;

typedef struct tagJB_SERVER_SET_INFO{
	DWORD	dwSize;
	DWORD	dwIp;			//Server Ip
	DWORD	wMediaPort;		//Media Port:8200
	DWORD	wWebPort;		//Http Port:80
	DWORD	dwNetMask;
	DWORD	dwGateway;
	DWORD	dwDNS;
	DWORD	dwComputerIP;
	
	BOOL	bEnableDHCP;	
	BOOL	bEnableAutoDNS;
	BOOL	bEncodeAudio;
	
	char	szMac[6];
	char	szoldMac[6];
	char	szServerName[32];	
}JBNV_SET_SIGHT_SERVER_INFO_EX;

///����ͷ,������������
typedef struct
{
	DWORD	dwSize;
	DWORD	nCmd;
	DWORD	dwPackFlag; // == SERVER_PACK_FLAG
	DWORD	nErrorCode;
	
}JBNV_BROADCAST_HEADER_EX;

 
//this is the broadcast package over the network
typedef struct tagJBNV_SERVER_INFO_BROADCAST{
	DWORD	nBufSize;       /*sieze of JBNV_SET_SERVER_INFO_BROADCAST*/
	JBNV_BROADCAST_HEADER_EX			hdr;
	JBNV_SET_SIGHT_SERVER_INFO_EX      	setInfo;
	JB_CENTER_INFO					    nxServer;
}JBNV_SET_SERVER_INFO_BROADCAST_EX;

typedef struct tagJBNV_SERVER_INFO_BROADCAST_V2{
	DWORD	                            nBufSize;       /*sieze of JBNV_SET_SERVER_INFO_BROADCAST*/
	JBNV_BROADCAST_HEADER_EX			hdr;
	JBNV_SET_SIGHT_SERVER_INFO_EX      	setInfo;
	JBNV_NXSIGHT_SERVER_ADDR_V2         nxServer;
}JBNV_SET_SERVER_INFO_BROADCAST_EX_V2;


typedef struct tagJBNV_PTZ_CONTROL
{
	DWORD		dwSize;
	DWORD		dwChannel;
	DWORD		dwPTZCommand;		//PTZCMD_UP .....
	int			nPTZParam;		// ���ݾ��������ֶ���
	BYTE		byReserve[32];
}JBNV_PTZ_CONTROL;

//���ڼ�¼
typedef struct tagDMS_FR_ATTANDECNE_S
{
    DWORD dwSize;				// �ṹ���С
    DWORD id;					// ���ݿ�ΨһID
    BYTE  bDeviceID[8];         // �����ID,ʹ��MAC��ַ
    DWORD dwIPCType;            // ��������� 0��δ���壬1������������2�����������
    DWORD data_time;            // ����ʱ��
    char uuid[36];				// ��ԱΨһ�� UUID
    char name[32];				// ��Ա����
    int  sorce;                 // ���Ŷ�
    char identity_num[32];		// ���Ż����֤����
    char csReserved[32];        // ���� 
} DMS_FR_ATTANDENCE_S;

typedef struct tagDMS_FR_ATTANDENCE_QUERY_COND_S
{
    int struct_size;   	// �ṹ���С
    int page_size;      // ÿҳ��ʾ��������¼
    int page_index;     // ҳ�� 0,1,2,3
    DWORD start_time;   // ��ʼʱ��
    DWORD end_time;     // ����ʱ��
    int chn;            //����ͨ����ѯ��-1������IPC��[0-16)  1��16ͨ��
    char identity_num[32];   //������/����/���֤�����ѯ
    char reserved[64];
} DMS_FR_ATTANDENCE_QUERY_COND_S;

typedef struct
{
    int struct_size;    // �ṹ���С
    int total_size;     // ���ݿ��ܵļ�¼��
    int query_size;     // ��ǰ��ѯ����ļ�¼��
    DMS_FR_ATTANDENCE_S fr_log[100]; //����ܲ�ѯ100����
} DMS_FR_ATTANDENCE_QUERY_RES_S;

#define VFD_ERROR_LOAD_IMAGE        -10001   //����ͼƬʧ��
#define VFD_ERROR_ALLOC_MEM         -10002  //�����ڴ�ʧ��
#define VFD_ERROR_IMAGE_SIZE        -10003  //ͼƬ̫��
#define VFD_ERROR_CREATE_VFD        -10004  //����VFD���ʧ��
#define VFD_ERROR_VFD_RUN           -10005  //VFD�ڲ�����ʱ����
#define VFD_ERROR_VFD_ERROR         -10006  //VFD���ش���
#define VFD_ERROR_FACE_MORE         -10007  //��������1��
#define VFD_ERROR_RECT_INVALID      -10008  //û��⵽����
#define VFD_ERROR_FACE_SMALL        -10009  //����С��112 * 96
#define VFD_ERROR_OPEN_FILE         -10010  //������ļ�ʧ��
#define VFD_ERROR_QUALITY_LOW       -10011  //������������
 
int WINAPI JBNV_GetFaceImage(IN LPCSTR strImageFile,   //ԭʼͼƬ�����룩
                             IN LPCSTR strFaceImage,   //��ȡ������ͼƬ�������
                             OUT SIZE *lpInputImage,    //����ͼƬ�Ĵ�С
                             OUT RECT *lpSrcFacePos,    //ԭʼͼƬ������λ��
                             OUT RECT *lpDstFacePos);   //Ŀ��ͼƬ������λ��

//��� С��0 ��ֵ��Ϊ�����룬����0��Ϊ�ü���ͼƬ��ռ���ڴ��С
int WINAPI JBNV_GetFaceImageEx(
    BYTE *lpSrcImage,       //����������ԭʼJPEGͼƬ����
    DWORD dwImageSize,      //ͼƬ��С
    BYTE *lpOutImage,       //����ľ����ü���JPEGͼƬ
    DWORD dwBufferSize,     //�����������С
    RECT *lpDstFacePos);     //����ľ����ü���JPEGͼƬ�ϵ�����λ��


//0 ���� 1 ��������2��������3VIP
typedef struct tagDMS_FR_ALARM_ATTR_S
{
    int dwSize;	// �ṹ���С
    int voice_custom;	// �Ƿ����Զ���ȶԽ������ 0/1
    BYTE ouput[16];		// ������Ӧ���� ��λ�����ʾ   bit0-bit7 bit3:�̵������ bit4:�������
    BYTE voice[16];		// ѡ�еıȶԽ������ 0,1,2,����0��1�����Զ���2
    char reserved[32];
} DMS_FR_ALARM_ATTR_S;


typedef struct tagDMS_FR_VOICE_CONFIG
{
    DWORD	dwSize;
    WORD	wFormatTag; // DMS_PT_G711A
    WORD	wFileSize;
    BYTE	byData[64*1024];
} DMS_FR_VOICE_CONFIG;   //���ݸ�ʽ


#define DMS_NET_GET_TRIPLINECFG             0x020243        //��ȡ���߲���
#define DMS_NET_SET_TRIPLINECFG             0x020244        //���ð��߲���

//2018-12-10
typedef struct tagJB_CHANNEL_TRIP_LINE{
    DWORD			dwSize;
    DWORD			dwChannel;				//ͨ����
    BOOL            bShotSnap;
    JB_SCHED_TIME	jbScheduleTime[8];		//����ʱ��Σ�����һ�������졢ÿ�ա�
   
    POINT           pt1;
    POINT           pt2;
    DWORD           dir;                    //���߷��� 0��ʾ����, 1��ʾ˫��, ��������°��߷���ʼ��Ϊ��㵽ĩβ��ֱ�ߵ���ʱ�뷽��
    
    BOOL            bLight;					// �׹�����
    int             bVoice;					// ��������,0��ɶ��������1�����¼������ & ������ź�

    DWORD			nDuration;				//����IO�˿��������ʱ��(��)
    BOOL			bAlarmIOOut[4];			//̽ͷ���

    WORD			wVoiceCount;			// ����
    WORD            wVoiceIndex;			// ѡ�еģ��Զ��� 0xFFFF
    int				bVoiceCustom;			// �Ƿ�ʹ���Զ�����Ƶ
    BOOL            bShowHuman;             // �Ƿ���ʾ����
    BYTE          	reserve[128];
}JB_CHANNEL_TRIP_LINE,*PJB_CHANNEL_TRIP_LINE;

 
 
typedef enum 
{
    PLATE_UNCERTAIN			= 0,			//!< ��ȷ����
    PLATE_BLUE				= 1,			//!< ���Ƴ�
    PLATE_YELLOW			= 2,			//!< ������Ƴ�
    PLATE_POLICE			= 4,			//!< ����
    PLATE_WUJING			= 8,			//!< �侯����
    PLATE_DBYELLOW			= 16,			//!< ˫�����
    PLATE_MOTOR				= 32,			//!< Ħ�г�
    PLATE_INSTRUCTIONCAR	= 64,			//!< ������
    PLATE_MILITARY			= 128,			//!< ����
    PLATE_PERSONAL			= 256,			//!< ���Ի���
    PLATE_GANGAO			= 512,			//!< �۰ĳ�
    PLATE_EMBASSY			= 1024,			//!< ʹ�ݳ�
    PLATE_NONGLARE			= 2048,			//!< ��ʽ����(������)
    PLATE_AVIATION			= 4096,			//!< �񺽳���
    PLATE_NEWENERGY			= 8192,			//!< ����Դ����
    PLATE_NEWENERGYBIG		= 0x00004000,	//!< ����Դ���ƴ󳵣�
    
    PLATE_WHITE_TWOTWO		= 0x10000001,	//!< 2+2ģ�ͣ�
    PLATE_WHITE_TWOTHR		= 0x10000002,	//!< 2+3ģ�ͣ�
    PLATE_WHITE_THRTWO		= 0x10000004,	//!< 3+2ģ�ͣ�
    PLATE_WHITE_THRTHR		= 0x10000008,	//!< 3+3ģ�ͣ�
    PLATE_WHITE_THRFOR		= 0x10000010,	//!< 3+4ģ�ͣ�
    
    PLATE_BLACK_THRTWO		= 0x10000020,	//!< 3+2ģ�ͣ�
    PLATE_BLACK_TWOTHR		= 0x10000040,	//!< 2+3ģ�ͣ�
    PLATE_BLACK_THRTHR		= 0x10000080,	//!< 3+3ģ�ͣ�
    PLATE_BLACK_TWOFOR		= 0x10000100,	//!< 2+4ģ�ͣ�
    PLATE_BLACK_FORTWO		= 0x10000200,	//!< 4+2ģ�ͣ�
    PLATE_BLACK_THRFOR		= 0x10000400,	//!< 3+4ģ�ͣ�
}PLATETYPE_E;


typedef struct tagJB_LPR_ALARM_DATA
{
    DWORD           dwSize;
    int             s32EventCode;		        //!< �¼���
    int             s32LandId;				    //!< ����ID    			   	   						
    char            cVehicleType[24];           //!< ��������     			   						  			   						
    char 	        cVehicleColor[32];		    //!< ������ɫ
    char 	        cPlateColor[32];		    //!< ������ɫ
    char            cPlateNum[16];              //���ƺ�
    int             lConfidence;               //�������Ŷ�
    PLATETYPE_E		ePlateType;				    //��������
    int             s32PicDataLen;			    //!< ͼƬ��С			   						
}JB_LPR_ALARM_DATA;

#define DMS_NET_CMD_SET_IP_ADAPTIVE_PARAM   0xA01000F4    //IP����Ӧ״̬����
#define DMS_NET_CMD_GET_IP_ADAPTIVE_PARAM   0xA01000F5    //IP����Ӧ״̬��ȡ

typedef struct
{
    int dwSize;   	   // �ṹ���С
    int ip_adaptive;   //�Ƿ���IP����Ӧ
    char reserve[64];
} DMS_NET_IP_ADAPTIVE_PARAM_S;

 
#define DMS_NET_CMD_SET_RECG_TEXT        0xA01000FA    // �����豸�ȶ���ʾ�բ����   DMS_NET_RECG_TEXT_INFOR_S
#define DMS_NET_CMD_GET_RECG_TEXT        0xA01000FB    // ��ȡ�豸�ȶ���ʾ�� (բ��)    DMS_NET_RECG_TEXT_INFOR_S

//0 İ���� 1 ��������2��������3VIP
typedef struct tagDMS_NET_RECG_TEXT_INFOR_S
{
    int  dwSize;    			// �ṹ���С
    int  type[16];               //0-Ĭ����ʾ���� 1-�Զ����ı�
    char text[16][32]; 			// �Զ��延ӭ��
    char reserve[64];
}DMS_NET_RECG_TEXT_INFOR_S;

typedef struct tagDMS_FR_RECORD_QUERY_COND_S
{
    int struct_size;   	// �ṹ���С
    int page_size;      // ÿҳ��ʾ��������¼
    int page_index;     // ҳ�� 0,1,2,3...
    char reserved[64];
} DMS_FR_RECORD_QUERY_COND_S;

// ��ѯ����
typedef struct
{
    int struct_size;   	// �ṹ���С
    char start_time[20];     // ��ʼʱ��   YYYY-MM-DD hh:mm:ss
    char end_time[20];       // ����ʱ��
    int page_size;      // ÿҳ��ʾ��������¼ ���DMS_FR_QUERY_HIS_MAX_NUM
    int page_index;     // ҳ�� 0,1,2,3...
    char reserved[64];
} DMS_FR_RECORD_QUERY_BY_TIME_REQ_S;

#define DMS_FR_QUERY_HIS_MAX_NUM 100

typedef struct
{
    int struct_size;    // �ṹ���С
    unsigned int id;    // ���ݿ�ΨһID
    char datetime[24];  // �ȶ�ʱ��
    char uuid[36];      // UUID
    char name[32];      // ����
    int age;            // ����
    char sex;           // �Ա� ��F��/��M��
    char role;           // 1-������ 2-������ ...
    char identity_num[30]; // ���֤��
    char info[64];         // ��ע��Ϣ
    char iccard[32];       // ic����
    char phone[16];        // �绰����
    int valid_time_type;        // ��Ч������ 0:ÿ��(һ����ʼ����-һ���������) 1:����(0-6/������-������) 2:����(��ʼ����ʱ���-��������ʱ���)
    unsigned int start_time;    // ��ʼʱ��
    unsigned int expire_time;   // ����ʱ��
    int ndepartmentid;          //����ID
    int nworkid;                //Ա��ID
    int nHostelID;              //¥��ID
    char department_name[24];   //��������
    char reserved[128];
    unsigned int face_data_len; // ����ͼ���ݳ���
} DMS_FR_RECORD_S;

typedef struct
{
    int struct_size;    // �ṹ���С
    int total_size;     // ���ݿ��ܵļ�¼��
    int query_size;     // ��ǰ��ѯ����ļ�¼��
    DMS_FR_RECORD_S record[DMS_FR_QUERY_HIS_MAX_NUM]; // ����ͼƬ����
} DMS_FR_RECORD_QUERY_RES_S;

 

#endif