#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsVirtualprizeUserGetModel(object):

    def __init__(self):
        self._biz_type = None
        self._grant_time = None
        self._open_id = None
        self._out_prize_ids = None
        self._status = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def grant_time(self):
        return self._grant_time

    @grant_time.setter
    def grant_time(self, value):
        self._grant_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_prize_ids(self):
        return self._out_prize_ids

    @out_prize_ids.setter
    def out_prize_ids(self, value):
        if isinstance(value, list):
            self._out_prize_ids = list()
            for i in value:
                self._out_prize_ids.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.grant_time:
            if hasattr(self.grant_time, 'to_alipay_dict'):
                params['grant_time'] = self.grant_time.to_alipay_dict()
            else:
                params['grant_time'] = self.grant_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_prize_ids:
            if isinstance(self.out_prize_ids, list):
                for i in range(0, len(self.out_prize_ids)):
                    element = self.out_prize_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_prize_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_prize_ids, 'to_alipay_dict'):
                params['out_prize_ids'] = self.out_prize_ids.to_alipay_dict()
            else:
                params['out_prize_ids'] = self.out_prize_ids
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayCommerceSportsVirtualprizeUserGetModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'grant_time' in d:
            o.grant_time = d['grant_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_prize_ids' in d:
            o.out_prize_ids = d['out_prize_ids']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


