#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCrowdDataSyncModel(object):

    def __init__(self):
        self._biz_from = None
        self._create_id = None
        self._crowd_id = None
        self._crowd_name = None
        self._crowd_size = None
        self._crowd_status = None
        self._end_time = None
        self._owner_id = None
        self._start_time = None
        self._update_circle_type = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def create_id(self):
        return self._create_id

    @create_id.setter
    def create_id(self, value):
        self._create_id = value
    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def crowd_size(self):
        return self._crowd_size

    @crowd_size.setter
    def crowd_size(self, value):
        self._crowd_size = value
    @property
    def crowd_status(self):
        return self._crowd_status

    @crowd_status.setter
    def crowd_status(self, value):
        self._crowd_status = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def update_circle_type(self):
        return self._update_circle_type

    @update_circle_type.setter
    def update_circle_type(self, value):
        self._update_circle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.create_id:
            if hasattr(self.create_id, 'to_alipay_dict'):
                params['create_id'] = self.create_id.to_alipay_dict()
            else:
                params['create_id'] = self.create_id
        if self.crowd_id:
            if hasattr(self.crowd_id, 'to_alipay_dict'):
                params['crowd_id'] = self.crowd_id.to_alipay_dict()
            else:
                params['crowd_id'] = self.crowd_id
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.crowd_size:
            if hasattr(self.crowd_size, 'to_alipay_dict'):
                params['crowd_size'] = self.crowd_size.to_alipay_dict()
            else:
                params['crowd_size'] = self.crowd_size
        if self.crowd_status:
            if hasattr(self.crowd_status, 'to_alipay_dict'):
                params['crowd_status'] = self.crowd_status.to_alipay_dict()
            else:
                params['crowd_status'] = self.crowd_status
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.update_circle_type:
            if hasattr(self.update_circle_type, 'to_alipay_dict'):
                params['update_circle_type'] = self.update_circle_type.to_alipay_dict()
            else:
                params['update_circle_type'] = self.update_circle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCrowdDataSyncModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'create_id' in d:
            o.create_id = d['create_id']
        if 'crowd_id' in d:
            o.crowd_id = d['crowd_id']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'crowd_size' in d:
            o.crowd_size = d['crowd_size']
        if 'crowd_status' in d:
            o.crowd_status = d['crowd_status']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'update_circle_type' in d:
            o.update_circle_type = d['update_circle_type']
        return o


