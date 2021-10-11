#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockStocktoolDeliverQueryModel(object):

    def __init__(self):
        self._position_list = None
        self._user_id = None

    @property
    def position_list(self):
        return self._position_list

    @position_list.setter
    def position_list(self, value):
        if isinstance(value, list):
            self._position_list = list()
            for i in value:
                self._position_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.position_list:
            if isinstance(self.position_list, list):
                for i in range(0, len(self.position_list)):
                    element = self.position_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position_list[i] = element.to_alipay_dict()
            if hasattr(self.position_list, 'to_alipay_dict'):
                params['position_list'] = self.position_list.to_alipay_dict()
            else:
                params['position_list'] = self.position_list
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
        o = AntfortuneStockStocktoolDeliverQueryModel()
        if 'position_list' in d:
            o.position_list = d['position_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


