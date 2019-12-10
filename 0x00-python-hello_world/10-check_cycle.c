#include "lists.h"

/**
 * check_cylce - a function that checks if a singly linked list has a
 * cycle in it
 * @list: the list to check
 *
 * Return: 1, if a cycle is present or 0, if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tort = list;

	while (tort && hare && hare->next)
	{
		tort = tort->next;
		hare = hare->next->next;

		if (hare == tort)
			return (1);
	}

	return (0);
}
