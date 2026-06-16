\* Backlog_Planning *\
Minimize
OBJ: 10000 Backlog_('P1',_0) + 10000 Backlog_('P1',_1)
 + 10000 Backlog_('P1',_10) + 10000 Backlog_('P1',_11)
 + 10000 Backlog_('P1',_2) + 10000 Backlog_('P1',_3) + 10000 Backlog_('P1',_4)
 + 10000 Backlog_('P1',_5) + 10000 Backlog_('P1',_6) + 10000 Backlog_('P1',_7)
 + 10000 Backlog_('P1',_8) + 10000 Backlog_('P1',_9) + 10 Firing_0
 + 10 Firing_1 + 10 Firing_10 + 10 Firing_11 + 10 Firing_2 + 10 Firing_3
 + 10 Firing_4 + 10 Firing_5 + 10 Firing_6 + 10 Firing_7 + 10 Firing_8
 + 10 Firing_9 + 10 Hiring_0 + 10 Hiring_1 + 10 Hiring_10 + 10 Hiring_11
 + 10 Hiring_2 + 10 Hiring_3 + 10 Hiring_4 + 10 Hiring_5 + 10 Hiring_6
 + 10 Hiring_7 + 10 Hiring_8 + 10 Hiring_9 + Inv_('P1',_0) + Inv_('P1',_1)
 + Inv_('P1',_10) + Inv_('P1',_11) + Inv_('P1',_2) + Inv_('P1',_3)
 + Inv_('P1',_4) + Inv_('P1',_5) + Inv_('P1',_6) + Inv_('P1',_7)
 + Inv_('P1',_8) + Inv_('P1',_9) + 5 Prod_('P1',_0) + 5 Prod_('P1',_1)
 + 5 Prod_('P1',_10) + 5 Prod_('P1',_11) + 5 Prod_('P1',_2) + 5 Prod_('P1',_3)
 + 5 Prod_('P1',_4) + 5 Prod_('P1',_5) + 5 Prod_('P1',_6) + 5 Prod_('P1',_7)
 + 5 Prod_('P1',_8) + 5 Prod_('P1',_9) + 100 Workers_0 + 100 Workers_1
 + 100 Workers_10 + 100 Workers_11 + 100 Workers_2 + 100 Workers_3
 + 100 Workers_4 + 100 Workers_5 + 100 Workers_6 + 100 Workers_7
 + 100 Workers_8 + 100 Workers_9
Subject To
_C1: Backlog_('P1',_0) - Inv_('P1',_0) + Prod_('P1',_0) = 300
_C10: - Backlog_('P1',_8) + Backlog_('P1',_9) + Inv_('P1',_8) - Inv_('P1',_9)
 + Prod_('P1',_9) = 300
_C11: Backlog_('P1',_10) - Backlog_('P1',_9) - Inv_('P1',_10) + Inv_('P1',_9)
 + Prod_('P1',_10) = 300
_C12: - Backlog_('P1',_10) + Backlog_('P1',_11) + Inv_('P1',_10)
 - Inv_('P1',_11) + Prod_('P1',_11) = 300
_C13: Firing_0 - Hiring_0 + Workers_0 = 40
_C14: Prod_('P1',_0) - 10 Workers_0 <= 0
_C15: Workers_0 >= 10
_C16: Workers_0 <= 15
_C17: Firing_1 - Hiring_1 - Workers_0 + Workers_1 = 0
_C18: Prod_('P1',_1) - 10 Workers_1 <= 0
_C19: Workers_1 >= 10
_C2: - Backlog_('P1',_0) + Backlog_('P1',_1) + Inv_('P1',_0) - Inv_('P1',_1)
 + Prod_('P1',_1) = 350
_C20: Workers_1 <= 15
_C21: Firing_2 - Hiring_2 - Workers_1 + Workers_2 = 0
_C22: Prod_('P1',_2) - 10 Workers_2 <= 0
_C23: Workers_2 >= 10
_C24: Workers_2 <= 15
_C25: Firing_3 - Hiring_3 - Workers_2 + Workers_3 = 0
_C26: Prod_('P1',_3) - 10 Workers_3 <= 0
_C27: Workers_3 >= 10
_C28: Workers_3 <= 15
_C29: Firing_4 - Hiring_4 - Workers_3 + Workers_4 = 0
_C3: - Backlog_('P1',_1) + Backlog_('P1',_2) + Inv_('P1',_1) - Inv_('P1',_2)
 + Prod_('P1',_2) = 500
_C30: Prod_('P1',_4) - 10 Workers_4 <= 0
_C31: Workers_4 >= 10
_C32: Workers_4 <= 15
_C33: Firing_5 - Hiring_5 - Workers_4 + Workers_5 = 0
_C34: Prod_('P1',_5) - 10 Workers_5 <= 0
_C35: Workers_5 >= 10
_C36: Workers_5 <= 15
_C37: Firing_6 - Hiring_6 - Workers_5 + Workers_6 = 0
_C38: Prod_('P1',_6) - 10 Workers_6 <= 0
_C39: Workers_6 >= 10
_C4: - Backlog_('P1',_2) + Backlog_('P1',_3) + Inv_('P1',_2) - Inv_('P1',_3)
 + Prod_('P1',_3) = 600
_C40: Workers_6 <= 15
_C41: Firing_7 - Hiring_7 - Workers_6 + Workers_7 = 0
_C42: Prod_('P1',_7) - 10 Workers_7 <= 0
_C43: Workers_7 >= 10
_C44: Workers_7 <= 15
_C45: Firing_8 - Hiring_8 - Workers_7 + Workers_8 = 0
_C46: Prod_('P1',_8) - 10 Workers_8 <= 0
_C47: Workers_8 >= 10
_C48: Workers_8 <= 15
_C49: Firing_9 - Hiring_9 - Workers_8 + Workers_9 = 0
_C5: - Backlog_('P1',_3) + Backlog_('P1',_4) + Inv_('P1',_3) - Inv_('P1',_4)
 + Prod_('P1',_4) = 400
_C50: Prod_('P1',_9) - 10 Workers_9 <= 0
_C51: Workers_9 >= 10
_C52: Workers_9 <= 15
_C53: Firing_10 - Hiring_10 + Workers_10 - Workers_9 = 0
_C54: Prod_('P1',_10) - 10 Workers_10 <= 0
_C55: Workers_10 >= 10
_C56: Workers_10 <= 15
_C57: Firing_11 - Hiring_11 - Workers_10 + Workers_11 = 0
_C58: Prod_('P1',_11) - 10 Workers_11 <= 0
_C59: Workers_11 >= 10
_C6: - Backlog_('P1',_4) + Backlog_('P1',_5) + Inv_('P1',_4) - Inv_('P1',_5)
 + Prod_('P1',_5) = 300
_C60: Workers_11 <= 15
_C61: Backlog_('P1',_11) = 0
_C7: - Backlog_('P1',_5) + Backlog_('P1',_6) + Inv_('P1',_5) - Inv_('P1',_6)
 + Prod_('P1',_6) = 300
_C8: - Backlog_('P1',_6) + Backlog_('P1',_7) + Inv_('P1',_6) - Inv_('P1',_7)
 + Prod_('P1',_7) = 300
_C9: - Backlog_('P1',_7) + Backlog_('P1',_8) + Inv_('P1',_7) - Inv_('P1',_8)
 + Prod_('P1',_8) = 300
Bounds
 0 <= Firing_0
 0 <= Firing_1
 0 <= Firing_10
 0 <= Firing_11
 0 <= Firing_2
 0 <= Firing_3
 0 <= Firing_4
 0 <= Firing_5
 0 <= Firing_6
 0 <= Firing_7
 0 <= Firing_8
 0 <= Firing_9
 0 <= Hiring_0
 0 <= Hiring_1
 0 <= Hiring_10
 0 <= Hiring_11
 0 <= Hiring_2
 0 <= Hiring_3
 0 <= Hiring_4
 0 <= Hiring_5
 0 <= Hiring_6
 0 <= Hiring_7
 0 <= Hiring_8
 0 <= Hiring_9
 0 <= Prod_('P1',_0)
 0 <= Prod_('P1',_1)
 0 <= Prod_('P1',_10)
 0 <= Prod_('P1',_11)
 0 <= Prod_('P1',_2)
 0 <= Prod_('P1',_3)
 0 <= Prod_('P1',_4)
 0 <= Prod_('P1',_5)
 0 <= Prod_('P1',_6)
 0 <= Prod_('P1',_7)
 0 <= Prod_('P1',_8)
 0 <= Prod_('P1',_9)
 0 <= Workers_0
 0 <= Workers_1
 0 <= Workers_10
 0 <= Workers_11
 0 <= Workers_2
 0 <= Workers_3
 0 <= Workers_4
 0 <= Workers_5
 0 <= Workers_6
 0 <= Workers_7
 0 <= Workers_8
 0 <= Workers_9
Generals
Firing_0
Firing_1
Firing_10
Firing_11
Firing_2
Firing_3
Firing_4
Firing_5
Firing_6
Firing_7
Firing_8
Firing_9
Hiring_0
Hiring_1
Hiring_10
Hiring_11
Hiring_2
Hiring_3
Hiring_4
Hiring_5
Hiring_6
Hiring_7
Hiring_8
Hiring_9
Prod_('P1',_0)
Prod_('P1',_1)
Prod_('P1',_10)
Prod_('P1',_11)
Prod_('P1',_2)
Prod_('P1',_3)
Prod_('P1',_4)
Prod_('P1',_5)
Prod_('P1',_6)
Prod_('P1',_7)
Prod_('P1',_8)
Prod_('P1',_9)
Workers_0
Workers_1
Workers_10
Workers_11
Workers_2
Workers_3
Workers_4
Workers_5
Workers_6
Workers_7
Workers_8
Workers_9
End
