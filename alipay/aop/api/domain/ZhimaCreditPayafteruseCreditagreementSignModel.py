#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditagreementSignModel(object):

    def __init__(self):
        self._cancel_back_link = None
        self._category_id = None
        self._external_logon_id = None
        self._extra_param = None
        self._out_agreement_no = None
        self._product_code = None
        self._return_back_link = None
        self._zm_service_id = None

    @property
    def cancel_back_link(self):
        return self._cancel_back_link

    @cancel_back_link.setter
    def cancel_back_link(self, value):
        self._cancel_back_link = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def external_logon_id(self):
        return self._external_logon_id

    @external_logon_id.setter
    def external_logon_id(self, value):
        self._external_logon_id = value
    @property
    def extra_param(self):
        return self._extra_param

    @extra_param.setter
    def extra_param(self, value):
        self._extra_param = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def return_back_link(self):
        return self._return_back_link

    @return_back_link.setter
    def return_back_link(self, value):
        self._return_back_link = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cancel_back_link:
            if hasattr(self.cancel_back_link, 'to_alipay_dict'):
                params['cancel_back_link'] = self.cancel_back_link.to_alipay_dict()
            else:
                params['cancel_back_link'] = self.cancel_back_link
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.external_logon_id:
            if hasattr(self.external_logon_id, 'to_alipay_dict'):
                params['external_logon_id'] = self.external_logon_id.to_alipay_dict()
            else:
                params['external_logon_id'] = self.external_logon_id
        if self.extra_param:
            if hasattr(self.extra_param, 'to_alipay_dict'):
                params['extra_param'] = self.extra_param.to_alipay_dict()
            else:
                params['extra_param'] = self.extra_param
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.return_back_link:
            if hasattr(self.return_back_link, 'to_alipay_dict'):
                params['return_back_link'] = self.return_back_link.to_alipay_dict()
            else:
                params['return_back_link'] = self.return_back_link
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditagreementSignModel()
        if 'cancel_back_link' in d:
            o.cancel_back_link = d['cancel_back_link']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'external_logon_id' in d:
            o.external_logon_id = d['external_logon_id']
        if 'extra_param' in d:
            o.extra_param = d['extra_param']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'return_back_link' in d:
            o.return_back_link = d['return_back_link']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


