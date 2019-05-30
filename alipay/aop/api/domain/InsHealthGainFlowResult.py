#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsHealthGainFlowResult(object):

    def __init__(self):
        self._biz_type = None
        self._entrance = None
        self._new_sum_insured = None
        self._offer_time = None
        self._old_sum_insured = None
        self._out_biz_no = None
        self._policy_no = None
        self._product_group_biz_type = None
        self._source = None
        self._sp_no = None
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
    def new_sum_insured(self):
        return self._new_sum_insured

    @new_sum_insured.setter
    def new_sum_insured(self, value):
        self._new_sum_insured = value
    @property
    def offer_time(self):
        return self._offer_time

    @offer_time.setter
    def offer_time(self, value):
        self._offer_time = value
    @property
    def old_sum_insured(self):
        return self._old_sum_insured

    @old_sum_insured.setter
    def old_sum_insured(self, value):
        self._old_sum_insured = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def product_group_biz_type(self):
        return self._product_group_biz_type

    @product_group_biz_type.setter
    def product_group_biz_type(self, value):
        self._product_group_biz_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sp_no(self):
        return self._sp_no

    @sp_no.setter
    def sp_no(self, value):
        self._sp_no = value
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
        if self.new_sum_insured:
            if hasattr(self.new_sum_insured, 'to_alipay_dict'):
                params['new_sum_insured'] = self.new_sum_insured.to_alipay_dict()
            else:
                params['new_sum_insured'] = self.new_sum_insured
        if self.offer_time:
            if hasattr(self.offer_time, 'to_alipay_dict'):
                params['offer_time'] = self.offer_time.to_alipay_dict()
            else:
                params['offer_time'] = self.offer_time
        if self.old_sum_insured:
            if hasattr(self.old_sum_insured, 'to_alipay_dict'):
                params['old_sum_insured'] = self.old_sum_insured.to_alipay_dict()
            else:
                params['old_sum_insured'] = self.old_sum_insured
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.policy_no:
            if hasattr(self.policy_no, 'to_alipay_dict'):
                params['policy_no'] = self.policy_no.to_alipay_dict()
            else:
                params['policy_no'] = self.policy_no
        if self.product_group_biz_type:
            if hasattr(self.product_group_biz_type, 'to_alipay_dict'):
                params['product_group_biz_type'] = self.product_group_biz_type.to_alipay_dict()
            else:
                params['product_group_biz_type'] = self.product_group_biz_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sp_no:
            if hasattr(self.sp_no, 'to_alipay_dict'):
                params['sp_no'] = self.sp_no.to_alipay_dict()
            else:
                params['sp_no'] = self.sp_no
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
        o = InsHealthGainFlowResult()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'entrance' in d:
            o.entrance = d['entrance']
        if 'new_sum_insured' in d:
            o.new_sum_insured = d['new_sum_insured']
        if 'offer_time' in d:
            o.offer_time = d['offer_time']
        if 'old_sum_insured' in d:
            o.old_sum_insured = d['old_sum_insured']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'policy_no' in d:
            o.policy_no = d['policy_no']
        if 'product_group_biz_type' in d:
            o.product_group_biz_type = d['product_group_biz_type']
        if 'source' in d:
            o.source = d['source']
        if 'sp_no' in d:
            o.sp_no = d['sp_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


