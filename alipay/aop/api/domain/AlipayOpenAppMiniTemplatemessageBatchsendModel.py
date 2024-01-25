#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMiniTemplatemessageBatchsendModel(object):

    def __init__(self):
        self._crowd_code = None
        self._data = None
        self._page = None
        self._schedule_send_time = None
        self._template_id = None

    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def schedule_send_time(self):
        return self._schedule_send_time

    @schedule_send_time.setter
    def schedule_send_time(self, value):
        self._schedule_send_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.schedule_send_time:
            if hasattr(self.schedule_send_time, 'to_alipay_dict'):
                params['schedule_send_time'] = self.schedule_send_time.to_alipay_dict()
            else:
                params['schedule_send_time'] = self.schedule_send_time
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMiniTemplatemessageBatchsendModel()
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'data' in d:
            o.data = d['data']
        if 'page' in d:
            o.page = d['page']
        if 'schedule_send_time' in d:
            o.schedule_send_time = d['schedule_send_time']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


