#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppOrdermanagerCertificateuseQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._store_id = None
        self._write_off_end = None
        self._write_off_shop_ids = None
        self._write_off_start = None
        self._write_off_status = None

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
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def write_off_end(self):
        return self._write_off_end

    @write_off_end.setter
    def write_off_end(self, value):
        self._write_off_end = value
    @property
    def write_off_shop_ids(self):
        return self._write_off_shop_ids

    @write_off_shop_ids.setter
    def write_off_shop_ids(self, value):
        if isinstance(value, list):
            self._write_off_shop_ids = list()
            for i in value:
                self._write_off_shop_ids.append(i)
    @property
    def write_off_start(self):
        return self._write_off_start

    @write_off_start.setter
    def write_off_start(self, value):
        self._write_off_start = value
    @property
    def write_off_status(self):
        return self._write_off_status

    @write_off_status.setter
    def write_off_status(self, value):
        self._write_off_status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.write_off_end:
            if hasattr(self.write_off_end, 'to_alipay_dict'):
                params['write_off_end'] = self.write_off_end.to_alipay_dict()
            else:
                params['write_off_end'] = self.write_off_end
        if self.write_off_shop_ids:
            if isinstance(self.write_off_shop_ids, list):
                for i in range(0, len(self.write_off_shop_ids)):
                    element = self.write_off_shop_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.write_off_shop_ids[i] = element.to_alipay_dict()
            if hasattr(self.write_off_shop_ids, 'to_alipay_dict'):
                params['write_off_shop_ids'] = self.write_off_shop_ids.to_alipay_dict()
            else:
                params['write_off_shop_ids'] = self.write_off_shop_ids
        if self.write_off_start:
            if hasattr(self.write_off_start, 'to_alipay_dict'):
                params['write_off_start'] = self.write_off_start.to_alipay_dict()
            else:
                params['write_off_start'] = self.write_off_start
        if self.write_off_status:
            if hasattr(self.write_off_status, 'to_alipay_dict'):
                params['write_off_status'] = self.write_off_status.to_alipay_dict()
            else:
                params['write_off_status'] = self.write_off_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppOrdermanagerCertificateuseQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'write_off_end' in d:
            o.write_off_end = d['write_off_end']
        if 'write_off_shop_ids' in d:
            o.write_off_shop_ids = d['write_off_shop_ids']
        if 'write_off_start' in d:
            o.write_off_start = d['write_off_start']
        if 'write_off_status' in d:
            o.write_off_status = d['write_off_status']
        return o


