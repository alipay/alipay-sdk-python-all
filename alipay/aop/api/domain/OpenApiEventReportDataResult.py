#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiEventReportItemVO import OpenApiEventReportItemVO


class OpenApiEventReportDataResult(object):

    def __init__(self):
        self._async_query_id = None
        self._async_query_status = None
        self._items = None
        self._sync_query_result_valid = None

    @property
    def async_query_id(self):
        return self._async_query_id

    @async_query_id.setter
    def async_query_id(self, value):
        self._async_query_id = value
    @property
    def async_query_status(self):
        return self._async_query_status

    @async_query_status.setter
    def async_query_status(self, value):
        self._async_query_status = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, OpenApiEventReportItemVO):
                    self._items.append(i)
                else:
                    self._items.append(OpenApiEventReportItemVO.from_alipay_dict(i))
    @property
    def sync_query_result_valid(self):
        return self._sync_query_result_valid

    @sync_query_result_valid.setter
    def sync_query_result_valid(self, value):
        self._sync_query_result_valid = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_query_id:
            if hasattr(self.async_query_id, 'to_alipay_dict'):
                params['async_query_id'] = self.async_query_id.to_alipay_dict()
            else:
                params['async_query_id'] = self.async_query_id
        if self.async_query_status:
            if hasattr(self.async_query_status, 'to_alipay_dict'):
                params['async_query_status'] = self.async_query_status.to_alipay_dict()
            else:
                params['async_query_status'] = self.async_query_status
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        if self.sync_query_result_valid:
            if hasattr(self.sync_query_result_valid, 'to_alipay_dict'):
                params['sync_query_result_valid'] = self.sync_query_result_valid.to_alipay_dict()
            else:
                params['sync_query_result_valid'] = self.sync_query_result_valid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiEventReportDataResult()
        if 'async_query_id' in d:
            o.async_query_id = d['async_query_id']
        if 'async_query_status' in d:
            o.async_query_status = d['async_query_status']
        if 'items' in d:
            o.items = d['items']
        if 'sync_query_result_valid' in d:
            o.sync_query_result_valid = d['sync_query_result_valid']
        return o


