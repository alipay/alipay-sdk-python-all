#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineMarketShopCreateModel(object):

    def __init__(self):
        self._address = None
        self._audit_images = None
        self._auth_letter = None
        self._biz_version = None
        self._box = None
        self._branch_shop_name = None
        self._brand_logo = None
        self._brand_name = None
        self._business_certificate = None
        self._business_certificate_expires = None
        self._business_time = None
        self._category_id = None
        self._city_code = None
        self._contact_number = None
        self._creator = None
        self._district_code = None
        self._enterprise_logon_id = None
        self._enterprise_name = None
        self._implement_id = None
        self._is_operating_online = None
        self._isv_uid = None
        self._latitude = None
        self._leads_id = None
        self._licence = None
        self._licence_code = None
        self._licence_expires = None
        self._licence_name = None
        self._longitude = None
        self._main_image = None
        self._main_shop_name = None
        self._no_smoking = None
        self._notify_mobile = None
        self._online_image = None
        self._online_url = None
        self._op_role = None
        self._operate_notify_url = None
        self._other_authorization = None
        self._parking = None
        self._partner_id = None
        self._pay_type = None
        self._province_code = None
        self._ref_apply_id = None
        self._request_id = None
        self._store_id = None
        self._value_added = None
        self._version = None
        self._wifi = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def audit_images(self):
        return self._audit_images

    @audit_images.setter
    def audit_images(self, value):
        self._audit_images = value
    @property
    def auth_letter(self):
        return self._auth_letter

    @auth_letter.setter
    def auth_letter(self, value):
        self._auth_letter = value
    @property
    def biz_version(self):
        return self._biz_version

    @biz_version.setter
    def biz_version(self, value):
        self._biz_version = value
    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, value):
        self._box = value
    @property
    def branch_shop_name(self):
        return self._branch_shop_name

    @branch_shop_name.setter
    def branch_shop_name(self, value):
        self._branch_shop_name = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def business_certificate(self):
        return self._business_certificate

    @business_certificate.setter
    def business_certificate(self, value):
        self._business_certificate = value
    @property
    def business_certificate_expires(self):
        return self._business_certificate_expires

    @business_certificate_expires.setter
    def business_certificate_expires(self, value):
        self._business_certificate_expires = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def enterprise_logon_id(self):
        return self._enterprise_logon_id

    @enterprise_logon_id.setter
    def enterprise_logon_id(self, value):
        self._enterprise_logon_id = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def implement_id(self):
        return self._implement_id

    @implement_id.setter
    def implement_id(self, value):
        self._implement_id = value
    @property
    def is_operating_online(self):
        return self._is_operating_online

    @is_operating_online.setter
    def is_operating_online(self, value):
        self._is_operating_online = value
    @property
    def isv_uid(self):
        return self._isv_uid

    @isv_uid.setter
    def isv_uid(self, value):
        self._isv_uid = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def licence(self):
        return self._licence

    @licence.setter
    def licence(self, value):
        self._licence = value
    @property
    def licence_code(self):
        return self._licence_code

    @licence_code.setter
    def licence_code(self, value):
        self._licence_code = value
    @property
    def licence_expires(self):
        return self._licence_expires

    @licence_expires.setter
    def licence_expires(self, value):
        self._licence_expires = value
    @property
    def licence_name(self):
        return self._licence_name

    @licence_name.setter
    def licence_name(self, value):
        self._licence_name = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def main_shop_name(self):
        return self._main_shop_name

    @main_shop_name.setter
    def main_shop_name(self, value):
        self._main_shop_name = value
    @property
    def no_smoking(self):
        return self._no_smoking

    @no_smoking.setter
    def no_smoking(self, value):
        self._no_smoking = value
    @property
    def notify_mobile(self):
        return self._notify_mobile

    @notify_mobile.setter
    def notify_mobile(self, value):
        self._notify_mobile = value
    @property
    def online_image(self):
        return self._online_image

    @online_image.setter
    def online_image(self, value):
        self._online_image = value
    @property
    def online_url(self):
        return self._online_url

    @online_url.setter
    def online_url(self, value):
        self._online_url = value
    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value
    @property
    def operate_notify_url(self):
        return self._operate_notify_url

    @operate_notify_url.setter
    def operate_notify_url(self, value):
        self._operate_notify_url = value
    @property
    def other_authorization(self):
        return self._other_authorization

    @other_authorization.setter
    def other_authorization(self, value):
        self._other_authorization = value
    @property
    def parking(self):
        return self._parking

    @parking.setter
    def parking(self, value):
        self._parking = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def ref_apply_id(self):
        return self._ref_apply_id

    @ref_apply_id.setter
    def ref_apply_id(self, value):
        self._ref_apply_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def value_added(self):
        return self._value_added

    @value_added.setter
    def value_added(self, value):
        self._value_added = value
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value
    @property
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, value):
        self._wifi = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.audit_images:
            if hasattr(self.audit_images, 'to_alipay_dict'):
                params['audit_images'] = self.audit_images.to_alipay_dict()
            else:
                params['audit_images'] = self.audit_images
        if self.auth_letter:
            if hasattr(self.auth_letter, 'to_alipay_dict'):
                params['auth_letter'] = self.auth_letter.to_alipay_dict()
            else:
                params['auth_letter'] = self.auth_letter
        if self.biz_version:
            if hasattr(self.biz_version, 'to_alipay_dict'):
                params['biz_version'] = self.biz_version.to_alipay_dict()
            else:
                params['biz_version'] = self.biz_version
        if self.box:
            if hasattr(self.box, 'to_alipay_dict'):
                params['box'] = self.box.to_alipay_dict()
            else:
                params['box'] = self.box
        if self.branch_shop_name:
            if hasattr(self.branch_shop_name, 'to_alipay_dict'):
                params['branch_shop_name'] = self.branch_shop_name.to_alipay_dict()
            else:
                params['branch_shop_name'] = self.branch_shop_name
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.business_certificate:
            if hasattr(self.business_certificate, 'to_alipay_dict'):
                params['business_certificate'] = self.business_certificate.to_alipay_dict()
            else:
                params['business_certificate'] = self.business_certificate
        if self.business_certificate_expires:
            if hasattr(self.business_certificate_expires, 'to_alipay_dict'):
                params['business_certificate_expires'] = self.business_certificate_expires.to_alipay_dict()
            else:
                params['business_certificate_expires'] = self.business_certificate_expires
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.contact_number:
            if hasattr(self.contact_number, 'to_alipay_dict'):
                params['contact_number'] = self.contact_number.to_alipay_dict()
            else:
                params['contact_number'] = self.contact_number
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.enterprise_logon_id:
            if hasattr(self.enterprise_logon_id, 'to_alipay_dict'):
                params['enterprise_logon_id'] = self.enterprise_logon_id.to_alipay_dict()
            else:
                params['enterprise_logon_id'] = self.enterprise_logon_id
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.implement_id:
            if hasattr(self.implement_id, 'to_alipay_dict'):
                params['implement_id'] = self.implement_id.to_alipay_dict()
            else:
                params['implement_id'] = self.implement_id
        if self.is_operating_online:
            if hasattr(self.is_operating_online, 'to_alipay_dict'):
                params['is_operating_online'] = self.is_operating_online.to_alipay_dict()
            else:
                params['is_operating_online'] = self.is_operating_online
        if self.isv_uid:
            if hasattr(self.isv_uid, 'to_alipay_dict'):
                params['isv_uid'] = self.isv_uid.to_alipay_dict()
            else:
                params['isv_uid'] = self.isv_uid
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.licence:
            if hasattr(self.licence, 'to_alipay_dict'):
                params['licence'] = self.licence.to_alipay_dict()
            else:
                params['licence'] = self.licence
        if self.licence_code:
            if hasattr(self.licence_code, 'to_alipay_dict'):
                params['licence_code'] = self.licence_code.to_alipay_dict()
            else:
                params['licence_code'] = self.licence_code
        if self.licence_expires:
            if hasattr(self.licence_expires, 'to_alipay_dict'):
                params['licence_expires'] = self.licence_expires.to_alipay_dict()
            else:
                params['licence_expires'] = self.licence_expires
        if self.licence_name:
            if hasattr(self.licence_name, 'to_alipay_dict'):
                params['licence_name'] = self.licence_name.to_alipay_dict()
            else:
                params['licence_name'] = self.licence_name
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.main_shop_name:
            if hasattr(self.main_shop_name, 'to_alipay_dict'):
                params['main_shop_name'] = self.main_shop_name.to_alipay_dict()
            else:
                params['main_shop_name'] = self.main_shop_name
        if self.no_smoking:
            if hasattr(self.no_smoking, 'to_alipay_dict'):
                params['no_smoking'] = self.no_smoking.to_alipay_dict()
            else:
                params['no_smoking'] = self.no_smoking
        if self.notify_mobile:
            if hasattr(self.notify_mobile, 'to_alipay_dict'):
                params['notify_mobile'] = self.notify_mobile.to_alipay_dict()
            else:
                params['notify_mobile'] = self.notify_mobile
        if self.online_image:
            if hasattr(self.online_image, 'to_alipay_dict'):
                params['online_image'] = self.online_image.to_alipay_dict()
            else:
                params['online_image'] = self.online_image
        if self.online_url:
            if hasattr(self.online_url, 'to_alipay_dict'):
                params['online_url'] = self.online_url.to_alipay_dict()
            else:
                params['online_url'] = self.online_url
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        if self.operate_notify_url:
            if hasattr(self.operate_notify_url, 'to_alipay_dict'):
                params['operate_notify_url'] = self.operate_notify_url.to_alipay_dict()
            else:
                params['operate_notify_url'] = self.operate_notify_url
        if self.other_authorization:
            if hasattr(self.other_authorization, 'to_alipay_dict'):
                params['other_authorization'] = self.other_authorization.to_alipay_dict()
            else:
                params['other_authorization'] = self.other_authorization
        if self.parking:
            if hasattr(self.parking, 'to_alipay_dict'):
                params['parking'] = self.parking.to_alipay_dict()
            else:
                params['parking'] = self.parking
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.ref_apply_id:
            if hasattr(self.ref_apply_id, 'to_alipay_dict'):
                params['ref_apply_id'] = self.ref_apply_id.to_alipay_dict()
            else:
                params['ref_apply_id'] = self.ref_apply_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.value_added:
            if hasattr(self.value_added, 'to_alipay_dict'):
                params['value_added'] = self.value_added.to_alipay_dict()
            else:
                params['value_added'] = self.value_added
        if self.version:
            if hasattr(self.version, 'to_alipay_dict'):
                params['version'] = self.version.to_alipay_dict()
            else:
                params['version'] = self.version
        if self.wifi:
            if hasattr(self.wifi, 'to_alipay_dict'):
                params['wifi'] = self.wifi.to_alipay_dict()
            else:
                params['wifi'] = self.wifi
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'audit_images' in d:
            o.audit_images = d['audit_images']
        if 'auth_letter' in d:
            o.auth_letter = d['auth_letter']
        if 'biz_version' in d:
            o.biz_version = d['biz_version']
        if 'box' in d:
            o.box = d['box']
        if 'branch_shop_name' in d:
            o.branch_shop_name = d['branch_shop_name']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'business_certificate' in d:
            o.business_certificate = d['business_certificate']
        if 'business_certificate_expires' in d:
            o.business_certificate_expires = d['business_certificate_expires']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'contact_number' in d:
            o.contact_number = d['contact_number']
        if 'creator' in d:
            o.creator = d['creator']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'enterprise_logon_id' in d:
            o.enterprise_logon_id = d['enterprise_logon_id']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'implement_id' in d:
            o.implement_id = d['implement_id']
        if 'is_operating_online' in d:
            o.is_operating_online = d['is_operating_online']
        if 'isv_uid' in d:
            o.isv_uid = d['isv_uid']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'licence' in d:
            o.licence = d['licence']
        if 'licence_code' in d:
            o.licence_code = d['licence_code']
        if 'licence_expires' in d:
            o.licence_expires = d['licence_expires']
        if 'licence_name' in d:
            o.licence_name = d['licence_name']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'main_shop_name' in d:
            o.main_shop_name = d['main_shop_name']
        if 'no_smoking' in d:
            o.no_smoking = d['no_smoking']
        if 'notify_mobile' in d:
            o.notify_mobile = d['notify_mobile']
        if 'online_image' in d:
            o.online_image = d['online_image']
        if 'online_url' in d:
            o.online_url = d['online_url']
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'operate_notify_url' in d:
            o.operate_notify_url = d['operate_notify_url']
        if 'other_authorization' in d:
            o.other_authorization = d['other_authorization']
        if 'parking' in d:
            o.parking = d['parking']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'ref_apply_id' in d:
            o.ref_apply_id = d['ref_apply_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'value_added' in d:
            o.value_added = d['value_added']
        if 'version' in d:
            o.version = d['version']
        if 'wifi' in d:
            o.wifi = d['wifi']
        return o


