#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupControlRuleVO(object):

    def __init__(self):
        self._app_id_list = None
        self._check_position_list = None
        self._domain_name_white_list = None
        self._key_word_list = None
        self._msg_type_list = None
        self._rule_type = None
        self._time_limit = None
        self._total_msg_limit = None

    @property
    def app_id_list(self):
        return self._app_id_list

    @app_id_list.setter
    def app_id_list(self, value):
        if isinstance(value, list):
            self._app_id_list = list()
            for i in value:
                self._app_id_list.append(i)
    @property
    def check_position_list(self):
        return self._check_position_list

    @check_position_list.setter
    def check_position_list(self, value):
        if isinstance(value, list):
            self._check_position_list = list()
            for i in value:
                self._check_position_list.append(i)
    @property
    def domain_name_white_list(self):
        return self._domain_name_white_list

    @domain_name_white_list.setter
    def domain_name_white_list(self, value):
        if isinstance(value, list):
            self._domain_name_white_list = list()
            for i in value:
                self._domain_name_white_list.append(i)
    @property
    def key_word_list(self):
        return self._key_word_list

    @key_word_list.setter
    def key_word_list(self, value):
        if isinstance(value, list):
            self._key_word_list = list()
            for i in value:
                self._key_word_list.append(i)
    @property
    def msg_type_list(self):
        return self._msg_type_list

    @msg_type_list.setter
    def msg_type_list(self, value):
        if isinstance(value, list):
            self._msg_type_list = list()
            for i in value:
                self._msg_type_list.append(i)
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def time_limit(self):
        return self._time_limit

    @time_limit.setter
    def time_limit(self, value):
        self._time_limit = value
    @property
    def total_msg_limit(self):
        return self._total_msg_limit

    @total_msg_limit.setter
    def total_msg_limit(self, value):
        self._total_msg_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_id_list:
            if isinstance(self.app_id_list, list):
                for i in range(0, len(self.app_id_list)):
                    element = self.app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.app_id_list, 'to_alipay_dict'):
                params['app_id_list'] = self.app_id_list.to_alipay_dict()
            else:
                params['app_id_list'] = self.app_id_list
        if self.check_position_list:
            if isinstance(self.check_position_list, list):
                for i in range(0, len(self.check_position_list)):
                    element = self.check_position_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_position_list[i] = element.to_alipay_dict()
            if hasattr(self.check_position_list, 'to_alipay_dict'):
                params['check_position_list'] = self.check_position_list.to_alipay_dict()
            else:
                params['check_position_list'] = self.check_position_list
        if self.domain_name_white_list:
            if isinstance(self.domain_name_white_list, list):
                for i in range(0, len(self.domain_name_white_list)):
                    element = self.domain_name_white_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.domain_name_white_list[i] = element.to_alipay_dict()
            if hasattr(self.domain_name_white_list, 'to_alipay_dict'):
                params['domain_name_white_list'] = self.domain_name_white_list.to_alipay_dict()
            else:
                params['domain_name_white_list'] = self.domain_name_white_list
        if self.key_word_list:
            if isinstance(self.key_word_list, list):
                for i in range(0, len(self.key_word_list)):
                    element = self.key_word_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_word_list[i] = element.to_alipay_dict()
            if hasattr(self.key_word_list, 'to_alipay_dict'):
                params['key_word_list'] = self.key_word_list.to_alipay_dict()
            else:
                params['key_word_list'] = self.key_word_list
        if self.msg_type_list:
            if isinstance(self.msg_type_list, list):
                for i in range(0, len(self.msg_type_list)):
                    element = self.msg_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.msg_type_list[i] = element.to_alipay_dict()
            if hasattr(self.msg_type_list, 'to_alipay_dict'):
                params['msg_type_list'] = self.msg_type_list.to_alipay_dict()
            else:
                params['msg_type_list'] = self.msg_type_list
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.time_limit:
            if hasattr(self.time_limit, 'to_alipay_dict'):
                params['time_limit'] = self.time_limit.to_alipay_dict()
            else:
                params['time_limit'] = self.time_limit
        if self.total_msg_limit:
            if hasattr(self.total_msg_limit, 'to_alipay_dict'):
                params['total_msg_limit'] = self.total_msg_limit.to_alipay_dict()
            else:
                params['total_msg_limit'] = self.total_msg_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupControlRuleVO()
        if 'app_id_list' in d:
            o.app_id_list = d['app_id_list']
        if 'check_position_list' in d:
            o.check_position_list = d['check_position_list']
        if 'domain_name_white_list' in d:
            o.domain_name_white_list = d['domain_name_white_list']
        if 'key_word_list' in d:
            o.key_word_list = d['key_word_list']
        if 'msg_type_list' in d:
            o.msg_type_list = d['msg_type_list']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'time_limit' in d:
            o.time_limit = d['time_limit']
        if 'total_msg_limit' in d:
            o.total_msg_limit = d['total_msg_limit']
        return o


