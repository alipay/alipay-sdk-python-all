#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceItemRestrictRule import ServiceItemRestrictRule
from alipay.aop.api.domain.SubUserInfo import SubUserInfo


class AlipayCommerceMedicalServicepackageGrantbyphonenoCreateModel(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._effect_days = None
        self._name = None
        self._open_id = None
        self._open_main = None
        self._out_unique_biz_no = None
        self._phone_no = None
        self._project_id = None
        self._service_item_restrict_rule_list = None
        self._start_time = None
        self._sub_user_info_list = None
        self._user_id = None
        self._user_start_time = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def effect_days(self):
        return self._effect_days

    @effect_days.setter
    def effect_days(self, value):
        self._effect_days = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def open_main(self):
        return self._open_main

    @open_main.setter
    def open_main(self, value):
        self._open_main = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def service_item_restrict_rule_list(self):
        return self._service_item_restrict_rule_list

    @service_item_restrict_rule_list.setter
    def service_item_restrict_rule_list(self, value):
        if isinstance(value, ServiceItemRestrictRule):
            self._service_item_restrict_rule_list = value
        else:
            self._service_item_restrict_rule_list = ServiceItemRestrictRule.from_alipay_dict(value)
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_user_info_list(self):
        return self._sub_user_info_list

    @sub_user_info_list.setter
    def sub_user_info_list(self, value):
        if isinstance(value, list):
            self._sub_user_info_list = list()
            for i in value:
                if isinstance(i, SubUserInfo):
                    self._sub_user_info_list.append(i)
                else:
                    self._sub_user_info_list.append(SubUserInfo.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_start_time(self):
        return self._user_start_time

    @user_start_time.setter
    def user_start_time(self, value):
        self._user_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.effect_days:
            if hasattr(self.effect_days, 'to_alipay_dict'):
                params['effect_days'] = self.effect_days.to_alipay_dict()
            else:
                params['effect_days'] = self.effect_days
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.open_main:
            if hasattr(self.open_main, 'to_alipay_dict'):
                params['open_main'] = self.open_main.to_alipay_dict()
            else:
                params['open_main'] = self.open_main
        if self.out_unique_biz_no:
            if hasattr(self.out_unique_biz_no, 'to_alipay_dict'):
                params['out_unique_biz_no'] = self.out_unique_biz_no.to_alipay_dict()
            else:
                params['out_unique_biz_no'] = self.out_unique_biz_no
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.service_item_restrict_rule_list:
            if hasattr(self.service_item_restrict_rule_list, 'to_alipay_dict'):
                params['service_item_restrict_rule_list'] = self.service_item_restrict_rule_list.to_alipay_dict()
            else:
                params['service_item_restrict_rule_list'] = self.service_item_restrict_rule_list
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_user_info_list:
            if isinstance(self.sub_user_info_list, list):
                for i in range(0, len(self.sub_user_info_list)):
                    element = self.sub_user_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_user_info_list[i] = element.to_alipay_dict()
            if hasattr(self.sub_user_info_list, 'to_alipay_dict'):
                params['sub_user_info_list'] = self.sub_user_info_list.to_alipay_dict()
            else:
                params['sub_user_info_list'] = self.sub_user_info_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_start_time:
            if hasattr(self.user_start_time, 'to_alipay_dict'):
                params['user_start_time'] = self.user_start_time.to_alipay_dict()
            else:
                params['user_start_time'] = self.user_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalServicepackageGrantbyphonenoCreateModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'effect_days' in d:
            o.effect_days = d['effect_days']
        if 'name' in d:
            o.name = d['name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'open_main' in d:
            o.open_main = d['open_main']
        if 'out_unique_biz_no' in d:
            o.out_unique_biz_no = d['out_unique_biz_no']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'service_item_restrict_rule_list' in d:
            o.service_item_restrict_rule_list = d['service_item_restrict_rule_list']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_user_info_list' in d:
            o.sub_user_info_list = d['sub_user_info_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_start_time' in d:
            o.user_start_time = d['user_start_time']
        return o


