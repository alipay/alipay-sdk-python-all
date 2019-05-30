#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdOnlineModel(object):

    def __init__(self):
        self._biz_token = None
        self._op_type = None
        self._outer_id_list = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def outer_id_list(self):
        return self._outer_id_list

    @outer_id_list.setter
    def outer_id_list(self, value):
        if isinstance(value, list):
            self._outer_id_list = list()
            for i in value:
                self._outer_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.outer_id_list:
            if isinstance(self.outer_id_list, list):
                for i in range(0, len(self.outer_id_list)):
                    element = self.outer_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.outer_id_list[i] = element.to_alipay_dict()
            if hasattr(self.outer_id_list, 'to_alipay_dict'):
                params['outer_id_list'] = self.outer_id_list.to_alipay_dict()
            else:
                params['outer_id_list'] = self.outer_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdOnlineModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'outer_id_list' in d:
            o.outer_id_list = d['outer_id_list']
        return o


