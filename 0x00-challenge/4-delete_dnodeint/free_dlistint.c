#include <string.h>
#include <stdlib.h>
#include "lists.h"

/**
 * free_dlistint - Free a list
 *
 * @head: A pointer to the first element of list
 */
void free_dlistint(dlistint_t *head)
{
    dlistint_t *nd;

    while (head)
    {
        nd = head;
        head = head->next;
        free(nd);
    }
}

