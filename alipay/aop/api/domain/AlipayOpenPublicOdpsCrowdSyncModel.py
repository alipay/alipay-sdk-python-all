#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicOdpsCrowdSyncModel(object):

    def __init__(self):
        self._channel = None
        self._crowd_name = None
        self._data_partition = None
        self._field_name = None
        self._group_id = None
        self._table_name = None
        self._user_type = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def data_partition(self):
        return self._data_partition

    @data_partition.setter
    def data_partition(self, value):
        if isinstance(value, list):
            self._data_partition = list()
            for i in value:
                self._data_partition.append(i)
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.data_partition:
            if isinstance(self.data_partition, list):
                for i in range(0, len(self.data_partition)):
                    element = self.data_partition[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_partition[i] = element.to_alipay_dict()
            if hasattr(self.data_partition, 'to_alipay_dict'):
                params['data_partition'] = self.data_partition.to_alipay_dict()
            else:
                params['data_partition'] = self.data_partition
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicOdpsCrowdSyncModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'data_partition' in d:
            o.data_partition = d['data_partition']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


