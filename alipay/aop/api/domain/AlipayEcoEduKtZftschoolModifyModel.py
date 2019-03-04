#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleCardInfoKt import SettleCardInfoKt
from alipay.aop.api.domain.AddressInfoKt import AddressInfoKt
from alipay.aop.api.domain.ContactInfoKt import ContactInfoKt
from alipay.aop.api.domain.MerchantInvoiceInfoKt import MerchantInvoiceInfoKt
from alipay.aop.api.domain.IndustryQualificationInfoKt import IndustryQualificationInfoKt
from alipay.aop.api.domain.SiteInfoKt import SiteInfoKt


class AlipayEcoEduKtZftschoolModifyModel(object):

    def __init__(self):
        self._biz_cards = None
        self._business_address = None
        self._cert_image = None
        self._cert_image_back = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._contact_infos = None
        self._invoice_info = None
        self._isv_notify_url = None
        self._legal_cert_back_image = None
        self._legal_cert_front_image = None
        self._legal_cert_no = None
        self._legal_name = None
        self._license_auth_letter_image = None
        self._mcc = None
        self._merchant_type = None
        self._order_id = None
        self._out_biz_no = None
        self._out_door_images = None
        self._partner_name = None
        self._partner_phone = None
        self._partner_pid = None
        self._qualifications = None
        self._school_name = None
        self._school_type = None
        self._service = None
        self._service_phone = None
        self._sign_time_with_isv = None
        self._sites = None
        self._status = None

    @property
    def biz_cards(self):
        return self._biz_cards

    @biz_cards.setter
    def biz_cards(self, value):
        if isinstance(value, list):
            self._biz_cards = list()
            for i in value:
                if isinstance(i, SettleCardInfoKt):
                    self._biz_cards.append(i)
                else:
                    self._biz_cards.append(SettleCardInfoKt.from_alipay_dict(i))
    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, AddressInfoKt):
            self._business_address = value
        else:
            self._business_address = AddressInfoKt.from_alipay_dict(value)
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
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
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
                if isinstance(i, ContactInfoKt):
                    self._contact_infos.append(i)
                else:
                    self._contact_infos.append(ContactInfoKt.from_alipay_dict(i))
    @property
    def invoice_info(self):
        return self._invoice_info

    @invoice_info.setter
    def invoice_info(self, value):
        if isinstance(value, MerchantInvoiceInfoKt):
            self._invoice_info = value
        else:
            self._invoice_info = MerchantInvoiceInfoKt.from_alipay_dict(value)
    @property
    def isv_notify_url(self):
        return self._isv_notify_url

    @isv_notify_url.setter
    def isv_notify_url(self, value):
        self._isv_notify_url = value
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
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def partner_phone(self):
        return self._partner_phone

    @partner_phone.setter
    def partner_phone(self, value):
        self._partner_phone = value
    @property
    def partner_pid(self):
        return self._partner_pid

    @partner_pid.setter
    def partner_pid(self, value):
        self._partner_pid = value
    @property
    def qualifications(self):
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value):
        if isinstance(value, list):
            self._qualifications = list()
            for i in value:
                if isinstance(i, IndustryQualificationInfoKt):
                    self._qualifications.append(i)
                else:
                    self._qualifications.append(IndustryQualificationInfoKt.from_alipay_dict(i))
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_type(self):
        return self._school_type

    @school_type.setter
    def school_type(self, value):
        self._school_type = value
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
                if isinstance(i, SiteInfoKt):
                    self._sites.append(i)
                else:
                    self._sites.append(SiteInfoKt.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
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
        if self.invoice_info:
            if hasattr(self.invoice_info, 'to_alipay_dict'):
                params['invoice_info'] = self.invoice_info.to_alipay_dict()
            else:
                params['invoice_info'] = self.invoice_info
        if self.isv_notify_url:
            if hasattr(self.isv_notify_url, 'to_alipay_dict'):
                params['isv_notify_url'] = self.isv_notify_url.to_alipay_dict()
            else:
                params['isv_notify_url'] = self.isv_notify_url
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
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.partner_phone:
            if hasattr(self.partner_phone, 'to_alipay_dict'):
                params['partner_phone'] = self.partner_phone.to_alipay_dict()
            else:
                params['partner_phone'] = self.partner_phone
        if self.partner_pid:
            if hasattr(self.partner_pid, 'to_alipay_dict'):
                params['partner_pid'] = self.partner_pid.to_alipay_dict()
            else:
                params['partner_pid'] = self.partner_pid
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
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_type:
            if hasattr(self.school_type, 'to_alipay_dict'):
                params['school_type'] = self.school_type.to_alipay_dict()
            else:
                params['school_type'] = self.school_type
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduKtZftschoolModifyModel()
        if 'biz_cards' in d:
            o.biz_cards = d['biz_cards']
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_image_back' in d:
            o.cert_image_back = d['cert_image_back']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'contact_infos' in d:
            o.contact_infos = d['contact_infos']
        if 'invoice_info' in d:
            o.invoice_info = d['invoice_info']
        if 'isv_notify_url' in d:
            o.isv_notify_url = d['isv_notify_url']
        if 'legal_cert_back_image' in d:
            o.legal_cert_back_image = d['legal_cert_back_image']
        if 'legal_cert_front_image' in d:
            o.legal_cert_front_image = d['legal_cert_front_image']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'mcc' in d:
            o.mcc = d['mcc']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'partner_phone' in d:
            o.partner_phone = d['partner_phone']
        if 'partner_pid' in d:
            o.partner_pid = d['partner_pid']
        if 'qualifications' in d:
            o.qualifications = d['qualifications']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_type' in d:
            o.school_type = d['school_type']
        if 'service' in d:
            o.service = d['service']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        if 'sign_time_with_isv' in d:
            o.sign_time_with_isv = d['sign_time_with_isv']
        if 'sites' in d:
            o.sites = d['sites']
        if 'status' in d:
            o.status = d['status']
        return o


