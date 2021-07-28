#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KnCertSendOrderDetail(object):

    def __init__(self):
        self._cert_remain_point = None
        self._cert_template_id = None
        self._gmt_create = None
        self._gmt_expire = None
        self._send_order_id = None

    @property
    def cert_remain_point(self):
        return self._cert_remain_point

    @cert_remain_point.setter
    def cert_remain_point(self, value):
        self._cert_remain_point = value
    @property
    def cert_template_id(self):
        return self._cert_template_id

    @cert_template_id.setter
    def cert_template_id(self, value):
        self._cert_template_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expire(self):
        return self._gmt_expire

    @gmt_expire.setter
    def gmt_expire(self, value):
        self._gmt_expire = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_remain_point:
            if hasattr(self.cert_remain_point, 'to_alipay_dict'):
                params['cert_remain_point'] = self.cert_remain_point.to_alipay_dict()
            else:
                params['cert_remain_point'] = self.cert_remain_point
        if self.cert_template_id:
            if hasattr(self.cert_template_id, 'to_alipay_dict'):
                params['cert_template_id'] = self.cert_template_id.to_alipay_dict()
            else:
                params['cert_template_id'] = self.cert_template_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_expire:
            if hasattr(self.gmt_expire, 'to_alipay_dict'):
                params['gmt_expire'] = self.gmt_expire.to_alipay_dict()
            else:
                params['gmt_expire'] = self.gmt_expire
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KnCertSendOrderDetail()
        if 'cert_remain_point' in d:
            o.cert_remain_point = d['cert_remain_point']
        if 'cert_template_id' in d:
            o.cert_template_id = d['cert_template_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_expire' in d:
            o.gmt_expire = d['gmt_expire']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        return o


