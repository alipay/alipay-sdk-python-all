#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContract(object):

    def __init__(self):
        self._alipay_user_id = None
        self._contract_content = None
        self._end_time = None
        self._page_url = None
        self._start_time = None
        self._subscribe = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def contract_content(self):
        return self._contract_content

    @contract_content.setter
    def contract_content(self, value):
        self._contract_content = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def subscribe(self):
        return self._subscribe

    @subscribe.setter
    def subscribe(self, value):
        self._subscribe = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.contract_content:
            if hasattr(self.contract_content, 'to_alipay_dict'):
                params['contract_content'] = self.contract_content.to_alipay_dict()
            else:
                params['contract_content'] = self.contract_content
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.page_url:
            if hasattr(self.page_url, 'to_alipay_dict'):
                params['page_url'] = self.page_url.to_alipay_dict()
            else:
                params['page_url'] = self.page_url
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.subscribe:
            if hasattr(self.subscribe, 'to_alipay_dict'):
                params['subscribe'] = self.subscribe.to_alipay_dict()
            else:
                params['subscribe'] = self.subscribe
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContract()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'contract_content' in d:
            o.contract_content = d['contract_content']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'page_url' in d:
            o.page_url = d['page_url']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'subscribe' in d:
            o.subscribe = d['subscribe']
        return o


