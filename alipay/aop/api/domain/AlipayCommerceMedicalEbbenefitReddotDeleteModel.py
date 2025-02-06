#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEbbenefitReddotDeleteModel(object):

    def __init__(self):
        self._eb_user_id = None
        self._inquiry_mode = None
        self._order_id = None
        self._order_type = None
        self._out_order_id = None
        self._out_parent_order_id = None
        self._out_sub_user_id = None
        self._out_user_id = None

    @property
    def eb_user_id(self):
        return self._eb_user_id

    @eb_user_id.setter
    def eb_user_id(self, value):
        self._eb_user_id = value
    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_parent_order_id(self):
        return self._out_parent_order_id

    @out_parent_order_id.setter
    def out_parent_order_id(self, value):
        self._out_parent_order_id = value
    @property
    def out_sub_user_id(self):
        return self._out_sub_user_id

    @out_sub_user_id.setter
    def out_sub_user_id(self, value):
        self._out_sub_user_id = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.eb_user_id:
            if hasattr(self.eb_user_id, 'to_alipay_dict'):
                params['eb_user_id'] = self.eb_user_id.to_alipay_dict()
            else:
                params['eb_user_id'] = self.eb_user_id
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_parent_order_id:
            if hasattr(self.out_parent_order_id, 'to_alipay_dict'):
                params['out_parent_order_id'] = self.out_parent_order_id.to_alipay_dict()
            else:
                params['out_parent_order_id'] = self.out_parent_order_id
        if self.out_sub_user_id:
            if hasattr(self.out_sub_user_id, 'to_alipay_dict'):
                params['out_sub_user_id'] = self.out_sub_user_id.to_alipay_dict()
            else:
                params['out_sub_user_id'] = self.out_sub_user_id
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEbbenefitReddotDeleteModel()
        if 'eb_user_id' in d:
            o.eb_user_id = d['eb_user_id']
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_parent_order_id' in d:
            o.out_parent_order_id = d['out_parent_order_id']
        if 'out_sub_user_id' in d:
            o.out_sub_user_id = d['out_sub_user_id']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        return o


