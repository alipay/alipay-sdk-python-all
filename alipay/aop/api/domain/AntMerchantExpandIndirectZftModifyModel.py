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


class AntMerchantExpandIndirectZftModifyModel(object):

    def __init__(self):
        self._additional_cert_image = None
        self._additional_cert_no = None
        self._additional_cert_type = None
        self._alias_name = None
        self._alipay_logon_id = None
        self._binding_alipay_logon_id = None
        self._biz_cards = None
        self._business_address = None
        self._cert_image = None
        self._cert_image_back = None
        self._cert_type = None
        self._contact_infos = None
        self._default_settle_rule = None
        self._external_id = None
        self._in_door_images = None
        self._info_source_open_id = None
        self._info_source_uid = None
        self._invoice_info = None
        self._legal_cert_back_image = None
        self._legal_cert_front_image = None
        self._legal_cert_no = None
        self._legal_cert_type = None
        self._legal_name = None
        self._license_auth_letter_image = None
        self._mcc = None
        self._merchant_type = None
        self._name = None
        self._out_door_images = None
        self._oversea_settle_account = None
        self._oversea_settle_open_id = None
        self._qualifications = None
        self._service = None
        self._service_phone = None
        self._sign_time_with_isv = None
        self._sites = None
        self._smid = None
        self._trade_scene = None

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
        if isinstance(value, list):
            self._biz_cards = list()
            for i in value:
                if isinstance(i, SettleCardInfo):
                    self._biz_cards.append(i)
                else:
                    self._biz_cards.append(SettleCardInfo.from_alipay_dict(i))
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
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
    @property
    def cert_image_back(self):
        return self._cert_image_back

    @cert_image_back.setter
    def cert_image_back(self, value):
        self._cert_image_back = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def contact_infos(self):
        return self._contact_infos

    @contact_infos.setter
    def contact_infos(self, value):
        if isinstance(value, list):
            self._contact_infos = list()
            for i in value:
                if isinstance(i, ContactInfo):
                    self._contact_infos.append(i)
                else:
                    self._contact_infos.append(ContactInfo.from_alipay_dict(i))
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
        if isinstance(value, list):
            self._in_door_images = list()
            for i in value:
                self._in_door_images.append(i)
    @property
    def info_source_open_id(self):
        return self._info_source_open_id

    @info_source_open_id.setter
    def info_source_open_id(self, value):
        self._info_source_open_id = value
    @property
    def info_source_uid(self):
        return self._info_source_uid

    @info_source_uid.setter
    def info_source_uid(self, value):
        self._info_source_uid = value
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
    def legal_cert_back_image(self):
        return self._legal_cert_back_image

    @legal_cert_back_image.setter
    def legal_cert_back_image(self, value):
        self._legal_cert_back_image = value
    @property
    def legal_cert_front_image(self):
        return self._legal_cert_front_image

    @legal_cert_front_image.setter
    def legal_cert_front_image(self, value):
        self._legal_cert_front_image = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_cert_type(self):
        return self._legal_cert_type

    @legal_cert_type.setter
    def legal_cert_type(self, value):
        self._legal_cert_type = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
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
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_door_images(self):
        return self._out_door_images

    @out_door_images.setter
    def out_door_images(self, value):
        if isinstance(value, list):
            self._out_door_images = list()
            for i in value:
                self._out_door_images.append(i)
    @property
    def oversea_settle_account(self):
        return self._oversea_settle_account

    @oversea_settle_account.setter
    def oversea_settle_account(self, value):
        self._oversea_settle_account = value
    @property
    def oversea_settle_open_id(self):
        return self._oversea_settle_open_id

    @oversea_settle_open_id.setter
    def oversea_settle_open_id(self, value):
        self._oversea_settle_open_id = value
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
        if isinstance(value, list):
            self._sites = list()
            for i in value:
                if isinstance(i, SiteInfo):
                    self._sites.append(i)
                else:
                    self._sites.append(SiteInfo.from_alipay_dict(i))
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def trade_scene(self):
        return self._trade_scene

    @trade_scene.setter
    def trade_scene(self, value):
        if isinstance(value, list):
            self._trade_scene = list()
            for i in value:
                self._trade_scene.append(i)


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
            if isinstance(self.biz_cards, list):
                for i in range(0, len(self.biz_cards)):
                    element = self.biz_cards[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_cards[i] = element.to_alipay_dict()
            if hasattr(self.biz_cards, 'to_alipay_dict'):
                params['biz_cards'] = self.biz_cards.to_alipay_dict()
            else:
                params['biz_cards'] = self.biz_cards
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.cert_image:
            if hasattr(self.cert_image, 'to_alipay_dict'):
                params['cert_image'] = self.cert_image.to_alipay_dict()
            else:
                params['cert_image'] = self.cert_image
        if self.cert_image_back:
            if hasattr(self.cert_image_back, 'to_alipay_dict'):
                params['cert_image_back'] = self.cert_image_back.to_alipay_dict()
            else:
                params['cert_image_back'] = self.cert_image_back
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.contact_infos:
            if isinstance(self.contact_infos, list):
                for i in range(0, len(self.contact_infos)):
                    element = self.contact_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_infos[i] = element.to_alipay_dict()
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
            if isinstance(self.in_door_images, list):
                for i in range(0, len(self.in_door_images)):
                    element = self.in_door_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.in_door_images[i] = element.to_alipay_dict()
            if hasattr(self.in_door_images, 'to_alipay_dict'):
                params['in_door_images'] = self.in_door_images.to_alipay_dict()
            else:
                params['in_door_images'] = self.in_door_images
        if self.info_source_open_id:
            if hasattr(self.info_source_open_id, 'to_alipay_dict'):
                params['info_source_open_id'] = self.info_source_open_id.to_alipay_dict()
            else:
                params['info_source_open_id'] = self.info_source_open_id
        if self.info_source_uid:
            if hasattr(self.info_source_uid, 'to_alipay_dict'):
                params['info_source_uid'] = self.info_source_uid.to_alipay_dict()
            else:
                params['info_source_uid'] = self.info_source_uid
        if self.invoice_info:
            if hasattr(self.invoice_info, 'to_alipay_dict'):
                params['invoice_info'] = self.invoice_info.to_alipay_dict()
            else:
                params['invoice_info'] = self.invoice_info
        if self.legal_cert_back_image:
            if hasattr(self.legal_cert_back_image, 'to_alipay_dict'):
                params['legal_cert_back_image'] = self.legal_cert_back_image.to_alipay_dict()
            else:
                params['legal_cert_back_image'] = self.legal_cert_back_image
        if self.legal_cert_front_image:
            if hasattr(self.legal_cert_front_image, 'to_alipay_dict'):
                params['legal_cert_front_image'] = self.legal_cert_front_image.to_alipay_dict()
            else:
                params['legal_cert_front_image'] = self.legal_cert_front_image
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_cert_type:
            if hasattr(self.legal_cert_type, 'to_alipay_dict'):
                params['legal_cert_type'] = self.legal_cert_type.to_alipay_dict()
            else:
                params['legal_cert_type'] = self.legal_cert_type
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
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
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_door_images:
            if isinstance(self.out_door_images, list):
                for i in range(0, len(self.out_door_images)):
                    element = self.out_door_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_door_images[i] = element.to_alipay_dict()
            if hasattr(self.out_door_images, 'to_alipay_dict'):
                params['out_door_images'] = self.out_door_images.to_alipay_dict()
            else:
                params['out_door_images'] = self.out_door_images
        if self.oversea_settle_account:
            if hasattr(self.oversea_settle_account, 'to_alipay_dict'):
                params['oversea_settle_account'] = self.oversea_settle_account.to_alipay_dict()
            else:
                params['oversea_settle_account'] = self.oversea_settle_account
        if self.oversea_settle_open_id:
            if hasattr(self.oversea_settle_open_id, 'to_alipay_dict'):
                params['oversea_settle_open_id'] = self.oversea_settle_open_id.to_alipay_dict()
            else:
                params['oversea_settle_open_id'] = self.oversea_settle_open_id
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
            if isinstance(self.sites, list):
                for i in range(0, len(self.sites)):
                    element = self.sites[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sites[i] = element.to_alipay_dict()
            if hasattr(self.sites, 'to_alipay_dict'):
                params['sites'] = self.sites.to_alipay_dict()
            else:
                params['sites'] = self.sites
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.trade_scene:
            if isinstance(self.trade_scene, list):
                for i in range(0, len(self.trade_scene)):
                    element = self.trade_scene[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_scene[i] = element.to_alipay_dict()
            if hasattr(self.trade_scene, 'to_alipay_dict'):
                params['trade_scene'] = self.trade_scene.to_alipay_dict()
            else:
                params['trade_scene'] = self.trade_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftModifyModel()
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
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_image_back' in d:
            o.cert_image_back = d['cert_image_back']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'contact_infos' in d:
            o.contact_infos = d['contact_infos']
        if 'default_settle_rule' in d:
            o.default_settle_rule = d['default_settle_rule']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'in_door_images' in d:
            o.in_door_images = d['in_door_images']
        if 'info_source_open_id' in d:
            o.info_source_open_id = d['info_source_open_id']
        if 'info_source_uid' in d:
            o.info_source_uid = d['info_source_uid']
        if 'invoice_info' in d:
            o.invoice_info = d['invoice_info']
        if 'legal_cert_back_image' in d:
            o.legal_cert_back_image = d['legal_cert_back_image']
        if 'legal_cert_front_image' in d:
            o.legal_cert_front_image = d['legal_cert_front_image']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_cert_type' in d:
            o.legal_cert_type = d['legal_cert_type']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'name' in d:
            o.name = d['name']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'oversea_settle_account' in d:
            o.oversea_settle_account = d['oversea_settle_account']
        if 'oversea_settle_open_id' in d:
            o.oversea_settle_open_id = d['oversea_settle_open_id']
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
        if 'smid' in d:
            o.smid = d['smid']
        if 'trade_scene' in d:
            o.trade_scene = d['trade_scene']
        return o


