#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialOpengreenEnergyQueryModel(object):

    def __init__(self):
        self._biz_no = None
        self._end_time = None
        self._ext_info = None
        self._green_actions = None
        self._pid = None
        self._source = None
        self._start_time = None
        self._user_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def green_actions(self):
        return self._green_actions

    @green_actions.setter
    def green_actions(self, value):
        if isinstance(value, list):
            self._green_actions = list()
            for i in value:
                self._green_actions.append(i)
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.green_actions:
            if isinstance(self.green_actions, list):
                for i in range(0, len(self.green_actions)):
                    element = self.green_actions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.green_actions[i] = element.to_alipay_dict()
            if hasattr(self.green_actions, 'to_alipay_dict'):
                params['green_actions'] = self.green_actions.to_alipay_dict()
            else:
                params['green_actions'] = self.green_actions
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AlipaySocialOpengreenEnergyQueryModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'green_actions' in d:
            o.green_actions = d['green_actions']
        if 'pid' in d:
            o.pid = d['pid']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


