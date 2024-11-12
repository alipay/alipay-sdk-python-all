#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMallWalletruleSetModel(object):

    def __init__(self):
        self._digital_shop_id_list = None
        self._mall_id = None
        self._type = None
        self._wallet_template_id = None
        self._wallet_template_pid = None

    @property
    def digital_shop_id_list(self):
        return self._digital_shop_id_list

    @digital_shop_id_list.setter
    def digital_shop_id_list(self, value):
        if isinstance(value, list):
            self._digital_shop_id_list = list()
            for i in value:
                self._digital_shop_id_list.append(i)
    @property
    def mall_id(self):
        return self._mall_id

    @mall_id.setter
    def mall_id(self, value):
        self._mall_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def wallet_template_id(self):
        return self._wallet_template_id

    @wallet_template_id.setter
    def wallet_template_id(self, value):
        self._wallet_template_id = value
    @property
    def wallet_template_pid(self):
        return self._wallet_template_pid

    @wallet_template_pid.setter
    def wallet_template_pid(self, value):
        self._wallet_template_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.digital_shop_id_list:
            if isinstance(self.digital_shop_id_list, list):
                for i in range(0, len(self.digital_shop_id_list)):
                    element = self.digital_shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.digital_shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.digital_shop_id_list, 'to_alipay_dict'):
                params['digital_shop_id_list'] = self.digital_shop_id_list.to_alipay_dict()
            else:
                params['digital_shop_id_list'] = self.digital_shop_id_list
        if self.mall_id:
            if hasattr(self.mall_id, 'to_alipay_dict'):
                params['mall_id'] = self.mall_id.to_alipay_dict()
            else:
                params['mall_id'] = self.mall_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.wallet_template_id:
            if hasattr(self.wallet_template_id, 'to_alipay_dict'):
                params['wallet_template_id'] = self.wallet_template_id.to_alipay_dict()
            else:
                params['wallet_template_id'] = self.wallet_template_id
        if self.wallet_template_pid:
            if hasattr(self.wallet_template_pid, 'to_alipay_dict'):
                params['wallet_template_pid'] = self.wallet_template_pid.to_alipay_dict()
            else:
                params['wallet_template_pid'] = self.wallet_template_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMallWalletruleSetModel()
        if 'digital_shop_id_list' in d:
            o.digital_shop_id_list = d['digital_shop_id_list']
        if 'mall_id' in d:
            o.mall_id = d['mall_id']
        if 'type' in d:
            o.type = d['type']
        if 'wallet_template_id' in d:
            o.wallet_template_id = d['wallet_template_id']
        if 'wallet_template_pid' in d:
            o.wallet_template_pid = d['wallet_template_pid']
        return o


