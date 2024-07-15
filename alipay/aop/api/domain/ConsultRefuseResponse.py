#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultRefuseResponse(object):

    def __init__(self):
        self._channel = None
        self._refuse_code = None
        self._refuse_msg = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.refuse_code:
            if hasattr(self.refuse_code, 'to_alipay_dict'):
                params['refuse_code'] = self.refuse_code.to_alipay_dict()
            else:
                params['refuse_code'] = self.refuse_code
        if self.refuse_msg:
            if hasattr(self.refuse_msg, 'to_alipay_dict'):
                params['refuse_msg'] = self.refuse_msg.to_alipay_dict()
            else:
                params['refuse_msg'] = self.refuse_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultRefuseResponse()
        if 'channel' in d:
            o.channel = d['channel']
        if 'refuse_code' in d:
            o.refuse_code = d['refuse_code']
        if 'refuse_msg' in d:
            o.refuse_msg = d['refuse_msg']
        return o


