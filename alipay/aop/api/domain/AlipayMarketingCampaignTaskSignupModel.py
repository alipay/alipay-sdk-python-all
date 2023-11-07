#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignTaskSignupModel(object):

    def __init__(self):
        self._channel_info = None
        self._open_id = None
        self._out_biz_no = None
        self._task_cen_id = None
        self._task_id = None
        self._user_id = None

    @property
    def channel_info(self):
        return self._channel_info

    @channel_info.setter
    def channel_info(self, value):
        self._channel_info = value
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
    def task_cen_id(self):
        return self._task_cen_id

    @task_cen_id.setter
    def task_cen_id(self, value):
        self._task_cen_id = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_info:
            if hasattr(self.channel_info, 'to_alipay_dict'):
                params['channel_info'] = self.channel_info.to_alipay_dict()
            else:
                params['channel_info'] = self.channel_info
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
        if self.task_cen_id:
            if hasattr(self.task_cen_id, 'to_alipay_dict'):
                params['task_cen_id'] = self.task_cen_id.to_alipay_dict()
            else:
                params['task_cen_id'] = self.task_cen_id
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
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
        o = AlipayMarketingCampaignTaskSignupModel()
        if 'channel_info' in d:
            o.channel_info = d['channel_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'task_cen_id' in d:
            o.task_cen_id = d['task_cen_id']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


