#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateReverseResult(object):

    def __init__(self):
        self._certificate_id = None
        self._msg = None
        self._result = None
        self._use_order_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def use_order_no(self):
        return self._use_order_no

    @use_order_no.setter
    def use_order_no(self, value):
        self._use_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        if self.use_order_no:
            if hasattr(self.use_order_no, 'to_alipay_dict'):
                params['use_order_no'] = self.use_order_no.to_alipay_dict()
            else:
                params['use_order_no'] = self.use_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateReverseResult()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'msg' in d:
            o.msg = d['msg']
        if 'result' in d:
            o.result = d['result']
        if 'use_order_no' in d:
            o.use_order_no = d['use_order_no']
        return o


