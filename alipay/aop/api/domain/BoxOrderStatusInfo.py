#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BoxOrderStatusInfo(object):

    def __init__(self):
        self._data = None
        self._ext_info = None
        self._gmt_modified = None
        self._item_id = None
        self._latest_status = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def latest_status(self):
        return self._latest_status

    @latest_status.setter
    def latest_status(self, value):
        self._latest_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.latest_status:
            if hasattr(self.latest_status, 'to_alipay_dict'):
                params['latest_status'] = self.latest_status.to_alipay_dict()
            else:
                params['latest_status'] = self.latest_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BoxOrderStatusInfo()
        if 'data' in d:
            o.data = d['data']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'latest_status' in d:
            o.latest_status = d['latest_status']
        return o


