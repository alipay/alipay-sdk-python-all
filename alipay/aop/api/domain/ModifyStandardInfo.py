#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StandardConditionInfo import StandardConditionInfo
from alipay.aop.api.domain.StandardConditionInfo import StandardConditionInfo


class ModifyStandardInfo(object):

    def __init__(self):
        self._add_condition_list = None
        self._consume_mode = None
        self._delete_condition_id_list = None
        self._modify_condition_list = None
        self._open_rule_id = None
        self._payment_policy = None
        self._personal_qrcode_mode = None
        self._standard_desc = None
        self._standard_id = None
        self._standard_name = None

    @property
    def add_condition_list(self):
        return self._add_condition_list

    @add_condition_list.setter
    def add_condition_list(self, value):
        if isinstance(value, list):
            self._add_condition_list = list()
            for i in value:
                if isinstance(i, StandardConditionInfo):
                    self._add_condition_list.append(i)
                else:
                    self._add_condition_list.append(StandardConditionInfo.from_alipay_dict(i))
    @property
    def consume_mode(self):
        return self._consume_mode

    @consume_mode.setter
    def consume_mode(self, value):
        self._consume_mode = value
    @property
    def delete_condition_id_list(self):
        return self._delete_condition_id_list

    @delete_condition_id_list.setter
    def delete_condition_id_list(self, value):
        if isinstance(value, list):
            self._delete_condition_id_list = list()
            for i in value:
                self._delete_condition_id_list.append(i)
    @property
    def modify_condition_list(self):
        return self._modify_condition_list

    @modify_condition_list.setter
    def modify_condition_list(self, value):
        if isinstance(value, list):
            self._modify_condition_list = list()
            for i in value:
                if isinstance(i, StandardConditionInfo):
                    self._modify_condition_list.append(i)
                else:
                    self._modify_condition_list.append(StandardConditionInfo.from_alipay_dict(i))
    @property
    def open_rule_id(self):
        return self._open_rule_id

    @open_rule_id.setter
    def open_rule_id(self, value):
        self._open_rule_id = value
    @property
    def payment_policy(self):
        return self._payment_policy

    @payment_policy.setter
    def payment_policy(self, value):
        self._payment_policy = value
    @property
    def personal_qrcode_mode(self):
        return self._personal_qrcode_mode

    @personal_qrcode_mode.setter
    def personal_qrcode_mode(self, value):
        self._personal_qrcode_mode = value
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
        if self.add_condition_list:
            if isinstance(self.add_condition_list, list):
                for i in range(0, len(self.add_condition_list)):
                    element = self.add_condition_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.add_condition_list[i] = element.to_alipay_dict()
            if hasattr(self.add_condition_list, 'to_alipay_dict'):
                params['add_condition_list'] = self.add_condition_list.to_alipay_dict()
            else:
                params['add_condition_list'] = self.add_condition_list
        if self.consume_mode:
            if hasattr(self.consume_mode, 'to_alipay_dict'):
                params['consume_mode'] = self.consume_mode.to_alipay_dict()
            else:
                params['consume_mode'] = self.consume_mode
        if self.delete_condition_id_list:
            if isinstance(self.delete_condition_id_list, list):
                for i in range(0, len(self.delete_condition_id_list)):
                    element = self.delete_condition_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delete_condition_id_list[i] = element.to_alipay_dict()
            if hasattr(self.delete_condition_id_list, 'to_alipay_dict'):
                params['delete_condition_id_list'] = self.delete_condition_id_list.to_alipay_dict()
            else:
                params['delete_condition_id_list'] = self.delete_condition_id_list
        if self.modify_condition_list:
            if isinstance(self.modify_condition_list, list):
                for i in range(0, len(self.modify_condition_list)):
                    element = self.modify_condition_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.modify_condition_list[i] = element.to_alipay_dict()
            if hasattr(self.modify_condition_list, 'to_alipay_dict'):
                params['modify_condition_list'] = self.modify_condition_list.to_alipay_dict()
            else:
                params['modify_condition_list'] = self.modify_condition_list
        if self.open_rule_id:
            if hasattr(self.open_rule_id, 'to_alipay_dict'):
                params['open_rule_id'] = self.open_rule_id.to_alipay_dict()
            else:
                params['open_rule_id'] = self.open_rule_id
        if self.payment_policy:
            if hasattr(self.payment_policy, 'to_alipay_dict'):
                params['payment_policy'] = self.payment_policy.to_alipay_dict()
            else:
                params['payment_policy'] = self.payment_policy
        if self.personal_qrcode_mode:
            if hasattr(self.personal_qrcode_mode, 'to_alipay_dict'):
                params['personal_qrcode_mode'] = self.personal_qrcode_mode.to_alipay_dict()
            else:
                params['personal_qrcode_mode'] = self.personal_qrcode_mode
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
        o = ModifyStandardInfo()
        if 'add_condition_list' in d:
            o.add_condition_list = d['add_condition_list']
        if 'consume_mode' in d:
            o.consume_mode = d['consume_mode']
        if 'delete_condition_id_list' in d:
            o.delete_condition_id_list = d['delete_condition_id_list']
        if 'modify_condition_list' in d:
            o.modify_condition_list = d['modify_condition_list']
        if 'open_rule_id' in d:
            o.open_rule_id = d['open_rule_id']
        if 'payment_policy' in d:
            o.payment_policy = d['payment_policy']
        if 'personal_qrcode_mode' in d:
            o.personal_qrcode_mode = d['personal_qrcode_mode']
        if 'standard_desc' in d:
            o.standard_desc = d['standard_desc']
        if 'standard_id' in d:
            o.standard_id = d['standard_id']
        if 'standard_name' in d:
            o.standard_name = d['standard_name']
        return o


