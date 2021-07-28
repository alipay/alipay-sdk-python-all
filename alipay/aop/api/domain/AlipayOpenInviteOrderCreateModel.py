#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenInviteOrderCreateModel(object):

    def __init__(self):
        self._isv_biz_id = None
        self._isv_return_url = None

    @property
    def isv_biz_id(self):
        return self._isv_biz_id

    @isv_biz_id.setter
    def isv_biz_id(self, value):
        self._isv_biz_id = value
    @property
    def isv_return_url(self):
        return self._isv_return_url

    @isv_return_url.setter
    def isv_return_url(self, value):
        self._isv_return_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_biz_id:
            if hasattr(self.isv_biz_id, 'to_alipay_dict'):
                params['isv_biz_id'] = self.isv_biz_id.to_alipay_dict()
            else:
                params['isv_biz_id'] = self.isv_biz_id
        if self.isv_return_url:
            if hasattr(self.isv_return_url, 'to_alipay_dict'):
                params['isv_return_url'] = self.isv_return_url.to_alipay_dict()
            else:
                params['isv_return_url'] = self.isv_return_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenInviteOrderCreateModel()
        if 'isv_biz_id' in d:
            o.isv_biz_id = d['isv_biz_id']
        if 'isv_return_url' in d:
            o.isv_return_url = d['isv_return_url']
        return o


