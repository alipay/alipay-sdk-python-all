#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessLicenseCertFileds import BusinessLicenseCertFileds
from alipay.aop.api.domain.CertFields import CertFields
from alipay.aop.api.domain.IdCardImg import IdCardImg


class ZolozIdentificationCustomerIdcardCertifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._business_license_cert = None
        self._cert = None
        self._idcard_img = None
        self._operater_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def business_license_cert(self):
        return self._business_license_cert

    @business_license_cert.setter
    def business_license_cert(self, value):
        if isinstance(value, BusinessLicenseCertFileds):
            self._business_license_cert = value
        else:
            self._business_license_cert = BusinessLicenseCertFileds.from_alipay_dict(value)
    @property
    def cert(self):
        return self._cert

    @cert.setter
    def cert(self, value):
        if isinstance(value, CertFields):
            self._cert = value
        else:
            self._cert = CertFields.from_alipay_dict(value)
    @property
    def idcard_img(self):
        return self._idcard_img

    @idcard_img.setter
    def idcard_img(self, value):
        if isinstance(value, IdCardImg):
            self._idcard_img = value
        else:
            self._idcard_img = IdCardImg.from_alipay_dict(value)
    @property
    def operater_id(self):
        return self._operater_id

    @operater_id.setter
    def operater_id(self, value):
        self._operater_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.business_license_cert:
            if hasattr(self.business_license_cert, 'to_alipay_dict'):
                params['business_license_cert'] = self.business_license_cert.to_alipay_dict()
            else:
                params['business_license_cert'] = self.business_license_cert
        if self.cert:
            if hasattr(self.cert, 'to_alipay_dict'):
                params['cert'] = self.cert.to_alipay_dict()
            else:
                params['cert'] = self.cert
        if self.idcard_img:
            if hasattr(self.idcard_img, 'to_alipay_dict'):
                params['idcard_img'] = self.idcard_img.to_alipay_dict()
            else:
                params['idcard_img'] = self.idcard_img
        if self.operater_id:
            if hasattr(self.operater_id, 'to_alipay_dict'):
                params['operater_id'] = self.operater_id.to_alipay_dict()
            else:
                params['operater_id'] = self.operater_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationCustomerIdcardCertifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'business_license_cert' in d:
            o.business_license_cert = d['business_license_cert']
        if 'cert' in d:
            o.cert = d['cert']
        if 'idcard_img' in d:
            o.idcard_img = d['idcard_img']
        if 'operater_id' in d:
            o.operater_id = d['operater_id']
        return o


