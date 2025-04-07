#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanTriggerActionExtInfo import ConsumerLoanTriggerActionExtInfo


class AlipayCommerceBillEventTriggerModel(object):

    def __init__(self):
        self._action_ext_info = None
        self._bill_id_list = None
        self._open_id = None
        self._user_id = None

    @property
    def action_ext_info(self):
        return self._action_ext_info

    @action_ext_info.setter
    def action_ext_info(self, value):
        if isinstance(value, ConsumerLoanTriggerActionExtInfo):
            self._action_ext_info = value
        else:
            self._action_ext_info = ConsumerLoanTriggerActionExtInfo.from_alipay_dict(value)
    @property
    def bill_id_list(self):
        return self._bill_id_list

    @bill_id_list.setter
    def bill_id_list(self, value):
        if isinstance(value, list):
            self._bill_id_list = list()
            for i in value:
                self._bill_id_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_ext_info:
            if hasattr(self.action_ext_info, 'to_alipay_dict'):
                params['action_ext_info'] = self.action_ext_info.to_alipay_dict()
            else:
                params['action_ext_info'] = self.action_ext_info
        if self.bill_id_list:
            if isinstance(self.bill_id_list, list):
                for i in range(0, len(self.bill_id_list)):
                    element = self.bill_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_id_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_id_list, 'to_alipay_dict'):
                params['bill_id_list'] = self.bill_id_list.to_alipay_dict()
            else:
                params['bill_id_list'] = self.bill_id_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = AlipayCommerceBillEventTriggerModel()
        if 'action_ext_info' in d:
            o.action_ext_info = d['action_ext_info']
        if 'bill_id_list' in d:
            o.bill_id_list = d['bill_id_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


