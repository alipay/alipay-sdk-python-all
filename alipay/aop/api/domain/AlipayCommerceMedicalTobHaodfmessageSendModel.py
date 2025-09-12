#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalTobHaodfmessageSendModel(object):

    def __init__(self):
        self._msg_content = None
        self._type = None

    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalTobHaodfmessageSendModel()
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'type' in d:
            o.type = d['type']
        return o


