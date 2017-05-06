#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int fsize,total=0;
char text[100];

struct frame // defines the structure of the frame. 'id' is sequence number, while str contains the message.
{
	int id;
	char *str;
};

typedef struct frame * Frame; // alias for 'struct frame' = Frame.
Frame srcarr[100]={NULL};

void makeframe();
void populateframe(int);
void display();
void jumble();
void sort();

void main()
{
	printf("Enter the message\n");
	//scanf("%s",text); scanf returns segmentation fault incase your message has a blank space, so we use gets() although with warnings.
	gets(text);
	printf("Enter frame size\n");
	scanf("%d",&fsize);
	makeframe();
}

void makeframe()
{
	int i;
	for(i=0;text[i]!='\0';i++) // travese the string (i.e message until NULL)
	{
		populateframe(i);
		i=i+fsize-1; 
	}
	display();
	jumble();
	sort();
}

void populateframe(int low)
{
	int i;
	Frame ptr = (Frame)malloc(sizeof(struct frame));
	char *cptr = (char *)malloc(fsize*sizeof(char));
	for(i=0;i<fsize;i++)
	{
		if(text[low+i]=='\0')
		{
			*(cptr+i)=text[low+i];
			break;
		}
		*(cptr + i)= text[low+i];
	}
	ptr->id=total;
	ptr->str=cptr;
	srcarr[total]=ptr;
	total++;
}

void display()
{
	int i;
	for(i=0;i<total;i++)
	{
		printf("%d %s\n",srcarr[i]->id,srcarr[i]->str);
	}
}


void jumble()
{
// here we just generate a random index value 'j' , and swap it with known index value 'i'.
// here we observe that total keeps track of the number of frames formed.
	int i,j;
	Frame temp;
	for(i=0;i<total;i++)
	{
		j=rand()%total;
		temp = srcarr[i];
		srcarr[i]=srcarr[j];
		srcarr[j]=temp;
	}
	printf("After jumble frames are :\n");
	for(i=0;i<total;i++)
	{
		printf("%d %s\n", srcarr[i]->id,srcarr[i]->str);
	}
}

void sort()
{
// we sort the jumbled frames according to their sequence number i.e 'id', using bubble sort.
	int i,j;
	Frame temp;
	for(i=0;i<total;i++)
	{
		for(j=i+1;j<total;j++)
		{
			if(srcarr[j]->id < srcarr[i]->id)
			{
				temp = srcarr[i];
				srcarr[i]=srcarr[j];
				srcarr[j]=temp;
			}
		}
	}
	printf("After sorting frames are\n");
	for(i=0;i<total;i++)
		printf("%d %s\n",srcarr[i]->id,srcarr[i]->str);
}

























		






		
