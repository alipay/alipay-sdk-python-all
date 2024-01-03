#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonTransferSignModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._sign_pid = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sign_pid(self):
        return self._sign_pid

    @sign_pid.setter
    def sign_pid(self, value):
        self._sign_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sign_pid:
            if hasattr(self.sign_pid, 'to_alipay_dict'):
                params['sign_pid'] = self.sign_pid.to_alipay_dict()
            else:
                params['sign_pid'] = self.sign_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonTransferSignModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sign_pid' in d:
            o.sign_pid = d['sign_pid']
        return o


