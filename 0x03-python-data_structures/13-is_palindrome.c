#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * Return: 1 if palindrome, 0 otherwise
 * --------------------------
 * Prototype: int is_palindrome(listint_t **head)
 * --------------------------
 * @head: pointer to head of list
 *
 * --------------------------
 * By Youssef Hassane
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
