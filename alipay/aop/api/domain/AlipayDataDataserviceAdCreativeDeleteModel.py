#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdCreativeDeleteModel(object):

    def __init__(self):
        self._biz_token = None
        self._creative_outer_id_list = None
        self._deal_id = None
        self._deal_type = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def creative_outer_id_list(self):
        return self._creative_outer_id_list

    @creative_outer_id_list.setter
    def creative_outer_id_list(self, value):
        if isinstance(value, list):
            self._creative_outer_id_list = list()
            for i in value:
                self._creative_outer_id_list.append(i)
    @property
    def deal_id(self):
        return self._deal_id

    @deal_id.setter
    def deal_id(self, value):
        self._deal_id = value
    @property
    def deal_type(self):
        return self._deal_type

    @deal_type.setter
    def deal_type(self, value):
        self._deal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.creative_outer_id_list:
            if isinstance(self.creative_outer_id_list, list):
                for i in range(0, len(self.creative_outer_id_list)):
                    element = self.creative_outer_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_outer_id_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_outer_id_list, 'to_alipay_dict'):
                params['creative_outer_id_list'] = self.creative_outer_id_list.to_alipay_dict()
            else:
                params['creative_outer_id_list'] = self.creative_outer_id_list
        if self.deal_id:
            if hasattr(self.deal_id, 'to_alipay_dict'):
                params['deal_id'] = self.deal_id.to_alipay_dict()
            else:
                params['deal_id'] = self.deal_id
        if self.deal_type:
            if hasattr(self.deal_type, 'to_alipay_dict'):
                params['deal_type'] = self.deal_type.to_alipay_dict()
            else:
                params['deal_type'] = self.deal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdCreativeDeleteModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'creative_outer_id_list' in d:
            o.creative_outer_id_list = d['creative_outer_id_list']
        if 'deal_id' in d:
            o.deal_id = d['deal_id']
        if 'deal_type' in d:
            o.deal_type = d['deal_type']
        return o


