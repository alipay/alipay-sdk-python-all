#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerCheckInfoDTO(object):

    def __init__(self):
        self._bd_dept_name = None
        self._bd_name = None
        self._bd_work_no = None
        self._bid = None
        self._cid = None
        self._customer_short_name = None
        self._ep_cert_no = None
        self._ep_name = None
        self._match_type = None

    @property
    def bd_dept_name(self):
        return self._bd_dept_name

    @bd_dept_name.setter
    def bd_dept_name(self, value):
        self._bd_dept_name = value
    @property
    def bd_name(self):
        return self._bd_name

    @bd_name.setter
    def bd_name(self, value):
        self._bd_name = value
    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def customer_short_name(self):
        return self._customer_short_name

    @customer_short_name.setter
    def customer_short_name(self, value):
        self._customer_short_name = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_dept_name:
            if hasattr(self.bd_dept_name, 'to_alipay_dict'):
                params['bd_dept_name'] = self.bd_dept_name.to_alipay_dict()
            else:
                params['bd_dept_name'] = self.bd_dept_name
        if self.bd_name:
            if hasattr(self.bd_name, 'to_alipay_dict'):
                params['bd_name'] = self.bd_name.to_alipay_dict()
            else:
                params['bd_name'] = self.bd_name
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.customer_short_name:
            if hasattr(self.customer_short_name, 'to_alipay_dict'):
                params['customer_short_name'] = self.customer_short_name.to_alipay_dict()
            else:
                params['customer_short_name'] = self.customer_short_name
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.match_type:
            if hasattr(self.match_type, 'to_alipay_dict'):
                params['match_type'] = self.match_type.to_alipay_dict()
            else:
                params['match_type'] = self.match_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerCheckInfoDTO()
        if 'bd_dept_name' in d:
            o.bd_dept_name = d['bd_dept_name']
        if 'bd_name' in d:
            o.bd_name = d['bd_name']
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'bid' in d:
            o.bid = d['bid']
        if 'cid' in d:
            o.cid = d['cid']
        if 'customer_short_name' in d:
            o.customer_short_name = d['customer_short_name']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'match_type' in d:
            o.match_type = d['match_type']
        return o


