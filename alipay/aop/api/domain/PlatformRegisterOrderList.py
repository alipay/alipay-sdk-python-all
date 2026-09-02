#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PlatformRegisterOrderList(object):

    def __init__(self):
        self._order_detail_url = None
        self._order_id = None
        self._order_pay_status = None
        self._order_prop = None
        self._register_date = None
        self._status = None

    @property
    def order_detail_url(self):
        return self._order_detail_url

    @order_detail_url.setter
    def order_detail_url(self, value):
        self._order_detail_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_pay_status(self):
        return self._order_pay_status

    @order_pay_status.setter
    def order_pay_status(self, value):
        self._order_pay_status = value
    @property
    def order_prop(self):
        return self._order_prop

    @order_prop.setter
    def order_prop(self, value):
        self._order_prop = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_detail_url:
            if hasattr(self.order_detail_url, 'to_alipay_dict'):
                params['order_detail_url'] = self.order_detail_url.to_alipay_dict()
            else:
                params['order_detail_url'] = self.order_detail_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_pay_status:
            if hasattr(self.order_pay_status, 'to_alipay_dict'):
                params['order_pay_status'] = self.order_pay_status.to_alipay_dict()
            else:
                params['order_pay_status'] = self.order_pay_status
        if self.order_prop:
            if hasattr(self.order_prop, 'to_alipay_dict'):
                params['order_prop'] = self.order_prop.to_alipay_dict()
            else:
                params['order_prop'] = self.order_prop
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
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
        o = PlatformRegisterOrderList()
        if 'order_detail_url' in d:
            o.order_detail_url = d['order_detail_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_pay_status' in d:
            o.order_pay_status = d['order_pay_status']
        if 'order_prop' in d:
            o.order_prop = d['order_prop']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'status' in d:
            o.status = d['status']
        return o


