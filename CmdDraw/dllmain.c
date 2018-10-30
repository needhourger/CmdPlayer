/* Replace "dll.h" with the name of your header */
#include "dll.h"
#include <windows.h>

//���Ժ��� 
DLLIMPORT void HelloWorld()
{
	MessageBox(0,"Hello World from DLL!\n","Hi",MB_ICONINFORMATION);
}

//�޸������й�� 
DLLIMPORT int gotoxy(int x,int y){
	COORD pos={x,y};
	HANDLE hConsole=GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(hConsole,pos);
	return 0;
}

//������������������ 
DLLIMPORT int console_init(int width,int height){
	//���� 
	system("cls");
	
	//��ȡ�����д��ھ�� 
	HANDLE hConsole=GetStdHandle(STD_OUTPUT_HANDLE);
	
	//���������л�������С�Լ����ڴ�С 
	CONSOLE_FONT_INFOEX font_info={sizeof(font_info)};
	COORD font_size={10,10};
	GetCurrentConsoleFontEx(hConsole,0,&font_info);
	font_info.dwFontSize=font_size;
	SetCurrentConsoleFontEx(hConsole,0,&font_info);

	//���������������С 
	COORD buff_size;
	buff_size.X=width+3;
	buff_size.Y=height+3;
	SMALL_RECT win_size;
	win_size.Top=0;
	win_size.Left=0;
	win_size.Bottom=height+2;
	win_size.Right=width+2; 
	SetConsoleScreenBufferSize(hConsole,buff_size);
	SetConsoleWindowInfo(hConsole,TRUE,&win_size);
	
} 


BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD fdwReason,LPVOID lpvReserved)
{
	switch(fdwReason)
	{
		case DLL_PROCESS_ATTACH:
		{
			break;
		}
		case DLL_PROCESS_DETACH:
		{
			break;
		}
		case DLL_THREAD_ATTACH:
		{
			break;
		}
		case DLL_THREAD_DETACH:
		{
			break;
		}
	}
	
	/* Return TRUE on success, FALSE on failure */
	return TRUE;
}
