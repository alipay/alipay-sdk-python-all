#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MdAddressInfo import MdAddressInfo
from alipay.aop.api.domain.MdCertificateInfo import MdCertificateInfo
from alipay.aop.api.domain.ContactPerson import ContactPerson
from alipay.aop.api.domain.MccInfo import MccInfo


class AlipayMerchantPaymrchdataQrcodeCreateModel(object):

    def __init__(self):
        self._business_address_info = None
        self._certificate_infos = None
        self._contact_persons = None
        self._external_id = None
        self._mcc_info = None
        self._merchant_name = None
        self._shop_door_pic = None
        self._source = None

    @property
    def business_address_info(self):
        return self._business_address_info

    @business_address_info.setter
    def business_address_info(self, value):
        if isinstance(value, MdAddressInfo):
            self._business_address_info = value
        else:
            self._business_address_info = MdAddressInfo.from_alipay_dict(value)
    @property
    def certificate_infos(self):
        return self._certificate_infos

    @certificate_infos.setter
    def certificate_infos(self, value):
        if isinstance(value, list):
            self._certificate_infos = list()
            for i in value:
                if isinstance(i, MdCertificateInfo):
                    self._certificate_infos.append(i)
                else:
                    self._certificate_infos.append(MdCertificateInfo.from_alipay_dict(i))
    @property
    def contact_persons(self):
        return self._contact_persons

    @contact_persons.setter
    def contact_persons(self, value):
        if isinstance(value, list):
            self._contact_persons = list()
            for i in value:
                if isinstance(i, ContactPerson):
                    self._contact_persons.append(i)
                else:
                    self._contact_persons.append(ContactPerson.from_alipay_dict(i))
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def mcc_info(self):
        return self._mcc_info

    @mcc_info.setter
    def mcc_info(self, value):
        if isinstance(value, MccInfo):
            self._mcc_info = value
        else:
            self._mcc_info = MccInfo.from_alipay_dict(value)
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def shop_door_pic(self):
        return self._shop_door_pic

    @shop_door_pic.setter
    def shop_door_pic(self, value):
        self._shop_door_pic = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_address_info:
            if hasattr(self.business_address_info, 'to_alipay_dict'):
                params['business_address_info'] = self.business_address_info.to_alipay_dict()
            else:
                params['business_address_info'] = self.business_address_info
        if self.certificate_infos:
            if isinstance(self.certificate_infos, list):
                for i in range(0, len(self.certificate_infos)):
                    element = self.certificate_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_infos[i] = element.to_alipay_dict()
            if hasattr(self.certificate_infos, 'to_alipay_dict'):
                params['certificate_infos'] = self.certificate_infos.to_alipay_dict()
            else:
                params['certificate_infos'] = self.certificate_infos
        if self.contact_persons:
            if isinstance(self.contact_persons, list):
                for i in range(0, len(self.contact_persons)):
                    element = self.contact_persons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_persons[i] = element.to_alipay_dict()
            if hasattr(self.contact_persons, 'to_alipay_dict'):
                params['contact_persons'] = self.contact_persons.to_alipay_dict()
            else:
                params['contact_persons'] = self.contact_persons
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.mcc_info:
            if hasattr(self.mcc_info, 'to_alipay_dict'):
                params['mcc_info'] = self.mcc_info.to_alipay_dict()
            else:
                params['mcc_info'] = self.mcc_info
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.shop_door_pic:
            if hasattr(self.shop_door_pic, 'to_alipay_dict'):
                params['shop_door_pic'] = self.shop_door_pic.to_alipay_dict()
            else:
                params['shop_door_pic'] = self.shop_door_pic
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantPaymrchdataQrcodeCreateModel()
        if 'business_address_info' in d:
            o.business_address_info = d['business_address_info']
        if 'certificate_infos' in d:
            o.certificate_infos = d['certificate_infos']
        if 'contact_persons' in d:
            o.contact_persons = d['contact_persons']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'mcc_info' in d:
            o.mcc_info = d['mcc_info']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'shop_door_pic' in d:
            o.shop_door_pic = d['shop_door_pic']
        if 'source' in d:
            o.source = d['source']
        return o


