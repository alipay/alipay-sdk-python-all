#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VerifyLogisticsDetail(object):

    def __init__(self):
        self._check_phone_no = None
        self._logistics_code = None
        self._logistics_company = None
        self._tracking_number = None

    @property
    def check_phone_no(self):
        return self._check_phone_no

    @check_phone_no.setter
    def check_phone_no(self, value):
        self._check_phone_no = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def logistics_company(self):
        return self._logistics_company

    @logistics_company.setter
    def logistics_company(self, value):
        self._logistics_company = value
    @property
    def tracking_number(self):
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, value):
        self._tracking_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_phone_no:
            if hasattr(self.check_phone_no, 'to_alipay_dict'):
                params['check_phone_no'] = self.check_phone_no.to_alipay_dict()
            else:
                params['check_phone_no'] = self.check_phone_no
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.logistics_company:
            if hasattr(self.logistics_company, 'to_alipay_dict'):
                params['logistics_company'] = self.logistics_company.to_alipay_dict()
            else:
                params['logistics_company'] = self.logistics_company
        if self.tracking_number:
            if hasattr(self.tracking_number, 'to_alipay_dict'):
                params['tracking_number'] = self.tracking_number.to_alipay_dict()
            else:
                params['tracking_number'] = self.tracking_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyLogisticsDetail()
        if 'check_phone_no' in d:
            o.check_phone_no = d['check_phone_no']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_company' in d:
            o.logistics_company = d['logistics_company']
        if 'tracking_number' in d:
            o.tracking_number = d['tracking_number']
        return o


