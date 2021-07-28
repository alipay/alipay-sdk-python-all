#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTransferBalanceQueryModel(object):

    def __init__(self):
        self._account_alias = None
        self._pass_through_info = None

    @property
    def account_alias(self):
        return self._account_alias

    @account_alias.setter
    def account_alias(self, value):
        self._account_alias = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_alias:
            if hasattr(self.account_alias, 'to_alipay_dict'):
                params['account_alias'] = self.account_alias.to_alipay_dict()
            else:
                params['account_alias'] = self.account_alias
        if self.pass_through_info:
            if hasattr(self.pass_through_info, 'to_alipay_dict'):
                params['pass_through_info'] = self.pass_through_info.to_alipay_dict()
            else:
                params['pass_through_info'] = self.pass_through_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTransferBalanceQueryModel()
        if 'account_alias' in d:
            o.account_alias = d['account_alias']
        if 'pass_through_info' in d:
            o.pass_through_info = d['pass_through_info']
        return o


