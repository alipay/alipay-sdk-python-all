#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyBasicInfo import ApplyBasicInfo


class AnttechBlockchainDefinInsuranceApplyCreateModel(object):

    def __init__(self):
        self._apply_basic_info = None
        self._business_code = None
        self._parm = None
        self._pdt_mkt_code = None
        self._platform_access_type = None
        self._platform_code = None
        self._product_code = None
        self._subject_information = None
        self._trade_no = None

    @property
    def apply_basic_info(self):
        return self._apply_basic_info

    @apply_basic_info.setter
    def apply_basic_info(self, value):
        if isinstance(value, ApplyBasicInfo):
            self._apply_basic_info = value
        else:
            self._apply_basic_info = ApplyBasicInfo.from_alipay_dict(value)
    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value
    @property
    def pdt_mkt_code(self):
        return self._pdt_mkt_code

    @pdt_mkt_code.setter
    def pdt_mkt_code(self, value):
        self._pdt_mkt_code = value
    @property
    def platform_access_type(self):
        return self._platform_access_type

    @platform_access_type.setter
    def platform_access_type(self, value):
        self._platform_access_type = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def subject_information(self):
        return self._subject_information

    @subject_information.setter
    def subject_information(self, value):
        self._subject_information = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_basic_info:
            if hasattr(self.apply_basic_info, 'to_alipay_dict'):
                params['apply_basic_info'] = self.apply_basic_info.to_alipay_dict()
            else:
                params['apply_basic_info'] = self.apply_basic_info
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.parm:
            if hasattr(self.parm, 'to_alipay_dict'):
                params['parm'] = self.parm.to_alipay_dict()
            else:
                params['parm'] = self.parm
        if self.pdt_mkt_code:
            if hasattr(self.pdt_mkt_code, 'to_alipay_dict'):
                params['pdt_mkt_code'] = self.pdt_mkt_code.to_alipay_dict()
            else:
                params['pdt_mkt_code'] = self.pdt_mkt_code
        if self.platform_access_type:
            if hasattr(self.platform_access_type, 'to_alipay_dict'):
                params['platform_access_type'] = self.platform_access_type.to_alipay_dict()
            else:
                params['platform_access_type'] = self.platform_access_type
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.subject_information:
            if hasattr(self.subject_information, 'to_alipay_dict'):
                params['subject_information'] = self.subject_information.to_alipay_dict()
            else:
                params['subject_information'] = self.subject_information
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinInsuranceApplyCreateModel()
        if 'apply_basic_info' in d:
            o.apply_basic_info = d['apply_basic_info']
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'parm' in d:
            o.parm = d['parm']
        if 'pdt_mkt_code' in d:
            o.pdt_mkt_code = d['pdt_mkt_code']
        if 'platform_access_type' in d:
            o.platform_access_type = d['platform_access_type']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'subject_information' in d:
            o.subject_information = d['subject_information']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


