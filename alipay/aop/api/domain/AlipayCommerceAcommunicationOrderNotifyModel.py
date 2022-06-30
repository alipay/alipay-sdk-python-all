#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationOrderNotifyModel(object):

    def __init__(self):
        self._alipay_order_no = None
        self._code = None
        self._msg = None
        self._out_order_no = None
        self._out_order_status = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_order_status(self):
        return self._out_order_status

    @out_order_status.setter
    def out_order_status(self, value):
        self._out_order_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_order_status:
            if hasattr(self.out_order_status, 'to_alipay_dict'):
                params['out_order_status'] = self.out_order_status.to_alipay_dict()
            else:
                params['out_order_status'] = self.out_order_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationOrderNotifyModel()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'code' in d:
            o.code = d['code']
        if 'msg' in d:
            o.msg = d['msg']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_order_status' in d:
            o.out_order_status = d['out_order_status']
        return o


