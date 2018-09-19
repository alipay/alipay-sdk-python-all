#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractBasicInfo(object):

    def __init__(self):
        self._brief_desc = None
        self._contract_name = None
        self._contract_no = None
        self._expire_time = None
        self._last_promise_date = None
        self._order = None
        self._sign_time = None
        self._source = None
        self._status = None

    @property
    def brief_desc(self):
        return self._brief_desc

    @brief_desc.setter
    def brief_desc(self, value):
        self._brief_desc = value
    @property
    def contract_name(self):
        return self._contract_name

    @contract_name.setter
    def contract_name(self, value):
        self._contract_name = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def last_promise_date(self):
        return self._last_promise_date

    @last_promise_date.setter
    def last_promise_date(self, value):
        self._last_promise_date = value
    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.brief_desc:
            if hasattr(self.brief_desc, 'to_alipay_dict'):
                params['brief_desc'] = self.brief_desc.to_alipay_dict()
            else:
                params['brief_desc'] = self.brief_desc
        if self.contract_name:
            if hasattr(self.contract_name, 'to_alipay_dict'):
                params['contract_name'] = self.contract_name.to_alipay_dict()
            else:
                params['contract_name'] = self.contract_name
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.last_promise_date:
            if hasattr(self.last_promise_date, 'to_alipay_dict'):
                params['last_promise_date'] = self.last_promise_date.to_alipay_dict()
            else:
                params['last_promise_date'] = self.last_promise_date
        if self.order:
            if hasattr(self.order, 'to_alipay_dict'):
                params['order'] = self.order.to_alipay_dict()
            else:
                params['order'] = self.order
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractBasicInfo()
        if 'brief_desc' in d:
            o.brief_desc = d['brief_desc']
        if 'contract_name' in d:
            o.contract_name = d['contract_name']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'last_promise_date' in d:
            o.last_promise_date = d['last_promise_date']
        if 'order' in d:
            o.order = d['order']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        return o


