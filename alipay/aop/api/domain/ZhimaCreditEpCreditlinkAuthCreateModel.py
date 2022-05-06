#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditLinkAgreementInfo import CreditLinkAgreementInfo


class ZhimaCreditEpCreditlinkAuthCreateModel(object):

    def __init__(self):
        self._agreement_info_list = None
        self._auth_merchant_id = None
        self._cognizant_cert_no = None
        self._cognizant_mobile = None
        self._cognizant_name = None
        self._data_type = None
        self._ep_cert_no = None
        self._ep_name = None
        self._link_type = None
        self._merchant_request_id = None

    @property
    def agreement_info_list(self):
        return self._agreement_info_list

    @agreement_info_list.setter
    def agreement_info_list(self, value):
        if isinstance(value, list):
            self._agreement_info_list = list()
            for i in value:
                if isinstance(i, CreditLinkAgreementInfo):
                    self._agreement_info_list.append(i)
                else:
                    self._agreement_info_list.append(CreditLinkAgreementInfo.from_alipay_dict(i))
    @property
    def auth_merchant_id(self):
        return self._auth_merchant_id

    @auth_merchant_id.setter
    def auth_merchant_id(self, value):
        self._auth_merchant_id = value
    @property
    def cognizant_cert_no(self):
        return self._cognizant_cert_no

    @cognizant_cert_no.setter
    def cognizant_cert_no(self, value):
        self._cognizant_cert_no = value
    @property
    def cognizant_mobile(self):
        return self._cognizant_mobile

    @cognizant_mobile.setter
    def cognizant_mobile(self, value):
        self._cognizant_mobile = value
    @property
    def cognizant_name(self):
        return self._cognizant_name

    @cognizant_name.setter
    def cognizant_name(self, value):
        self._cognizant_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def link_type(self):
        return self._link_type

    @link_type.setter
    def link_type(self, value):
        self._link_type = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_info_list:
            if isinstance(self.agreement_info_list, list):
                for i in range(0, len(self.agreement_info_list)):
                    element = self.agreement_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_info_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_info_list, 'to_alipay_dict'):
                params['agreement_info_list'] = self.agreement_info_list.to_alipay_dict()
            else:
                params['agreement_info_list'] = self.agreement_info_list
        if self.auth_merchant_id:
            if hasattr(self.auth_merchant_id, 'to_alipay_dict'):
                params['auth_merchant_id'] = self.auth_merchant_id.to_alipay_dict()
            else:
                params['auth_merchant_id'] = self.auth_merchant_id
        if self.cognizant_cert_no:
            if hasattr(self.cognizant_cert_no, 'to_alipay_dict'):
                params['cognizant_cert_no'] = self.cognizant_cert_no.to_alipay_dict()
            else:
                params['cognizant_cert_no'] = self.cognizant_cert_no
        if self.cognizant_mobile:
            if hasattr(self.cognizant_mobile, 'to_alipay_dict'):
                params['cognizant_mobile'] = self.cognizant_mobile.to_alipay_dict()
            else:
                params['cognizant_mobile'] = self.cognizant_mobile
        if self.cognizant_name:
            if hasattr(self.cognizant_name, 'to_alipay_dict'):
                params['cognizant_name'] = self.cognizant_name.to_alipay_dict()
            else:
                params['cognizant_name'] = self.cognizant_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.link_type:
            if hasattr(self.link_type, 'to_alipay_dict'):
                params['link_type'] = self.link_type.to_alipay_dict()
            else:
                params['link_type'] = self.link_type
        if self.merchant_request_id:
            if hasattr(self.merchant_request_id, 'to_alipay_dict'):
                params['merchant_request_id'] = self.merchant_request_id.to_alipay_dict()
            else:
                params['merchant_request_id'] = self.merchant_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkAuthCreateModel()
        if 'agreement_info_list' in d:
            o.agreement_info_list = d['agreement_info_list']
        if 'auth_merchant_id' in d:
            o.auth_merchant_id = d['auth_merchant_id']
        if 'cognizant_cert_no' in d:
            o.cognizant_cert_no = d['cognizant_cert_no']
        if 'cognizant_mobile' in d:
            o.cognizant_mobile = d['cognizant_mobile']
        if 'cognizant_name' in d:
            o.cognizant_name = d['cognizant_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'link_type' in d:
            o.link_type = d['link_type']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        return o


