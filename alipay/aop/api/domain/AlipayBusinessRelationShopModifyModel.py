#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessRelationShopAddresss import BusinessRelationShopAddresss
from alipay.aop.api.domain.BusinessRelationExtInfo import BusinessRelationExtInfo


class AlipayBusinessRelationShopModifyModel(object):

    def __init__(self):
        self._business_address = None
        self._cert_image = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._contact_mobile = None
        self._contact_phone = None
        self._ext_infos = None
        self._group_id = None
        self._group_sub_type = None
        self._group_type = None
        self._out_door_images = None
        self._real_shop_id = None
        self._real_shop_logo = None
        self._real_shop_no = None
        self._shop_category = None
        self._shop_name = None

    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        if isinstance(value, list):
            self._business_address = list()
            for i in value:
                if isinstance(i, BusinessRelationShopAddresss):
                    self._business_address.append(i)
                else:
                    self._business_address.append(BusinessRelationShopAddresss.from_alipay_dict(i))
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
                if isinstance(i, BusinessRelationExtInfo):
                    self._ext_infos.append(i)
                else:
                    self._ext_infos.append(BusinessRelationExtInfo.from_alipay_dict(i))
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_sub_type(self):
        return self._group_sub_type

    @group_sub_type.setter
    def group_sub_type(self, value):
        self._group_sub_type = value
    @property
    def group_type(self):
        return self._group_type

    @group_type.setter
    def group_type(self, value):
        self._group_type = value
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
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value
    @property
    def real_shop_logo(self):
        return self._real_shop_logo

    @real_shop_logo.setter
    def real_shop_logo(self, value):
        self._real_shop_logo = value
    @property
    def real_shop_no(self):
        return self._real_shop_no

    @real_shop_no.setter
    def real_shop_no(self, value):
        self._real_shop_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.business_address:
            if isinstance(self.business_address, list):
                for i in range(0, len(self.business_address)):
                    element = self.business_address[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_address[i] = element.to_alipay_dict()
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
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
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_sub_type:
            if hasattr(self.group_sub_type, 'to_alipay_dict'):
                params['group_sub_type'] = self.group_sub_type.to_alipay_dict()
            else:
                params['group_sub_type'] = self.group_sub_type
        if self.group_type:
            if hasattr(self.group_type, 'to_alipay_dict'):
                params['group_type'] = self.group_type.to_alipay_dict()
            else:
                params['group_type'] = self.group_type
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
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        if self.real_shop_logo:
            if hasattr(self.real_shop_logo, 'to_alipay_dict'):
                params['real_shop_logo'] = self.real_shop_logo.to_alipay_dict()
            else:
                params['real_shop_logo'] = self.real_shop_logo
        if self.real_shop_no:
            if hasattr(self.real_shop_no, 'to_alipay_dict'):
                params['real_shop_no'] = self.real_shop_no.to_alipay_dict()
            else:
                params['real_shop_no'] = self.real_shop_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessRelationShopModifyModel()
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'cert_image' in d:
            o.cert_image = d['cert_image']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_sub_type' in d:
            o.group_sub_type = d['group_sub_type']
        if 'group_type' in d:
            o.group_type = d['group_type']
        if 'out_door_images' in d:
            o.out_door_images = d['out_door_images']
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        if 'real_shop_logo' in d:
            o.real_shop_logo = d['real_shop_logo']
        if 'real_shop_no' in d:
            o.real_shop_no = d['real_shop_no']
        if 'shop_category' in d:
            o.shop_category = d['shop_category']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


