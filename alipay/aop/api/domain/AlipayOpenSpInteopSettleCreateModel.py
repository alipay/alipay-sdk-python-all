#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleBankCardInfo import SettleBankCardInfo
from alipay.aop.api.domain.BizOpenCertificateInfoForEntry import BizOpenCertificateInfoForEntry
from alipay.aop.api.domain.BizOpenCertificateInfoForEntry import BizOpenCertificateInfoForEntry
from alipay.aop.api.domain.BizOpenCertificateInfoForEntry import BizOpenCertificateInfoForEntry
from alipay.aop.api.domain.BizOpenCommonMerchantLicenseInfo import BizOpenCommonMerchantLicenseInfo


class AlipayOpenSpInteopSettleCreateModel(object):

    def __init__(self):
        self._bank_card_info = None
        self._benefit_info = None
        self._benefit_infos = None
        self._inteop_order_no = None
        self._legal_info = None
        self._license_info = None
        self._merchant_type = None
        self._operator_login_id = None

    @property
    def bank_card_info(self):
        return self._bank_card_info

    @bank_card_info.setter
    def bank_card_info(self, value):
        if isinstance(value, SettleBankCardInfo):
            self._bank_card_info = value
        else:
            self._bank_card_info = SettleBankCardInfo.from_alipay_dict(value)
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
    def benefit_infos(self):
        return self._benefit_infos

    @benefit_infos.setter
    def benefit_infos(self, value):
        if isinstance(value, list):
            self._benefit_infos = list()
            for i in value:
                if isinstance(i, BizOpenCertificateInfoForEntry):
                    self._benefit_infos.append(i)
                else:
                    self._benefit_infos.append(BizOpenCertificateInfoForEntry.from_alipay_dict(i))
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
    @property
    def operator_login_id(self):
        return self._operator_login_id

    @operator_login_id.setter
    def operator_login_id(self, value):
        self._operator_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bank_card_info:
            if hasattr(self.bank_card_info, 'to_alipay_dict'):
                params['bank_card_info'] = self.bank_card_info.to_alipay_dict()
            else:
                params['bank_card_info'] = self.bank_card_info
        if self.benefit_info:
            if hasattr(self.benefit_info, 'to_alipay_dict'):
                params['benefit_info'] = self.benefit_info.to_alipay_dict()
            else:
                params['benefit_info'] = self.benefit_info
        if self.benefit_infos:
            if isinstance(self.benefit_infos, list):
                for i in range(0, len(self.benefit_infos)):
                    element = self.benefit_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.benefit_infos[i] = element.to_alipay_dict()
            if hasattr(self.benefit_infos, 'to_alipay_dict'):
                params['benefit_infos'] = self.benefit_infos.to_alipay_dict()
            else:
                params['benefit_infos'] = self.benefit_infos
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
        if self.operator_login_id:
            if hasattr(self.operator_login_id, 'to_alipay_dict'):
                params['operator_login_id'] = self.operator_login_id.to_alipay_dict()
            else:
                params['operator_login_id'] = self.operator_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopSettleCreateModel()
        if 'bank_card_info' in d:
            o.bank_card_info = d['bank_card_info']
        if 'benefit_info' in d:
            o.benefit_info = d['benefit_info']
        if 'benefit_infos' in d:
            o.benefit_infos = d['benefit_infos']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'legal_info' in d:
            o.legal_info = d['legal_info']
        if 'license_info' in d:
            o.license_info = d['license_info']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'operator_login_id' in d:
            o.operator_login_id = d['operator_login_id']
        return o


