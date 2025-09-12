#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DormitoryConfig import DormitoryConfig


class AlipayCommerceEducateCheckinRuleCreateModel(object):

    def __init__(self):
        self._auth_activity_id = None
        self._authentication_type = None
        self._check_out_end_minutes = None
        self._check_out_end_type = None
        self._check_out_start_minutes = None
        self._check_out_start_type = None
        self._dormitory_config = None
        self._enable_check_in = None
        self._enable_check_out = None
        self._enable_status = None
        self._end_minutes = None
        self._end_time = None
        self._end_type = None
        self._frequency_type = None
        self._inst_id = None
        self._nfc_check = None
        self._picture_check = None
        self._place_check = None
        self._place_id_list = None
        self._radius = None
        self._rule_name = None
        self._rule_type = None
        self._start_minutes = None
        self._start_time = None
        self._start_type = None
        self._week_day_list = None

    @property
    def auth_activity_id(self):
        return self._auth_activity_id

    @auth_activity_id.setter
    def auth_activity_id(self, value):
        self._auth_activity_id = value
    @property
    def authentication_type(self):
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, value):
        self._authentication_type = value
    @property
    def check_out_end_minutes(self):
        return self._check_out_end_minutes

    @check_out_end_minutes.setter
    def check_out_end_minutes(self, value):
        self._check_out_end_minutes = value
    @property
    def check_out_end_type(self):
        return self._check_out_end_type

    @check_out_end_type.setter
    def check_out_end_type(self, value):
        self._check_out_end_type = value
    @property
    def check_out_start_minutes(self):
        return self._check_out_start_minutes

    @check_out_start_minutes.setter
    def check_out_start_minutes(self, value):
        self._check_out_start_minutes = value
    @property
    def check_out_start_type(self):
        return self._check_out_start_type

    @check_out_start_type.setter
    def check_out_start_type(self, value):
        self._check_out_start_type = value
    @property
    def dormitory_config(self):
        return self._dormitory_config

    @dormitory_config.setter
    def dormitory_config(self, value):
        if isinstance(value, DormitoryConfig):
            self._dormitory_config = value
        else:
            self._dormitory_config = DormitoryConfig.from_alipay_dict(value)
    @property
    def enable_check_in(self):
        return self._enable_check_in

    @enable_check_in.setter
    def enable_check_in(self, value):
        self._enable_check_in = value
    @property
    def enable_check_out(self):
        return self._enable_check_out

    @enable_check_out.setter
    def enable_check_out(self, value):
        self._enable_check_out = value
    @property
    def enable_status(self):
        return self._enable_status

    @enable_status.setter
    def enable_status(self, value):
        self._enable_status = value
    @property
    def end_minutes(self):
        return self._end_minutes

    @end_minutes.setter
    def end_minutes(self, value):
        self._end_minutes = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def end_type(self):
        return self._end_type

    @end_type.setter
    def end_type(self, value):
        self._end_type = value
    @property
    def frequency_type(self):
        return self._frequency_type

    @frequency_type.setter
    def frequency_type(self, value):
        self._frequency_type = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def nfc_check(self):
        return self._nfc_check

    @nfc_check.setter
    def nfc_check(self, value):
        self._nfc_check = value
    @property
    def picture_check(self):
        return self._picture_check

    @picture_check.setter
    def picture_check(self, value):
        self._picture_check = value
    @property
    def place_check(self):
        return self._place_check

    @place_check.setter
    def place_check(self, value):
        self._place_check = value
    @property
    def place_id_list(self):
        return self._place_id_list

    @place_id_list.setter
    def place_id_list(self, value):
        if isinstance(value, list):
            self._place_id_list = list()
            for i in value:
                self._place_id_list.append(i)
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def start_minutes(self):
        return self._start_minutes

    @start_minutes.setter
    def start_minutes(self, value):
        self._start_minutes = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def start_type(self):
        return self._start_type

    @start_type.setter
    def start_type(self, value):
        self._start_type = value
    @property
    def week_day_list(self):
        return self._week_day_list

    @week_day_list.setter
    def week_day_list(self, value):
        if isinstance(value, list):
            self._week_day_list = list()
            for i in value:
                self._week_day_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.auth_activity_id:
            if hasattr(self.auth_activity_id, 'to_alipay_dict'):
                params['auth_activity_id'] = self.auth_activity_id.to_alipay_dict()
            else:
                params['auth_activity_id'] = self.auth_activity_id
        if self.authentication_type:
            if hasattr(self.authentication_type, 'to_alipay_dict'):
                params['authentication_type'] = self.authentication_type.to_alipay_dict()
            else:
                params['authentication_type'] = self.authentication_type
        if self.check_out_end_minutes:
            if hasattr(self.check_out_end_minutes, 'to_alipay_dict'):
                params['check_out_end_minutes'] = self.check_out_end_minutes.to_alipay_dict()
            else:
                params['check_out_end_minutes'] = self.check_out_end_minutes
        if self.check_out_end_type:
            if hasattr(self.check_out_end_type, 'to_alipay_dict'):
                params['check_out_end_type'] = self.check_out_end_type.to_alipay_dict()
            else:
                params['check_out_end_type'] = self.check_out_end_type
        if self.check_out_start_minutes:
            if hasattr(self.check_out_start_minutes, 'to_alipay_dict'):
                params['check_out_start_minutes'] = self.check_out_start_minutes.to_alipay_dict()
            else:
                params['check_out_start_minutes'] = self.check_out_start_minutes
        if self.check_out_start_type:
            if hasattr(self.check_out_start_type, 'to_alipay_dict'):
                params['check_out_start_type'] = self.check_out_start_type.to_alipay_dict()
            else:
                params['check_out_start_type'] = self.check_out_start_type
        if self.dormitory_config:
            if hasattr(self.dormitory_config, 'to_alipay_dict'):
                params['dormitory_config'] = self.dormitory_config.to_alipay_dict()
            else:
                params['dormitory_config'] = self.dormitory_config
        if self.enable_check_in:
            if hasattr(self.enable_check_in, 'to_alipay_dict'):
                params['enable_check_in'] = self.enable_check_in.to_alipay_dict()
            else:
                params['enable_check_in'] = self.enable_check_in
        if self.enable_check_out:
            if hasattr(self.enable_check_out, 'to_alipay_dict'):
                params['enable_check_out'] = self.enable_check_out.to_alipay_dict()
            else:
                params['enable_check_out'] = self.enable_check_out
        if self.enable_status:
            if hasattr(self.enable_status, 'to_alipay_dict'):
                params['enable_status'] = self.enable_status.to_alipay_dict()
            else:
                params['enable_status'] = self.enable_status
        if self.end_minutes:
            if hasattr(self.end_minutes, 'to_alipay_dict'):
                params['end_minutes'] = self.end_minutes.to_alipay_dict()
            else:
                params['end_minutes'] = self.end_minutes
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.end_type:
            if hasattr(self.end_type, 'to_alipay_dict'):
                params['end_type'] = self.end_type.to_alipay_dict()
            else:
                params['end_type'] = self.end_type
        if self.frequency_type:
            if hasattr(self.frequency_type, 'to_alipay_dict'):
                params['frequency_type'] = self.frequency_type.to_alipay_dict()
            else:
                params['frequency_type'] = self.frequency_type
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.nfc_check:
            if hasattr(self.nfc_check, 'to_alipay_dict'):
                params['nfc_check'] = self.nfc_check.to_alipay_dict()
            else:
                params['nfc_check'] = self.nfc_check
        if self.picture_check:
            if hasattr(self.picture_check, 'to_alipay_dict'):
                params['picture_check'] = self.picture_check.to_alipay_dict()
            else:
                params['picture_check'] = self.picture_check
        if self.place_check:
            if hasattr(self.place_check, 'to_alipay_dict'):
                params['place_check'] = self.place_check.to_alipay_dict()
            else:
                params['place_check'] = self.place_check
        if self.place_id_list:
            if isinstance(self.place_id_list, list):
                for i in range(0, len(self.place_id_list)):
                    element = self.place_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.place_id_list[i] = element.to_alipay_dict()
            if hasattr(self.place_id_list, 'to_alipay_dict'):
                params['place_id_list'] = self.place_id_list.to_alipay_dict()
            else:
                params['place_id_list'] = self.place_id_list
        if self.radius:
            if hasattr(self.radius, 'to_alipay_dict'):
                params['radius'] = self.radius.to_alipay_dict()
            else:
                params['radius'] = self.radius
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.start_minutes:
            if hasattr(self.start_minutes, 'to_alipay_dict'):
                params['start_minutes'] = self.start_minutes.to_alipay_dict()
            else:
                params['start_minutes'] = self.start_minutes
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.start_type:
            if hasattr(self.start_type, 'to_alipay_dict'):
                params['start_type'] = self.start_type.to_alipay_dict()
            else:
                params['start_type'] = self.start_type
        if self.week_day_list:
            if isinstance(self.week_day_list, list):
                for i in range(0, len(self.week_day_list)):
                    element = self.week_day_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_day_list[i] = element.to_alipay_dict()
            if hasattr(self.week_day_list, 'to_alipay_dict'):
                params['week_day_list'] = self.week_day_list.to_alipay_dict()
            else:
                params['week_day_list'] = self.week_day_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCheckinRuleCreateModel()
        if 'auth_activity_id' in d:
            o.auth_activity_id = d['auth_activity_id']
        if 'authentication_type' in d:
            o.authentication_type = d['authentication_type']
        if 'check_out_end_minutes' in d:
            o.check_out_end_minutes = d['check_out_end_minutes']
        if 'check_out_end_type' in d:
            o.check_out_end_type = d['check_out_end_type']
        if 'check_out_start_minutes' in d:
            o.check_out_start_minutes = d['check_out_start_minutes']
        if 'check_out_start_type' in d:
            o.check_out_start_type = d['check_out_start_type']
        if 'dormitory_config' in d:
            o.dormitory_config = d['dormitory_config']
        if 'enable_check_in' in d:
            o.enable_check_in = d['enable_check_in']
        if 'enable_check_out' in d:
            o.enable_check_out = d['enable_check_out']
        if 'enable_status' in d:
            o.enable_status = d['enable_status']
        if 'end_minutes' in d:
            o.end_minutes = d['end_minutes']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'end_type' in d:
            o.end_type = d['end_type']
        if 'frequency_type' in d:
            o.frequency_type = d['frequency_type']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'nfc_check' in d:
            o.nfc_check = d['nfc_check']
        if 'picture_check' in d:
            o.picture_check = d['picture_check']
        if 'place_check' in d:
            o.place_check = d['place_check']
        if 'place_id_list' in d:
            o.place_id_list = d['place_id_list']
        if 'radius' in d:
            o.radius = d['radius']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'start_minutes' in d:
            o.start_minutes = d['start_minutes']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'start_type' in d:
            o.start_type = d['start_type']
        if 'week_day_list' in d:
            o.week_day_list = d['week_day_list']
        return o


