#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradePayConsultModel(object):

    def __init__(self):
        self._agreement_no = None
        self._apply_amount = None
        self._biz_scene = None
        self._buyer_id = None
        self._consult_phase = None
        self._extend_params = None
        self._product_code = None
        self._request_no = None
        self._subject = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def consult_phase(self):
        return self._consult_phase

    @consult_phase.setter
    def consult_phase(self, value):
        self._consult_phase = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.consult_phase:
            if hasattr(self.consult_phase, 'to_alipay_dict'):
                params['consult_phase'] = self.consult_phase.to_alipay_dict()
            else:
                params['consult_phase'] = self.consult_phase
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradePayConsultModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'consult_phase' in d:
            o.consult_phase = d['consult_phase']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'subject' in d:
            o.subject = d['subject']
        return o


