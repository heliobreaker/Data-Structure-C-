//This is a program for deleting a node at nth position in the linked list
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
    node *cur=new node();
    node *temp=new node();

    temp->data=data;
    temp->next=NULL;

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

void Print()
{
    node *temp=new node();
    temp=head;
    while(temp!=NULL)
    {
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}

void Delete(int position)
{
    int i;
    node *current1=new node();
    node *current2=new node();
    current1=head;
    current2=current1->next;

    if(position==1)
    {
        head=current2;
        delete(current1);//freeing the memory of current1
        return;//return control to the main function
    }
    for(i=2;i<=(position-1);i++) //iterate the list until we find the previous node of the node to be deleted
    {
        current1=current1->next;
    }
    current1->next=current2->next;//update the next address of previous node to the next node of the node to be deleted
    delete(current2);//free the memory of the deleted node
}

int main()
{
    int pos,n,x,first;
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
    cout<<"The List is (without deleting):"<<endl;
    Print();

    cout<<"Enter which position to delete:";
    cin>>pos;
    Delete(pos);
    cout<<"The list after deletion is:";
    Print();

}
