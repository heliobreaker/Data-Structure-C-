//This function reverses a link list using iterative method

#include<iostream>
using namespace std;


class node
{
public:
    int data;
    node *next;
};
node *head=new node();

void Print(node *p)
{
    if(p==NULL)
    {
        return; //return control to the main function
    }
    else
    {
        cout<<p->data<<" ";
        Print(p->next);
    }
    cout<<endl;
}

void Create(int data)
{
    node *temp=new node();
    node *current=new node();
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

void Reverse(node *head)
{
    node *prev=new node();
    node *nxt=new node();
    node *current=new node();

    current=head;

    prev=NULL;

    while(current!=NULL)//traverse the list
    {
        nxt=current->next; //Saving location of current->next
        current->next=prev;//Updating the current->next address to the previous node
        prev=current; // shifting the address of present current node to previous node
        current=nxt; //updating the address of current node to next node
    }
    head=prev;  //updating new head node where current=NULL
    Print(head);
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
        Create(x);
    }

    cout<<"The Main List is :"<<endl;
    Print(head);


    cout<<"The Reversed list is:"<<endl;
    Reverse(head);

    return 0;

}
