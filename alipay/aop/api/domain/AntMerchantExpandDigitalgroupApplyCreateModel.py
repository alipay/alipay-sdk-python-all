#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopExtInfo import ShopExtInfo
from alipay.aop.api.domain.AlipayTagVO import AlipayTagVO


class AntMerchantExpandDigitalgroupApplyCreateModel(object):

    def __init__(self):
        self._address = None
        self._brand_id = None
        self._brand_name = None
        self._business_license_no = None
        self._business_license_pic = None
        self._business_time = None
        self._category_final = None
        self._category_one = None
        self._channel = None
        self._city = None
        self._contact_phone = None
        self._district = None
        self._ext_info = None
        self._g_name = None
        self._g_shopid = None
        self._latitude = None
        self._legal_person_card = None
        self._legal_person_name = None
        self._longitude = None
        self._province = None
        self._shop_albums = None
        self._shop_business_status = None
        self._shop_videos = None
        self._status = None
        self._store_head_pic = None
        self._store_logo = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def business_time(self):
        return self._business_time

    @business_time.setter
    def business_time(self, value):
        self._business_time = value
    @property
    def category_final(self):
        return self._category_final

    @category_final.setter
    def category_final(self, value):
        self._category_final = value
    @property
    def category_one(self):
        return self._category_one

    @category_one.setter
    def category_one(self, value):
        self._category_one = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, ShopExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(ShopExtInfo.from_alipay_dict(i))
    @property
    def g_name(self):
        return self._g_name

    @g_name.setter
    def g_name(self, value):
        self._g_name = value
    @property
    def g_shopid(self):
        return self._g_shopid

    @g_shopid.setter
    def g_shopid(self, value):
        self._g_shopid = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def legal_person_card(self):
        return self._legal_person_card

    @legal_person_card.setter
    def legal_person_card(self, value):
        self._legal_person_card = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def shop_albums(self):
        return self._shop_albums

    @shop_albums.setter
    def shop_albums(self, value):
        if isinstance(value, list):
            self._shop_albums = list()
            for i in value:
                if isinstance(i, AlipayTagVO):
                    self._shop_albums.append(i)
                else:
                    self._shop_albums.append(AlipayTagVO.from_alipay_dict(i))
    @property
    def shop_business_status(self):
        return self._shop_business_status

    @shop_business_status.setter
    def shop_business_status(self, value):
        self._shop_business_status = value
    @property
    def shop_videos(self):
        return self._shop_videos

    @shop_videos.setter
    def shop_videos(self, value):
        if isinstance(value, list):
            self._shop_videos = list()
            for i in value:
                self._shop_videos.append(i)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def store_head_pic(self):
        return self._store_head_pic

    @store_head_pic.setter
    def store_head_pic(self, value):
        if isinstance(value, list):
            self._store_head_pic = list()
            for i in value:
                self._store_head_pic.append(i)
    @property
    def store_logo(self):
        return self._store_logo

    @store_logo.setter
    def store_logo(self, value):
        self._store_logo = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.business_time:
            if hasattr(self.business_time, 'to_alipay_dict'):
                params['business_time'] = self.business_time.to_alipay_dict()
            else:
                params['business_time'] = self.business_time
        if self.category_final:
            if hasattr(self.category_final, 'to_alipay_dict'):
                params['category_final'] = self.category_final.to_alipay_dict()
            else:
                params['category_final'] = self.category_final
        if self.category_one:
            if hasattr(self.category_one, 'to_alipay_dict'):
                params['category_one'] = self.category_one.to_alipay_dict()
            else:
                params['category_one'] = self.category_one
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.g_name:
            if hasattr(self.g_name, 'to_alipay_dict'):
                params['g_name'] = self.g_name.to_alipay_dict()
            else:
                params['g_name'] = self.g_name
        if self.g_shopid:
            if hasattr(self.g_shopid, 'to_alipay_dict'):
                params['g_shopid'] = self.g_shopid.to_alipay_dict()
            else:
                params['g_shopid'] = self.g_shopid
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.legal_person_card:
            if hasattr(self.legal_person_card, 'to_alipay_dict'):
                params['legal_person_card'] = self.legal_person_card.to_alipay_dict()
            else:
                params['legal_person_card'] = self.legal_person_card
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.shop_albums:
            if isinstance(self.shop_albums, list):
                for i in range(0, len(self.shop_albums)):
                    element = self.shop_albums[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_albums[i] = element.to_alipay_dict()
            if hasattr(self.shop_albums, 'to_alipay_dict'):
                params['shop_albums'] = self.shop_albums.to_alipay_dict()
            else:
                params['shop_albums'] = self.shop_albums
        if self.shop_business_status:
            if hasattr(self.shop_business_status, 'to_alipay_dict'):
                params['shop_business_status'] = self.shop_business_status.to_alipay_dict()
            else:
                params['shop_business_status'] = self.shop_business_status
        if self.shop_videos:
            if isinstance(self.shop_videos, list):
                for i in range(0, len(self.shop_videos)):
                    element = self.shop_videos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_videos[i] = element.to_alipay_dict()
            if hasattr(self.shop_videos, 'to_alipay_dict'):
                params['shop_videos'] = self.shop_videos.to_alipay_dict()
            else:
                params['shop_videos'] = self.shop_videos
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.store_head_pic:
            if isinstance(self.store_head_pic, list):
                for i in range(0, len(self.store_head_pic)):
                    element = self.store_head_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.store_head_pic[i] = element.to_alipay_dict()
            if hasattr(self.store_head_pic, 'to_alipay_dict'):
                params['store_head_pic'] = self.store_head_pic.to_alipay_dict()
            else:
                params['store_head_pic'] = self.store_head_pic
        if self.store_logo:
            if hasattr(self.store_logo, 'to_alipay_dict'):
                params['store_logo'] = self.store_logo.to_alipay_dict()
            else:
                params['store_logo'] = self.store_logo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDigitalgroupApplyCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'category_final' in d:
            o.category_final = d['category_final']
        if 'category_one' in d:
            o.category_one = d['category_one']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city' in d:
            o.city = d['city']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'district' in d:
            o.district = d['district']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'g_name' in d:
            o.g_name = d['g_name']
        if 'g_shopid' in d:
            o.g_shopid = d['g_shopid']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'legal_person_card' in d:
            o.legal_person_card = d['legal_person_card']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province' in d:
            o.province = d['province']
        if 'shop_albums' in d:
            o.shop_albums = d['shop_albums']
        if 'shop_business_status' in d:
            o.shop_business_status = d['shop_business_status']
        if 'shop_videos' in d:
            o.shop_videos = d['shop_videos']
        if 'status' in d:
            o.status = d['status']
        if 'store_head_pic' in d:
            o.store_head_pic = d['store_head_pic']
        if 'store_logo' in d:
            o.store_logo = d['store_logo']
        return o


