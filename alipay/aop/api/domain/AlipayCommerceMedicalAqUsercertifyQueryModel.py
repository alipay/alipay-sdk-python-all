#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAqUsercertifyQueryModel(object):

    def __init__(self):
        self._access_token = None
        self._aq_sub_id = None
        self._biz_app_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def aq_sub_id(self):
        return self._aq_sub_id

    @aq_sub_id.setter
    def aq_sub_id(self, value):
        self._aq_sub_id = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.aq_sub_id:
            if hasattr(self.aq_sub_id, 'to_alipay_dict'):
                params['aq_sub_id'] = self.aq_sub_id.to_alipay_dict()
            else:
                params['aq_sub_id'] = self.aq_sub_id
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAqUsercertifyQueryModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'aq_sub_id' in d:
            o.aq_sub_id = d['aq_sub_id']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        return o


