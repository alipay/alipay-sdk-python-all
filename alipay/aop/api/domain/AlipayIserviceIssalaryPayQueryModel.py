#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIssalaryPayQueryModel(object):

    def __init__(self):
        self._user_bill_no_list = None

    @property
    def user_bill_no_list(self):
        return self._user_bill_no_list

    @user_bill_no_list.setter
    def user_bill_no_list(self, value):
        if isinstance(value, list):
            self._user_bill_no_list = list()
            for i in value:
                self._user_bill_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.user_bill_no_list:
            if isinstance(self.user_bill_no_list, list):
                for i in range(0, len(self.user_bill_no_list)):
                    element = self.user_bill_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_bill_no_list[i] = element.to_alipay_dict()
            if hasattr(self.user_bill_no_list, 'to_alipay_dict'):
                params['user_bill_no_list'] = self.user_bill_no_list.to_alipay_dict()
            else:
                params['user_bill_no_list'] = self.user_bill_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIssalaryPayQueryModel()
        if 'user_bill_no_list' in d:
            o.user_bill_no_list = d['user_bill_no_list']
        return o


