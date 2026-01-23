#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcActivityGrayModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._ant_shop_id = None
        self._gray_account_list = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def ant_shop_id(self):
        return self._ant_shop_id

    @ant_shop_id.setter
    def ant_shop_id(self, value):
        self._ant_shop_id = value
    @property
    def gray_account_list(self):
        return self._gray_account_list

    @gray_account_list.setter
    def gray_account_list(self, value):
        if isinstance(value, list):
            self._gray_account_list = list()
            for i in value:
                self._gray_account_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.ant_shop_id:
            if hasattr(self.ant_shop_id, 'to_alipay_dict'):
                params['ant_shop_id'] = self.ant_shop_id.to_alipay_dict()
            else:
                params['ant_shop_id'] = self.ant_shop_id
        if self.gray_account_list:
            if isinstance(self.gray_account_list, list):
                for i in range(0, len(self.gray_account_list)):
                    element = self.gray_account_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gray_account_list[i] = element.to_alipay_dict()
            if hasattr(self.gray_account_list, 'to_alipay_dict'):
                params['gray_account_list'] = self.gray_account_list.to_alipay_dict()
            else:
                params['gray_account_list'] = self.gray_account_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcActivityGrayModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'ant_shop_id' in d:
            o.ant_shop_id = d['ant_shop_id']
        if 'gray_account_list' in d:
            o.gray_account_list = d['gray_account_list']
        return o


