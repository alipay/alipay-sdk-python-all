#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.RiskDetectionMap import RiskDetectionMap
from alipay.aop.api.domain.RiskDetectionMap import RiskDetectionMap


class RiskDetectionRequest(object):

    def __init__(self):
        self._detection_amount = None
        self._detection_source = None
        self._document_no = None
        self._document_type = None
        self._ext_info = None
        self._identity_id = None
        self._risk_detection_parameters = None
        self._second_level_business_link = None
        self._settle_ip_role_id = None

    @property
    def detection_amount(self):
        return self._detection_amount

    @detection_amount.setter
    def detection_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._detection_amount = value
        else:
            self._detection_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def detection_source(self):
        return self._detection_source

    @detection_source.setter
    def detection_source(self, value):
        self._detection_source = value
    @property
    def document_no(self):
        return self._document_no

    @document_no.setter
    def document_no(self, value):
        self._document_no = value
    @property
    def document_type(self):
        return self._document_type

    @document_type.setter
    def document_type(self, value):
        self._document_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, RiskDetectionMap):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(RiskDetectionMap.from_alipay_dict(i))
    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value
    @property
    def risk_detection_parameters(self):
        return self._risk_detection_parameters

    @risk_detection_parameters.setter
    def risk_detection_parameters(self, value):
        if isinstance(value, list):
            self._risk_detection_parameters = list()
            for i in value:
                if isinstance(i, RiskDetectionMap):
                    self._risk_detection_parameters.append(i)
                else:
                    self._risk_detection_parameters.append(RiskDetectionMap.from_alipay_dict(i))
    @property
    def second_level_business_link(self):
        return self._second_level_business_link

    @second_level_business_link.setter
    def second_level_business_link(self, value):
        self._second_level_business_link = value
    @property
    def settle_ip_role_id(self):
        return self._settle_ip_role_id

    @settle_ip_role_id.setter
    def settle_ip_role_id(self, value):
        self._settle_ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.detection_amount:
            if hasattr(self.detection_amount, 'to_alipay_dict'):
                params['detection_amount'] = self.detection_amount.to_alipay_dict()
            else:
                params['detection_amount'] = self.detection_amount
        if self.detection_source:
            if hasattr(self.detection_source, 'to_alipay_dict'):
                params['detection_source'] = self.detection_source.to_alipay_dict()
            else:
                params['detection_source'] = self.detection_source
        if self.document_no:
            if hasattr(self.document_no, 'to_alipay_dict'):
                params['document_no'] = self.document_no.to_alipay_dict()
            else:
                params['document_no'] = self.document_no
        if self.document_type:
            if hasattr(self.document_type, 'to_alipay_dict'):
                params['document_type'] = self.document_type.to_alipay_dict()
            else:
                params['document_type'] = self.document_type
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        if self.risk_detection_parameters:
            if isinstance(self.risk_detection_parameters, list):
                for i in range(0, len(self.risk_detection_parameters)):
                    element = self.risk_detection_parameters[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_detection_parameters[i] = element.to_alipay_dict()
            if hasattr(self.risk_detection_parameters, 'to_alipay_dict'):
                params['risk_detection_parameters'] = self.risk_detection_parameters.to_alipay_dict()
            else:
                params['risk_detection_parameters'] = self.risk_detection_parameters
        if self.second_level_business_link:
            if hasattr(self.second_level_business_link, 'to_alipay_dict'):
                params['second_level_business_link'] = self.second_level_business_link.to_alipay_dict()
            else:
                params['second_level_business_link'] = self.second_level_business_link
        if self.settle_ip_role_id:
            if hasattr(self.settle_ip_role_id, 'to_alipay_dict'):
                params['settle_ip_role_id'] = self.settle_ip_role_id.to_alipay_dict()
            else:
                params['settle_ip_role_id'] = self.settle_ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskDetectionRequest()
        if 'detection_amount' in d:
            o.detection_amount = d['detection_amount']
        if 'detection_source' in d:
            o.detection_source = d['detection_source']
        if 'document_no' in d:
            o.document_no = d['document_no']
        if 'document_type' in d:
            o.document_type = d['document_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        if 'risk_detection_parameters' in d:
            o.risk_detection_parameters = d['risk_detection_parameters']
        if 'second_level_business_link' in d:
            o.second_level_business_link = d['second_level_business_link']
        if 'settle_ip_role_id' in d:
            o.settle_ip_role_id = d['settle_ip_role_id']
        return o


