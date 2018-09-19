#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCustomertagSaveModel(object):

    def __init__(self):
        self._biz_type = None
        self._tag_name = None
        self._tag_value = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def tag_value(self):
        return self._tag_value

    @tag_value.setter
    def tag_value(self, value):
        self._tag_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.tag_value:
            if hasattr(self.tag_value, 'to_alipay_dict'):
                params['tag_value'] = self.tag_value.to_alipay_dict()
            else:
                params['tag_value'] = self.tag_value
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
        o = AlipayUserCustomertagSaveModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'tag_value' in d:
            o.tag_value = d['tag_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


