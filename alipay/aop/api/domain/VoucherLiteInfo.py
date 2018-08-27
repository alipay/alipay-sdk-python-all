#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherLiteInfo(object):

    def __init__(self):
        self._send_time = None
        self._status = None
        self._template_id = None
        self._voucher_id = None

    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherLiteInfo()
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


