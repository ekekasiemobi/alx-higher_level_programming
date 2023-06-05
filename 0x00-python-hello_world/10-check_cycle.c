#include "lists.h"

/**
 * check_cycle - checks for cycle in singly linked list
 * @list: items in singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	if (!list)
	{
		return (0);
	}

	while (temp != NULL && temp->next != NULL)
	{
		current = current->next;
		temp = temp->next->next;

		if (current == temp)
		{
			return (1);
		}
	}

	return (0);
}
