//This program creates a link list From user inputs

#include<iostream>
using namespace std;


class node
{
public:
    int data;
    node *next;
};
node *head=new node();

void create(int data)   //this function is for creating  a linked list in order
{
    node *cur=new node(); //allocate a key pointer for traversing
    node *temp=new node();//allocate a temporary pointer for data

    cur=head;

    temp->data=data;
    temp->next=NULL;

    while(1)
    {
        if(cur->next==NULL)
        {
            cur->next=temp;
            break;
        }
        else
        {
            cur=cur->next;
        }
    }
}

void Print()
{
    node *temp=new node();
    temp=head;      //we do not want to change the head pointer
    cout<<"The List is:";<<endl;            //so we assigned another pointer to head
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}

int main()
{
    int n,first,x;
    cout<<"Enter the number of nodes:";
    cin>>n;
    cin>>first;
    head->data=first;
    head->next=NULL;
    cout<<"Enter the data:"<<endl;
    for(int i=1;i<n;i++)
    {
        cin>>x;
        create(x);
        Print();
    }

    return 0;
}
