#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceBillDingstaffbizorderQueryModel(object):

    def __init__(self):
        self._biz_trans_id = None
        self._biz_type = None
        self._direction = None
        self._gmt_date_end = None
        self._gmt_date_start = None
        self._last_id = None
        self._order_id = None
        self._page_size = None
        self._title = None
        self._virtual_user_id = None

    @property
    def biz_trans_id(self):
        return self._biz_trans_id

    @biz_trans_id.setter
    def biz_trans_id(self, value):
        self._biz_trans_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
    @property
    def gmt_date_end(self):
        return self._gmt_date_end

    @gmt_date_end.setter
    def gmt_date_end(self, value):
        self._gmt_date_end = value
    @property
    def gmt_date_start(self):
        return self._gmt_date_start

    @gmt_date_start.setter
    def gmt_date_start(self, value):
        self._gmt_date_start = value
    @property
    def last_id(self):
        return self._last_id

    @last_id.setter
    def last_id(self, value):
        self._last_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def virtual_user_id(self):
        return self._virtual_user_id

    @virtual_user_id.setter
    def virtual_user_id(self, value):
        self._virtual_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_trans_id:
            if hasattr(self.biz_trans_id, 'to_alipay_dict'):
                params['biz_trans_id'] = self.biz_trans_id.to_alipay_dict()
            else:
                params['biz_trans_id'] = self.biz_trans_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.direction:
            if hasattr(self.direction, 'to_alipay_dict'):
                params['direction'] = self.direction.to_alipay_dict()
            else:
                params['direction'] = self.direction
        if self.gmt_date_end:
            if hasattr(self.gmt_date_end, 'to_alipay_dict'):
                params['gmt_date_end'] = self.gmt_date_end.to_alipay_dict()
            else:
                params['gmt_date_end'] = self.gmt_date_end
        if self.gmt_date_start:
            if hasattr(self.gmt_date_start, 'to_alipay_dict'):
                params['gmt_date_start'] = self.gmt_date_start.to_alipay_dict()
            else:
                params['gmt_date_start'] = self.gmt_date_start
        if self.last_id:
            if hasattr(self.last_id, 'to_alipay_dict'):
                params['last_id'] = self.last_id.to_alipay_dict()
            else:
                params['last_id'] = self.last_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.virtual_user_id:
            if hasattr(self.virtual_user_id, 'to_alipay_dict'):
                params['virtual_user_id'] = self.virtual_user_id.to_alipay_dict()
            else:
                params['virtual_user_id'] = self.virtual_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceBillDingstaffbizorderQueryModel()
        if 'biz_trans_id' in d:
            o.biz_trans_id = d['biz_trans_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'direction' in d:
            o.direction = d['direction']
        if 'gmt_date_end' in d:
            o.gmt_date_end = d['gmt_date_end']
        if 'gmt_date_start' in d:
            o.gmt_date_start = d['gmt_date_start']
        if 'last_id' in d:
            o.last_id = d['last_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'title' in d:
            o.title = d['title']
        if 'virtual_user_id' in d:
            o.virtual_user_id = d['virtual_user_id']
        return o


