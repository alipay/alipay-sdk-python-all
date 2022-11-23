#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserGamecenterIncrementgameactionSubmitModel(object):

    def __init__(self):
        self._action_code = None
        self._action_finish_channel = None
        self._action_finish_date = None
        self._alipay_user_id = None
        self._open_id = None
        self._out_biz_no = None

    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def action_finish_channel(self):
        return self._action_finish_channel

    @action_finish_channel.setter
    def action_finish_channel(self, value):
        self._action_finish_channel = value
    @property
    def action_finish_date(self):
        return self._action_finish_date

    @action_finish_date.setter
    def action_finish_date(self, value):
        self._action_finish_date = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.action_code:
            if hasattr(self.action_code, 'to_alipay_dict'):
                params['action_code'] = self.action_code.to_alipay_dict()
            else:
                params['action_code'] = self.action_code
        if self.action_finish_channel:
            if hasattr(self.action_finish_channel, 'to_alipay_dict'):
                params['action_finish_channel'] = self.action_finish_channel.to_alipay_dict()
            else:
                params['action_finish_channel'] = self.action_finish_channel
        if self.action_finish_date:
            if hasattr(self.action_finish_date, 'to_alipay_dict'):
                params['action_finish_date'] = self.action_finish_date.to_alipay_dict()
            else:
                params['action_finish_date'] = self.action_finish_date
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserGamecenterIncrementgameactionSubmitModel()
        if 'action_code' in d:
            o.action_code = d['action_code']
        if 'action_finish_channel' in d:
            o.action_finish_channel = d['action_finish_channel']
        if 'action_finish_date' in d:
            o.action_finish_date = d['action_finish_date']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


