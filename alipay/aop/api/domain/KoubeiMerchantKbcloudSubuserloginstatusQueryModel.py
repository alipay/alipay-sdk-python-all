#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantKbcloudSubuserloginstatusQueryModel(object):

    def __init__(self):
        self._session_id = None
        self._sub_user_id = None

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def sub_user_id(self):
        return self._sub_user_id

    @sub_user_id.setter
    def sub_user_id(self, value):
        self._sub_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.sub_user_id:
            if hasattr(self.sub_user_id, 'to_alipay_dict'):
                params['sub_user_id'] = self.sub_user_id.to_alipay_dict()
            else:
                params['sub_user_id'] = self.sub_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantKbcloudSubuserloginstatusQueryModel()
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'sub_user_id' in d:
            o.sub_user_id = d['sub_user_id']
        return o


