#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserAppBizDataInfo import UserAppBizDataInfo


class AlipayOpenMiniBizdataTemplatemessageUploadModel(object):

    def __init__(self):
        self._biz_data_list = None

    @property
    def biz_data_list(self):
        return self._biz_data_list

    @biz_data_list.setter
    def biz_data_list(self, value):
        if isinstance(value, list):
            self._biz_data_list = list()
            for i in value:
                if isinstance(i, UserAppBizDataInfo):
                    self._biz_data_list.append(i)
                else:
                    self._biz_data_list.append(UserAppBizDataInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data_list:
            if isinstance(self.biz_data_list, list):
                for i in range(0, len(self.biz_data_list)):
                    element = self.biz_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_data_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_data_list, 'to_alipay_dict'):
                params['biz_data_list'] = self.biz_data_list.to_alipay_dict()
            else:
                params['biz_data_list'] = self.biz_data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniBizdataTemplatemessageUploadModel()
        if 'biz_data_list' in d:
            o.biz_data_list = d['biz_data_list']
        return o


