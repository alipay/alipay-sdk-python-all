#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeductOrderDetail import DeductOrderDetail


class AlipayUserMpointAuthbasePayModel(object):

    def __init__(self):
        self._biz_sub_type = None
        self._biz_type = None
        self._deduct_order_detail = None
        self._open_id = None
        self._out_biz_no = None
        self._point = None
        self._user_id = None

    @property
    def biz_sub_type(self):
        return self._biz_sub_type

    @biz_sub_type.setter
    def biz_sub_type(self, value):
        self._biz_sub_type = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def deduct_order_detail(self):
        return self._deduct_order_detail

    @deduct_order_detail.setter
    def deduct_order_detail(self, value):
        if isinstance(value, DeductOrderDetail):
            self._deduct_order_detail = value
        else:
            self._deduct_order_detail = DeductOrderDetail.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_sub_type:
            if hasattr(self.biz_sub_type, 'to_alipay_dict'):
                params['biz_sub_type'] = self.biz_sub_type.to_alipay_dict()
            else:
                params['biz_sub_type'] = self.biz_sub_type
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.deduct_order_detail:
            if hasattr(self.deduct_order_detail, 'to_alipay_dict'):
                params['deduct_order_detail'] = self.deduct_order_detail.to_alipay_dict()
            else:
                params['deduct_order_detail'] = self.deduct_order_detail
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserMpointAuthbasePayModel()
        if 'biz_sub_type' in d:
            o.biz_sub_type = d['biz_sub_type']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'deduct_order_detail' in d:
            o.deduct_order_detail = d['deduct_order_detail']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'point' in d:
            o.point = d['point']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


