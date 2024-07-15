#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ProductProperty import ProductProperty
from alipay.aop.api.domain.LmCategoryVO import LmCategoryVO
from alipay.aop.api.domain.MpcLmSkuVO import MpcLmSkuVO
from alipay.aop.api.domain.ProductProperty import ProductProperty


class AlipayCloudCloudpromoMallItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallItemQueryResponse, self).__init__()
        self._attr = None
        self._brand = None
        self._can_sell = None
        self._category_chain = None
        self._category_id = None
        self._desc_path = None
        self._division_code = None
        self._fuzzy_quantity = None
        self._img_url = None
        self._main_pic = None
        self._mpc_item_id = None
        self._mpc_sku_vo = None
        self._product_properties = None
        self._product_status = None
        self._product_type = None
        self._shop_id = None
        self._sold_quantity = None
        self._tax_code = None
        self._tax_rate = None
        self._title = None

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, value):
        if isinstance(value, list):
            self._attr = list()
            for i in value:
                if isinstance(i, ProductProperty):
                    self._attr.append(i)
                else:
                    self._attr.append(ProductProperty.from_alipay_dict(i))
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def can_sell(self):
        return self._can_sell

    @can_sell.setter
    def can_sell(self, value):
        self._can_sell = value
    @property
    def category_chain(self):
        return self._category_chain

    @category_chain.setter
    def category_chain(self, value):
        if isinstance(value, list):
            self._category_chain = list()
            for i in value:
                if isinstance(i, LmCategoryVO):
                    self._category_chain.append(i)
                else:
                    self._category_chain.append(LmCategoryVO.from_alipay_dict(i))
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def desc_path(self):
        return self._desc_path

    @desc_path.setter
    def desc_path(self, value):
        self._desc_path = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def fuzzy_quantity(self):
        return self._fuzzy_quantity

    @fuzzy_quantity.setter
    def fuzzy_quantity(self, value):
        self._fuzzy_quantity = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def main_pic(self):
        return self._main_pic

    @main_pic.setter
    def main_pic(self, value):
        self._main_pic = value
    @property
    def mpc_item_id(self):
        return self._mpc_item_id

    @mpc_item_id.setter
    def mpc_item_id(self, value):
        self._mpc_item_id = value
    @property
    def mpc_sku_vo(self):
        return self._mpc_sku_vo

    @mpc_sku_vo.setter
    def mpc_sku_vo(self, value):
        if isinstance(value, list):
            self._mpc_sku_vo = list()
            for i in value:
                if isinstance(i, MpcLmSkuVO):
                    self._mpc_sku_vo.append(i)
                else:
                    self._mpc_sku_vo.append(MpcLmSkuVO.from_alipay_dict(i))
    @property
    def product_properties(self):
        return self._product_properties

    @product_properties.setter
    def product_properties(self, value):
        if isinstance(value, list):
            self._product_properties = list()
            for i in value:
                if isinstance(i, ProductProperty):
                    self._product_properties.append(i)
                else:
                    self._product_properties.append(ProductProperty.from_alipay_dict(i))
    @property
    def product_status(self):
        return self._product_status

    @product_status.setter
    def product_status(self, value):
        self._product_status = value
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
    def sold_quantity(self):
        return self._sold_quantity

    @sold_quantity.setter
    def sold_quantity(self, value):
        self._sold_quantity = value
    @property
    def tax_code(self):
        return self._tax_code

    @tax_code.setter
    def tax_code(self, value):
        self._tax_code = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallItemQueryResponse, self).parse_response_content(response_content)
        if 'attr' in response:
            self.attr = response['attr']
        if 'brand' in response:
            self.brand = response['brand']
        if 'can_sell' in response:
            self.can_sell = response['can_sell']
        if 'category_chain' in response:
            self.category_chain = response['category_chain']
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'desc_path' in response:
            self.desc_path = response['desc_path']
        if 'division_code' in response:
            self.division_code = response['division_code']
        if 'fuzzy_quantity' in response:
            self.fuzzy_quantity = response['fuzzy_quantity']
        if 'img_url' in response:
            self.img_url = response['img_url']
        if 'main_pic' in response:
            self.main_pic = response['main_pic']
        if 'mpc_item_id' in response:
            self.mpc_item_id = response['mpc_item_id']
        if 'mpc_sku_vo' in response:
            self.mpc_sku_vo = response['mpc_sku_vo']
        if 'product_properties' in response:
            self.product_properties = response['product_properties']
        if 'product_status' in response:
            self.product_status = response['product_status']
        if 'product_type' in response:
            self.product_type = response['product_type']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'sold_quantity' in response:
            self.sold_quantity = response['sold_quantity']
        if 'tax_code' in response:
            self.tax_code = response['tax_code']
        if 'tax_rate' in response:
            self.tax_rate = response['tax_rate']
        if 'title' in response:
            self.title = response['title']
