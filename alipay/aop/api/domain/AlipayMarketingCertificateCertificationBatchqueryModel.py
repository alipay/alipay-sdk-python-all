#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCertificateCertificationBatchqueryModel(object):

    def __init__(self):
        self._code_list = None
        self._open_id = None
        self._order_id = None
        self._user_id = None

    @property
    def code_list(self):
        return self._code_list

    @code_list.setter
    def code_list(self, value):
        if isinstance(value, list):
            self._code_list = list()
            for i in value:
                self._code_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_list:
            if isinstance(self.code_list, list):
                for i in range(0, len(self.code_list)):
                    element = self.code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.code_list[i] = element.to_alipay_dict()
            if hasattr(self.code_list, 'to_alipay_dict'):
                params['code_list'] = self.code_list.to_alipay_dict()
            else:
                params['code_list'] = self.code_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
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
        o = AlipayMarketingCertificateCertificationBatchqueryModel()
        if 'code_list' in d:
            o.code_list = d['code_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


