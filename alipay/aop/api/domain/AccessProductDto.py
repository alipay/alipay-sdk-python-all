#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AccessProductAttrValueDto import AccessProductAttrValueDto


class AccessProductDto(object):

    def __init__(self):
        self._buyer_work_no = None
        self._catalog_category_id = None
        self._category_code = None
        self._data_source = None
        self._img_url_list = None
        self._leading_pur_org = None
        self._mall_url = None
        self._order_type = None
        self._product_attr_value_list = None
        self._product_desc = None
        self._product_name = None
        self._purchase_channel = None
        self._recommendation = None
        self._source_category_id = None
        self._source_category_name = None
        self._source_type = None
        self._source_value = None
        self._unit = None

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
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
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
    def leading_pur_org(self):
        return self._leading_pur_org

    @leading_pur_org.setter
    def leading_pur_org(self, value):
        if isinstance(value, list):
            self._leading_pur_org = list()
            for i in value:
                self._leading_pur_org.append(i)
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
                if isinstance(i, AccessProductAttrValueDto):
                    self._product_attr_value_list.append(i)
                else:
                    self._product_attr_value_list.append(AccessProductAttrValueDto.from_alipay_dict(i))
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
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
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
        if self.leading_pur_org:
            if isinstance(self.leading_pur_org, list):
                for i in range(0, len(self.leading_pur_org)):
                    element = self.leading_pur_org[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.leading_pur_org[i] = element.to_alipay_dict()
            if hasattr(self.leading_pur_org, 'to_alipay_dict'):
                params['leading_pur_org'] = self.leading_pur_org.to_alipay_dict()
            else:
                params['leading_pur_org'] = self.leading_pur_org
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
        o = AccessProductDto()
        if 'buyer_work_no' in d:
            o.buyer_work_no = d['buyer_work_no']
        if 'catalog_category_id' in d:
            o.catalog_category_id = d['catalog_category_id']
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'img_url_list' in d:
            o.img_url_list = d['img_url_list']
        if 'leading_pur_org' in d:
            o.leading_pur_org = d['leading_pur_org']
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
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'source_value' in d:
            o.source_value = d['source_value']
        if 'unit' in d:
            o.unit = d['unit']
        return o


