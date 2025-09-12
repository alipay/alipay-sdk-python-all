#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizOpenCertificateInfoForEntry import BizOpenCertificateInfoForEntry
from alipay.aop.api.domain.BizOpenCertificateInfoForEntry import BizOpenCertificateInfoForEntry
from alipay.aop.api.domain.BizOpenCommonMerchantLicenseInfo import BizOpenCommonMerchantLicenseInfo


class AlipayOpenSpInteopSettleCreateModel(object):

    def __init__(self):
        self._benefit_info = None
        self._inteop_order_no = None
        self._legal_info = None
        self._legal_person_logon_id = None
        self._license_info = None
        self._merchant_type = None

    @property
    def benefit_info(self):
        return self._benefit_info

    @benefit_info.setter
    def benefit_info(self, value):
        if isinstance(value, BizOpenCertificateInfoForEntry):
            self._benefit_info = value
        else:
            self._benefit_info = BizOpenCertificateInfoForEntry.from_alipay_dict(value)
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def legal_info(self):
        return self._legal_info

    @legal_info.setter
    def legal_info(self, value):
        if isinstance(value, BizOpenCertificateInfoForEntry):
            self._legal_info = value
        else:
            self._legal_info = BizOpenCertificateInfoForEntry.from_alipay_dict(value)
    @property
    def legal_person_logon_id(self):
        return self._legal_person_logon_id

    @legal_person_logon_id.setter
    def legal_person_logon_id(self, value):
        self._legal_person_logon_id = value
    @property
    def license_info(self):
        return self._license_info

    @license_info.setter
    def license_info(self, value):
        if isinstance(value, BizOpenCommonMerchantLicenseInfo):
            self._license_info = value
        else:
            self._license_info = BizOpenCommonMerchantLicenseInfo.from_alipay_dict(value)
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_info:
            if hasattr(self.benefit_info, 'to_alipay_dict'):
                params['benefit_info'] = self.benefit_info.to_alipay_dict()
            else:
                params['benefit_info'] = self.benefit_info
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.legal_info:
            if hasattr(self.legal_info, 'to_alipay_dict'):
                params['legal_info'] = self.legal_info.to_alipay_dict()
            else:
                params['legal_info'] = self.legal_info
        if self.legal_person_logon_id:
            if hasattr(self.legal_person_logon_id, 'to_alipay_dict'):
                params['legal_person_logon_id'] = self.legal_person_logon_id.to_alipay_dict()
            else:
                params['legal_person_logon_id'] = self.legal_person_logon_id
        if self.license_info:
            if hasattr(self.license_info, 'to_alipay_dict'):
                params['license_info'] = self.license_info.to_alipay_dict()
            else:
                params['license_info'] = self.license_info
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopSettleCreateModel()
        if 'benefit_info' in d:
            o.benefit_info = d['benefit_info']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'legal_info' in d:
            o.legal_info = d['legal_info']
        if 'legal_person_logon_id' in d:
            o.legal_person_logon_id = d['legal_person_logon_id']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        return o


