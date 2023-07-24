#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IncomeDistributionTransInInfo import IncomeDistributionTransInInfo


class AnttechBlockchainFinanceDistributionRuleCreateModel(object):

    def __init__(self):
        self._distribution_pro_no = None
        self._request_no = None
        self._trans_in_info = None
        self._trans_out_account_no = None
        self._trans_out_account_type = None
        self._trans_out_cert_no = None
        self._trans_out_cert_type = None
        self._trans_out_name = None

    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def trans_in_info(self):
        return self._trans_in_info

    @trans_in_info.setter
    def trans_in_info(self, value):
        if isinstance(value, list):
            self._trans_in_info = list()
            for i in value:
                if isinstance(i, IncomeDistributionTransInInfo):
                    self._trans_in_info.append(i)
                else:
                    self._trans_in_info.append(IncomeDistributionTransInInfo.from_alipay_dict(i))
    @property
    def trans_out_account_no(self):
        return self._trans_out_account_no

    @trans_out_account_no.setter
    def trans_out_account_no(self, value):
        self._trans_out_account_no = value
    @property
    def trans_out_account_type(self):
        return self._trans_out_account_type

    @trans_out_account_type.setter
    def trans_out_account_type(self, value):
        self._trans_out_account_type = value
    @property
    def trans_out_cert_no(self):
        return self._trans_out_cert_no

    @trans_out_cert_no.setter
    def trans_out_cert_no(self, value):
        self._trans_out_cert_no = value
    @property
    def trans_out_cert_type(self):
        return self._trans_out_cert_type

    @trans_out_cert_type.setter
    def trans_out_cert_type(self, value):
        self._trans_out_cert_type = value
    @property
    def trans_out_name(self):
        return self._trans_out_name

    @trans_out_name.setter
    def trans_out_name(self, value):
        self._trans_out_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.trans_in_info:
            if isinstance(self.trans_in_info, list):
                for i in range(0, len(self.trans_in_info)):
                    element = self.trans_in_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_in_info[i] = element.to_alipay_dict()
            if hasattr(self.trans_in_info, 'to_alipay_dict'):
                params['trans_in_info'] = self.trans_in_info.to_alipay_dict()
            else:
                params['trans_in_info'] = self.trans_in_info
        if self.trans_out_account_no:
            if hasattr(self.trans_out_account_no, 'to_alipay_dict'):
                params['trans_out_account_no'] = self.trans_out_account_no.to_alipay_dict()
            else:
                params['trans_out_account_no'] = self.trans_out_account_no
        if self.trans_out_account_type:
            if hasattr(self.trans_out_account_type, 'to_alipay_dict'):
                params['trans_out_account_type'] = self.trans_out_account_type.to_alipay_dict()
            else:
                params['trans_out_account_type'] = self.trans_out_account_type
        if self.trans_out_cert_no:
            if hasattr(self.trans_out_cert_no, 'to_alipay_dict'):
                params['trans_out_cert_no'] = self.trans_out_cert_no.to_alipay_dict()
            else:
                params['trans_out_cert_no'] = self.trans_out_cert_no
        if self.trans_out_cert_type:
            if hasattr(self.trans_out_cert_type, 'to_alipay_dict'):
                params['trans_out_cert_type'] = self.trans_out_cert_type.to_alipay_dict()
            else:
                params['trans_out_cert_type'] = self.trans_out_cert_type
        if self.trans_out_name:
            if hasattr(self.trans_out_name, 'to_alipay_dict'):
                params['trans_out_name'] = self.trans_out_name.to_alipay_dict()
            else:
                params['trans_out_name'] = self.trans_out_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceDistributionRuleCreateModel()
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'trans_in_info' in d:
            o.trans_in_info = d['trans_in_info']
        if 'trans_out_account_no' in d:
            o.trans_out_account_no = d['trans_out_account_no']
        if 'trans_out_account_type' in d:
            o.trans_out_account_type = d['trans_out_account_type']
        if 'trans_out_cert_no' in d:
            o.trans_out_cert_no = d['trans_out_cert_no']
        if 'trans_out_cert_type' in d:
            o.trans_out_cert_type = d['trans_out_cert_type']
        if 'trans_out_name' in d:
            o.trans_out_name = d['trans_out_name']
        return o


