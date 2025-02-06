#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SceneCommissionInfo import SceneCommissionInfo


class AlipayOpenSpCommissionCreateModel(object):

    def __init__(self):
        self._commission_info_list = None
        self._merchant_id = None
        self._merchant_logon_id = None
        self._merchant_name = None

    @property
    def commission_info_list(self):
        return self._commission_info_list

    @commission_info_list.setter
    def commission_info_list(self, value):
        if isinstance(value, list):
            self._commission_info_list = list()
            for i in value:
                if isinstance(i, SceneCommissionInfo):
                    self._commission_info_list.append(i)
                else:
                    self._commission_info_list.append(SceneCommissionInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_info_list:
            if isinstance(self.commission_info_list, list):
                for i in range(0, len(self.commission_info_list)):
                    element = self.commission_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commission_info_list[i] = element.to_alipay_dict()
            if hasattr(self.commission_info_list, 'to_alipay_dict'):
                params['commission_info_list'] = self.commission_info_list.to_alipay_dict()
            else:
                params['commission_info_list'] = self.commission_info_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_logon_id:
            if hasattr(self.merchant_logon_id, 'to_alipay_dict'):
                params['merchant_logon_id'] = self.merchant_logon_id.to_alipay_dict()
            else:
                params['merchant_logon_id'] = self.merchant_logon_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpCommissionCreateModel()
        if 'commission_info_list' in d:
            o.commission_info_list = d['commission_info_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_logon_id' in d:
            o.merchant_logon_id = d['merchant_logon_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        return o


