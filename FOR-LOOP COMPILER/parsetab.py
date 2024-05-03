
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA FOR IDENTIFIER IN LPAREN NUMBER RANGE RPARENfor_loop : FOR IDENTIFIER IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON statementsstatements : statementstatements : statements statementstatement : IDENTIFIER LPAREN IDENTIFIER RPAREN'
    
_lr_action_items = {'FOR':([0,],[2,]),'$end':([1,13,14,16,18,],[0,-1,-2,-3,-4,]),'IDENTIFIER':([2,11,13,14,15,16,18,],[3,12,12,-2,17,-3,-4,]),'IN':([3,],[4,]),'RANGE':([4,],[5,]),'LPAREN':([5,12,],[6,15,]),'NUMBER':([6,8,],[7,9,]),'COMMA':([7,],[8,]),'RPAREN':([9,17,],[10,18,]),'COLON':([10,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'for_loop':([0,],[1,]),'statements':([11,],[13,]),'statement':([11,13,],[14,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> for_loop","S'",1,None,None,None),
  ('for_loop -> FOR IDENTIFIER IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON statements','for_loop',11,'p_for_loop','parser.py',6),
  ('statements -> statement','statements',1,'p_statements','parser.py',11),
  ('statements -> statements statement','statements',2,'p_statements_more','parser.py',15),
  ('statement -> IDENTIFIER LPAREN IDENTIFIER RPAREN','statement',4,'p_statement_function_call','parser.py',20),
]
