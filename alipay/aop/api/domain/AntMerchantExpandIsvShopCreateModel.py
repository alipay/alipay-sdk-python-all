#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopBusinessTime import ShopBusinessTime


class AntMerchantExpandIsvShopCreateModel(object):

    def __init__(self):
        self._address = None
        self._address_memo = None
        self._attachment_list = None
        self._biz_type = None
        self._business_time = None
        self._campus_id = None
        self._campus_name = None
        self._category_label = None
        self._city_code = None
        self._contact_mobile = None
        self._contact_phone = None
        self._district_code = None
        self._isv_contact_mobile = None
        self._isv_contact_name = None
        self._memo = None
        self._pid = None
        self._province_code = None
        self._qualification_proof_list = None
        self._qualification_proof_type = None
        self._shop_category = None
        self._shop_name = None
        self._shop_type = None
        self._store_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_memo(self):
        return self._address_memo

    @address_memo.setter
    def address_memo(self, value):
        self._address_memo = value
    @property
    def attachment_list(self):
        return self._attachment_list

    @attachment_list.setter
    def attachment_list(self, value):
        self._attachment_list = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
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
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def category_label(self):
        return self._category_label

    @category_label.setter
    def category_label(self, value):
        self._category_label = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
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
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def isv_contact_mobile(self):
        return self._isv_contact_mobile

    @isv_contact_mobile.setter
    def isv_contact_mobile(self, value):
        self._isv_contact_mobile = value
    @property
    def isv_contact_name(self):
        return self._isv_contact_name

    @isv_contact_name.setter
    def isv_contact_name(self, value):
        self._isv_contact_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def qualification_proof_list(self):
        return self._qualification_proof_list

    @qualification_proof_list.setter
    def qualification_proof_list(self, value):
        self._qualification_proof_list = value
    @property
    def qualification_proof_type(self):
        return self._qualification_proof_type

    @qualification_proof_type.setter
    def qualification_proof_type(self, value):
        self._qualification_proof_type = value
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
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_memo:
            if hasattr(self.address_memo, 'to_alipay_dict'):
                params['address_memo'] = self.address_memo.to_alipay_dict()
            else:
                params['address_memo'] = self.address_memo
        if self.attachment_list:
            if hasattr(self.attachment_list, 'to_alipay_dict'):
                params['attachment_list'] = self.attachment_list.to_alipay_dict()
            else:
                params['attachment_list'] = self.attachment_list
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
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
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.category_label:
            if hasattr(self.category_label, 'to_alipay_dict'):
                params['category_label'] = self.category_label.to_alipay_dict()
            else:
                params['category_label'] = self.category_label
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
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
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.isv_contact_mobile:
            if hasattr(self.isv_contact_mobile, 'to_alipay_dict'):
                params['isv_contact_mobile'] = self.isv_contact_mobile.to_alipay_dict()
            else:
                params['isv_contact_mobile'] = self.isv_contact_mobile
        if self.isv_contact_name:
            if hasattr(self.isv_contact_name, 'to_alipay_dict'):
                params['isv_contact_name'] = self.isv_contact_name.to_alipay_dict()
            else:
                params['isv_contact_name'] = self.isv_contact_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.qualification_proof_list:
            if hasattr(self.qualification_proof_list, 'to_alipay_dict'):
                params['qualification_proof_list'] = self.qualification_proof_list.to_alipay_dict()
            else:
                params['qualification_proof_list'] = self.qualification_proof_list
        if self.qualification_proof_type:
            if hasattr(self.qualification_proof_type, 'to_alipay_dict'):
                params['qualification_proof_type'] = self.qualification_proof_type.to_alipay_dict()
            else:
                params['qualification_proof_type'] = self.qualification_proof_type
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
        o = AntMerchantExpandIsvShopCreateModel()
        if 'address' in d:
            o.address = d['address']
        if 'address_memo' in d:
            o.address_memo = d['address_memo']
        if 'attachment_list' in d:
            o.attachment_list = d['attachment_list']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'business_time' in d:
            o.business_time = d['business_time']
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'category_label' in d:
            o.category_label = d['category_label']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'isv_contact_mobile' in d:
            o.isv_contact_mobile = d['isv_contact_mobile']
        if 'isv_contact_name' in d:
            o.isv_contact_name = d['isv_contact_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'pid' in d:
            o.pid = d['pid']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'qualification_proof_list' in d:
            o.qualification_proof_list = d['qualification_proof_list']
        if 'qualification_proof_type' in d:
            o.qualification_proof_type = d['qualification_proof_type']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'store_id' in d:
            o.store_id = d['store_id']
        return o


