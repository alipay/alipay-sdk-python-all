#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubscribeMemberInfoDTO(object):

    def __init__(self):
        self._expired_date = None
        self._left_times = None
        self._subscribe_date = None
        self._subscribe_package_id = None
        self._subscribe_package_type = None
        self._subscribe_times = None

    @property
    def expired_date(self):
        return self._expired_date

    @expired_date.setter
    def expired_date(self, value):
        self._expired_date = value
    @property
    def left_times(self):
        return self._left_times

    @left_times.setter
    def left_times(self, value):
        self._left_times = value
    @property
    def subscribe_date(self):
        return self._subscribe_date

    @subscribe_date.setter
    def subscribe_date(self, value):
        self._subscribe_date = value
    @property
    def subscribe_package_id(self):
        return self._subscribe_package_id

    @subscribe_package_id.setter
    def subscribe_package_id(self, value):
        self._subscribe_package_id = value
    @property
    def subscribe_package_type(self):
        return self._subscribe_package_type

    @subscribe_package_type.setter
    def subscribe_package_type(self, value):
        self._subscribe_package_type = value
    @property
    def subscribe_times(self):
        return self._subscribe_times

    @subscribe_times.setter
    def subscribe_times(self, value):
        self._subscribe_times = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_date:
            if hasattr(self.expired_date, 'to_alipay_dict'):
                params['expired_date'] = self.expired_date.to_alipay_dict()
            else:
                params['expired_date'] = self.expired_date
        if self.left_times:
            if hasattr(self.left_times, 'to_alipay_dict'):
                params['left_times'] = self.left_times.to_alipay_dict()
            else:
                params['left_times'] = self.left_times
        if self.subscribe_date:
            if hasattr(self.subscribe_date, 'to_alipay_dict'):
                params['subscribe_date'] = self.subscribe_date.to_alipay_dict()
            else:
                params['subscribe_date'] = self.subscribe_date
        if self.subscribe_package_id:
            if hasattr(self.subscribe_package_id, 'to_alipay_dict'):
                params['subscribe_package_id'] = self.subscribe_package_id.to_alipay_dict()
            else:
                params['subscribe_package_id'] = self.subscribe_package_id
        if self.subscribe_package_type:
            if hasattr(self.subscribe_package_type, 'to_alipay_dict'):
                params['subscribe_package_type'] = self.subscribe_package_type.to_alipay_dict()
            else:
                params['subscribe_package_type'] = self.subscribe_package_type
        if self.subscribe_times:
            if hasattr(self.subscribe_times, 'to_alipay_dict'):
                params['subscribe_times'] = self.subscribe_times.to_alipay_dict()
            else:
                params['subscribe_times'] = self.subscribe_times
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscribeMemberInfoDTO()
        if 'expired_date' in d:
            o.expired_date = d['expired_date']
        if 'left_times' in d:
            o.left_times = d['left_times']
        if 'subscribe_date' in d:
            o.subscribe_date = d['subscribe_date']
        if 'subscribe_package_id' in d:
            o.subscribe_package_id = d['subscribe_package_id']
        if 'subscribe_package_type' in d:
            o.subscribe_package_type = d['subscribe_package_type']
        if 'subscribe_times' in d:
            o.subscribe_times = d['subscribe_times']
        return o


