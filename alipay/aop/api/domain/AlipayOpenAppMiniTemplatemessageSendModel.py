#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMiniTemplatemessageSendModel(object):

    def __init__(self):
        self._data = None
        self._form_id = None
        self._page = None
        self._to_user_id = None
        self._user_template_id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def form_id(self):
        return self._form_id

    @form_id.setter
    def form_id(self, value):
        self._form_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value
    @property
    def user_template_id(self):
        return self._user_template_id

    @user_template_id.setter
    def user_template_id(self, value):
        self._user_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.form_id:
            if hasattr(self.form_id, 'to_alipay_dict'):
                params['form_id'] = self.form_id.to_alipay_dict()
            else:
                params['form_id'] = self.form_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        if self.user_template_id:
            if hasattr(self.user_template_id, 'to_alipay_dict'):
                params['user_template_id'] = self.user_template_id.to_alipay_dict()
            else:
                params['user_template_id'] = self.user_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMiniTemplatemessageSendModel()
        if 'data' in d:
            o.data = d['data']
        if 'form_id' in d:
            o.form_id = d['form_id']
        if 'page' in d:
            o.page = d['page']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        if 'user_template_id' in d:
            o.user_template_id = d['user_template_id']
        return o


