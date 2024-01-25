#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantQipanOdpscrowdCreateModel(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_desc = None
        self._crowd_name = None
        self._external_crowd_code = None
        self._hidden = None
        self._identify_column = None
        self._is_partition = None
        self._partition_column = None
        self._project = None
        self._refresh_period = None
        self._table = None
        self._where_columns = None
        self._where_condition = None

    @property
    def apply_channel_list(self):
        return self._apply_channel_list

    @apply_channel_list.setter
    def apply_channel_list(self, value):
        if isinstance(value, list):
            self._apply_channel_list = list()
            for i in value:
                self._apply_channel_list.append(i)
    @property
    def crowd_desc(self):
        return self._crowd_desc

    @crowd_desc.setter
    def crowd_desc(self, value):
        self._crowd_desc = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def external_crowd_code(self):
        return self._external_crowd_code

    @external_crowd_code.setter
    def external_crowd_code(self, value):
        self._external_crowd_code = value
    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value
    @property
    def identify_column(self):
        return self._identify_column

    @identify_column.setter
    def identify_column(self, value):
        self._identify_column = value
    @property
    def is_partition(self):
        return self._is_partition

    @is_partition.setter
    def is_partition(self, value):
        self._is_partition = value
    @property
    def partition_column(self):
        return self._partition_column

    @partition_column.setter
    def partition_column(self, value):
        self._partition_column = value
    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, value):
        self._project = value
    @property
    def refresh_period(self):
        return self._refresh_period

    @refresh_period.setter
    def refresh_period(self, value):
        self._refresh_period = value
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        self._table = value
    @property
    def where_columns(self):
        return self._where_columns

    @where_columns.setter
    def where_columns(self, value):
        if isinstance(value, list):
            self._where_columns = list()
            for i in value:
                self._where_columns.append(i)
    @property
    def where_condition(self):
        return self._where_condition

    @where_condition.setter
    def where_condition(self, value):
        self._where_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_channel_list:
            if isinstance(self.apply_channel_list, list):
                for i in range(0, len(self.apply_channel_list)):
                    element = self.apply_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_channel_list, 'to_alipay_dict'):
                params['apply_channel_list'] = self.apply_channel_list.to_alipay_dict()
            else:
                params['apply_channel_list'] = self.apply_channel_list
        if self.crowd_desc:
            if hasattr(self.crowd_desc, 'to_alipay_dict'):
                params['crowd_desc'] = self.crowd_desc.to_alipay_dict()
            else:
                params['crowd_desc'] = self.crowd_desc
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.external_crowd_code:
            if hasattr(self.external_crowd_code, 'to_alipay_dict'):
                params['external_crowd_code'] = self.external_crowd_code.to_alipay_dict()
            else:
                params['external_crowd_code'] = self.external_crowd_code
        if self.hidden:
            if hasattr(self.hidden, 'to_alipay_dict'):
                params['hidden'] = self.hidden.to_alipay_dict()
            else:
                params['hidden'] = self.hidden
        if self.identify_column:
            if hasattr(self.identify_column, 'to_alipay_dict'):
                params['identify_column'] = self.identify_column.to_alipay_dict()
            else:
                params['identify_column'] = self.identify_column
        if self.is_partition:
            if hasattr(self.is_partition, 'to_alipay_dict'):
                params['is_partition'] = self.is_partition.to_alipay_dict()
            else:
                params['is_partition'] = self.is_partition
        if self.partition_column:
            if hasattr(self.partition_column, 'to_alipay_dict'):
                params['partition_column'] = self.partition_column.to_alipay_dict()
            else:
                params['partition_column'] = self.partition_column
        if self.project:
            if hasattr(self.project, 'to_alipay_dict'):
                params['project'] = self.project.to_alipay_dict()
            else:
                params['project'] = self.project
        if self.refresh_period:
            if hasattr(self.refresh_period, 'to_alipay_dict'):
                params['refresh_period'] = self.refresh_period.to_alipay_dict()
            else:
                params['refresh_period'] = self.refresh_period
        if self.table:
            if hasattr(self.table, 'to_alipay_dict'):
                params['table'] = self.table.to_alipay_dict()
            else:
                params['table'] = self.table
        if self.where_columns:
            if isinstance(self.where_columns, list):
                for i in range(0, len(self.where_columns)):
                    element = self.where_columns[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.where_columns[i] = element.to_alipay_dict()
            if hasattr(self.where_columns, 'to_alipay_dict'):
                params['where_columns'] = self.where_columns.to_alipay_dict()
            else:
                params['where_columns'] = self.where_columns
        if self.where_condition:
            if hasattr(self.where_condition, 'to_alipay_dict'):
                params['where_condition'] = self.where_condition.to_alipay_dict()
            else:
                params['where_condition'] = self.where_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanOdpscrowdCreateModel()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_desc' in d:
            o.crowd_desc = d['crowd_desc']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'external_crowd_code' in d:
            o.external_crowd_code = d['external_crowd_code']
        if 'hidden' in d:
            o.hidden = d['hidden']
        if 'identify_column' in d:
            o.identify_column = d['identify_column']
        if 'is_partition' in d:
            o.is_partition = d['is_partition']
        if 'partition_column' in d:
            o.partition_column = d['partition_column']
        if 'project' in d:
            o.project = d['project']
        if 'refresh_period' in d:
            o.refresh_period = d['refresh_period']
        if 'table' in d:
            o.table = d['table']
        if 'where_columns' in d:
            o.where_columns = d['where_columns']
        if 'where_condition' in d:
            o.where_condition = d['where_condition']
        return o


