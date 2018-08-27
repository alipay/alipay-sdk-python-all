#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskOfflinevarsQueryModel(object):

    def __init__(self):
        self._rowkeys = None

    @property
    def rowkeys(self):
        return self._rowkeys

    @rowkeys.setter
    def rowkeys(self, value):
        self._rowkeys = value


    def to_alipay_dict(self):
        params = dict()
        if self.rowkeys:
            if hasattr(self.rowkeys, 'to_alipay_dict'):
                params['rowkeys'] = self.rowkeys.to_alipay_dict()
            else:
                params['rowkeys'] = self.rowkeys
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskOfflinevarsQueryModel()
        if 'rowkeys' in d:
            o.rowkeys = d['rowkeys']
        return o


