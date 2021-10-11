#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleCardInfo import SettleCardInfo
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.DefaultSettleRule import DefaultSettleRule
from alipay.aop.api.domain.MerchantInvoiceInfo import MerchantInvoiceInfo
from alipay.aop.api.domain.IndustryQualificationInfo import IndustryQualificationInfo
from alipay.aop.api.domain.SiteInfo import SiteInfo


class AntMerchantExpandIndirectZftSimplecreateModel(object):

    def __init__(self):
        self._additional_cert_image = None
        self._additional_cert_no = None
        self._additional_cert_type = None
        self._alias_name = None
        self._alipay_logon_id = None
        self._binding_alipay_logon_id = None
        self._biz_cards = None
        self._business_address = None
        self._contact_infos = None
        self._default_settle_rule = None
        self._external_id = None
        self._in_door_images = None
        self._invoice_info = None
        self._license_auth_letter_image = None
        self._mcc = None
        self._out_door_images = None
        self._qualifications = None
        self._service = None
        self._service_phone = None
        self._sign_time_with_isv = None
        self._sites = None

    @property
    def additional_cert_image(self):
        return self._additional_cert_image

    @additional_cert_image.setter
    def additional_cert_image(self, value):
        self._additional_cert_image = value
    @property
    def additional_cert_no(self):
        return self._additional_cert_no

    @additional_cert_no.setter
    def additional_cert_no(self, value):
        self._additional_cert_no = value
    @property
    def additional_cert_type(self):
        return self._additional_cert_type

    @additional_cert_type.setter
    def additional_cert_type(self, value):
        self._additional_cert_type = value
    @property
    def alias_name(self):
        return self._alias_name

    @alias_name.setter
    def alias_name(self, value):
        self._alias_name = value
    @property
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def binding_alipay_logon_id(self):
        return self._binding_alipay_logon_id

    @binding_alipay_logon_id.setter
    def binding_alipay_logon_id(self, value):
        self._binding_alipay_logon_id = value
    @property
    def biz_cards(self):
        return self._biz_cards

    @biz_cards.setter
    def biz_cards(self, value):
        if isinstance(value, SettleCardInfo):
            self._biz_cards = value
        else:
            self._biz_cards = SettleCardInfo.from_alipay_dict(value)
    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, AddressInfo):
            self._business_address = value
        else:
            self._business_address = AddressInfo.from_alipay_dict(value)
    @property
    def contact_infos(self):
        return self._contact_infos

    @contact_infos.setter
    def contact_infos(self, value):
        if isinstance(value, ContactInfo):
            self._contact_infos = value
        else:
            self._contact_infos = ContactInfo.from_alipay_dict(value)
    @property
    def default_settle_rule(self):
        return self._default_settle_rule

    @default_settle_rule.setter
    def default_settle_rule(self, value):
        if isinstance(value, DefaultSettleRule):
            self._default_settle_rule = value
        else:
            self._default_settle_rule = DefaultSettleRule.from_alipay_dict(value)
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def in_door_images(self):
        return self._in_door_images

    @in_door_images.setter
    def in_door_images(self, value):
        self._in_door_images = value
    @property
    def invoice_info(self):
        return self._invoice_info

    @invoice_info.setter
    def invoice_info(self, value):
        if isinstance(value, MerchantInvoiceInfo):
            self._invoice_info = value
        else:
            self._invoice_info = MerchantInvoiceInfo.from_alipay_dict(value)
    @property
    def license_auth_letter_image(self):
        return self._license_auth_letter_image

    @license_auth_letter_image.setter
    def license_auth_letter_image(self, value):
        self._license_auth_letter_image = value
    @property
    def mcc(self):
        return self._mcc

    @mcc.setter
    def mcc(self, value):
        self._mcc = value
    @property
    def out_door_images(self):
        return self._out_door_images

    @out_door_images.setter
    def out_door_images(self, value):
        self._out_door_images = value
    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, IndustryQualificationInfo):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(IndustryQualificationInfo.from_alipay_dict(i))
    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        if isinstance(value, list):
            self._service = list()
            for i in value:
                self._service.append(i)
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def sign_time_with_isv(self):
        return self._sign_time_with_isv

    @sign_time_with_isv.setter
    def sign_time_with_isv(self, value):
        self._sign_time_with_isv = value
    @property
    def sites(self):
        return self._sites

    @sites.setter
    def sites(self, value):
        if isinstance(value, SiteInfo):
            self._sites = value
        else:
            self._sites = SiteInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.additional_cert_image:
            if hasattr(self.additional_cert_image, 'to_alipay_dict'):
                params['additional_cert_image'] = self.additional_cert_image.to_alipay_dict()
            else:
                params['additional_cert_image'] = self.additional_cert_image
        if self.additional_cert_no:
            if hasattr(self.additional_cert_no, 'to_alipay_dict'):
                params['additional_cert_no'] = self.additional_cert_no.to_alipay_dict()
            else:
                params['additional_cert_no'] = self.additional_cert_no
        if self.additional_cert_type:
            if hasattr(self.additional_cert_type, 'to_alipay_dict'):
                params['additional_cert_type'] = self.additional_cert_type.to_alipay_dict()
            else:
                params['additional_cert_type'] = self.additional_cert_type
        if self.alias_name:
            if hasattr(self.alias_name, 'to_alipay_dict'):
                params['alias_name'] = self.alias_name.to_alipay_dict()
            else:
                params['alias_name'] = self.alias_name
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.binding_alipay_logon_id:
            if hasattr(self.binding_alipay_logon_id, 'to_alipay_dict'):
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id.to_alipay_dict()
            else:
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id
        if self.biz_cards:
            if hasattr(self.biz_cards, 'to_alipay_dict'):
                params['biz_cards'] = self.biz_cards.to_alipay_dict()
            else:
                params['biz_cards'] = self.biz_cards
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.contact_infos:
            if hasattr(self.contact_infos, 'to_alipay_dict'):
                params['contact_infos'] = self.contact_infos.to_alipay_dict()
            else:
                params['contact_infos'] = self.contact_infos
        if self.default_settle_rule:
            if hasattr(self.default_settle_rule, 'to_alipay_dict'):
                params['default_settle_rule'] = self.default_settle_rule.to_alipay_dict()
            else:
                params['default_settle_rule'] = self.default_settle_rule
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.in_door_images:
            if hasattr(self.in_door_images, 'to_alipay_dict'):
                params['in_door_images'] = self.in_door_images.to_alipay_dict()
            else:
                params['in_door_images'] = self.in_door_images
        if self.invoice_info:
            if hasattr(self.invoice_info, 'to_alipay_dict'):
                params['invoice_info'] = self.invoice_info.to_alipay_dict()
            else:
                params['invoice_info'] = self.invoice_info
        if self.license_auth_letter_image:
            if hasattr(self.license_auth_letter_image, 'to_alipay_dict'):
                params['license_auth_letter_image'] = self.license_auth_letter_image.to_alipay_dict()
            else:
                params['license_auth_letter_image'] = self.license_auth_letter_image
        if self.mcc:
            if hasattr(self.mcc, 'to_alipay_dict'):
                params['mcc'] = self.mcc.to_alipay_dict()
            else:
                params['mcc'] = self.mcc
        if self.out_door_images:
            if hasattr(self.out_door_images, 'to_alipay_dict'):
                params['out_door_images'] = self.out_door_images.to_alipay_dict()
            else:
                params['out_door_images'] = self.out_door_images
        if self.qualifications:
            if isinstance(self.qualifications, list):
                for i in range(0, len(self.qualifications)):
                    element = self.qualifications[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.qualifications[i] = element.to_alipay_dict()
            if hasattr(self.qualifications, 'to_alipay_dict'):
                params['qualifications'] = self.qualifications.to_alipay_dict()
            else:
                params['qualifications'] = self.qualifications
        if self.service:
            if isinstance(self.service, list):
                for i in range(0, len(self.service)):
                    element = self.service[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service[i] = element.to_alipay_dict()
            if hasattr(self.service, 'to_alipay_dict'):
                params['service'] = self.service.to_alipay_dict()
            else:
                params['service'] = self.service
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        if self.sign_time_with_isv:
            if hasattr(self.sign_time_with_isv, 'to_alipay_dict'):
                params['sign_time_with_isv'] = self.sign_time_with_isv.to_alipay_dict()
            else:
                params['sign_time_with_isv'] = self.sign_time_with_isv
        if self.sites:
            if hasattr(self.sites, 'to_alipay_dict'):
                params['sites'] = self.sites.to_alipay_dict()
            else:
                params['sites'] = self.sites
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftSimplecreateModel()
        if 'additional_cert_image' in d:
            o.additional_cert_image = d['additional_cert_image']
        if 'additional_cert_no' in d:
            o.additional_cert_no = d['additional_cert_no']
        if 'additional_cert_type' in d:
            o.additional_cert_type = d['additional_cert_type']
        if 'alias_name' in d:
            o.alias_name = d['alias_name']
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'binding_alipay_logon_id' in d:
            o.binding_alipay_logon_id = d['binding_alipay_logon_id']
        if 'biz_cards' in d:
            o.biz_cards = d['biz_cards']
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'contact_infos' in d:
            o.contact_infos = d['contact_infos']
        if 'default_settle_rule' in d:
            o.default_settle_rule = d['default_settle_rule']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'in_door_images' in d:
            o.in_door_images = d['in_door_images']
        if 'invoice_info' in d:
            o.invoice_info = d['invoice_info']
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'qualifications' in d:
            o.qualifications = d['qualifications']
        if 'service' in d:
            o.service = d['service']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'sign_time_with_isv' in d:
            o.sign_time_with_isv = d['sign_time_with_isv']
        if 'sites' in d:
            o.sites = d['sites']
        return o


