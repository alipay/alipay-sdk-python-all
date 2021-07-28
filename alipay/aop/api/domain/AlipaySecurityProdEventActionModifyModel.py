#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdEventActionModifyModel(object):

    def __init__(self):
        self._msg = None
        self._socplt_key = None
        self._status = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def socplt_key(self):
        return self._socplt_key

    @socplt_key.setter
    def socplt_key(self, value):
        self._socplt_key = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.socplt_key:
            if hasattr(self.socplt_key, 'to_alipay_dict'):
                params['socplt_key'] = self.socplt_key.to_alipay_dict()
            else:
                params['socplt_key'] = self.socplt_key
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
        o = AlipaySecurityProdEventActionModifyModel()
        if 'msg' in d:
            o.msg = d['msg']
        if 'socplt_key' in d:
            o.socplt_key = d['socplt_key']
        if 'status' in d:
            o.status = d['status']
        return o


