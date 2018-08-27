#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsPerson import InsPerson
from alipay.aop.api.domain.InsClaimPolicy import InsClaimPolicy
from alipay.aop.api.domain.InsPerson import InsPerson


class AlipayInsSceneClaimApplyModel(object):

    def __init__(self):
        self._accident_address = None
        self._accident_desc = None
        self._accident_time = None
        self._beneficiary = None
        self._bill_title = None
        self._biz_data = None
        self._claim_fee = None
        self._claim_policy_list = None
        self._out_biz_no = None
        self._out_request_no = None
        self._prod_code = None
        self._reporter = None

    @property
    def accident_address(self):
        return self._accident_address

    @accident_address.setter
    def accident_address(self, value):
        self._accident_address = value
    @property
    def accident_desc(self):
        return self._accident_desc

    @accident_desc.setter
    def accident_desc(self, value):
        self._accident_desc = value
    @property
    def accident_time(self):
        return self._accident_time

    @accident_time.setter
    def accident_time(self, value):
        self._accident_time = value
    @property
    def beneficiary(self):
        return self._beneficiary

    @beneficiary.setter
    def beneficiary(self, value):
        if isinstance(value, InsPerson):
            self._beneficiary = value
        else:
            self._beneficiary = InsPerson.from_alipay_dict(value)
    @property
    def bill_title(self):
        return self._bill_title

    @bill_title.setter
    def bill_title(self, value):
        self._bill_title = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def claim_policy_list(self):
        return self._claim_policy_list

    @claim_policy_list.setter
    def claim_policy_list(self, value):
        if isinstance(value, list):
            self._claim_policy_list = list()
            for i in value:
                if isinstance(i, InsClaimPolicy):
                    self._claim_policy_list.append(i)
                else:
                    self._claim_policy_list.append(InsClaimPolicy.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def reporter(self):
        return self._reporter

    @reporter.setter
    def reporter(self, value):
        if isinstance(value, InsPerson):
            self._reporter = value
        else:
            self._reporter = InsPerson.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.accident_address:
            if hasattr(self.accident_address, 'to_alipay_dict'):
                params['accident_address'] = self.accident_address.to_alipay_dict()
            else:
                params['accident_address'] = self.accident_address
        if self.accident_desc:
            if hasattr(self.accident_desc, 'to_alipay_dict'):
                params['accident_desc'] = self.accident_desc.to_alipay_dict()
            else:
                params['accident_desc'] = self.accident_desc
        if self.accident_time:
            if hasattr(self.accident_time, 'to_alipay_dict'):
                params['accident_time'] = self.accident_time.to_alipay_dict()
            else:
                params['accident_time'] = self.accident_time
        if self.beneficiary:
            if hasattr(self.beneficiary, 'to_alipay_dict'):
                params['beneficiary'] = self.beneficiary.to_alipay_dict()
            else:
                params['beneficiary'] = self.beneficiary
        if self.bill_title:
            if hasattr(self.bill_title, 'to_alipay_dict'):
                params['bill_title'] = self.bill_title.to_alipay_dict()
            else:
                params['bill_title'] = self.bill_title
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.claim_policy_list:
            if isinstance(self.claim_policy_list, list):
                for i in range(0, len(self.claim_policy_list)):
                    element = self.claim_policy_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claim_policy_list[i] = element.to_alipay_dict()
            if hasattr(self.claim_policy_list, 'to_alipay_dict'):
                params['claim_policy_list'] = self.claim_policy_list.to_alipay_dict()
            else:
                params['claim_policy_list'] = self.claim_policy_list
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.reporter:
            if hasattr(self.reporter, 'to_alipay_dict'):
                params['reporter'] = self.reporter.to_alipay_dict()
            else:
                params['reporter'] = self.reporter
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneClaimApplyModel()
        if 'accident_address' in d:
            o.accident_address = d['accident_address']
        if 'accident_desc' in d:
            o.accident_desc = d['accident_desc']
        if 'accident_time' in d:
            o.accident_time = d['accident_time']
        if 'beneficiary' in d:
            o.beneficiary = d['beneficiary']
        if 'bill_title' in d:
            o.bill_title = d['bill_title']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'claim_policy_list' in d:
            o.claim_policy_list = d['claim_policy_list']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'reporter' in d:
            o.reporter = d['reporter']
        return o


