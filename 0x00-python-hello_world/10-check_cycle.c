#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle using Floyd's algorithm.
 * Return: 1 if a cycle is detected, 0 otherwise.
 * --------------------------
 * Prototype: int check_cycle(listint_t *list);
 * --------------------------
 * @list: A pointer to the head of the linked list.
 * --------------------------
 * By Youssef Hassane
 */

int check_cycle(listint_t *list)
{
	/* Declare two pointers, slow and fast */
	/* initially pointing to the head of the list */
	listint_t *theSlowPointer;
	listint_t *theFastPointer;
	/* If the list is empty, there can't be a cycle */
	if (list == NULL)
		return (ZERO);
	/* Initialize both pointers to the beginning of the list */
	theSlowPointer = list;
	theFastPointer = list;
	/* Traverse the list using the "tortoise and hare" approach */
	while (theFastPointer != NULL && theFastPointer->next != NULL)
	{
		/* Move the slow pointer one step at a time */
		theSlowPointer = theSlowPointer->next;
		/* Move the fast pointer two steps at a time */
		theFastPointer = theFastPointer->next->next;
		/* If the pointers meet, a cycle is detected */
		if (theSlowPointer == theFastPointer)
		{
			/* Return 1 to indicate the presence of a cycle */
			return (ONE);
		}
	}
	/* If the loop completes without detecting a cycle, return 0 */
	return (ZERO);
}
