#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsHealthSendFlowResult(object):

    def __init__(self):
        self._biz_type = None
        self._entrance = None
        self._offer_time = None
        self._out_biz_no = None
        self._product_group_biz_type = None
        self._product_sum_insured = None
        self._source = None
        self._status = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def entrance(self):
        return self._entrance

    @entrance.setter
    def entrance(self, value):
        self._entrance = value
    @property
    def offer_time(self):
        return self._offer_time

    @offer_time.setter
    def offer_time(self, value):
        self._offer_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_group_biz_type(self):
        return self._product_group_biz_type

    @product_group_biz_type.setter
    def product_group_biz_type(self, value):
        self._product_group_biz_type = value
    @property
    def product_sum_insured(self):
        return self._product_sum_insured

    @product_sum_insured.setter
    def product_sum_insured(self, value):
        self._product_sum_insured = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.entrance:
            if hasattr(self.entrance, 'to_alipay_dict'):
                params['entrance'] = self.entrance.to_alipay_dict()
            else:
                params['entrance'] = self.entrance
        if self.offer_time:
            if hasattr(self.offer_time, 'to_alipay_dict'):
                params['offer_time'] = self.offer_time.to_alipay_dict()
            else:
                params['offer_time'] = self.offer_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_group_biz_type:
            if hasattr(self.product_group_biz_type, 'to_alipay_dict'):
                params['product_group_biz_type'] = self.product_group_biz_type.to_alipay_dict()
            else:
                params['product_group_biz_type'] = self.product_group_biz_type
        if self.product_sum_insured:
            if hasattr(self.product_sum_insured, 'to_alipay_dict'):
                params['product_sum_insured'] = self.product_sum_insured.to_alipay_dict()
            else:
                params['product_sum_insured'] = self.product_sum_insured
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = InsHealthSendFlowResult()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'offer_time' in d:
            o.offer_time = d['offer_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_group_biz_type' in d:
            o.product_group_biz_type = d['product_group_biz_type']
        if 'product_sum_insured' in d:
            o.product_sum_insured = d['product_sum_insured']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


