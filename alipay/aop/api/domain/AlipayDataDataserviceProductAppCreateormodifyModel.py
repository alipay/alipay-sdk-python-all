#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemAttrDto import ItemAttrDto
from alipay.aop.api.domain.ItemCategoryDto import ItemCategoryDto
from alipay.aop.api.domain.ItemDescInfoDto import ItemDescInfoDto
from alipay.aop.api.domain.LandingTypeDto import LandingTypeDto
from alipay.aop.api.domain.SellsInfo import SellsInfo
from alipay.aop.api.domain.ItemSkuDto import ItemSkuDto


class AlipayDataDataserviceProductAppCreateormodifyModel(object):

    def __init__(self):
        self._attrs = None
        self._barcode = None
        self._biz_token = None
        self._category = None
        self._desc = None
        self._desc_info = None
        self._direct_path = None
        self._entity_type = None
        self._head_img = None
        self._image_list = None
        self._item_sub_type = None
        self._landing = None
        self._original_price = None
        self._out_item_id = None
        self._out_source = None
        self._owner_oid = None
        self._owner_pid = None
        self._path = None
        self._price_unit = None
        self._principal_tag = None
        self._prod_app_id = None
        self._sale_price = None
        self._sale_status = None
        self._sells_info = None
        self._skus = None
        self._stock_num = None
        self._title = None

    @property
    def attrs(self):
        return self._attrs

    @attrs.setter
    def attrs(self, value):
        if isinstance(value, list):
            self._attrs = list()
            for i in value:
                if isinstance(i, ItemAttrDto):
                    self._attrs.append(i)
                else:
                    self._attrs.append(ItemAttrDto.from_alipay_dict(i))
    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, ItemCategoryDto):
            self._category = value
        else:
            self._category = ItemCategoryDto.from_alipay_dict(value)
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def desc_info(self):
        return self._desc_info

    @desc_info.setter
    def desc_info(self, value):
        if isinstance(value, ItemDescInfoDto):
            self._desc_info = value
        else:
            self._desc_info = ItemDescInfoDto.from_alipay_dict(value)
    @property
    def direct_path(self):
        return self._direct_path

    @direct_path.setter
    def direct_path(self, value):
        self._direct_path = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def head_img(self):
        return self._head_img

    @head_img.setter
    def head_img(self, value):
        self._head_img = value
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def item_sub_type(self):
        return self._item_sub_type

    @item_sub_type.setter
    def item_sub_type(self, value):
        self._item_sub_type = value
    @property
    def landing(self):
        return self._landing

    @landing.setter
    def landing(self, value):
        if isinstance(value, list):
            self._landing = list()
            for i in value:
                if isinstance(i, LandingTypeDto):
                    self._landing.append(i)
                else:
                    self._landing.append(LandingTypeDto.from_alipay_dict(i))
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def out_source(self):
        return self._out_source

    @out_source.setter
    def out_source(self, value):
        self._out_source = value
    @property
    def owner_oid(self):
        return self._owner_oid

    @owner_oid.setter
    def owner_oid(self, value):
        self._owner_oid = value
    @property
    def owner_pid(self):
        return self._owner_pid

    @owner_pid.setter
    def owner_pid(self, value):
        self._owner_pid = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def prod_app_id(self):
        return self._prod_app_id

    @prod_app_id.setter
    def prod_app_id(self, value):
        self._prod_app_id = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def sale_status(self):
        return self._sale_status

    @sale_status.setter
    def sale_status(self, value):
        self._sale_status = value
    @property
    def sells_info(self):
        return self._sells_info

    @sells_info.setter
    def sells_info(self, value):
        if isinstance(value, SellsInfo):
            self._sells_info = value
        else:
            self._sells_info = SellsInfo.from_alipay_dict(value)
    @property
    def skus(self):
        return self._skus

    @skus.setter
    def skus(self, value):
        if isinstance(value, list):
            self._skus = list()
            for i in value:
                if isinstance(i, ItemSkuDto):
                    self._skus.append(i)
                else:
                    self._skus.append(ItemSkuDto.from_alipay_dict(i))
    @property
    def stock_num(self):
        return self._stock_num

    @stock_num.setter
    def stock_num(self, value):
        self._stock_num = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.attrs:
            if isinstance(self.attrs, list):
                for i in range(0, len(self.attrs)):
                    element = self.attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attrs[i] = element.to_alipay_dict()
            if hasattr(self.attrs, 'to_alipay_dict'):
                params['attrs'] = self.attrs.to_alipay_dict()
            else:
                params['attrs'] = self.attrs
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.desc_info:
            if hasattr(self.desc_info, 'to_alipay_dict'):
                params['desc_info'] = self.desc_info.to_alipay_dict()
            else:
                params['desc_info'] = self.desc_info
        if self.direct_path:
            if hasattr(self.direct_path, 'to_alipay_dict'):
                params['direct_path'] = self.direct_path.to_alipay_dict()
            else:
                params['direct_path'] = self.direct_path
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.head_img:
            if hasattr(self.head_img, 'to_alipay_dict'):
                params['head_img'] = self.head_img.to_alipay_dict()
            else:
                params['head_img'] = self.head_img
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.item_sub_type:
            if hasattr(self.item_sub_type, 'to_alipay_dict'):
                params['item_sub_type'] = self.item_sub_type.to_alipay_dict()
            else:
                params['item_sub_type'] = self.item_sub_type
        if self.landing:
            if isinstance(self.landing, list):
                for i in range(0, len(self.landing)):
                    element = self.landing[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.landing[i] = element.to_alipay_dict()
            if hasattr(self.landing, 'to_alipay_dict'):
                params['landing'] = self.landing.to_alipay_dict()
            else:
                params['landing'] = self.landing
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.out_source:
            if hasattr(self.out_source, 'to_alipay_dict'):
                params['out_source'] = self.out_source.to_alipay_dict()
            else:
                params['out_source'] = self.out_source
        if self.owner_oid:
            if hasattr(self.owner_oid, 'to_alipay_dict'):
                params['owner_oid'] = self.owner_oid.to_alipay_dict()
            else:
                params['owner_oid'] = self.owner_oid
        if self.owner_pid:
            if hasattr(self.owner_pid, 'to_alipay_dict'):
                params['owner_pid'] = self.owner_pid.to_alipay_dict()
            else:
                params['owner_pid'] = self.owner_pid
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.prod_app_id:
            if hasattr(self.prod_app_id, 'to_alipay_dict'):
                params['prod_app_id'] = self.prod_app_id.to_alipay_dict()
            else:
                params['prod_app_id'] = self.prod_app_id
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.sale_status:
            if hasattr(self.sale_status, 'to_alipay_dict'):
                params['sale_status'] = self.sale_status.to_alipay_dict()
            else:
                params['sale_status'] = self.sale_status
        if self.sells_info:
            if hasattr(self.sells_info, 'to_alipay_dict'):
                params['sells_info'] = self.sells_info.to_alipay_dict()
            else:
                params['sells_info'] = self.sells_info
        if self.skus:
            if isinstance(self.skus, list):
                for i in range(0, len(self.skus)):
                    element = self.skus[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skus[i] = element.to_alipay_dict()
            if hasattr(self.skus, 'to_alipay_dict'):
                params['skus'] = self.skus.to_alipay_dict()
            else:
                params['skus'] = self.skus
        if self.stock_num:
            if hasattr(self.stock_num, 'to_alipay_dict'):
                params['stock_num'] = self.stock_num.to_alipay_dict()
            else:
                params['stock_num'] = self.stock_num
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceProductAppCreateormodifyModel()
        if 'attrs' in d:
            o.attrs = d['attrs']
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'category' in d:
            o.category = d['category']
        if 'desc' in d:
            o.desc = d['desc']
        if 'desc_info' in d:
            o.desc_info = d['desc_info']
        if 'direct_path' in d:
            o.direct_path = d['direct_path']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'head_img' in d:
            o.head_img = d['head_img']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'item_sub_type' in d:
            o.item_sub_type = d['item_sub_type']
        if 'landing' in d:
            o.landing = d['landing']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'out_source' in d:
            o.out_source = d['out_source']
        if 'owner_oid' in d:
            o.owner_oid = d['owner_oid']
        if 'owner_pid' in d:
            o.owner_pid = d['owner_pid']
        if 'path' in d:
            o.path = d['path']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'prod_app_id' in d:
            o.prod_app_id = d['prod_app_id']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'sale_status' in d:
            o.sale_status = d['sale_status']
        if 'sells_info' in d:
            o.sells_info = d['sells_info']
        if 'skus' in d:
            o.skus = d['skus']
        if 'stock_num' in d:
            o.stock_num = d['stock_num']
        if 'title' in d:
            o.title = d['title']
        return o


