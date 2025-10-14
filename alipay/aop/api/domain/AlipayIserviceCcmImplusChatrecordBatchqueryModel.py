#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmImplusChatrecordBatchqueryModel(object):

    def __init__(self):
        self._ccs_instance_id = None
        self._cid = None
        self._cursor_id = None
        self._direction = None
        self._end_id = None
        self._page_size = None

    @property
    def ccs_instance_id(self):
        return self._ccs_instance_id

    @ccs_instance_id.setter
    def ccs_instance_id(self, value):
        self._ccs_instance_id = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def cursor_id(self):
        return self._cursor_id

    @cursor_id.setter
    def cursor_id(self, value):
        self._cursor_id = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def end_id(self):
        return self._end_id

    @end_id.setter
    def end_id(self, value):
        self._end_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.ccs_instance_id:
            if hasattr(self.ccs_instance_id, 'to_alipay_dict'):
                params['ccs_instance_id'] = self.ccs_instance_id.to_alipay_dict()
            else:
                params['ccs_instance_id'] = self.ccs_instance_id
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.cursor_id:
            if hasattr(self.cursor_id, 'to_alipay_dict'):
                params['cursor_id'] = self.cursor_id.to_alipay_dict()
            else:
                params['cursor_id'] = self.cursor_id
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.end_id:
            if hasattr(self.end_id, 'to_alipay_dict'):
                params['end_id'] = self.end_id.to_alipay_dict()
            else:
                params['end_id'] = self.end_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCcmImplusChatrecordBatchqueryModel()
        if 'ccs_instance_id' in d:
            o.ccs_instance_id = d['ccs_instance_id']
        if 'cid' in d:
            o.cid = d['cid']
        if 'cursor_id' in d:
            o.cursor_id = d['cursor_id']
        if 'direction' in d:
            o.direction = d['direction']
        if 'end_id' in d:
            o.end_id = d['end_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


