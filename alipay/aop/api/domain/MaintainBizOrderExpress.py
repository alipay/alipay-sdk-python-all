#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaintainBizOrderExpress(object):

    def __init__(self):
        self._create_time = None
        self._express_code = None
        self._express_no = None
        self._sender_addr = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def express_code(self):
        return self._express_code

    @express_code.setter
    def express_code(self, value):
        self._express_code = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def sender_addr(self):
        return self._sender_addr

    @sender_addr.setter
    def sender_addr(self, value):
        self._sender_addr = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.express_code:
            if hasattr(self.express_code, 'to_alipay_dict'):
                params['express_code'] = self.express_code.to_alipay_dict()
            else:
                params['express_code'] = self.express_code
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
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
        o = MaintainBizOrderExpress()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'express_code' in d:
            o.express_code = d['express_code']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'sender_addr' in d:
            o.sender_addr = d['sender_addr']
        return o


