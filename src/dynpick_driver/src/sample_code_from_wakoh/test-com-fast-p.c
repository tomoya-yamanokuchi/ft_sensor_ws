// test-com.c
#define 	DEBUGSS	0

#include	<stdio.h>
#include	<fcntl.h>
#include	<time.h>
#include	<termios.h>
#include	<string.h>

#define true		1
#define false		0
#define CHAR_BIT 8

int SetComAttr(int fdc);


void encode(int c) {
    for (int i = 0; i < CHAR_BIT; i++) {
        printf("%d", !!((c << i) & 0x80));
    }
}


int main()
	{
	int			status;
	FILE			*fd;
	int			fdc;
	char			fname[64];
	char			devname[64];
	char			str[256];
	unsigned short	data[6];
	int			comNo;
	int			tick;
	int			clk, clkb, clkb2, clk0;
	int			tw;
	int			num;
	int			n;


	fd = NULL;
	fdc = -1;

start :
	// COMポートをオープン
	printf("Enter COM port > ");
	scanf("%d", &comNo);
	printf("Open /dev/ttyUSB%d\n", comNo);

	sprintf(devname, "/dev/ttyUSB%d", comNo);
	fdc = open(devname, O_RDWR | O_NOCTTY | O_NONBLOCK);
	if (fdc < 0)
		goto over;

	// サンプリング周期を得る
	tw = 16;
	printf("Enter sampling time (ms) > ");
	scanf("%d", &tw);
	printf("Sampling time = %d ms\n", tw);

	printf("Enter File name > ");
	scanf("%s", fname);
	fd = fopen(fname, "w");
	if (!fd)
		goto over;

	// COMポートのボーレート等を設定
	SetComAttr(fdc);

	// データを読み出す
	printf("=== record data ===\n");
	clk0 = clock() / (CLOCKS_PER_SEC / 1000);
	clkb = 0;
	clkb2 = 0;
	num = 0;

	// 感度係数(主軸感度)を返す（初回分）
	write(fdc, "P", 1);


	// 感度係数(主軸感度)を得る
	int i;
	unsigned long dataL[6];
	unsigned short cs;
	for (i = 0; i < 6; i++){
		read(fdc, &dataL[i], 4);
	}

	// チェックサムを得る
	read(fdc, &cs, 2);
	// printf("-------------\n");
	// printf("%d\n", cs);
	// printf("-------------\n");

    // std::string a;
    // while ((c = getchar()) != EOF) {
    //     encode(c);
    // }


	// 感度係数を表示
	printf("%ld, %ld, %ld, %ld, %ld, %ld\n",
			dataL[0], dataL[1], dataL[2], dataL[3], dataL[4], dataL[5]);

	printf("%lu, %lu, %lu, %lu, %lu, %lu\n",
			dataL[0], dataL[1], dataL[2], dataL[3], dataL[4], dataL[5]);

	// printf("%f, %f, %f, %f, %f, %f\n",
	// 		dataL[0], dataL[1], dataL[2], dataL[3], dataL[4], dataL[5]);

	return 0;
	// ---------------------------------------------


	init_keyboard();

	while (true)
		{
		// サンプリング周期だけ待つ
		while (true)
			{
			clk = clock() / (CLOCKS_PER_SEC / 1000) - clk0;

			if (clk >= clkb + tw)
				{
				clkb = clk / tw * tw;
				break;
				}
			}

		// 感度係数(主軸感度)を返す（次回分）
		write(fdc, "P", 1);

		// 単データを得る
// 		n = read(fdc, str, 26);
// 		if (n < 26)
// 			{
// //			printf ("=== error ! n = %d ===\n", n);
// 			goto skip;
// 			}

		for (i = 0; i < 6; i++){
			read(fdc, &dataL[i], 4);
		}

		sscanf(str, "%4hx%4hx%4hx%4hx%4hx%4hx",
			 &data[0], &data[1], &data[2], &data[3], &data[4], &data[5]);

		sprintf(str, "%05d,%05d,%05d,%05d,%05d,%05d,%05d\n",
			clk / tw * tw,
			data[0], data[1], data[2], data[3], data[4], data[5]);

		fprintf(fd, str);
		num++;

skip :
		if (clk >= 10000)
			break;

		// コンソールに間引き表示
		if (clk >= clkb2 + 1000)
			{
			printf(str);
			if (kbhit() &&
				readch() == '.')
				break;
			clkb2 = clk / 1000 * 1000;
			}
		}

over1 :
	close_keyboard();
over :
	if (fd)
		{
		fclose(fd);
		fd = NULL;
		}

	if (fdc >= 0)
		{
		close(fdc);
		fdc = -1;
		}

	printf ("=== num = %d ===\n", num);

	printf("exit (y / n) ? > ");
	scanf("%s", str);
	if (str[0] == 'y')
		{
//		exit(0);
		}
	else
		{
		goto start;
		}
	}


int SetComAttr(int fdc)
	{
	int			n;

	struct termios	term;


	// ボーレート等を設定
	n = tcgetattr(fdc, &term);
	if (n < 0)
		goto over;

	bzero(&term, sizeof(term));

	term.c_cflag = B921600 | CS8 | CLOCAL | CREAD;
	term.c_iflag = IGNPAR;
	term.c_oflag = 0;
	term.c_lflag = 0;/*ICANON;*/

	term.c_cc[VINTR]    = 0;     /* Ctrl-c */
	term.c_cc[VQUIT]    = 0;     /* Ctrl-? */
	term.c_cc[VERASE]   = 0;     /* del */
	term.c_cc[VKILL]    = 0;     /* @ */
	term.c_cc[VEOF]     = 4;     /* Ctrl-d */
	term.c_cc[VTIME]    = 0;
	term.c_cc[VMIN]     = 0;
	term.c_cc[VSWTC]    = 0;     /* '?0' */
	term.c_cc[VSTART]   = 0;     /* Ctrl-q */
	term.c_cc[VSTOP]    = 0;     /* Ctrl-s */
	term.c_cc[VSUSP]    = 0;     /* Ctrl-z */
	term.c_cc[VEOL]     = 0;     /* '?0' */
	term.c_cc[VREPRINT] = 0;     /* Ctrl-r */
	term.c_cc[VDISCARD] = 0;     /* Ctrl-u */
	term.c_cc[VWERASE]  = 0;     /* Ctrl-w */
	term.c_cc[VLNEXT]   = 0;     /* Ctrl-v */
	term.c_cc[VEOL2]    = 0;     /* '?0' */

//	tcflush(fdc, TCIFLUSH);
	n = tcsetattr(fdc, TCSANOW, &term);
over :

	return (n);
	}
