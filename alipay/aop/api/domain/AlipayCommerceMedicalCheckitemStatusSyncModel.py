#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckOrderData import CheckOrderData


class AlipayCommerceMedicalCheckitemStatusSyncModel(object):

    def __init__(self):
        self._check_item_data_list = None
        self._fulfillment_no = None
        self._fulfillment_on = None
        self._open_id = None
        self._type = None
        self._user_id = None

    @property
    def check_item_data_list(self):
        return self._check_item_data_list

    @check_item_data_list.setter
    def check_item_data_list(self, value):
        if isinstance(value, list):
            self._check_item_data_list = list()
            for i in value:
                if isinstance(i, CheckOrderData):
                    self._check_item_data_list.append(i)
                else:
                    self._check_item_data_list.append(CheckOrderData.from_alipay_dict(i))
    @property
    def fulfillment_no(self):
        return self._fulfillment_no

    @fulfillment_no.setter
    def fulfillment_no(self, value):
        self._fulfillment_no = value
    @property
    def fulfillment_on(self):
        return self._fulfillment_on

    @fulfillment_on.setter
    def fulfillment_on(self, value):
        self._fulfillment_on = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_item_data_list:
            if isinstance(self.check_item_data_list, list):
                for i in range(0, len(self.check_item_data_list)):
                    element = self.check_item_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_item_data_list[i] = element.to_alipay_dict()
            if hasattr(self.check_item_data_list, 'to_alipay_dict'):
                params['check_item_data_list'] = self.check_item_data_list.to_alipay_dict()
            else:
                params['check_item_data_list'] = self.check_item_data_list
        if self.fulfillment_no:
            if hasattr(self.fulfillment_no, 'to_alipay_dict'):
                params['fulfillment_no'] = self.fulfillment_no.to_alipay_dict()
            else:
                params['fulfillment_no'] = self.fulfillment_no
        if self.fulfillment_on:
            if hasattr(self.fulfillment_on, 'to_alipay_dict'):
                params['fulfillment_on'] = self.fulfillment_on.to_alipay_dict()
            else:
                params['fulfillment_on'] = self.fulfillment_on
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayCommerceMedicalCheckitemStatusSyncModel()
        if 'check_item_data_list' in d:
            o.check_item_data_list = d['check_item_data_list']
        if 'fulfillment_no' in d:
            o.fulfillment_no = d['fulfillment_no']
        if 'fulfillment_on' in d:
            o.fulfillment_on = d['fulfillment_on']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


