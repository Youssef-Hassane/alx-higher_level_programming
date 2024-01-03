#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * Return: the address of the new node, or NULL if it failed
 * --------------------------
 * Prototype:listint_t *insert_node(listint_t **head, int number);
 * --------------------------
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be inserted
 * --------------------------
 * By Youssef Hassane
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;

	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
