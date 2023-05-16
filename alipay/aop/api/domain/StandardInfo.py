#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssetShareSourceInfo import AssetShareSourceInfo
from alipay.aop.api.domain.StandardConditionInfo import StandardConditionInfo


class StandardInfo(object):

    def __init__(self):
        self._asset_share_source_info = None
        self._consume_mode = None
        self._expense_type_sub_category = None
        self._open_rule_id = None
        self._outer_source_id = None
        self._payment_policy = None
        self._standard_condition_info_list = None
        self._standard_desc = None
        self._standard_id = None
        self._standard_name = None

    @property
    def asset_share_source_info(self):
        return self._asset_share_source_info

    @asset_share_source_info.setter
    def asset_share_source_info(self, value):
        if isinstance(value, AssetShareSourceInfo):
            self._asset_share_source_info = value
        else:
            self._asset_share_source_info = AssetShareSourceInfo.from_alipay_dict(value)
    @property
    def consume_mode(self):
        return self._consume_mode

    @consume_mode.setter
    def consume_mode(self, value):
        self._consume_mode = value
    @property
    def expense_type_sub_category(self):
        return self._expense_type_sub_category

    @expense_type_sub_category.setter
    def expense_type_sub_category(self, value):
        self._expense_type_sub_category = value
    @property
    def open_rule_id(self):
        return self._open_rule_id

    @open_rule_id.setter
    def open_rule_id(self, value):
        self._open_rule_id = value
    @property
    def outer_source_id(self):
        return self._outer_source_id

    @outer_source_id.setter
    def outer_source_id(self, value):
        self._outer_source_id = value
    @property
    def payment_policy(self):
        return self._payment_policy

    @payment_policy.setter
    def payment_policy(self, value):
        self._payment_policy = value
    @property
    def standard_condition_info_list(self):
        return self._standard_condition_info_list

    @standard_condition_info_list.setter
    def standard_condition_info_list(self, value):
        if isinstance(value, list):
            self._standard_condition_info_list = list()
            for i in value:
                if isinstance(i, StandardConditionInfo):
                    self._standard_condition_info_list.append(i)
                else:
                    self._standard_condition_info_list.append(StandardConditionInfo.from_alipay_dict(i))
    @property
    def standard_desc(self):
        return self._standard_desc

    @standard_desc.setter
    def standard_desc(self, value):
        self._standard_desc = value
    @property
    def standard_id(self):
        return self._standard_id

    @standard_id.setter
    def standard_id(self, value):
        self._standard_id = value
    @property
    def standard_name(self):
        return self._standard_name

    @standard_name.setter
    def standard_name(self, value):
        self._standard_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_share_source_info:
            if hasattr(self.asset_share_source_info, 'to_alipay_dict'):
                params['asset_share_source_info'] = self.asset_share_source_info.to_alipay_dict()
            else:
                params['asset_share_source_info'] = self.asset_share_source_info
        if self.consume_mode:
            if hasattr(self.consume_mode, 'to_alipay_dict'):
                params['consume_mode'] = self.consume_mode.to_alipay_dict()
            else:
                params['consume_mode'] = self.consume_mode
        if self.expense_type_sub_category:
            if hasattr(self.expense_type_sub_category, 'to_alipay_dict'):
                params['expense_type_sub_category'] = self.expense_type_sub_category.to_alipay_dict()
            else:
                params['expense_type_sub_category'] = self.expense_type_sub_category
        if self.open_rule_id:
            if hasattr(self.open_rule_id, 'to_alipay_dict'):
                params['open_rule_id'] = self.open_rule_id.to_alipay_dict()
            else:
                params['open_rule_id'] = self.open_rule_id
        if self.outer_source_id:
            if hasattr(self.outer_source_id, 'to_alipay_dict'):
                params['outer_source_id'] = self.outer_source_id.to_alipay_dict()
            else:
                params['outer_source_id'] = self.outer_source_id
        if self.payment_policy:
            if hasattr(self.payment_policy, 'to_alipay_dict'):
                params['payment_policy'] = self.payment_policy.to_alipay_dict()
            else:
                params['payment_policy'] = self.payment_policy
        if self.standard_condition_info_list:
            if isinstance(self.standard_condition_info_list, list):
                for i in range(0, len(self.standard_condition_info_list)):
                    element = self.standard_condition_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_condition_info_list[i] = element.to_alipay_dict()
            if hasattr(self.standard_condition_info_list, 'to_alipay_dict'):
                params['standard_condition_info_list'] = self.standard_condition_info_list.to_alipay_dict()
            else:
                params['standard_condition_info_list'] = self.standard_condition_info_list
        if self.standard_desc:
            if hasattr(self.standard_desc, 'to_alipay_dict'):
                params['standard_desc'] = self.standard_desc.to_alipay_dict()
            else:
                params['standard_desc'] = self.standard_desc
        if self.standard_id:
            if hasattr(self.standard_id, 'to_alipay_dict'):
                params['standard_id'] = self.standard_id.to_alipay_dict()
            else:
                params['standard_id'] = self.standard_id
        if self.standard_name:
            if hasattr(self.standard_name, 'to_alipay_dict'):
                params['standard_name'] = self.standard_name.to_alipay_dict()
            else:
                params['standard_name'] = self.standard_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardInfo()
        if 'asset_share_source_info' in d:
            o.asset_share_source_info = d['asset_share_source_info']
        if 'consume_mode' in d:
            o.consume_mode = d['consume_mode']
        if 'expense_type_sub_category' in d:
            o.expense_type_sub_category = d['expense_type_sub_category']
        if 'open_rule_id' in d:
            o.open_rule_id = d['open_rule_id']
        if 'outer_source_id' in d:
            o.outer_source_id = d['outer_source_id']
        if 'payment_policy' in d:
            o.payment_policy = d['payment_policy']
        if 'standard_condition_info_list' in d:
            o.standard_condition_info_list = d['standard_condition_info_list']
        if 'standard_desc' in d:
            o.standard_desc = d['standard_desc']
        if 'standard_id' in d:
            o.standard_id = d['standard_id']
        if 'standard_name' in d:
            o.standard_name = d['standard_name']
        return o


