#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MessageReceiveVO(object):

    def __init__(self):
        self._msg_enum = None
        self._msg_receive_state = None

    @property
    def msg_enum(self):
        return self._msg_enum

    @msg_enum.setter
    def msg_enum(self, value):
        self._msg_enum = value
    @property
    def msg_receive_state(self):
        return self._msg_receive_state

    @msg_receive_state.setter
    def msg_receive_state(self, value):
        self._msg_receive_state = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_enum:
            if hasattr(self.msg_enum, 'to_alipay_dict'):
                params['msg_enum'] = self.msg_enum.to_alipay_dict()
            else:
                params['msg_enum'] = self.msg_enum
        if self.msg_receive_state:
            if hasattr(self.msg_receive_state, 'to_alipay_dict'):
                params['msg_receive_state'] = self.msg_receive_state.to_alipay_dict()
            else:
                params['msg_receive_state'] = self.msg_receive_state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MessageReceiveVO()
        if 'msg_enum' in d:
            o.msg_enum = d['msg_enum']
        if 'msg_receive_state' in d:
            o.msg_receive_state = d['msg_receive_state']
        return o


