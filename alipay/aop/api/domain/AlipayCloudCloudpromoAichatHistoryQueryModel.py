#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoAichatHistoryQueryModel(object):

    def __init__(self):
        self._customer_id = None
        self._greater_request_id = None
        self._less_request_id = None
        self._num = None
        self._page = None
        self._scene_id = None
        self._source_id = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def greater_request_id(self):
        return self._greater_request_id

    @greater_request_id.setter
    def greater_request_id(self, value):
        self._greater_request_id = value
    @property
    def less_request_id(self):
        return self._less_request_id

    @less_request_id.setter
    def less_request_id(self, value):
        self._less_request_id = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.greater_request_id:
            if hasattr(self.greater_request_id, 'to_alipay_dict'):
                params['greater_request_id'] = self.greater_request_id.to_alipay_dict()
            else:
                params['greater_request_id'] = self.greater_request_id
        if self.less_request_id:
            if hasattr(self.less_request_id, 'to_alipay_dict'):
                params['less_request_id'] = self.less_request_id.to_alipay_dict()
            else:
                params['less_request_id'] = self.less_request_id
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAichatHistoryQueryModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'greater_request_id' in d:
            o.greater_request_id = d['greater_request_id']
        if 'less_request_id' in d:
            o.less_request_id = d['less_request_id']
        if 'num' in d:
            o.num = d['num']
        if 'page' in d:
            o.page = d['page']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


