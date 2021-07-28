#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantPayforprivilegePayCreateModel(object):

    def __init__(self):
        self._member_id = None
        self._out_biz_no = None
        self._promotion_plan_id = None
        self._user_id = None

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def promotion_plan_id(self):
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, value):
        self._promotion_plan_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.promotion_plan_id:
            if hasattr(self.promotion_plan_id, 'to_alipay_dict'):
                params['promotion_plan_id'] = self.promotion_plan_id.to_alipay_dict()
            else:
                params['promotion_plan_id'] = self.promotion_plan_id
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
        o = AlipayMerchantPayforprivilegePayCreateModel()
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'promotion_plan_id' in d:
            o.promotion_plan_id = d['promotion_plan_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


