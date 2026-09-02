#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TpaBillDataDTO import TpaBillDataDTO


class AlipayCommerceInsuranceTpabilldataSyncModel(object):

    def __init__(self):
        self._tpa_bill_data_list = None
        self._tpa_id = None

    @property
    def tpa_bill_data_list(self):
        return self._tpa_bill_data_list

    @tpa_bill_data_list.setter
    def tpa_bill_data_list(self, value):
        if isinstance(value, list):
            self._tpa_bill_data_list = list()
            for i in value:
                if isinstance(i, TpaBillDataDTO):
                    self._tpa_bill_data_list.append(i)
                else:
                    self._tpa_bill_data_list.append(TpaBillDataDTO.from_alipay_dict(i))
    @property
    def tpa_id(self):
        return self._tpa_id

    @tpa_id.setter
    def tpa_id(self, value):
        self._tpa_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tpa_bill_data_list:
            if isinstance(self.tpa_bill_data_list, list):
                for i in range(0, len(self.tpa_bill_data_list)):
                    element = self.tpa_bill_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tpa_bill_data_list[i] = element.to_alipay_dict()
            if hasattr(self.tpa_bill_data_list, 'to_alipay_dict'):
                params['tpa_bill_data_list'] = self.tpa_bill_data_list.to_alipay_dict()
            else:
                params['tpa_bill_data_list'] = self.tpa_bill_data_list
        if self.tpa_id:
            if hasattr(self.tpa_id, 'to_alipay_dict'):
                params['tpa_id'] = self.tpa_id.to_alipay_dict()
            else:
                params['tpa_id'] = self.tpa_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceInsuranceTpabilldataSyncModel()
        if 'tpa_bill_data_list' in d:
            o.tpa_bill_data_list = d['tpa_bill_data_list']
        if 'tpa_id' in d:
            o.tpa_id = d['tpa_id']
        return o


