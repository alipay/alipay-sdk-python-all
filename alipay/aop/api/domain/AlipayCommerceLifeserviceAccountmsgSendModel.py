#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceAccountmsgSendModel(object):

    def __init__(self):
        self._settle_account_id_list = None

    @property
    def settle_account_id_list(self):
        return self._settle_account_id_list

    @settle_account_id_list.setter
    def settle_account_id_list(self, value):
        if isinstance(value, list):
            self._settle_account_id_list = list()
            for i in value:
                self._settle_account_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.settle_account_id_list:
            if isinstance(self.settle_account_id_list, list):
                for i in range(0, len(self.settle_account_id_list)):
                    element = self.settle_account_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_account_id_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_account_id_list, 'to_alipay_dict'):
                params['settle_account_id_list'] = self.settle_account_id_list.to_alipay_dict()
            else:
                params['settle_account_id_list'] = self.settle_account_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceAccountmsgSendModel()
        if 'settle_account_id_list' in d:
            o.settle_account_id_list = d['settle_account_id_list']
        return o


