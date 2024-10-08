#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardOrderSetModel(object):

    def __init__(self):
        self._cancel_period_list = None
        self._card_id = None
        self._open_id = None
        self._operation_type = None
        self._user_id = None

    @property
    def cancel_period_list(self):
        return self._cancel_period_list

    @cancel_period_list.setter
    def cancel_period_list(self, value):
        if isinstance(value, list):
            self._cancel_period_list = list()
            for i in value:
                self._cancel_period_list.append(i)
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_period_list:
            if isinstance(self.cancel_period_list, list):
                for i in range(0, len(self.cancel_period_list)):
                    element = self.cancel_period_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cancel_period_list[i] = element.to_alipay_dict()
            if hasattr(self.cancel_period_list, 'to_alipay_dict'):
                params['cancel_period_list'] = self.cancel_period_list.to_alipay_dict()
            else:
                params['cancel_period_list'] = self.cancel_period_list
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
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
        o = AlipayCommerceMerchantcardOrderSetModel()
        if 'cancel_period_list' in d:
            o.cancel_period_list = d['cancel_period_list']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


