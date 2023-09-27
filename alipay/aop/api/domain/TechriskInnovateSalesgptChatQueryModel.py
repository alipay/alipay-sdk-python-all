#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TechriskInnovateSalesgptChatQueryModel(object):

    def __init__(self):
        self._chat_bot_id = None
        self._current_page = None
        self._mer_pid = None
        self._open_id = None
        self._page_size = None
        self._source_app_id = None
        self._user_id = None

    @property
    def chat_bot_id(self):
        return self._chat_bot_id

    @chat_bot_id.setter
    def chat_bot_id(self, value):
        self._chat_bot_id = value
    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def mer_pid(self):
        return self._mer_pid

    @mer_pid.setter
    def mer_pid(self, value):
        self._mer_pid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def source_app_id(self):
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, value):
        self._source_app_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chat_bot_id:
            if hasattr(self.chat_bot_id, 'to_alipay_dict'):
                params['chat_bot_id'] = self.chat_bot_id.to_alipay_dict()
            else:
                params['chat_bot_id'] = self.chat_bot_id
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.mer_pid:
            if hasattr(self.mer_pid, 'to_alipay_dict'):
                params['mer_pid'] = self.mer_pid.to_alipay_dict()
            else:
                params['mer_pid'] = self.mer_pid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.source_app_id:
            if hasattr(self.source_app_id, 'to_alipay_dict'):
                params['source_app_id'] = self.source_app_id.to_alipay_dict()
            else:
                params['source_app_id'] = self.source_app_id
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
        o = TechriskInnovateSalesgptChatQueryModel()
        if 'chat_bot_id' in d:
            o.chat_bot_id = d['chat_bot_id']
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'mer_pid' in d:
            o.mer_pid = d['mer_pid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'source_app_id' in d:
            o.source_app_id = d['source_app_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


