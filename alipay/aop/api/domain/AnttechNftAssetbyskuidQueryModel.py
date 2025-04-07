#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftAssetbyskuidQueryModel(object):

    def __init__(self):
        self._id_no = None
        self._id_type = None
        self._open_id = None
        self._page = None
        self._page_size = None
        self._product_instance_id = None
        self._req_msg_id = None
        self._sku_id = None

    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def product_instance_id(self):
        return self._product_instance_id

    @product_instance_id.setter
    def product_instance_id(self, value):
        self._product_instance_id = value
    @property
    def req_msg_id(self):
        return self._req_msg_id

    @req_msg_id.setter
    def req_msg_id(self, value):
        self._req_msg_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.product_instance_id:
            if hasattr(self.product_instance_id, 'to_alipay_dict'):
                params['product_instance_id'] = self.product_instance_id.to_alipay_dict()
            else:
                params['product_instance_id'] = self.product_instance_id
        if self.req_msg_id:
            if hasattr(self.req_msg_id, 'to_alipay_dict'):
                params['req_msg_id'] = self.req_msg_id.to_alipay_dict()
            else:
                params['req_msg_id'] = self.req_msg_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftAssetbyskuidQueryModel()
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'product_instance_id' in d:
            o.product_instance_id = d['product_instance_id']
        if 'req_msg_id' in d:
            o.req_msg_id = d['req_msg_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


