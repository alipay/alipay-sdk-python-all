#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdCreativeBatchqueryModel(object):

    def __init__(self):
        self._batch_tag = None
        self._biz_token = None
        self._current = None
        self._group_outer_id = None
        self._page_size = None
        self._plan_outer_id = None
        self._status = None

    @property
    def batch_tag(self):
        return self._batch_tag

    @batch_tag.setter
    def batch_tag(self, value):
        self._batch_tag = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
    @property
    def group_outer_id(self):
        return self._group_outer_id

    @group_outer_id.setter
    def group_outer_id(self, value):
        self._group_outer_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plan_outer_id(self):
        return self._plan_outer_id

    @plan_outer_id.setter
    def plan_outer_id(self, value):
        self._plan_outer_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_tag:
            if hasattr(self.batch_tag, 'to_alipay_dict'):
                params['batch_tag'] = self.batch_tag.to_alipay_dict()
            else:
                params['batch_tag'] = self.batch_tag
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.current:
            if hasattr(self.current, 'to_alipay_dict'):
                params['current'] = self.current.to_alipay_dict()
            else:
                params['current'] = self.current
        if self.group_outer_id:
            if hasattr(self.group_outer_id, 'to_alipay_dict'):
                params['group_outer_id'] = self.group_outer_id.to_alipay_dict()
            else:
                params['group_outer_id'] = self.group_outer_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plan_outer_id:
            if hasattr(self.plan_outer_id, 'to_alipay_dict'):
                params['plan_outer_id'] = self.plan_outer_id.to_alipay_dict()
            else:
                params['plan_outer_id'] = self.plan_outer_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdCreativeBatchqueryModel()
        if 'batch_tag' in d:
            o.batch_tag = d['batch_tag']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'current' in d:
            o.current = d['current']
        if 'group_outer_id' in d:
            o.group_outer_id = d['group_outer_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plan_outer_id' in d:
            o.plan_outer_id = d['plan_outer_id']
        if 'status' in d:
            o.status = d['status']
        return o


