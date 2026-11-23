#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BrandInfoItem import BrandInfoItem
from alipay.aop.api.domain.CertificateInfoItem import CertificateInfoItem
from alipay.aop.api.domain.MerchantContacInfo import MerchantContacInfo


class AlipayOpenMerchantQualificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMerchantQualificationQueryResponse, self).__init__()
        self._auth_status = None
        self._brand_infos = None
        self._certificates = None
        self._contact_persons = None
        self._legal_person = None
        self._mcc_code = None
        self._mcc_name = None
        self._merchant_name = None

    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def brand_infos(self):
        return self._brand_infos

    @brand_infos.setter
    def brand_infos(self, value):
        if isinstance(value, list):
            self._brand_infos = list()
            for i in value:
                if isinstance(i, BrandInfoItem):
                    self._brand_infos.append(i)
                else:
                    self._brand_infos.append(BrandInfoItem.from_alipay_dict(i))
    @property
    def certificates(self):
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        if isinstance(value, list):
            self._certificates = list()
            for i in value:
                if isinstance(i, CertificateInfoItem):
                    self._certificates.append(i)
                else:
                    self._certificates.append(CertificateInfoItem.from_alipay_dict(i))
    @property
    def contact_persons(self):
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, value):
        if isinstance(value, list):
            self._contact_persons = list()
            for i in value:
                if isinstance(i, MerchantContacInfo):
                    self._contact_persons.append(i)
                else:
                    self._contact_persons.append(MerchantContacInfo.from_alipay_dict(i))
    @property
    def legal_person(self):
        return self._legal_person

    @legal_person.setter
    def legal_person(self, value):
        self._legal_person = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mcc_name(self):
        return self._mcc_name

    @mcc_name.setter
    def mcc_name(self, value):
        self._mcc_name = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMerchantQualificationQueryResponse, self).parse_response_content(response_content)
        if 'auth_status' in response:
            self.auth_status = response['auth_status']
        if 'brand_infos' in response:
            self.brand_infos = response['brand_infos']
        if 'certificates' in response:
            self.certificates = response['certificates']
        if 'contact_persons' in response:
            self.contact_persons = response['contact_persons']
        if 'legal_person' in response:
            self.legal_person = response['legal_person']
        if 'mcc_code' in response:
            self.mcc_code = response['mcc_code']
        if 'mcc_name' in response:
            self.mcc_name = response['mcc_name']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
