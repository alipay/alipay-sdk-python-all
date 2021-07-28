#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SingleDynamicData import SingleDynamicData


class AlipaySocialBaseMessageDynamicicondataModifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._op_data = None
        self._op_type = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def op_data(self):
        return self._op_data

    @op_data.setter
    def op_data(self, value):
        if isinstance(value, SingleDynamicData):
            self._op_data = value
        else:
            self._op_data = SingleDynamicData.from_alipay_dict(value)
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.op_data:
            if hasattr(self.op_data, 'to_alipay_dict'):
                params['op_data'] = self.op_data.to_alipay_dict()
            else:
                params['op_data'] = self.op_data
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
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
        o = AlipaySocialBaseMessageDynamicicondataModifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'op_data' in d:
            o.op_data = d['op_data']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


