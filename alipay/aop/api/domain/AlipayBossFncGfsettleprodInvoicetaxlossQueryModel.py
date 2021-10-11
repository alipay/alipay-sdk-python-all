#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsettleprodInvoicetaxlossQueryModel(object):

    def __init__(self):
        self._bill_nos = None
        self._settle_ip_role_id = None

    @property
    def bill_nos(self):
        return self._bill_nos

    @bill_nos.setter
    def bill_nos(self, value):
        self._bill_nos = value
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_nos:
            if hasattr(self.bill_nos, 'to_alipay_dict'):
                params['bill_nos'] = self.bill_nos.to_alipay_dict()
            else:
                params['bill_nos'] = self.bill_nos
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoicetaxlossQueryModel()
        if 'bill_nos' in d:
            o.bill_nos = d['bill_nos']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        return o


