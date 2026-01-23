#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationTaskbenefitcenterPointModifyModel(object):

    def __init__(self):
        self._change_num = None
        self._change_type = None
        self._event_code = None
        self._event_desc = None
        self._open_id = None
        self._point_code = None
        self._user_id = None

    @property
    def change_num(self):
        return self._change_num

    @change_num.setter
    def change_num(self, value):
        self._change_num = value
    @property
    def change_type(self):
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        self._change_type = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def event_desc(self):
        return self._event_desc

    @event_desc.setter
    def event_desc(self, value):
        self._event_desc = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def point_code(self):
        return self._point_code

    @point_code.setter
    def point_code(self, value):
        self._point_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.change_num:
            if hasattr(self.change_num, 'to_alipay_dict'):
                params['change_num'] = self.change_num.to_alipay_dict()
            else:
                params['change_num'] = self.change_num
        if self.change_type:
            if hasattr(self.change_type, 'to_alipay_dict'):
                params['change_type'] = self.change_type.to_alipay_dict()
            else:
                params['change_type'] = self.change_type
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.event_desc:
            if hasattr(self.event_desc, 'to_alipay_dict'):
                params['event_desc'] = self.event_desc.to_alipay_dict()
            else:
                params['event_desc'] = self.event_desc
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.point_code:
            if hasattr(self.point_code, 'to_alipay_dict'):
                params['point_code'] = self.point_code.to_alipay_dict()
            else:
                params['point_code'] = self.point_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationTaskbenefitcenterPointModifyModel()
        if 'change_num' in d:
            o.change_num = d['change_num']
        if 'change_type' in d:
            o.change_type = d['change_type']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'event_desc' in d:
            o.event_desc = d['event_desc']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'point_code' in d:
            o.point_code = d['point_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


