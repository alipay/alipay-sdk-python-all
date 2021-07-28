#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdGroupQueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._group_outer_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def group_outer_id(self):
        return self._group_outer_id

    @group_outer_id.setter
    def group_outer_id(self, value):
        self._group_outer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.group_outer_id:
            if hasattr(self.group_outer_id, 'to_alipay_dict'):
                params['group_outer_id'] = self.group_outer_id.to_alipay_dict()
            else:
                params['group_outer_id'] = self.group_outer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdGroupQueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'group_outer_id' in d:
            o.group_outer_id = d['group_outer_id']
        return o


