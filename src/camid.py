#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
                    ) < 50 and math.fabs(
                    self._currentId[1] - NewId[1]
                    ) < 50
                ):
                self._currentId=NewId
                return True
            else:
                self._currentId=NewId
                return False
