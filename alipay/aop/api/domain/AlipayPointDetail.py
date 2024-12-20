#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPointDetail(object):

    def __init__(self):
        self._biz_group_no = None
        self._gmt_create = None
        self._id = None
        self._in_out_type = None
        self._order_id = None
        self._point = None
        self._trans_memo = None

    @property
    def biz_group_no(self):
        return self._biz_group_no

    @biz_group_no.setter
    def biz_group_no(self, value):
        self._biz_group_no = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def in_out_type(self):
        return self._in_out_type

    @in_out_type.setter
    def in_out_type(self, value):
        self._in_out_type = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_group_no:
            if hasattr(self.biz_group_no, 'to_alipay_dict'):
                params['biz_group_no'] = self.biz_group_no.to_alipay_dict()
            else:
                params['biz_group_no'] = self.biz_group_no
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.in_out_type:
            if hasattr(self.in_out_type, 'to_alipay_dict'):
                params['in_out_type'] = self.in_out_type.to_alipay_dict()
            else:
                params['in_out_type'] = self.in_out_type
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.trans_memo:
            if hasattr(self.trans_memo, 'to_alipay_dict'):
                params['trans_memo'] = self.trans_memo.to_alipay_dict()
            else:
                params['trans_memo'] = self.trans_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPointDetail()
        if 'biz_group_no' in d:
            o.biz_group_no = d['biz_group_no']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'id' in d:
            o.id = d['id']
        if 'in_out_type' in d:
            o.in_out_type = d['in_out_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'point' in d:
            o.point = d['point']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o


