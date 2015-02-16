/*---------------------------------------------------------------------*/
/* --- STC MCU Limited ------------------------------------------------*/
/* --- STC15Fxx 系列 读取程序区ID号并用软件模拟串口输出显示举例--------*/
/* --- Mobile: (86)13922805190 ----------------------------------------*/
/* --- Fax: 86-755-82905966 -------------------------------------------*/
/* --- Tel: 86-755-82948412 -------------------------------------------*/
/* --- Web: www.STCMCU.com --------------------------------------------*/
/* 如果要在程序中使用此代码,请在程序中注明使用了宏晶科技的资料及程序   */
/* 如果要在文章中应用此代码,请在文章中注明使用了宏晶科技的资料及程序   */
/*---------------------------------------------------------------------*/

//本示例在Keil开发环境下请选择Intel的8058芯片型号进行编译
//假定测试芯片的工作频率为18.432MHz

#include "reg51.h"

//-----------------------------------------
//define baudrate const
//BAUD = 65536 - FOSC/3/BAUDRATE/M (1T:M=1; 12T:M=12)
//NOTE: (FOSC/3/BAUDRATE) must be greater then 98, (RECOMMEND GREATER THEN 110)

#define BAUD    0xFF60                  //38400bps @ 18.432MHz


#define ID_ADDR_RAM 0x71                //STC15F104W系列ID号的存放在RAM区的地址
//#define ID_ADDR_RAM 0x71              //STC15F104W系列ID号的存放在RAM区的地址
//#define ID_ADDR_RAM 0xF1              //STC15F204EA系列ID号的存放在RAM区的地址

#define ID_ADDR_ROM 0x0ff9              //STC104W系列ID号的存放在ROM区的地址

sfr AUXR = 0x8E;
sbit RXB = P3^4;                        //define UART TX/RX port
sbit TXB = P3^5;

typedef bit BOOL;
typedef unsigned char BYTE;
typedef unsigned int WORD;

BYTE TBUF,RBUF;
BYTE TDAT,RDAT;
BYTE TCNT,RCNT;
BYTE TBIT,RBIT;
BOOL TING,RING;
BOOL TEND,REND;

void UART_INIT();
void UART_SEND(BYTE dat);

BYTE t, r;
BYTE buf[16];

void main()
{
//    BYTE idata *iptr;
    BYTE code *cptr;
    BYTE i;
    
    TMOD = 0x00;                        //timer0 in 16-bit auto reload mode
    AUXR = 0x80;                        //timer0 working at 1T mode
    TL0 = BAUD;
    TH0 = BAUD>>8;                      //initial timer0 and set reload value
    TR0 = 1;                            //tiemr0 start running
    ET0 = 1;                            //enable timer0 interrupt
    PT0 = 1;                            //improve timer0 interrupt priority
    EA = 1;                             //open global interrupt switch

    UART_INIT();
//    iptr = ID_ADDR_RAM;               //从RAM区读取ID号
//    for (i=0; i<7; i++)               //读7个字节
//    {
//        UART_SEND(*iptr++);           //发送ID到串口
//    }
    
    cptr = ID_ADDR_ROM;                 //从程序区读取ID号
    for (i=0; i<7; i++)                 //读7个字节
    {
        UART_SEND(*cptr++);             //发送ID到串口
    }

    while (1);
}

//-----------------------------------------
//Timer interrupt routine for UART

void tm0() interrupt 1 using 1
{
    if (RING)
    {
        if (--RCNT == 0)
        {
            RCNT = 3;                   //reset send baudrate counter
            if (--RBIT == 0)
            {
                RBUF = RDAT;            //save the data to RBUF
                RING = 0;               //stop receive
                REND = 1;               //set receive completed flag
            }
            else
            {
                RDAT >>= 1;
                if (RXB) RDAT |= 0x80;  //shift RX data to RX buffer
            }
        }
    }
    else if (!RXB)
    {
        RING = 1;                       //set start receive flag
        RCNT = 4;                       //initial receive baudrate counter
        RBIT = 9;                       //initial receive bit number (8 data bits + 1 stop bit)
    }

    if (--TCNT == 0)
    {
        TCNT = 3;                       //reset send baudrate counter
        if (TING)                       //judge whether sending
        {
            if (TBIT == 0)
            {
                TXB = 0;                //send start bit
                TDAT = TBUF;            //load data from TBUF to TDAT
                TBIT = 9;               //initial send bit number (8 data bits + 1 stop bit)
            }
            else
            {
                TDAT >>= 1;             //shift data to CY
                if (--TBIT == 0)
                {
                    TXB = 1;
                    TING = 0;           //stop send
                    TEND = 1;           //set send completed flag
                }
                else
                {
                    TXB = CY;           //write CY to TX port
                }
            }
        }
    }
}

//-----------------------------------------
//initial UART module variable

void UART_INIT()
{
    TING = 0;
    RING = 0;
    TEND = 1;
    REND = 0;
    TCNT = 0;
    RCNT = 0;
}

//-----------------------------------------
//Send UART data

void UART_SEND(BYTE dat)
{
    while (!TEND);
    TEND = 0;
    TBUF = dat;
    TING = 1;
}

