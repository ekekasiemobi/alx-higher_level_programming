#include "lists.h"
int my_index(listint_t *head, int number)
{
	int i = 0;
	
	while(head != NULL && head->n < number)
	{
		i++;
		head = head->next;
	}
	return (i);
}


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head;
	int i, index;
	
	new = malloc(sizeof(listint_t));
	new->n = number;
	if (temp == NULL)
	{
		temp = new;
		temp->next = NULL;
	}
	else if (temp->n > number)
	{
		new->next = temp;
		temp = new;
	}
	else
	{
		temp = *head;
		index = my_index(*head, number);
		for (i = 0; i < index - 1; i++)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (new);
}	
