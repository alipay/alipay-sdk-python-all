#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasPutplanListBatchqueryModel(object):

    def __init__(self):
        self._channel_category = None
        self._name = None
        self._page = None
        self._size = None
        self._status = None
        self._tenant_code = None
        self._user_id = None

    @property
    def channel_category(self):
        return self._channel_category

    @channel_category.setter
    def channel_category(self, value):
        self._channel_category = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tenant_code(self):
        return self._tenant_code

    @tenant_code.setter
    def tenant_code(self, value):
        self._tenant_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_category:
            if hasattr(self.channel_category, 'to_alipay_dict'):
                params['channel_category'] = self.channel_category.to_alipay_dict()
            else:
                params['channel_category'] = self.channel_category
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tenant_code:
            if hasattr(self.tenant_code, 'to_alipay_dict'):
                params['tenant_code'] = self.tenant_code.to_alipay_dict()
            else:
                params['tenant_code'] = self.tenant_code
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
        o = DatadigitalFincloudFinsaasPutplanListBatchqueryModel()
        if 'channel_category' in d:
            o.channel_category = d['channel_category']
        if 'name' in d:
            o.name = d['name']
        if 'page' in d:
            o.page = d['page']
        if 'size' in d:
            o.size = d['size']
        if 'status' in d:
            o.status = d['status']
        if 'tenant_code' in d:
            o.tenant_code = d['tenant_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


