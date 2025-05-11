#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandLeadsQueryModel(object):

    def __init__(self):
        self._leads_id = None

    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandLeadsQueryModel()
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        return o


