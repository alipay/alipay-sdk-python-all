#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromotePage(object):

    def __init__(self):
        self._page_id = None
        self._page_name = None
        self._page_status = None
        self._type = None

    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value
    @property
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def page_status(self):
        return self._page_status

    @page_status.setter
    def page_status(self, value):
        self._page_status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_id:
            if hasattr(self.page_id, 'to_alipay_dict'):
                params['page_id'] = self.page_id.to_alipay_dict()
            else:
                params['page_id'] = self.page_id
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.page_status:
            if hasattr(self.page_status, 'to_alipay_dict'):
                params['page_status'] = self.page_status.to_alipay_dict()
            else:
                params['page_status'] = self.page_status
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
        o = PromotePage()
        if 'page_id' in d:
            o.page_id = d['page_id']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'page_status' in d:
            o.page_status = d['page_status']
        if 'type' in d:
            o.type = d['type']
        return o


