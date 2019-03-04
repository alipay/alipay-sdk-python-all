#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KdsInfoModel import KdsInfoModel


class KoubeiCateringKdsInfoModifyModel(object):

    def __init__(self):
        self._kds_info_model_list = None

    @property
    def kds_info_model_list(self):
        return self._kds_info_model_list

    @kds_info_model_list.setter
    def kds_info_model_list(self, value):
        if isinstance(value, list):
            self._kds_info_model_list = list()
            for i in value:
                if isinstance(i, KdsInfoModel):
                    self._kds_info_model_list.append(i)
                else:
                    self._kds_info_model_list.append(KdsInfoModel.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.kds_info_model_list:
            if isinstance(self.kds_info_model_list, list):
                for i in range(0, len(self.kds_info_model_list)):
                    element = self.kds_info_model_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kds_info_model_list[i] = element.to_alipay_dict()
            if hasattr(self.kds_info_model_list, 'to_alipay_dict'):
                params['kds_info_model_list'] = self.kds_info_model_list.to_alipay_dict()
            else:
                params['kds_info_model_list'] = self.kds_info_model_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringKdsInfoModifyModel()
        if 'kds_info_model_list' in d:
            o.kds_info_model_list = d['kds_info_model_list']
        return o


