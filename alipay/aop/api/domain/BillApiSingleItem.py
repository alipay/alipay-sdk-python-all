#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BillApiSingleItem(object):

    def __init__(self):
        self._biz_in_no = None
        self._biz_state_desc = None
        self._category_name = None
        self._consume_fee = None
        self._consume_title = None
        self._gmt_create = None
        self._opposite_name = None
        self._stat_fee = None
        self._stat_type = None

    @property
    def biz_in_no(self):
        return self._biz_in_no

    @biz_in_no.setter
    def biz_in_no(self, value):
        self._biz_in_no = value
    @property
    def biz_state_desc(self):
        return self._biz_state_desc

    @biz_state_desc.setter
    def biz_state_desc(self, value):
        self._biz_state_desc = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def consume_fee(self):
        return self._consume_fee

    @consume_fee.setter
    def consume_fee(self, value):
        self._consume_fee = value
    @property
    def consume_title(self):
        return self._consume_title

    @consume_title.setter
    def consume_title(self, value):
        self._consume_title = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def opposite_name(self):
        return self._opposite_name

    @opposite_name.setter
    def opposite_name(self, value):
        self._opposite_name = value
    @property
    def stat_fee(self):
        return self._stat_fee

    @stat_fee.setter
    def stat_fee(self, value):
        self._stat_fee = value
    @property
    def stat_type(self):
        return self._stat_type

    @stat_type.setter
    def stat_type(self, value):
        self._stat_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_in_no:
            if hasattr(self.biz_in_no, 'to_alipay_dict'):
                params['biz_in_no'] = self.biz_in_no.to_alipay_dict()
            else:
                params['biz_in_no'] = self.biz_in_no
        if self.biz_state_desc:
            if hasattr(self.biz_state_desc, 'to_alipay_dict'):
                params['biz_state_desc'] = self.biz_state_desc.to_alipay_dict()
            else:
                params['biz_state_desc'] = self.biz_state_desc
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.consume_fee:
            if hasattr(self.consume_fee, 'to_alipay_dict'):
                params['consume_fee'] = self.consume_fee.to_alipay_dict()
            else:
                params['consume_fee'] = self.consume_fee
        if self.consume_title:
            if hasattr(self.consume_title, 'to_alipay_dict'):
                params['consume_title'] = self.consume_title.to_alipay_dict()
            else:
                params['consume_title'] = self.consume_title
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.opposite_name:
            if hasattr(self.opposite_name, 'to_alipay_dict'):
                params['opposite_name'] = self.opposite_name.to_alipay_dict()
            else:
                params['opposite_name'] = self.opposite_name
        if self.stat_fee:
            if hasattr(self.stat_fee, 'to_alipay_dict'):
                params['stat_fee'] = self.stat_fee.to_alipay_dict()
            else:
                params['stat_fee'] = self.stat_fee
        if self.stat_type:
            if hasattr(self.stat_type, 'to_alipay_dict'):
                params['stat_type'] = self.stat_type.to_alipay_dict()
            else:
                params['stat_type'] = self.stat_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillApiSingleItem()
        if 'biz_in_no' in d:
            o.biz_in_no = d['biz_in_no']
        if 'biz_state_desc' in d:
            o.biz_state_desc = d['biz_state_desc']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'consume_fee' in d:
            o.consume_fee = d['consume_fee']
        if 'consume_title' in d:
            o.consume_title = d['consume_title']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'opposite_name' in d:
            o.opposite_name = d['opposite_name']
        if 'stat_fee' in d:
            o.stat_fee = d['stat_fee']
        if 'stat_type' in d:
            o.stat_type = d['stat_type']
        return o


