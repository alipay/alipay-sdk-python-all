#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveInteractiveStateModifyModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._interactive_status = None
        self._interactive_type = None
        self._jump_url = None
        self._show_num = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def interactive_status(self):
        return self._interactive_status

    @interactive_status.setter
    def interactive_status(self, value):
        self._interactive_status = value
    @property
    def interactive_type(self):
        return self._interactive_type

    @interactive_type.setter
    def interactive_type(self, value):
        self._interactive_type = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def show_num(self):
        return self._show_num

    @show_num.setter
    def show_num(self, value):
        self._show_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.interactive_status:
            if hasattr(self.interactive_status, 'to_alipay_dict'):
                params['interactive_status'] = self.interactive_status.to_alipay_dict()
            else:
                params['interactive_status'] = self.interactive_status
        if self.interactive_type:
            if hasattr(self.interactive_type, 'to_alipay_dict'):
                params['interactive_type'] = self.interactive_type.to_alipay_dict()
            else:
                params['interactive_type'] = self.interactive_type
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.show_num:
            if hasattr(self.show_num, 'to_alipay_dict'):
                params['show_num'] = self.show_num.to_alipay_dict()
            else:
                params['show_num'] = self.show_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveInteractiveStateModifyModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'interactive_status' in d:
            o.interactive_status = d['interactive_status']
        if 'interactive_type' in d:
            o.interactive_type = d['interactive_type']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'show_num' in d:
            o.show_num = d['show_num']
        return o


