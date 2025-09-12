#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanAccountQueryDetailDTO(object):

    def __init__(self):
        self._amount = None
        self._biz_scene = None
        self._inst_id = None
        self._inst_in_time = None
        self._order_no = None
        self._order_status = None
        self._principal_user_id = None
        self._remain_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_in_time(self):
        return self._inst_in_time

    @inst_in_time.setter
    def inst_in_time(self, value):
        self._inst_in_time = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def principal_user_id(self):
        return self._principal_user_id

    @principal_user_id.setter
    def principal_user_id(self, value):
        self._principal_user_id = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.inst_in_time:
            if hasattr(self.inst_in_time, 'to_alipay_dict'):
                params['inst_in_time'] = self.inst_in_time.to_alipay_dict()
            else:
                params['inst_in_time'] = self.inst_in_time
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.principal_user_id:
            if hasattr(self.principal_user_id, 'to_alipay_dict'):
                params['principal_user_id'] = self.principal_user_id.to_alipay_dict()
            else:
                params['principal_user_id'] = self.principal_user_id
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanAccountQueryDetailDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'inst_in_time' in d:
            o.inst_in_time = d['inst_in_time']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'principal_user_id' in d:
            o.principal_user_id = d['principal_user_id']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        return o


