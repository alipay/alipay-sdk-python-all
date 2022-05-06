#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotVspOrgUserDeleteNotifyUserInfoRequest(object):

    def __init__(self):
        self._msg = None
        self._state = None
        self._vid = None

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg:
            if hasattr(self.msg, 'to_alipay_dict'):
                params['msg'] = self.msg.to_alipay_dict()
            else:
                params['msg'] = self.msg
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotVspOrgUserDeleteNotifyUserInfoRequest()
        if 'msg' in d:
            o.msg = d['msg']
        if 'state' in d:
            o.state = d['state']
        if 'vid' in d:
            o.vid = d['vid']
        return o


