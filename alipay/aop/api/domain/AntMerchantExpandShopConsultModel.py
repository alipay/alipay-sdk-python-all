#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleCardInfo import SettleCardInfo
from alipay.aop.api.domain.AddressInfo import AddressInfo
from alipay.aop.api.domain.ShopBusinessTime import ShopBusinessTime
from alipay.aop.api.domain.ContactInfo import ContactInfo
from alipay.aop.api.domain.ShopExtInfo import ShopExtInfo
from alipay.aop.api.domain.IndustryQualificationInfo import IndustryQualificationInfo


class AntMerchantExpandShopConsultModel(object):

    def __init__(self):
        self._biz_cards = None
        self._brand_id = None
        self._business_address = None
        self._business_time = None
        self._cert_image = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._contact_infos = None
        self._contact_mobile = None
        self._contact_phone = None
        self._ext_infos = None
        self._ip_role_id = None
        self._legal_cert_no = None
        self._legal_name = None
        self._license_auth_letter_image = None
        self._memo = None
        self._out_door_images = None
        self._qualifications = None
        self._scene = None
        self._settle_alipay_logon_id = None
        self._shop_category = None
        self._shop_name = None
        self._shop_type = None
        self._store_id = None

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
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
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
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        if isinstance(value, list):
            self._business_time = list()
            for i in value:
                if isinstance(i, ShopBusinessTime):
                    self._business_time.append(i)
                else:
                    self._business_time.append(ShopBusinessTime.from_alipay_dict(i))
    @property
    def cert_image(self):
        return self._cert_image

    @cert_image.setter
    def cert_image(self, value):
        self._cert_image = value
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
                if isinstance(i, ContactInfo):
                    self._contact_infos.append(i)
                else:
                    self._contact_infos.append(ContactInfo.from_alipay_dict(i))
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        if isinstance(value, list):
            self._ext_infos = list()
            for i in value:
                if isinstance(i, ShopExtInfo):
                    self._ext_infos.append(i)
                else:
                    self._ext_infos.append(ShopExtInfo.from_alipay_dict(i))
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
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
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def settle_alipay_logon_id(self):
        return self._settle_alipay_logon_id

    @settle_alipay_logon_id.setter
    def settle_alipay_logon_id(self, value):
        self._settle_alipay_logon_id = value
    @property
    def shop_category(self):
        return self._shop_category

    @shop_category.setter
    def shop_category(self, value):
        self._shop_category = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value


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
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.business_time:
            if isinstance(self.business_time, list):
                for i in range(0, len(self.business_time)):
                    element = self.business_time[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_time[i] = element.to_alipay_dict()
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.cert_image:
            if hasattr(self.cert_image, 'to_alipay_dict'):
                params['cert_image'] = self.cert_image.to_alipay_dict()
            else:
                params['cert_image'] = self.cert_image
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
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.ext_infos:
            if isinstance(self.ext_infos, list):
                for i in range(0, len(self.ext_infos)):
                    element = self.ext_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_infos[i] = element.to_alipay_dict()
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.settle_alipay_logon_id:
            if hasattr(self.settle_alipay_logon_id, 'to_alipay_dict'):
                params['settle_alipay_logon_id'] = self.settle_alipay_logon_id.to_alipay_dict()
            else:
                params['settle_alipay_logon_id'] = self.settle_alipay_logon_id
        if self.shop_category:
            if hasattr(self.shop_category, 'to_alipay_dict'):
                params['shop_category'] = self.shop_category.to_alipay_dict()
            else:
                params['shop_category'] = self.shop_category
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandShopConsultModel()
        if 'biz_cards' in d:
            o.biz_cards = d['biz_cards']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'contact_infos' in d:
            o.contact_infos = d['contact_infos']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'license_auth_letter_image' in d:
            o.license_auth_letter_image = d['license_auth_letter_image']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'qualifications' in d:
            o.qualifications = d['qualifications']
        if 'scene' in d:
            o.scene = d['scene']
        if 'settle_alipay_logon_id' in d:
            o.settle_alipay_logon_id = d['settle_alipay_logon_id']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


