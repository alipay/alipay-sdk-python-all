#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoMap import ExtInfoMap


class AlipayUserGamecenterEventSubmitModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._event_finish_channel = None
        self._event_finish_date = None
        self._event_id = None
        self._open_id = None
        self._out_biz_no = None
        self._property_map = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def event_finish_channel(self):
        return self._event_finish_channel

    @event_finish_channel.setter
    def event_finish_channel(self, value):
        self._event_finish_channel = value
    @property
    def event_finish_date(self):
        return self._event_finish_date

    @event_finish_date.setter
    def event_finish_date(self, value):
        self._event_finish_date = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def property_map(self):
        return self._property_map

    @property_map.setter
    def property_map(self, value):
        if isinstance(value, list):
            self._property_map = list()
            for i in value:
                if isinstance(i, ExtInfoMap):
                    self._property_map.append(i)
                else:
                    self._property_map.append(ExtInfoMap.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.event_finish_channel:
            if hasattr(self.event_finish_channel, 'to_alipay_dict'):
                params['event_finish_channel'] = self.event_finish_channel.to_alipay_dict()
            else:
                params['event_finish_channel'] = self.event_finish_channel
        if self.event_finish_date:
            if hasattr(self.event_finish_date, 'to_alipay_dict'):
                params['event_finish_date'] = self.event_finish_date.to_alipay_dict()
            else:
                params['event_finish_date'] = self.event_finish_date
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.property_map:
            if isinstance(self.property_map, list):
                for i in range(0, len(self.property_map)):
                    element = self.property_map[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.property_map[i] = element.to_alipay_dict()
            if hasattr(self.property_map, 'to_alipay_dict'):
                params['property_map'] = self.property_map.to_alipay_dict()
            else:
                params['property_map'] = self.property_map
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGamecenterEventSubmitModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'event_finish_channel' in d:
            o.event_finish_channel = d['event_finish_channel']
        if 'event_finish_date' in d:
            o.event_finish_date = d['event_finish_date']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'property_map' in d:
            o.property_map = d['property_map']
        return o


