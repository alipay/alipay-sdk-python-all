#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneCommonEndorseperiodApplyModel(object):

    def __init__(self):
        self._expected_effect_end_time = None
        self._expected_effect_start_time = None
        self._idempotent_no = None
        self._out_order_id = None
        self._partner_org_id = None
        self._pre_order_id = None

    @property
    def expected_effect_end_time(self):
        return self._expected_effect_end_time

    @expected_effect_end_time.setter
    def expected_effect_end_time(self, value):
        self._expected_effect_end_time = value
    @property
    def expected_effect_start_time(self):
        return self._expected_effect_start_time

    @expected_effect_start_time.setter
    def expected_effect_start_time(self, value):
        self._expected_effect_start_time = value
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expected_effect_end_time:
            if hasattr(self.expected_effect_end_time, 'to_alipay_dict'):
                params['expected_effect_end_time'] = self.expected_effect_end_time.to_alipay_dict()
            else:
                params['expected_effect_end_time'] = self.expected_effect_end_time
        if self.expected_effect_start_time:
            if hasattr(self.expected_effect_start_time, 'to_alipay_dict'):
                params['expected_effect_start_time'] = self.expected_effect_start_time.to_alipay_dict()
            else:
                params['expected_effect_start_time'] = self.expected_effect_start_time
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        if self.pre_order_id:
            if hasattr(self.pre_order_id, 'to_alipay_dict'):
                params['pre_order_id'] = self.pre_order_id.to_alipay_dict()
            else:
                params['pre_order_id'] = self.pre_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommonEndorseperiodApplyModel()
        if 'expected_effect_end_time' in d:
            o.expected_effect_end_time = d['expected_effect_end_time']
        if 'expected_effect_start_time' in d:
            o.expected_effect_start_time = d['expected_effect_start_time']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        if 'pre_order_id' in d:
            o.pre_order_id = d['pre_order_id']
        return o


