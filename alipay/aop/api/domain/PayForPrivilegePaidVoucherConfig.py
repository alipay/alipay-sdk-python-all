#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayForPrivilegePaidVoucherConfig(object):

    def __init__(self):
        self._send_count = None
        self._template_id = None

    @property
    def send_count(self):
        return self._send_count

    @send_count.setter
    def send_count(self, value):
        self._send_count = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.send_count:
            if hasattr(self.send_count, 'to_alipay_dict'):
                params['send_count'] = self.send_count.to_alipay_dict()
            else:
                params['send_count'] = self.send_count
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayForPrivilegePaidVoucherConfig()
        if 'send_count' in d:
            o.send_count = d['send_count']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


