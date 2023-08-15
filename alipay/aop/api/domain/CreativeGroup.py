#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreativeGroup(object):

    def __init__(self):
        self._create_time = None
        self._descrption = None
        self._group_id = None
        self._group_name = None
        self._item_sum_count = None
        self._status = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def descrption(self):
        return self._descrption

    @descrption.setter
    def descrption(self, value):
        self._descrption = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def item_sum_count(self):
        return self._item_sum_count

    @item_sum_count.setter
    def item_sum_count(self, value):
        self._item_sum_count = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.descrption:
            if hasattr(self.descrption, 'to_alipay_dict'):
                params['descrption'] = self.descrption.to_alipay_dict()
            else:
                params['descrption'] = self.descrption
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        if self.item_sum_count:
            if hasattr(self.item_sum_count, 'to_alipay_dict'):
                params['item_sum_count'] = self.item_sum_count.to_alipay_dict()
            else:
                params['item_sum_count'] = self.item_sum_count
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreativeGroup()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'descrption' in d:
            o.descrption = d['descrption']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        if 'item_sum_count' in d:
            o.item_sum_count = d['item_sum_count']
        if 'status' in d:
            o.status = d['status']
        return o


