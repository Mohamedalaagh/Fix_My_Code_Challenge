#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - Prints a doubly linkedlist of integers
 *
 * @h: A pointer to the first element of a list
 *
 * Return: The number of elements printed
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t i;

    i = 0;
    while (h)
    {
        printf("%d\n", h->n);
        h = h->next;
        i++;
    }
    return (i);
}

