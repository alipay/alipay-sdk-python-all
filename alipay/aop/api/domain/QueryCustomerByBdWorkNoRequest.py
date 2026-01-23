#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryCustomerByBdWorkNoRequest(object):

    def __init__(self):
        self._bd_work_no = None
        self._cid = None
        self._customer_name = None

    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryCustomerByBdWorkNoRequest()
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'cid' in d:
            o.cid = d['cid']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        return o


