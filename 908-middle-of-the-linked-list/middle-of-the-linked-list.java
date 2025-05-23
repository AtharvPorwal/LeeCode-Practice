/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        List<ListNode> arr = new ArrayList();
         int len = 0;
         while (head!= null){

            arr.add(head);
            head = head.next;
            len++;
         }
        return arr.get(len/2);
    }
}