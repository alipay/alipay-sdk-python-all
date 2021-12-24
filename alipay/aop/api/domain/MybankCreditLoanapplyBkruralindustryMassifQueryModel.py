#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyBkruralindustryMassifQueryModel(object):

    def __init__(self):
        self._business_no = None
        self._request_id = None
        self._uid = None

    @property
    def business_no(self):
        return self._business_no

    @business_no.setter
    def business_no(self, value):
        self._business_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_no:
            if hasattr(self.business_no, 'to_alipay_dict'):
                params['business_no'] = self.business_no.to_alipay_dict()
            else:
                params['business_no'] = self.business_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyBkruralindustryMassifQueryModel()
        if 'business_no' in d:
            o.business_no = d['business_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'uid' in d:
            o.uid = d['uid']
        return o


