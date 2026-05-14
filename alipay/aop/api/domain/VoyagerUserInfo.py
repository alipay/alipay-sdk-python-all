#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerUserInfo(object):

    def __init__(self):
        self._traffic_side_id = None
        self._traffic_side_open_id = None
        self._voyager_user_id = None

    @property
    def traffic_side_id(self):
        return self._traffic_side_id

    @traffic_side_id.setter
    def traffic_side_id(self, value):
        self._traffic_side_id = value
    @property
    def traffic_side_open_id(self):
        return self._traffic_side_open_id

    @traffic_side_open_id.setter
    def traffic_side_open_id(self, value):
        self._traffic_side_open_id = value
    @property
    def voyager_user_id(self):
        return self._voyager_user_id

    @voyager_user_id.setter
    def voyager_user_id(self, value):
        self._voyager_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.traffic_side_id:
            if hasattr(self.traffic_side_id, 'to_alipay_dict'):
                params['traffic_side_id'] = self.traffic_side_id.to_alipay_dict()
            else:
                params['traffic_side_id'] = self.traffic_side_id
        if self.traffic_side_open_id:
            if hasattr(self.traffic_side_open_id, 'to_alipay_dict'):
                params['traffic_side_open_id'] = self.traffic_side_open_id.to_alipay_dict()
            else:
                params['traffic_side_open_id'] = self.traffic_side_open_id
        if self.voyager_user_id:
            if hasattr(self.voyager_user_id, 'to_alipay_dict'):
                params['voyager_user_id'] = self.voyager_user_id.to_alipay_dict()
            else:
                params['voyager_user_id'] = self.voyager_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerUserInfo()
        if 'traffic_side_id' in d:
            o.traffic_side_id = d['traffic_side_id']
        if 'traffic_side_open_id' in d:
            o.traffic_side_open_id = d['traffic_side_open_id']
        if 'voyager_user_id' in d:
            o.voyager_user_id = d['voyager_user_id']
        return o


