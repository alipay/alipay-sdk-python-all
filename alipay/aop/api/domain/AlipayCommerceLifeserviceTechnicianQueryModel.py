#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceTechnicianQueryModel(object):

    def __init__(self):
        self._out_technician_ids = None
        self._page_num = None
        self._page_size = None
        self._shop_id = None
        self._status = None
        self._technician_ids = None

    @property
    def out_technician_ids(self):
        return self._out_technician_ids

    @out_technician_ids.setter
    def out_technician_ids(self, value):
        if isinstance(value, list):
            self._out_technician_ids = list()
            for i in value:
                self._out_technician_ids.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def technician_ids(self):
        return self._technician_ids

    @technician_ids.setter
    def technician_ids(self, value):
        if isinstance(value, list):
            self._technician_ids = list()
            for i in value:
                self._technician_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.out_technician_ids:
            if isinstance(self.out_technician_ids, list):
                for i in range(0, len(self.out_technician_ids)):
                    element = self.out_technician_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_technician_ids[i] = element.to_alipay_dict()
            if hasattr(self.out_technician_ids, 'to_alipay_dict'):
                params['out_technician_ids'] = self.out_technician_ids.to_alipay_dict()
            else:
                params['out_technician_ids'] = self.out_technician_ids
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.technician_ids:
            if isinstance(self.technician_ids, list):
                for i in range(0, len(self.technician_ids)):
                    element = self.technician_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.technician_ids[i] = element.to_alipay_dict()
            if hasattr(self.technician_ids, 'to_alipay_dict'):
                params['technician_ids'] = self.technician_ids.to_alipay_dict()
            else:
                params['technician_ids'] = self.technician_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceTechnicianQueryModel()
        if 'out_technician_ids' in d:
            o.out_technician_ids = d['out_technician_ids']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'technician_ids' in d:
            o.technician_ids = d['technician_ids']
        return o


