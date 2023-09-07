#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks  a cycle.
 * @list: head of singly-linked list.
 * Return: 0 no cycle - 1 is a cycle.
 */

int check_cycle(listint_t *list)
{
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	listint_t *node1 = list;
	listint_t *node2 = list;

	while (node2 != NULL && node2->next != NULL)
	{
		node1 = node1->next;
		node2 = node2->next->next;
		if (node1 == node2)
		{
			return (1);
		}
	}
}
