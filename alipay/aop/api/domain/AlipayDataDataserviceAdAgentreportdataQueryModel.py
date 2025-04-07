#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdAgentreportdataQueryModel(object):

    def __init__(self):
        self._alipay_pid = None
        self._biz_token = None
        self._conv_code_list = None
        self._conv_time_join_rule = None
        self._current = None
        self._delivery_mode = None
        self._end_date = None
        self._page_size = None
        self._principal_tag = None
        self._principal_tag_list = None
        self._query_type = None
        self._show_conv_data = None
        self._start_date = None

    @property
    def alipay_pid(self):
        return self._alipay_pid

    @alipay_pid.setter
    def alipay_pid(self, value):
        self._alipay_pid = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def conv_code_list(self):
        return self._conv_code_list

    @conv_code_list.setter
    def conv_code_list(self, value):
        if isinstance(value, list):
            self._conv_code_list = list()
            for i in value:
                self._conv_code_list.append(i)
    @property
    def conv_time_join_rule(self):
        return self._conv_time_join_rule

    @conv_time_join_rule.setter
    def conv_time_join_rule(self, value):
        self._conv_time_join_rule = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def delivery_mode(self):
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, value):
        self._delivery_mode = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def principal_tag_list(self):
        return self._principal_tag_list

    @principal_tag_list.setter
    def principal_tag_list(self, value):
        if isinstance(value, list):
            self._principal_tag_list = list()
            for i in value:
                self._principal_tag_list.append(i)
    @property
    def query_type(self):
        return self._query_type

    @query_type.setter
    def query_type(self, value):
        self._query_type = value
    @property
    def show_conv_data(self):
        return self._show_conv_data

    @show_conv_data.setter
    def show_conv_data(self, value):
        self._show_conv_data = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pid:
            if hasattr(self.alipay_pid, 'to_alipay_dict'):
                params['alipay_pid'] = self.alipay_pid.to_alipay_dict()
            else:
                params['alipay_pid'] = self.alipay_pid
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.conv_code_list:
            if isinstance(self.conv_code_list, list):
                for i in range(0, len(self.conv_code_list)):
                    element = self.conv_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conv_code_list[i] = element.to_alipay_dict()
            if hasattr(self.conv_code_list, 'to_alipay_dict'):
                params['conv_code_list'] = self.conv_code_list.to_alipay_dict()
            else:
                params['conv_code_list'] = self.conv_code_list
        if self.conv_time_join_rule:
            if hasattr(self.conv_time_join_rule, 'to_alipay_dict'):
                params['conv_time_join_rule'] = self.conv_time_join_rule.to_alipay_dict()
            else:
                params['conv_time_join_rule'] = self.conv_time_join_rule
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.delivery_mode:
            if hasattr(self.delivery_mode, 'to_alipay_dict'):
                params['delivery_mode'] = self.delivery_mode.to_alipay_dict()
            else:
                params['delivery_mode'] = self.delivery_mode
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.principal_tag_list:
            if isinstance(self.principal_tag_list, list):
                for i in range(0, len(self.principal_tag_list)):
                    element = self.principal_tag_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.principal_tag_list[i] = element.to_alipay_dict()
            if hasattr(self.principal_tag_list, 'to_alipay_dict'):
                params['principal_tag_list'] = self.principal_tag_list.to_alipay_dict()
            else:
                params['principal_tag_list'] = self.principal_tag_list
        if self.query_type:
            if hasattr(self.query_type, 'to_alipay_dict'):
                params['query_type'] = self.query_type.to_alipay_dict()
            else:
                params['query_type'] = self.query_type
        if self.show_conv_data:
            if hasattr(self.show_conv_data, 'to_alipay_dict'):
                params['show_conv_data'] = self.show_conv_data.to_alipay_dict()
            else:
                params['show_conv_data'] = self.show_conv_data
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdAgentreportdataQueryModel()
        if 'alipay_pid' in d:
            o.alipay_pid = d['alipay_pid']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'conv_code_list' in d:
            o.conv_code_list = d['conv_code_list']
        if 'conv_time_join_rule' in d:
            o.conv_time_join_rule = d['conv_time_join_rule']
        if 'current' in d:
            o.current = d['current']
        if 'delivery_mode' in d:
            o.delivery_mode = d['delivery_mode']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'principal_tag_list' in d:
            o.principal_tag_list = d['principal_tag_list']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'show_conv_data' in d:
            o.show_conv_data = d['show_conv_data']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


