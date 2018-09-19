#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbdishEstimatedInfo import KbdishEstimatedInfo


class KoubeiCateringDishEstimatedSyncModel(object):

    def __init__(self):
        self._biz_type = None
        self._kbdish_estimated_list = None
        self._syn_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def kbdish_estimated_list(self):
        return self._kbdish_estimated_list

    @kbdish_estimated_list.setter
    def kbdish_estimated_list(self, value):
        if isinstance(value, list):
            self._kbdish_estimated_list = list()
            for i in value:
                if isinstance(i, KbdishEstimatedInfo):
                    self._kbdish_estimated_list.append(i)
                else:
                    self._kbdish_estimated_list.append(KbdishEstimatedInfo.from_alipay_dict(i))
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.kbdish_estimated_list:
            if isinstance(self.kbdish_estimated_list, list):
                for i in range(0, len(self.kbdish_estimated_list)):
                    element = self.kbdish_estimated_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kbdish_estimated_list[i] = element.to_alipay_dict()
            if hasattr(self.kbdish_estimated_list, 'to_alipay_dict'):
                params['kbdish_estimated_list'] = self.kbdish_estimated_list.to_alipay_dict()
            else:
                params['kbdish_estimated_list'] = self.kbdish_estimated_list
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishEstimatedSyncModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'kbdish_estimated_list' in d:
            o.kbdish_estimated_list = d['kbdish_estimated_list']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


