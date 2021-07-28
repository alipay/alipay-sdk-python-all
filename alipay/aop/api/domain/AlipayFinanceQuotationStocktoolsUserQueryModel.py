#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinanceQuotationStocktoolsUserQueryModel(object):

    def __init__(self):
        self._inst_org_id = None
        self._tool_type = None
        self._user_id = None

    @property
    def inst_org_id(self):
        return self._inst_org_id

    @inst_org_id.setter
    def inst_org_id(self, value):
        self._inst_org_id = value
    @property
    def tool_type(self):
        return self._tool_type

    @tool_type.setter
    def tool_type(self, value):
        self._tool_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_org_id:
            if hasattr(self.inst_org_id, 'to_alipay_dict'):
                params['inst_org_id'] = self.inst_org_id.to_alipay_dict()
            else:
                params['inst_org_id'] = self.inst_org_id
        if self.tool_type:
            if hasattr(self.tool_type, 'to_alipay_dict'):
                params['tool_type'] = self.tool_type.to_alipay_dict()
            else:
                params['tool_type'] = self.tool_type
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
        o = AlipayFinanceQuotationStocktoolsUserQueryModel()
        if 'inst_org_id' in d:
            o.inst_org_id = d['inst_org_id']
        if 'tool_type' in d:
            o.tool_type = d['tool_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


