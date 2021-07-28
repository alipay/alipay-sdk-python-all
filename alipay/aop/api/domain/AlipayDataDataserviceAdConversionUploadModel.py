#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConversionData import ConversionData


class AlipayDataDataserviceAdConversionUploadModel(object):

    def __init__(self):
        self._biz_token = None
        self._conversion_data_list = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def conversion_data_list(self):
        return self._conversion_data_list

    @conversion_data_list.setter
    def conversion_data_list(self, value):
        if isinstance(value, list):
            self._conversion_data_list = list()
            for i in value:
                if isinstance(i, ConversionData):
                    self._conversion_data_list.append(i)
                else:
                    self._conversion_data_list.append(ConversionData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.conversion_data_list:
            if isinstance(self.conversion_data_list, list):
                for i in range(0, len(self.conversion_data_list)):
                    element = self.conversion_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conversion_data_list[i] = element.to_alipay_dict()
            if hasattr(self.conversion_data_list, 'to_alipay_dict'):
                params['conversion_data_list'] = self.conversion_data_list.to_alipay_dict()
            else:
                params['conversion_data_list'] = self.conversion_data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdConversionUploadModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'conversion_data_list' in d:
            o.conversion_data_list = d['conversion_data_list']
        return o


