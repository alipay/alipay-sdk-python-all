#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZmWatchListExtendInfo import ZmWatchListExtendInfo


class ZmWatchListDetail(object):

    def __init__(self):
        self._biz_code = None
        self._code = None
        self._extend_info = None
        self._level = None
        self._refresh_time = None
        self._settlement = None
        self._statement = None
        self._status = None
        self._type = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        if isinstance(value, list):
            self._extend_info = list()
            for i in value:
                if isinstance(i, ZmWatchListExtendInfo):
                    self._extend_info.append(i)
                else:
                    self._extend_info.append(ZmWatchListExtendInfo.from_alipay_dict(i))
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def refresh_time(self):
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, value):
        self._refresh_time = value
    @property
    def settlement(self):
        return self._settlement

    @settlement.setter
    def settlement(self, value):
        self._settlement = value
    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, value):
        self._statement = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.extend_info:
            if isinstance(self.extend_info, list):
                for i in range(0, len(self.extend_info)):
                    element = self.extend_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_info[i] = element.to_alipay_dict()
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.refresh_time:
            if hasattr(self.refresh_time, 'to_alipay_dict'):
                params['refresh_time'] = self.refresh_time.to_alipay_dict()
            else:
                params['refresh_time'] = self.refresh_time
        if self.settlement:
            if hasattr(self.settlement, 'to_alipay_dict'):
                params['settlement'] = self.settlement.to_alipay_dict()
            else:
                params['settlement'] = self.settlement
        if self.statement:
            if hasattr(self.statement, 'to_alipay_dict'):
                params['statement'] = self.statement.to_alipay_dict()
            else:
                params['statement'] = self.statement
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmWatchListDetail()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'code' in d:
            o.code = d['code']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'level' in d:
            o.level = d['level']
        if 'refresh_time' in d:
            o.refresh_time = d['refresh_time']
        if 'settlement' in d:
            o.settlement = d['settlement']
        if 'statement' in d:
            o.statement = d['statement']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


