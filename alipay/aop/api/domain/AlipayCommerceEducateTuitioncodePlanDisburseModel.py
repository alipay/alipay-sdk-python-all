#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateTuitioncodePlanDisburseModel(object):

    def __init__(self):
        self._out_order_no = None
        self._out_request_id = None
        self._plan_id = None
        self._plan_ids = None
        self._smid = None
        self._user_id = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_ids(self):
        return self._plan_ids

    @plan_ids.setter
    def plan_ids(self, value):
        if isinstance(value, list):
            self._plan_ids = list()
            for i in value:
                self._plan_ids.append(i)
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_request_id:
            if hasattr(self.out_request_id, 'to_alipay_dict'):
                params['out_request_id'] = self.out_request_id.to_alipay_dict()
            else:
                params['out_request_id'] = self.out_request_id
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.plan_ids:
            if isinstance(self.plan_ids, list):
                for i in range(0, len(self.plan_ids)):
                    element = self.plan_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_ids[i] = element.to_alipay_dict()
            if hasattr(self.plan_ids, 'to_alipay_dict'):
                params['plan_ids'] = self.plan_ids.to_alipay_dict()
            else:
                params['plan_ids'] = self.plan_ids
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
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
        o = AlipayCommerceEducateTuitioncodePlanDisburseModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_id' in d:
            o.out_request_id = d['out_request_id']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'plan_ids' in d:
            o.plan_ids = d['plan_ids']
        if 'smid' in d:
            o.smid = d['smid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


