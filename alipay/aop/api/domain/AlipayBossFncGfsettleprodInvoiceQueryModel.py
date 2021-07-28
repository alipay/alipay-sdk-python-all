#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfsettleprodInvoiceQueryModel(object):

    def __init__(self):
        self._kp_no = None
        self._seller_ip_role_ids = None

    @property
    def kp_no(self):
        return self._kp_no

    @kp_no.setter
    def kp_no(self, value):
        self._kp_no = value
    @property
    def seller_ip_role_ids(self):
        return self._seller_ip_role_ids

    @seller_ip_role_ids.setter
    def seller_ip_role_ids(self, value):
        if isinstance(value, list):
            self._seller_ip_role_ids = list()
            for i in value:
                self._seller_ip_role_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.kp_no:
            if hasattr(self.kp_no, 'to_alipay_dict'):
                params['kp_no'] = self.kp_no.to_alipay_dict()
            else:
                params['kp_no'] = self.kp_no
        if self.seller_ip_role_ids:
            if isinstance(self.seller_ip_role_ids, list):
                for i in range(0, len(self.seller_ip_role_ids)):
                    element = self.seller_ip_role_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.seller_ip_role_ids[i] = element.to_alipay_dict()
            if hasattr(self.seller_ip_role_ids, 'to_alipay_dict'):
                params['seller_ip_role_ids'] = self.seller_ip_role_ids.to_alipay_dict()
            else:
                params['seller_ip_role_ids'] = self.seller_ip_role_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoiceQueryModel()
        if 'kp_no' in d:
            o.kp_no = d['kp_no']
        if 'seller_ip_role_ids' in d:
            o.seller_ip_role_ids = d['seller_ip_role_ids']
        return o


