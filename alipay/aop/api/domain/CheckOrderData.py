#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckItemData import CheckItemData


class CheckOrderData(object):

    def __init__(self):
        self._check_item_list = None
        self._check_no = None

    @property
    def check_item_list(self):
        return self._check_item_list

    @check_item_list.setter
    def check_item_list(self, value):
        if isinstance(value, list):
            self._check_item_list = list()
            for i in value:
                if isinstance(i, CheckItemData):
                    self._check_item_list.append(i)
                else:
                    self._check_item_list.append(CheckItemData.from_alipay_dict(i))
    @property
    def check_no(self):
        return self._check_no

    @check_no.setter
    def check_no(self, value):
        self._check_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_item_list:
            if isinstance(self.check_item_list, list):
                for i in range(0, len(self.check_item_list)):
                    element = self.check_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_item_list[i] = element.to_alipay_dict()
            if hasattr(self.check_item_list, 'to_alipay_dict'):
                params['check_item_list'] = self.check_item_list.to_alipay_dict()
            else:
                params['check_item_list'] = self.check_item_list
        if self.check_no:
            if hasattr(self.check_no, 'to_alipay_dict'):
                params['check_no'] = self.check_no.to_alipay_dict()
            else:
                params['check_no'] = self.check_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckOrderData()
        if 'check_item_list' in d:
            o.check_item_list = d['check_item_list']
        if 'check_no' in d:
            o.check_no = d['check_no']
        return o


