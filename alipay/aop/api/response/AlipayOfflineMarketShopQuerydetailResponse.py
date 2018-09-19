#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketShopQuerydetailResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopQuerydetailResponse, self).__init__()
        self._address = None
        self._audit_desc = None
        self._audit_images = None
        self._audit_status = None
        self._auth_letter = None
        self._avg_price = None
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
        self._create_channel = None
        self._district_code = None
        self._gmt_shop_create = None
        self._gmt_shop_modified = None
        self._implement_id = None
        self._is_online = None
        self._is_operating_online = None
        self._is_show = None
        self._isv_uid = None
        self._latitude = None
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
        self._operate_notify_url = None
        self._other_auth_images = None
        self._parking = None
        self._partner_id = None
        self._pay_type = None
        self._payment_account = None
        self._pic_coll = None
        self._processed_qr_code = None
        self._provider_xiaoer_uid = None
        self._province_code = None
        self._qr_code = None
        self._shop_tags = None
        self._store_id = None
        self._value_added = None
        self._wifi = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def audit_images(self):
        return self._audit_images

    @audit_images.setter
    def audit_images(self, value):
        self._audit_images = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def auth_letter(self):
        return self._auth_letter

    @auth_letter.setter
    def auth_letter(self, value):
        self._auth_letter = value
    @property
    def avg_price(self):
        return self._avg_price

    @avg_price.setter
    def avg_price(self, value):
        self._avg_price = value
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
    def create_channel(self):
        return self._create_channel

    @create_channel.setter
    def create_channel(self, value):
        self._create_channel = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def gmt_shop_create(self):
        return self._gmt_shop_create

    @gmt_shop_create.setter
    def gmt_shop_create(self, value):
        self._gmt_shop_create = value
    @property
    def gmt_shop_modified(self):
        return self._gmt_shop_modified

    @gmt_shop_modified.setter
    def gmt_shop_modified(self, value):
        self._gmt_shop_modified = value
    @property
    def implement_id(self):
        return self._implement_id

    @implement_id.setter
    def implement_id(self, value):
        self._implement_id = value
    @property
    def is_online(self):
        return self._is_online

    @is_online.setter
    def is_online(self, value):
        self._is_online = value
    @property
    def is_operating_online(self):
        return self._is_operating_online

    @is_operating_online.setter
    def is_operating_online(self, value):
        self._is_operating_online = value
    @property
    def is_show(self):
        return self._is_show

    @is_show.setter
    def is_show(self, value):
        self._is_show = value
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
    def operate_notify_url(self):
        return self._operate_notify_url

    @operate_notify_url.setter
    def operate_notify_url(self, value):
        self._operate_notify_url = value
    @property
    def other_auth_images(self):
        return self._other_auth_images

    @other_auth_images.setter
    def other_auth_images(self, value):
        self._other_auth_images = value
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
    def payment_account(self):
        return self._payment_account

    @payment_account.setter
    def payment_account(self, value):
        self._payment_account = value
    @property
    def pic_coll(self):
        return self._pic_coll

    @pic_coll.setter
    def pic_coll(self, value):
        self._pic_coll = value
    @property
    def processed_qr_code(self):
        return self._processed_qr_code

    @processed_qr_code.setter
    def processed_qr_code(self, value):
        self._processed_qr_code = value
    @property
    def provider_xiaoer_uid(self):
        return self._provider_xiaoer_uid

    @provider_xiaoer_uid.setter
    def provider_xiaoer_uid(self, value):
        self._provider_xiaoer_uid = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def shop_tags(self):
        return self._shop_tags

    @shop_tags.setter
    def shop_tags(self, value):
        self._shop_tags = value
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
    def wifi(self):
        return self._wifi

    @wifi.setter
    def wifi(self, value):
        self._wifi = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopQuerydetailResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'audit_desc' in response:
            self.audit_desc = response['audit_desc']
        if 'audit_images' in response:
            self.audit_images = response['audit_images']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'auth_letter' in response:
            self.auth_letter = response['auth_letter']
        if 'avg_price' in response:
            self.avg_price = response['avg_price']
        if 'box' in response:
            self.box = response['box']
        if 'branch_shop_name' in response:
            self.branch_shop_name = response['branch_shop_name']
        if 'brand_logo' in response:
            self.brand_logo = response['brand_logo']
        if 'brand_name' in response:
            self.brand_name = response['brand_name']
        if 'business_certificate' in response:
            self.business_certificate = response['business_certificate']
        if 'business_certificate_expires' in response:
            self.business_certificate_expires = response['business_certificate_expires']
        if 'business_time' in response:
            self.business_time = response['business_time']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'city_code' in response:
            self.city_code = response['city_code']
        if 'contact_number' in response:
            self.contact_number = response['contact_number']
        if 'create_channel' in response:
            self.create_channel = response['create_channel']
        if 'district_code' in response:
            self.district_code = response['district_code']
        if 'gmt_shop_create' in response:
            self.gmt_shop_create = response['gmt_shop_create']
        if 'gmt_shop_modified' in response:
            self.gmt_shop_modified = response['gmt_shop_modified']
        if 'implement_id' in response:
            self.implement_id = response['implement_id']
        if 'is_online' in response:
            self.is_online = response['is_online']
        if 'is_operating_online' in response:
            self.is_operating_online = response['is_operating_online']
        if 'is_show' in response:
            self.is_show = response['is_show']
        if 'isv_uid' in response:
            self.isv_uid = response['isv_uid']
        if 'latitude' in response:
            self.latitude = response['latitude']
        if 'licence' in response:
            self.licence = response['licence']
        if 'licence_code' in response:
            self.licence_code = response['licence_code']
        if 'licence_expires' in response:
            self.licence_expires = response['licence_expires']
        if 'licence_name' in response:
            self.licence_name = response['licence_name']
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'main_image' in response:
            self.main_image = response['main_image']
        if 'main_shop_name' in response:
            self.main_shop_name = response['main_shop_name']
        if 'no_smoking' in response:
            self.no_smoking = response['no_smoking']
        if 'notify_mobile' in response:
            self.notify_mobile = response['notify_mobile']
        if 'online_image' in response:
            self.online_image = response['online_image']
        if 'operate_notify_url' in response:
            self.operate_notify_url = response['operate_notify_url']
        if 'other_auth_images' in response:
            self.other_auth_images = response['other_auth_images']
        if 'parking' in response:
            self.parking = response['parking']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'pay_type' in response:
            self.pay_type = response['pay_type']
        if 'payment_account' in response:
            self.payment_account = response['payment_account']
        if 'pic_coll' in response:
            self.pic_coll = response['pic_coll']
        if 'processed_qr_code' in response:
            self.processed_qr_code = response['processed_qr_code']
        if 'provider_xiaoer_uid' in response:
            self.provider_xiaoer_uid = response['provider_xiaoer_uid']
        if 'province_code' in response:
            self.province_code = response['province_code']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'shop_tags' in response:
            self.shop_tags = response['shop_tags']
        if 'store_id' in response:
            self.store_id = response['store_id']
        if 'value_added' in response:
            self.value_added = response['value_added']
        if 'wifi' in response:
            self.wifi = response['wifi']
