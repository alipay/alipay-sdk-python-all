#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceItemRestrictRule import ServiceItemRestrictRule


class SubUserInfo(object):

    def __init__(self):
        self._service_item_restrict_rule_list = None
        self._sub_start_time = None
        self._sub_user_cert_no = None
        self._sub_user_cert_type = None
        self._sub_user_effect_days = None
        self._sub_user_name = None
        self._sub_user_phone_no = None
        self._sub_user_start_time = None

    @property
    def service_item_restrict_rule_list(self):
        return self._service_item_restrict_rule_list

    @service_item_restrict_rule_list.setter
    def service_item_restrict_rule_list(self, value):
        if isinstance(value, list):
            self._service_item_restrict_rule_list = list()
            for i in value:
                if isinstance(i, ServiceItemRestrictRule):
                    self._service_item_restrict_rule_list.append(i)
                else:
                    self._service_item_restrict_rule_list.append(ServiceItemRestrictRule.from_alipay_dict(i))
    @property
    def sub_start_time(self):
        return self._sub_start_time

    @sub_start_time.setter
    def sub_start_time(self, value):
        self._sub_start_time = value
    @property
    def sub_user_cert_no(self):
        return self._sub_user_cert_no

    @sub_user_cert_no.setter
    def sub_user_cert_no(self, value):
        self._sub_user_cert_no = value
    @property
    def sub_user_cert_type(self):
        return self._sub_user_cert_type

    @sub_user_cert_type.setter
    def sub_user_cert_type(self, value):
        self._sub_user_cert_type = value
    @property
    def sub_user_effect_days(self):
        return self._sub_user_effect_days

    @sub_user_effect_days.setter
    def sub_user_effect_days(self, value):
        self._sub_user_effect_days = value
    @property
    def sub_user_name(self):
        return self._sub_user_name

    @sub_user_name.setter
    def sub_user_name(self, value):
        self._sub_user_name = value
    @property
    def sub_user_phone_no(self):
        return self._sub_user_phone_no

    @sub_user_phone_no.setter
    def sub_user_phone_no(self, value):
        self._sub_user_phone_no = value
    @property
    def sub_user_start_time(self):
        return self._sub_user_start_time

    @sub_user_start_time.setter
    def sub_user_start_time(self, value):
        self._sub_user_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.service_item_restrict_rule_list:
            if isinstance(self.service_item_restrict_rule_list, list):
                for i in range(0, len(self.service_item_restrict_rule_list)):
                    element = self.service_item_restrict_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_item_restrict_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.service_item_restrict_rule_list, 'to_alipay_dict'):
                params['service_item_restrict_rule_list'] = self.service_item_restrict_rule_list.to_alipay_dict()
            else:
                params['service_item_restrict_rule_list'] = self.service_item_restrict_rule_list
        if self.sub_start_time:
            if hasattr(self.sub_start_time, 'to_alipay_dict'):
                params['sub_start_time'] = self.sub_start_time.to_alipay_dict()
            else:
                params['sub_start_time'] = self.sub_start_time
        if self.sub_user_cert_no:
            if hasattr(self.sub_user_cert_no, 'to_alipay_dict'):
                params['sub_user_cert_no'] = self.sub_user_cert_no.to_alipay_dict()
            else:
                params['sub_user_cert_no'] = self.sub_user_cert_no
        if self.sub_user_cert_type:
            if hasattr(self.sub_user_cert_type, 'to_alipay_dict'):
                params['sub_user_cert_type'] = self.sub_user_cert_type.to_alipay_dict()
            else:
                params['sub_user_cert_type'] = self.sub_user_cert_type
        if self.sub_user_effect_days:
            if hasattr(self.sub_user_effect_days, 'to_alipay_dict'):
                params['sub_user_effect_days'] = self.sub_user_effect_days.to_alipay_dict()
            else:
                params['sub_user_effect_days'] = self.sub_user_effect_days
        if self.sub_user_name:
            if hasattr(self.sub_user_name, 'to_alipay_dict'):
                params['sub_user_name'] = self.sub_user_name.to_alipay_dict()
            else:
                params['sub_user_name'] = self.sub_user_name
        if self.sub_user_phone_no:
            if hasattr(self.sub_user_phone_no, 'to_alipay_dict'):
                params['sub_user_phone_no'] = self.sub_user_phone_no.to_alipay_dict()
            else:
                params['sub_user_phone_no'] = self.sub_user_phone_no
        if self.sub_user_start_time:
            if hasattr(self.sub_user_start_time, 'to_alipay_dict'):
                params['sub_user_start_time'] = self.sub_user_start_time.to_alipay_dict()
            else:
                params['sub_user_start_time'] = self.sub_user_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubUserInfo()
        if 'service_item_restrict_rule_list' in d:
            o.service_item_restrict_rule_list = d['service_item_restrict_rule_list']
        if 'sub_start_time' in d:
            o.sub_start_time = d['sub_start_time']
        if 'sub_user_cert_no' in d:
            o.sub_user_cert_no = d['sub_user_cert_no']
        if 'sub_user_cert_type' in d:
            o.sub_user_cert_type = d['sub_user_cert_type']
        if 'sub_user_effect_days' in d:
            o.sub_user_effect_days = d['sub_user_effect_days']
        if 'sub_user_name' in d:
            o.sub_user_name = d['sub_user_name']
        if 'sub_user_phone_no' in d:
            o.sub_user_phone_no = d['sub_user_phone_no']
        if 'sub_user_start_time' in d:
            o.sub_user_start_time = d['sub_user_start_time']
        return o


