#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountBaseInfo import SubAccountBaseInfo


class SubAccountBalanceQueryOrder(object):

    def __init__(self):
        self._sub_account_base_info = None

    @property
    def sub_account_base_info(self):
        return self._sub_account_base_info

    @sub_account_base_info.setter
    def sub_account_base_info(self, value):
        if isinstance(value, SubAccountBaseInfo):
            self._sub_account_base_info = value
        else:
            self._sub_account_base_info = SubAccountBaseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_base_info:
            if hasattr(self.sub_account_base_info, 'to_alipay_dict'):
                params['sub_account_base_info'] = self.sub_account_base_info.to_alipay_dict()
            else:
                params['sub_account_base_info'] = self.sub_account_base_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountBalanceQueryOrder()
        if 'sub_account_base_info' in d:
            o.sub_account_base_info = d['sub_account_base_info']
        return o


