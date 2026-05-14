#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RightsResult(object):

    def __init__(self):
        self._rights = None

    @property
    def rights(self):
        return self._rights

    @rights.setter
    def rights(self, value):
        self._rights = value


    def to_alipay_dict(self):
        params = dict()
        if self.rights:
            if hasattr(self.rights, 'to_alipay_dict'):
                params['rights'] = self.rights.to_alipay_dict()
            else:
                params['rights'] = self.rights
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RightsResult()
        if 'rights' in d:
            o.rights = d['rights']
        return o


