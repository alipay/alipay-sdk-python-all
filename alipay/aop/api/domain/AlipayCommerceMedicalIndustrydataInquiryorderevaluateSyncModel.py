#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalIndustrydataInquiryorderevaluateSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_order_id = None
        self._alipay_user_id = None
        self._evaluate_content = None
        self._evaluate_label = None
        self._evaluate_score = None
        self._evaluate_time = None
        self._merchant_user_id = None
        self._open_status = None
        self._out_order_id = None
        self._platform_code = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def evaluate_content(self):
        return self._evaluate_content

    @evaluate_content.setter
    def evaluate_content(self, value):
        self._evaluate_content = value
    @property
    def evaluate_label(self):
        return self._evaluate_label

    @evaluate_label.setter
    def evaluate_label(self, value):
        self._evaluate_label = value
    @property
    def evaluate_score(self):
        return self._evaluate_score

    @evaluate_score.setter
    def evaluate_score(self, value):
        self._evaluate_score = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def merchant_user_id(self):
        return self._merchant_user_id

    @merchant_user_id.setter
    def merchant_user_id(self, value):
        self._merchant_user_id = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.evaluate_content:
            if hasattr(self.evaluate_content, 'to_alipay_dict'):
                params['evaluate_content'] = self.evaluate_content.to_alipay_dict()
            else:
                params['evaluate_content'] = self.evaluate_content
        if self.evaluate_label:
            if hasattr(self.evaluate_label, 'to_alipay_dict'):
                params['evaluate_label'] = self.evaluate_label.to_alipay_dict()
            else:
                params['evaluate_label'] = self.evaluate_label
        if self.evaluate_score:
            if hasattr(self.evaluate_score, 'to_alipay_dict'):
                params['evaluate_score'] = self.evaluate_score.to_alipay_dict()
            else:
                params['evaluate_score'] = self.evaluate_score
        if self.evaluate_time:
            if hasattr(self.evaluate_time, 'to_alipay_dict'):
                params['evaluate_time'] = self.evaluate_time.to_alipay_dict()
            else:
                params['evaluate_time'] = self.evaluate_time
        if self.merchant_user_id:
            if hasattr(self.merchant_user_id, 'to_alipay_dict'):
                params['merchant_user_id'] = self.merchant_user_id.to_alipay_dict()
            else:
                params['merchant_user_id'] = self.merchant_user_id
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalIndustrydataInquiryorderevaluateSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'evaluate_content' in d:
            o.evaluate_content = d['evaluate_content']
        if 'evaluate_label' in d:
            o.evaluate_label = d['evaluate_label']
        if 'evaluate_score' in d:
            o.evaluate_score = d['evaluate_score']
        if 'evaluate_time' in d:
            o.evaluate_time = d['evaluate_time']
        if 'merchant_user_id' in d:
            o.merchant_user_id = d['merchant_user_id']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o


