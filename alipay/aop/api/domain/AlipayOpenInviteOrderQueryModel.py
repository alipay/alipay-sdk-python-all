#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInviteOrderQueryModel(object):

    def __init__(self):
        self._alipay_logon_id = None
        self._isv_biz_id = None

    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def isv_biz_id(self):
        return self._isv_biz_id

    @isv_biz_id.setter
    def isv_biz_id(self, value):
        self._isv_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.isv_biz_id:
            if hasattr(self.isv_biz_id, 'to_alipay_dict'):
                params['isv_biz_id'] = self.isv_biz_id.to_alipay_dict()
            else:
                params['isv_biz_id'] = self.isv_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInviteOrderQueryModel()
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'isv_biz_id' in d:
            o.isv_biz_id = d['isv_biz_id']
        return o


