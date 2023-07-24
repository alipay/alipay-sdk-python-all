#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PunchoutAccessProductAttrValueDto import PunchoutAccessProductAttrValueDto


class PunchoutAccessProductDTO(object):

    def __init__(self):
        self._brand_id = None
        self._brand_name = None
        self._buyer_work_no = None
        self._catalog_category_id = None
        self._category_code = None
        self._category_id = None
        self._category_use_id = None
        self._data_source = None
        self._front_category_id = None
        self._img_storage_type = None
        self._img_url_list = None
        self._mall_url = None
        self._order_type = None
        self._product_attr_value_list = None
        self._product_desc = None
        self._product_name = None
        self._purchase_channel = None
        self._recommendation = None
        self._source_category_id = None
        self._source_category_name = None
        self._source_info = None
        self._source_type = None
        self._source_value = None
        self._tenant_id = None
        self._unit = None

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
    def buyer_work_no(self):
        return self._buyer_work_no

    @buyer_work_no.setter
    def buyer_work_no(self, value):
        self._buyer_work_no = value
    @property
    def catalog_category_id(self):
        return self._catalog_category_id

    @catalog_category_id.setter
    def catalog_category_id(self, value):
        self._catalog_category_id = value
    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_use_id(self):
        return self._category_use_id

    @category_use_id.setter
    def category_use_id(self, value):
        self._category_use_id = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def front_category_id(self):
        return self._front_category_id

    @front_category_id.setter
    def front_category_id(self, value):
        self._front_category_id = value
    @property
    def img_storage_type(self):
        return self._img_storage_type

    @img_storage_type.setter
    def img_storage_type(self, value):
        self._img_storage_type = value
    @property
    def img_url_list(self):
        return self._img_url_list

    @img_url_list.setter
    def img_url_list(self, value):
        if isinstance(value, list):
            self._img_url_list = list()
            for i in value:
                self._img_url_list.append(i)
    @property
    def mall_url(self):
        return self._mall_url

    @mall_url.setter
    def mall_url(self, value):
        self._mall_url = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def product_attr_value_list(self):
        return self._product_attr_value_list

    @product_attr_value_list.setter
    def product_attr_value_list(self, value):
        if isinstance(value, list):
            self._product_attr_value_list = list()
            for i in value:
                if isinstance(i, PunchoutAccessProductAttrValueDto):
                    self._product_attr_value_list.append(i)
                else:
                    self._product_attr_value_list.append(PunchoutAccessProductAttrValueDto.from_alipay_dict(i))
    @property
    def product_desc(self):
        return self._product_desc

    @product_desc.setter
    def product_desc(self, value):
        self._product_desc = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def purchase_channel(self):
        return self._purchase_channel

    @purchase_channel.setter
    def purchase_channel(self, value):
        self._purchase_channel = value
    @property
    def recommendation(self):
        return self._recommendation

    @recommendation.setter
    def recommendation(self, value):
        self._recommendation = value
    @property
    def source_category_id(self):
        return self._source_category_id

    @source_category_id.setter
    def source_category_id(self, value):
        self._source_category_id = value
    @property
    def source_category_name(self):
        return self._source_category_name

    @source_category_name.setter
    def source_category_name(self, value):
        self._source_category_name = value
    @property
    def source_info(self):
        return self._source_info

    @source_info.setter
    def source_info(self, value):
        self._source_info = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def source_value(self):
        return self._source_value

    @source_value.setter
    def source_value(self, value):
        self._source_value = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.buyer_work_no:
            if hasattr(self.buyer_work_no, 'to_alipay_dict'):
                params['buyer_work_no'] = self.buyer_work_no.to_alipay_dict()
            else:
                params['buyer_work_no'] = self.buyer_work_no
        if self.catalog_category_id:
            if hasattr(self.catalog_category_id, 'to_alipay_dict'):
                params['catalog_category_id'] = self.catalog_category_id.to_alipay_dict()
            else:
                params['catalog_category_id'] = self.catalog_category_id
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_use_id:
            if hasattr(self.category_use_id, 'to_alipay_dict'):
                params['category_use_id'] = self.category_use_id.to_alipay_dict()
            else:
                params['category_use_id'] = self.category_use_id
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.front_category_id:
            if hasattr(self.front_category_id, 'to_alipay_dict'):
                params['front_category_id'] = self.front_category_id.to_alipay_dict()
            else:
                params['front_category_id'] = self.front_category_id
        if self.img_storage_type:
            if hasattr(self.img_storage_type, 'to_alipay_dict'):
                params['img_storage_type'] = self.img_storage_type.to_alipay_dict()
            else:
                params['img_storage_type'] = self.img_storage_type
        if self.img_url_list:
            if isinstance(self.img_url_list, list):
                for i in range(0, len(self.img_url_list)):
                    element = self.img_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.img_url_list[i] = element.to_alipay_dict()
            if hasattr(self.img_url_list, 'to_alipay_dict'):
                params['img_url_list'] = self.img_url_list.to_alipay_dict()
            else:
                params['img_url_list'] = self.img_url_list
        if self.mall_url:
            if hasattr(self.mall_url, 'to_alipay_dict'):
                params['mall_url'] = self.mall_url.to_alipay_dict()
            else:
                params['mall_url'] = self.mall_url
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.product_attr_value_list:
            if isinstance(self.product_attr_value_list, list):
                for i in range(0, len(self.product_attr_value_list)):
                    element = self.product_attr_value_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_attr_value_list[i] = element.to_alipay_dict()
            if hasattr(self.product_attr_value_list, 'to_alipay_dict'):
                params['product_attr_value_list'] = self.product_attr_value_list.to_alipay_dict()
            else:
                params['product_attr_value_list'] = self.product_attr_value_list
        if self.product_desc:
            if hasattr(self.product_desc, 'to_alipay_dict'):
                params['product_desc'] = self.product_desc.to_alipay_dict()
            else:
                params['product_desc'] = self.product_desc
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.purchase_channel:
            if hasattr(self.purchase_channel, 'to_alipay_dict'):
                params['purchase_channel'] = self.purchase_channel.to_alipay_dict()
            else:
                params['purchase_channel'] = self.purchase_channel
        if self.recommendation:
            if hasattr(self.recommendation, 'to_alipay_dict'):
                params['recommendation'] = self.recommendation.to_alipay_dict()
            else:
                params['recommendation'] = self.recommendation
        if self.source_category_id:
            if hasattr(self.source_category_id, 'to_alipay_dict'):
                params['source_category_id'] = self.source_category_id.to_alipay_dict()
            else:
                params['source_category_id'] = self.source_category_id
        if self.source_category_name:
            if hasattr(self.source_category_name, 'to_alipay_dict'):
                params['source_category_name'] = self.source_category_name.to_alipay_dict()
            else:
                params['source_category_name'] = self.source_category_name
        if self.source_info:
            if hasattr(self.source_info, 'to_alipay_dict'):
                params['source_info'] = self.source_info.to_alipay_dict()
            else:
                params['source_info'] = self.source_info
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.source_value:
            if hasattr(self.source_value, 'to_alipay_dict'):
                params['source_value'] = self.source_value.to_alipay_dict()
            else:
                params['source_value'] = self.source_value
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PunchoutAccessProductDTO()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'buyer_work_no' in d:
            o.buyer_work_no = d['buyer_work_no']
        if 'catalog_category_id' in d:
            o.catalog_category_id = d['catalog_category_id']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_use_id' in d:
            o.category_use_id = d['category_use_id']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'front_category_id' in d:
            o.front_category_id = d['front_category_id']
        if 'img_storage_type' in d:
            o.img_storage_type = d['img_storage_type']
        if 'img_url_list' in d:
            o.img_url_list = d['img_url_list']
        if 'mall_url' in d:
            o.mall_url = d['mall_url']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'product_attr_value_list' in d:
            o.product_attr_value_list = d['product_attr_value_list']
        if 'product_desc' in d:
            o.product_desc = d['product_desc']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'purchase_channel' in d:
            o.purchase_channel = d['purchase_channel']
        if 'recommendation' in d:
            o.recommendation = d['recommendation']
        if 'source_category_id' in d:
            o.source_category_id = d['source_category_id']
        if 'source_category_name' in d:
            o.source_category_name = d['source_category_name']
        if 'source_info' in d:
            o.source_info = d['source_info']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'source_value' in d:
            o.source_value = d['source_value']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'unit' in d:
            o.unit = d['unit']
        return o


