#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringDishCommgroupQueryModel(object):

    def __init__(self):
        self._comm_group_id = None
        self._page_no = None
        self._page_size = None

    @property
    def comm_group_id(self):
        return self._comm_group_id

    @comm_group_id.setter
    def comm_group_id(self, value):
        self._comm_group_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.comm_group_id:
            if hasattr(self.comm_group_id, 'to_alipay_dict'):
                params['comm_group_id'] = self.comm_group_id.to_alipay_dict()
            else:
                params['comm_group_id'] = self.comm_group_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringDishCommgroupQueryModel()
        if 'comm_group_id' in d:
            o.comm_group_id = d['comm_group_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


