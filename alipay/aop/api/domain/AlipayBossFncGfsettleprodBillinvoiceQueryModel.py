#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsettleprodBillinvoiceQueryModel(object):

    def __init__(self):
        self._bill_no = None
        self._seller_ip_role_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def seller_ip_role_id(self):
        return self._seller_ip_role_id

    @seller_ip_role_id.setter
    def seller_ip_role_id(self, value):
        self._seller_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.seller_ip_role_id:
            if hasattr(self.seller_ip_role_id, 'to_alipay_dict'):
                params['seller_ip_role_id'] = self.seller_ip_role_id.to_alipay_dict()
            else:
                params['seller_ip_role_id'] = self.seller_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodBillinvoiceQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'seller_ip_role_id' in d:
            o.seller_ip_role_id = d['seller_ip_role_id']
        return o


