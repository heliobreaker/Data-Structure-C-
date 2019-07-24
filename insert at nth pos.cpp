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
    node *current=new node();
    node *temp=new node();
    current=head;
    temp->data=data;
    temp->next=NULL;

    while(1)
    {
        if(current->next==NULL)
        {
            current->next=temp;
            break;
        }
        else
        {
            current=current->next;
        }
    }
}

void Insert(int data,int position)//this function inserts a node at nth position of the list
{
    int i;
    node *current=new node();
    node *temp=new node();
    temp->data=data;
    temp->next=NULL;
    current= head;
    if(position==1)
    {
        temp->next=head;
        head=temp;
        return;
    }
    for(i=2;i<=position;i++)
    {
        current=current->next;
    }
    temp->next=current->next;
    current->next=temp;
}

void Print(node *p)
{

    if(p==NULL)
    {
        return;
    }
    cout<<p->data<<" ";
    Print(p->next);
    cout<<endl;
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
    cout<<"The List is (without inserting):"<<endl;
    Print(head);

    cout<<"Enter which position to insert:";
    cin>>pos;
    cout<<"Enter the number:";
    cin>>data;
    Insert(data,(pos));
    cout<<"The Enhanced list is:";
    Print(head);

}
