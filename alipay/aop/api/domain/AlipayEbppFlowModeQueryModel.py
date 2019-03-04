#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppFlowModeQueryModel(object):

    def __init__(self):
        self._ext_msg = None
        self._mobile = None
        self._user_id = None

    @property
    def ext_msg(self):
        return self._ext_msg

    @ext_msg.setter
    def ext_msg(self, value):
        self._ext_msg = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_msg:
            if hasattr(self.ext_msg, 'to_alipay_dict'):
                params['ext_msg'] = self.ext_msg.to_alipay_dict()
            else:
                params['ext_msg'] = self.ext_msg
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppFlowModeQueryModel()
        if 'ext_msg' in d:
            o.ext_msg = d['ext_msg']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


