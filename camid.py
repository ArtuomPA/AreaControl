#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:15:32 2018

@author: user
"""
import math

class CamId:
    def __init__(self):
        self._currentId=[]
    
    def isCurrent(self, NewId):
        if self._currentId == []:
            self._currentId.extend(NewId)
            return False
        else:
            if (math.fabs(
                    self._currentId[0] - NewId[0]
                    ) < 40 and math.fabs(
                    self._currentId[0] - NewId[0]
                    ) < 40
                ):
                return True
            else:
                return False