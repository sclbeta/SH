//假定测试芯片的工作频率为12MHz

#include "reg52.h"
#include "intrins.h"

//-----------------------------------------------

unsigned char dat;

sbit p10=P1^0;
sbit p11=P1^1;

void InitUart();

int count=0;


void Intr() interrupt 0  //中断
{
	count = 1;
	dat = P0;
	TI = 1;

}

void main()
{
    InitUart();                     //初始化串口
    ES = 1;
    EA = 1;
	TI = 0;

	IT0 = 1;   //初始化中断
	EX0 = 1;

	p10=0;
	while (1);
}

/*----------------------------
UART 中断服务程序
-----------------------------*/
void Uart() interrupt 4 using 1
{
 
	if (TI)
    {
        TI = 0;                     //清除TI位
        if (count != 0)
        {
            count--;
            SBUF = dat;          //继续发送应答数据
        }
    }

    if (RI)
    {
        RI = 0;                     //清除RI位
        count = 1;
        dat = SBUF;              //并开发送应答数据
		//P1 = dat;

		switch (dat)
		{
			case 0xfe:p10=0;break;
			case 0xfd:p11=0;break;
			case 0x01:p10=1;break;
			case 0x02:p11=1;break;
			case 0xff:P1=0xff;break;
		 	
		}
    }
}

/*----------------------------
初始化串口
----------------------------*/
void InitUart()
{
    TMOD = 0x20;                //设置定时器1为8位自动重装载模式
	SCON = 0x50;
	PCON = 0x00;
	
    TH1 = 0xfd;
    TL1 = 0xfd;           //波特率9600
    TR1 = 1;
}

