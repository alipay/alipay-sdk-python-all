#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaxReceiptOnceInfo(object):

    def __init__(self):
        self._cognizant_mobile = None
        self._ep_tax_id = None

    @property
    def cognizant_mobile(self):
        return self._cognizant_mobile

    @cognizant_mobile.setter
    def cognizant_mobile(self, value):
        self._cognizant_mobile = value
    @property
    def ep_tax_id(self):
        return self._ep_tax_id

    @ep_tax_id.setter
    def ep_tax_id(self, value):
        self._ep_tax_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cognizant_mobile:
            if hasattr(self.cognizant_mobile, 'to_alipay_dict'):
                params['cognizant_mobile'] = self.cognizant_mobile.to_alipay_dict()
            else:
                params['cognizant_mobile'] = self.cognizant_mobile
        if self.ep_tax_id:
            if hasattr(self.ep_tax_id, 'to_alipay_dict'):
                params['ep_tax_id'] = self.ep_tax_id.to_alipay_dict()
            else:
                params['ep_tax_id'] = self.ep_tax_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaxReceiptOnceInfo()
        if 'cognizant_mobile' in d:
            o.cognizant_mobile = d['cognizant_mobile']
        if 'ep_tax_id' in d:
            o.ep_tax_id = d['ep_tax_id']
        return o


