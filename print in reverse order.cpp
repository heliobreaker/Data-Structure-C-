//This function prints linked list in reverse order without reversing the main linked list using recursive method
#include<iostream>
using namespace std;

class node
{
    public:
    int data;
    node *next;
};

node *head=new node();


void create(int data)
{
    node *temp=new node();
    temp->data=data;
    temp->next=NULL;

    node *cur=new node();
    cur=head;

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

void Print(node *p)
{
    if(p==NULL)
    {
        return;
    }
    else
    {
        cout<<p->data<<" ";
        Print(p->next);
    }
    cout<<endl;
}

void revrse(node *p)
{
    if(p==NULL)
    {
        return;
    }

    else
    {
        revrse(p->next);
        cout<<" "<<p->data;
    }
}

int main()
{
    int pos,n,x,data,first;
    cout<<"Enter number of elements in the list:";
    cin>>n;
    cin>>first;
    head->data=first;
    head->next=NULL;
    for(int i=2;i<=n;i++)
    {
        cin>>x;
        create(x);
    }

    cout<<"The List is :"<<endl;
    Print(head);

    cout<<"The Reversed list is:";
    revrse(head);

}
