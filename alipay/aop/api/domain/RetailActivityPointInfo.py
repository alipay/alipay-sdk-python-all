#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PrizeDetailInfo import PrizeDetailInfo


class RetailActivityPointInfo(object):

    def __init__(self):
        self._activity_name = None
        self._activity_type = None
        self._end_time = None
        self._point_amount_floor = None
        self._prize_info = None
        self._retail_activity_id = None
        self._start_time = None
        self._status = None

    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def point_amount_floor(self):
        return self._point_amount_floor

    @point_amount_floor.setter
    def point_amount_floor(self, value):
        self._point_amount_floor = value
    @property
    def prize_info(self):
        return self._prize_info

    @prize_info.setter
    def prize_info(self, value):
        if isinstance(value, list):
            self._prize_info = list()
            for i in value:
                if isinstance(i, PrizeDetailInfo):
                    self._prize_info.append(i)
                else:
                    self._prize_info.append(PrizeDetailInfo.from_alipay_dict(i))
    @property
    def retail_activity_id(self):
        return self._retail_activity_id

    @retail_activity_id.setter
    def retail_activity_id(self, value):
        self._retail_activity_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.point_amount_floor:
            if hasattr(self.point_amount_floor, 'to_alipay_dict'):
                params['point_amount_floor'] = self.point_amount_floor.to_alipay_dict()
            else:
                params['point_amount_floor'] = self.point_amount_floor
        if self.prize_info:
            if isinstance(self.prize_info, list):
                for i in range(0, len(self.prize_info)):
                    element = self.prize_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.prize_info[i] = element.to_alipay_dict()
            if hasattr(self.prize_info, 'to_alipay_dict'):
                params['prize_info'] = self.prize_info.to_alipay_dict()
            else:
                params['prize_info'] = self.prize_info
        if self.retail_activity_id:
            if hasattr(self.retail_activity_id, 'to_alipay_dict'):
                params['retail_activity_id'] = self.retail_activity_id.to_alipay_dict()
            else:
                params['retail_activity_id'] = self.retail_activity_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = RetailActivityPointInfo()
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'point_amount_floor' in d:
            o.point_amount_floor = d['point_amount_floor']
        if 'prize_info' in d:
            o.prize_info = d['prize_info']
        if 'retail_activity_id' in d:
            o.retail_activity_id = d['retail_activity_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


