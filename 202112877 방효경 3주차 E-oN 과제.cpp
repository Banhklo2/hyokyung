#define _CRT_NO_SECURE_WARNINGS
#include <stdio.h>

int total(int iValue[]);

int main()
{
	int iNum[6];
	int result;
	

	printf("���ڸ� �Է��ϼ���");
	scanf_s("%d, %d, %d, %d, %d, %d", &iNum[0], &iNum[1], &iNum[2], &iNum[3], &iNum[4], &iNum[5]);

	total(iNum);

	return 0;

}

int total(int iValue[])
{
	int iCount;
	int iSum = 0;
	for (iCount = 1; iCount <= 6; iCount++)
	{
		iSum = iSum + iCount;
	}

		printf("��� �迭�� �� : %d", iSum);

		return 0;

}