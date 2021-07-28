#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandShopBatchqueryModel(object):

    def __init__(self):
        self._page_no = None
        self._page_size = None
        self._scene = None
        self._store_open_id = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def store_open_id(self):
        return self._store_open_id

    @store_open_id.setter
    def store_open_id(self, value):
        self._store_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.store_open_id:
            if hasattr(self.store_open_id, 'to_alipay_dict'):
                params['store_open_id'] = self.store_open_id.to_alipay_dict()
            else:
                params['store_open_id'] = self.store_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandShopBatchqueryModel()
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene' in d:
            o.scene = d['scene']
        if 'store_open_id' in d:
            o.store_open_id = d['store_open_id']
        return o


