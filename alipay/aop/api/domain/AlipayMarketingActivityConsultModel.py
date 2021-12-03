#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultActivityInfo import ConsultActivityInfo


class AlipayMarketingActivityConsultModel(object):

    def __init__(self):
        self._consult_activity_info_list = None
        self._merchant_id = None
        self._user_id = None

    @property
    def consult_activity_info_list(self):
        return self._consult_activity_info_list

    @consult_activity_info_list.setter
    def consult_activity_info_list(self, value):
        if isinstance(value, list):
            self._consult_activity_info_list = list()
            for i in value:
                if isinstance(i, ConsultActivityInfo):
                    self._consult_activity_info_list.append(i)
                else:
                    self._consult_activity_info_list.append(ConsultActivityInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_activity_info_list:
            if isinstance(self.consult_activity_info_list, list):
                for i in range(0, len(self.consult_activity_info_list)):
                    element = self.consult_activity_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.consult_activity_info_list[i] = element.to_alipay_dict()
            if hasattr(self.consult_activity_info_list, 'to_alipay_dict'):
                params['consult_activity_info_list'] = self.consult_activity_info_list.to_alipay_dict()
            else:
                params['consult_activity_info_list'] = self.consult_activity_info_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
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
        o = AlipayMarketingActivityConsultModel()
        if 'consult_activity_info_list' in d:
            o.consult_activity_info_list = d['consult_activity_info_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


