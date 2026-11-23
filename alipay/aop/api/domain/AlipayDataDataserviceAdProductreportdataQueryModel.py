#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdProductreportdataQueryModel(object):

    def __init__(self):
        self._ad_level = None
        self._conv_code_list = None
        self._conv_time_join_rule = None
        self._creative_id_list = None
        self._current = None
        self._end_date = None
        self._entity_data_type = None
        self._entity_library_id_list = None
        self._entity_no_list = None
        self._group_id_list = None
        self._page_size = None
        self._plan_id_list = None
        self._principal_tag = None
        self._query_type = None
        self._show_conv_data = None
        self._start_date = None

    @property
    def ad_level(self):
        return self._ad_level

    @ad_level.setter
    def ad_level(self, value):
        self._ad_level = value
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
    def creative_id_list(self):
        return self._creative_id_list

    @creative_id_list.setter
    def creative_id_list(self, value):
        if isinstance(value, list):
            self._creative_id_list = list()
            for i in value:
                self._creative_id_list.append(i)
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def entity_data_type(self):
        return self._entity_data_type

    @entity_data_type.setter
    def entity_data_type(self, value):
        self._entity_data_type = value
    @property
    def entity_library_id_list(self):
        return self._entity_library_id_list

    @entity_library_id_list.setter
    def entity_library_id_list(self, value):
        if isinstance(value, list):
            self._entity_library_id_list = list()
            for i in value:
                self._entity_library_id_list.append(i)
    @property
    def entity_no_list(self):
        return self._entity_no_list

    @entity_no_list.setter
    def entity_no_list(self, value):
        if isinstance(value, list):
            self._entity_no_list = list()
            for i in value:
                self._entity_no_list.append(i)
    @property
    def group_id_list(self):
        return self._group_id_list

    @group_id_list.setter
    def group_id_list(self, value):
        if isinstance(value, list):
            self._group_id_list = list()
            for i in value:
                self._group_id_list.append(i)
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_id_list(self):
        return self._plan_id_list

    @plan_id_list.setter
    def plan_id_list(self, value):
        if isinstance(value, list):
            self._plan_id_list = list()
            for i in value:
                self._plan_id_list.append(i)
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
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
        if self.ad_level:
            if hasattr(self.ad_level, 'to_alipay_dict'):
                params['ad_level'] = self.ad_level.to_alipay_dict()
            else:
                params['ad_level'] = self.ad_level
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
        if self.creative_id_list:
            if isinstance(self.creative_id_list, list):
                for i in range(0, len(self.creative_id_list)):
                    element = self.creative_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_id_list[i] = element.to_alipay_dict()
            if hasattr(self.creative_id_list, 'to_alipay_dict'):
                params['creative_id_list'] = self.creative_id_list.to_alipay_dict()
            else:
                params['creative_id_list'] = self.creative_id_list
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.entity_data_type:
            if hasattr(self.entity_data_type, 'to_alipay_dict'):
                params['entity_data_type'] = self.entity_data_type.to_alipay_dict()
            else:
                params['entity_data_type'] = self.entity_data_type
        if self.entity_library_id_list:
            if isinstance(self.entity_library_id_list, list):
                for i in range(0, len(self.entity_library_id_list)):
                    element = self.entity_library_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_library_id_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_library_id_list, 'to_alipay_dict'):
                params['entity_library_id_list'] = self.entity_library_id_list.to_alipay_dict()
            else:
                params['entity_library_id_list'] = self.entity_library_id_list
        if self.entity_no_list:
            if isinstance(self.entity_no_list, list):
                for i in range(0, len(self.entity_no_list)):
                    element = self.entity_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.entity_no_list[i] = element.to_alipay_dict()
            if hasattr(self.entity_no_list, 'to_alipay_dict'):
                params['entity_no_list'] = self.entity_no_list.to_alipay_dict()
            else:
                params['entity_no_list'] = self.entity_no_list
        if self.group_id_list:
            if isinstance(self.group_id_list, list):
                for i in range(0, len(self.group_id_list)):
                    element = self.group_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_id_list[i] = element.to_alipay_dict()
            if hasattr(self.group_id_list, 'to_alipay_dict'):
                params['group_id_list'] = self.group_id_list.to_alipay_dict()
            else:
                params['group_id_list'] = self.group_id_list
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_id_list:
            if isinstance(self.plan_id_list, list):
                for i in range(0, len(self.plan_id_list)):
                    element = self.plan_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_id_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_id_list, 'to_alipay_dict'):
                params['plan_id_list'] = self.plan_id_list.to_alipay_dict()
            else:
                params['plan_id_list'] = self.plan_id_list
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
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
        o = AlipayDataDataserviceAdProductreportdataQueryModel()
        if 'ad_level' in d:
            o.ad_level = d['ad_level']
        if 'conv_code_list' in d:
            o.conv_code_list = d['conv_code_list']
        if 'conv_time_join_rule' in d:
            o.conv_time_join_rule = d['conv_time_join_rule']
        if 'creative_id_list' in d:
            o.creative_id_list = d['creative_id_list']
        if 'current' in d:
            o.current = d['current']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'entity_data_type' in d:
            o.entity_data_type = d['entity_data_type']
        if 'entity_library_id_list' in d:
            o.entity_library_id_list = d['entity_library_id_list']
        if 'entity_no_list' in d:
            o.entity_no_list = d['entity_no_list']
        if 'group_id_list' in d:
            o.group_id_list = d['group_id_list']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_id_list' in d:
            o.plan_id_list = d['plan_id_list']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'query_type' in d:
            o.query_type = d['query_type']
        if 'show_conv_data' in d:
            o.show_conv_data = d['show_conv_data']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


