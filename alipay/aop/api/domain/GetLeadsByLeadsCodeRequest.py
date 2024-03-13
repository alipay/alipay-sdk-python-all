#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GetLeadsByLeadsCodeRequest(object):

    def __init__(self):
        self._leads_code = None

    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GetLeadsByLeadsCodeRequest()
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        return o


