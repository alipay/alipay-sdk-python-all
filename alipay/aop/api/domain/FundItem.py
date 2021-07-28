#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundItem(object):

    def __init__(self):
        self._amount = None
        self._fund_create_time = None
        self._fund_finish_time = None
        self._fund_in_out = None
        self._fund_modify_time = None
        self._fund_tool_type_name = None
        self._gmt_biz_create = None
        self._owner_card_no = None
        self._promo_fund_tool = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_create_time(self):
        return self._fund_create_time

    @fund_create_time.setter
    def fund_create_time(self, value):
        self._fund_create_time = value
    @property
    def fund_finish_time(self):
        return self._fund_finish_time

    @fund_finish_time.setter
    def fund_finish_time(self, value):
        self._fund_finish_time = value
    @property
    def fund_in_out(self):
        return self._fund_in_out

    @fund_in_out.setter
    def fund_in_out(self, value):
        self._fund_in_out = value
    @property
    def fund_modify_time(self):
        return self._fund_modify_time

    @fund_modify_time.setter
    def fund_modify_time(self, value):
        self._fund_modify_time = value
    @property
    def fund_tool_type_name(self):
        return self._fund_tool_type_name

    @fund_tool_type_name.setter
    def fund_tool_type_name(self, value):
        self._fund_tool_type_name = value
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def owner_card_no(self):
        return self._owner_card_no

    @owner_card_no.setter
    def owner_card_no(self, value):
        self._owner_card_no = value
    @property
    def promo_fund_tool(self):
        return self._promo_fund_tool

    @promo_fund_tool.setter
    def promo_fund_tool(self, value):
        self._promo_fund_tool = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_create_time:
            if hasattr(self.fund_create_time, 'to_alipay_dict'):
                params['fund_create_time'] = self.fund_create_time.to_alipay_dict()
            else:
                params['fund_create_time'] = self.fund_create_time
        if self.fund_finish_time:
            if hasattr(self.fund_finish_time, 'to_alipay_dict'):
                params['fund_finish_time'] = self.fund_finish_time.to_alipay_dict()
            else:
                params['fund_finish_time'] = self.fund_finish_time
        if self.fund_in_out:
            if hasattr(self.fund_in_out, 'to_alipay_dict'):
                params['fund_in_out'] = self.fund_in_out.to_alipay_dict()
            else:
                params['fund_in_out'] = self.fund_in_out
        if self.fund_modify_time:
            if hasattr(self.fund_modify_time, 'to_alipay_dict'):
                params['fund_modify_time'] = self.fund_modify_time.to_alipay_dict()
            else:
                params['fund_modify_time'] = self.fund_modify_time
        if self.fund_tool_type_name:
            if hasattr(self.fund_tool_type_name, 'to_alipay_dict'):
                params['fund_tool_type_name'] = self.fund_tool_type_name.to_alipay_dict()
            else:
                params['fund_tool_type_name'] = self.fund_tool_type_name
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.owner_card_no:
            if hasattr(self.owner_card_no, 'to_alipay_dict'):
                params['owner_card_no'] = self.owner_card_no.to_alipay_dict()
            else:
                params['owner_card_no'] = self.owner_card_no
        if self.promo_fund_tool:
            if hasattr(self.promo_fund_tool, 'to_alipay_dict'):
                params['promo_fund_tool'] = self.promo_fund_tool.to_alipay_dict()
            else:
                params['promo_fund_tool'] = self.promo_fund_tool
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundItem()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_create_time' in d:
            o.fund_create_time = d['fund_create_time']
        if 'fund_finish_time' in d:
            o.fund_finish_time = d['fund_finish_time']
        if 'fund_in_out' in d:
            o.fund_in_out = d['fund_in_out']
        if 'fund_modify_time' in d:
            o.fund_modify_time = d['fund_modify_time']
        if 'fund_tool_type_name' in d:
            o.fund_tool_type_name = d['fund_tool_type_name']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'owner_card_no' in d:
            o.owner_card_no = d['owner_card_no']
        if 'promo_fund_tool' in d:
            o.promo_fund_tool = d['promo_fund_tool']
        return o


