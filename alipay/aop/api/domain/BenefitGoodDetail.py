#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyValueMap import KeyValueMap


class BenefitGoodDetail(object):

    def __init__(self):
        self._alipay_product_id = None
        self._category_id = None
        self._category_name = None
        self._detail_url = None
        self._expiration_date = None
        self._ext_info = None
        self._last_modified = None
        self._main_image = None
        self._original_price = None
        self._out_product_id = None
        self._out_product_status = None
        self._pid = None
        self._prescription_drug = None
        self._product_brand = None
        self._product_code = None
        self._product_desc = None
        self._product_feature = None
        self._product_name = None
        self._product_origin = None
        self._product_spec = None
        self._product_type = None
        self._shop_id = None
        self._source_channel = None
        self._sub_images = None
        self._sub_title = None
        self._suitable_crowd = None

    @property
    def alipay_product_id(self):
        return self._alipay_product_id

    @alipay_product_id.setter
    def alipay_product_id(self, value):
        self._alipay_product_id = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, KeyValueMap):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(KeyValueMap.from_alipay_dict(i))
    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value
    @property
    def main_image(self):
        return self._main_image

    @main_image.setter
    def main_image(self, value):
        self._main_image = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_product_id(self):
        return self._out_product_id

    @out_product_id.setter
    def out_product_id(self, value):
        self._out_product_id = value
    @property
    def out_product_status(self):
        return self._out_product_status

    @out_product_status.setter
    def out_product_status(self, value):
        self._out_product_status = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def prescription_drug(self):
        return self._prescription_drug

    @prescription_drug.setter
    def prescription_drug(self, value):
        self._prescription_drug = value
    @property
    def product_brand(self):
        return self._product_brand

    @product_brand.setter
    def product_brand(self, value):
        self._product_brand = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def product_feature(self):
        return self._product_feature

    @product_feature.setter
    def product_feature(self, value):
        self._product_feature = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_origin(self):
        return self._product_origin

    @product_origin.setter
    def product_origin(self, value):
        self._product_origin = value
    @property
    def product_spec(self):
        return self._product_spec

    @product_spec.setter
    def product_spec(self, value):
        self._product_spec = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def sub_images(self):
        return self._sub_images

    @sub_images.setter
    def sub_images(self, value):
        if isinstance(value, list):
            self._sub_images = list()
            for i in value:
                self._sub_images.append(i)
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def suitable_crowd(self):
        return self._suitable_crowd

    @suitable_crowd.setter
    def suitable_crowd(self, value):
        self._suitable_crowd = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_product_id:
            if hasattr(self.alipay_product_id, 'to_alipay_dict'):
                params['alipay_product_id'] = self.alipay_product_id.to_alipay_dict()
            else:
                params['alipay_product_id'] = self.alipay_product_id
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.expiration_date:
            if hasattr(self.expiration_date, 'to_alipay_dict'):
                params['expiration_date'] = self.expiration_date.to_alipay_dict()
            else:
                params['expiration_date'] = self.expiration_date
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
        if self.last_modified:
            if hasattr(self.last_modified, 'to_alipay_dict'):
                params['last_modified'] = self.last_modified.to_alipay_dict()
            else:
                params['last_modified'] = self.last_modified
        if self.main_image:
            if hasattr(self.main_image, 'to_alipay_dict'):
                params['main_image'] = self.main_image.to_alipay_dict()
            else:
                params['main_image'] = self.main_image
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_product_id:
            if hasattr(self.out_product_id, 'to_alipay_dict'):
                params['out_product_id'] = self.out_product_id.to_alipay_dict()
            else:
                params['out_product_id'] = self.out_product_id
        if self.out_product_status:
            if hasattr(self.out_product_status, 'to_alipay_dict'):
                params['out_product_status'] = self.out_product_status.to_alipay_dict()
            else:
                params['out_product_status'] = self.out_product_status
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.prescription_drug:
            if hasattr(self.prescription_drug, 'to_alipay_dict'):
                params['prescription_drug'] = self.prescription_drug.to_alipay_dict()
            else:
                params['prescription_drug'] = self.prescription_drug
        if self.product_brand:
            if hasattr(self.product_brand, 'to_alipay_dict'):
                params['product_brand'] = self.product_brand.to_alipay_dict()
            else:
                params['product_brand'] = self.product_brand
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.product_feature:
            if hasattr(self.product_feature, 'to_alipay_dict'):
                params['product_feature'] = self.product_feature.to_alipay_dict()
            else:
                params['product_feature'] = self.product_feature
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.product_origin:
            if hasattr(self.product_origin, 'to_alipay_dict'):
                params['product_origin'] = self.product_origin.to_alipay_dict()
            else:
                params['product_origin'] = self.product_origin
        if self.product_spec:
            if hasattr(self.product_spec, 'to_alipay_dict'):
                params['product_spec'] = self.product_spec.to_alipay_dict()
            else:
                params['product_spec'] = self.product_spec
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.sub_images:
            if isinstance(self.sub_images, list):
                for i in range(0, len(self.sub_images)):
                    element = self.sub_images[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_images[i] = element.to_alipay_dict()
            if hasattr(self.sub_images, 'to_alipay_dict'):
                params['sub_images'] = self.sub_images.to_alipay_dict()
            else:
                params['sub_images'] = self.sub_images
        if self.sub_title:
            if hasattr(self.sub_title, 'to_alipay_dict'):
                params['sub_title'] = self.sub_title.to_alipay_dict()
            else:
                params['sub_title'] = self.sub_title
        if self.suitable_crowd:
            if hasattr(self.suitable_crowd, 'to_alipay_dict'):
                params['suitable_crowd'] = self.suitable_crowd.to_alipay_dict()
            else:
                params['suitable_crowd'] = self.suitable_crowd
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitGoodDetail()
        if 'alipay_product_id' in d:
            o.alipay_product_id = d['alipay_product_id']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'expiration_date' in d:
            o.expiration_date = d['expiration_date']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'last_modified' in d:
            o.last_modified = d['last_modified']
        if 'main_image' in d:
            o.main_image = d['main_image']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_product_id' in d:
            o.out_product_id = d['out_product_id']
        if 'out_product_status' in d:
            o.out_product_status = d['out_product_status']
        if 'pid' in d:
            o.pid = d['pid']
        if 'prescription_drug' in d:
            o.prescription_drug = d['prescription_drug']
        if 'product_brand' in d:
            o.product_brand = d['product_brand']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_feature' in d:
            o.product_feature = d['product_feature']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'product_origin' in d:
            o.product_origin = d['product_origin']
        if 'product_spec' in d:
            o.product_spec = d['product_spec']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'sub_images' in d:
            o.sub_images = d['sub_images']
        if 'sub_title' in d:
            o.sub_title = d['sub_title']
        if 'suitable_crowd' in d:
            o.suitable_crowd = d['suitable_crowd']
        return o


