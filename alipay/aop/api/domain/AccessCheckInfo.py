#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessCheckItemInfo import AccessCheckItemInfo


class AccessCheckInfo(object):

    def __init__(self):
        self._access_check = None
        self._check_item_info_list = None

    @property
    def access_check(self):
        return self._access_check

    @access_check.setter
    def access_check(self, value):
        self._access_check = value
    @property
    def check_item_info_list(self):
        return self._check_item_info_list

    @check_item_info_list.setter
    def check_item_info_list(self, value):
        if isinstance(value, list):
            self._check_item_info_list = list()
            for i in value:
                if isinstance(i, AccessCheckItemInfo):
                    self._check_item_info_list.append(i)
                else:
                    self._check_item_info_list.append(AccessCheckItemInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.access_check:
            if hasattr(self.access_check, 'to_alipay_dict'):
                params['access_check'] = self.access_check.to_alipay_dict()
            else:
                params['access_check'] = self.access_check
        if self.check_item_info_list:
            if isinstance(self.check_item_info_list, list):
                for i in range(0, len(self.check_item_info_list)):
                    element = self.check_item_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_item_info_list[i] = element.to_alipay_dict()
            if hasattr(self.check_item_info_list, 'to_alipay_dict'):
                params['check_item_info_list'] = self.check_item_info_list.to_alipay_dict()
            else:
                params['check_item_info_list'] = self.check_item_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AccessCheckInfo()
        if 'access_check' in d:
            o.access_check = d['access_check']
        if 'check_item_info_list' in d:
            o.check_item_info_list = d['check_item_info_list']
        return o


