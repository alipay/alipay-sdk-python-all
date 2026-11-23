#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRetailCashbackplanModifyModel(object):

    def __init__(self):
        self._delivery_plan_id = None
        self._target_status = None
        self._white_list_users = None

    @property
    def delivery_plan_id(self):
        return self._delivery_plan_id

    @delivery_plan_id.setter
    def delivery_plan_id(self, value):
        self._delivery_plan_id = value
    @property
    def target_status(self):
        return self._target_status

    @target_status.setter
    def target_status(self, value):
        self._target_status = value
    @property
    def white_list_users(self):
        return self._white_list_users

    @white_list_users.setter
    def white_list_users(self, value):
        if isinstance(value, list):
            self._white_list_users = list()
            for i in value:
                self._white_list_users.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_plan_id:
            if hasattr(self.delivery_plan_id, 'to_alipay_dict'):
                params['delivery_plan_id'] = self.delivery_plan_id.to_alipay_dict()
            else:
                params['delivery_plan_id'] = self.delivery_plan_id
        if self.target_status:
            if hasattr(self.target_status, 'to_alipay_dict'):
                params['target_status'] = self.target_status.to_alipay_dict()
            else:
                params['target_status'] = self.target_status
        if self.white_list_users:
            if isinstance(self.white_list_users, list):
                for i in range(0, len(self.white_list_users)):
                    element = self.white_list_users[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.white_list_users[i] = element.to_alipay_dict()
            if hasattr(self.white_list_users, 'to_alipay_dict'):
                params['white_list_users'] = self.white_list_users.to_alipay_dict()
            else:
                params['white_list_users'] = self.white_list_users
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRetailCashbackplanModifyModel()
        if 'delivery_plan_id' in d:
            o.delivery_plan_id = d['delivery_plan_id']
        if 'target_status' in d:
            o.target_status = d['target_status']
        if 'white_list_users' in d:
            o.white_list_users = d['white_list_users']
        return o


