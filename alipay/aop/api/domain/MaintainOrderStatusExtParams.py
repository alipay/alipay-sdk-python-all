#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaintainOrderStatusExtParams(object):

    def __init__(self):
        self._logistics_code = None
        self._logistics_company = None
        self._logistics_no = None
        self._order_status_txt = None
        self._receiver_addr = None
        self._sender_addr = None

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
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value
    @property
    def order_status_txt(self):
        return self._order_status_txt

    @order_status_txt.setter
    def order_status_txt(self, value):
        self._order_status_txt = value
    @property
    def receiver_addr(self):
        return self._receiver_addr

    @receiver_addr.setter
    def receiver_addr(self, value):
        self._receiver_addr = value
    @property
    def sender_addr(self):
        return self._sender_addr

    @sender_addr.setter
    def sender_addr(self, value):
        self._sender_addr = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        if self.order_status_txt:
            if hasattr(self.order_status_txt, 'to_alipay_dict'):
                params['order_status_txt'] = self.order_status_txt.to_alipay_dict()
            else:
                params['order_status_txt'] = self.order_status_txt
        if self.receiver_addr:
            if hasattr(self.receiver_addr, 'to_alipay_dict'):
                params['receiver_addr'] = self.receiver_addr.to_alipay_dict()
            else:
                params['receiver_addr'] = self.receiver_addr
        if self.sender_addr:
            if hasattr(self.sender_addr, 'to_alipay_dict'):
                params['sender_addr'] = self.sender_addr.to_alipay_dict()
            else:
                params['sender_addr'] = self.sender_addr
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MaintainOrderStatusExtParams()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'logistics_company' in d:
            o.logistics_company = d['logistics_company']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        if 'order_status_txt' in d:
            o.order_status_txt = d['order_status_txt']
        if 'receiver_addr' in d:
            o.receiver_addr = d['receiver_addr']
        if 'sender_addr' in d:
            o.sender_addr = d['sender_addr']
        return o


