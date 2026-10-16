/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    void reorderList(ListNode* head) {
        // find mid
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next and fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        // reverse second half
        ListNode* prev = nullptr;
        ListNode* curr = slow->next;
        slow->next = nullptr;
        ListNode* nxt;
        while (curr){
            nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        // merge
        ListNode* first = head;
        ListNode* second = prev;
        ListNode *n1, *n2;
        while(second){
            n1 = first->next;
            n2 = second->next;
            first->next = second;
            second->next = n1;
            first = n1;
            second = n2;
        }
    }
};
