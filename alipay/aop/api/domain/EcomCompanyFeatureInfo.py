#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnchorInfo import AnchorInfo
from alipay.aop.api.domain.SaleFeatureInfo import SaleFeatureInfo
from alipay.aop.api.domain.ShopRatingInfo import ShopRatingInfo
from alipay.aop.api.domain.ProductDetailInfo import ProductDetailInfo
from alipay.aop.api.domain.ProductDetailInfo import ProductDetailInfo


class EcomCompanyFeatureInfo(object):

    def __init__(self):
        self._active_month_past_year = None
        self._active_shop_num = None
        self._anchor_list = None
        self._anchor_num = None
        self._business_list = None
        self._closed_shop_num = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._last_open_date_duration = None
        self._main_business = None
        self._off_shelf_num = None
        self._on_sale_brand_list = None
        self._on_sale_brand_num = None
        self._on_sale_item_num = None
        self._open_date_duration = None
        self._operation_shop_num = None
        self._person_name = None
        self._platform_list = None
        self._platform_num = None
        self._platform_past_year = None
        self._reg_city = None
        self._reg_county = None
        self._reg_duration = None
        self._reg_no = None
        self._reg_province = None
        self._sale_details = None
        self._sell_out_item_num = None
        self._shop_num_past_year = None
        self._shop_rating_list = None
        self._standard_amt_top_10_products = None
        self._standard_volume_top_10_products = None
        self._uscc = None

    @property
    def active_month_past_year(self):
        return self._active_month_past_year

    @active_month_past_year.setter
    def active_month_past_year(self, value):
        self._active_month_past_year = value
    @property
    def active_shop_num(self):
        return self._active_shop_num

    @active_shop_num.setter
    def active_shop_num(self, value):
        self._active_shop_num = value
    @property
    def anchor_list(self):
        return self._anchor_list

    @anchor_list.setter
    def anchor_list(self, value):
        if isinstance(value, list):
            self._anchor_list = list()
            for i in value:
                if isinstance(i, AnchorInfo):
                    self._anchor_list.append(i)
                else:
                    self._anchor_list.append(AnchorInfo.from_alipay_dict(i))
    @property
    def anchor_num(self):
        return self._anchor_num

    @anchor_num.setter
    def anchor_num(self, value):
        self._anchor_num = value
    @property
    def business_list(self):
        return self._business_list

    @business_list.setter
    def business_list(self, value):
        if isinstance(value, list):
            self._business_list = list()
            for i in value:
                self._business_list.append(i)
    @property
    def closed_shop_num(self):
        return self._closed_shop_num

    @closed_shop_num.setter
    def closed_shop_num(self, value):
        self._closed_shop_num = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def ent_status(self):
        return self._ent_status

    @ent_status.setter
    def ent_status(self, value):
        self._ent_status = value
    @property
    def ent_type(self):
        return self._ent_type

    @ent_type.setter
    def ent_type(self, value):
        self._ent_type = value
    @property
    def last_open_date_duration(self):
        return self._last_open_date_duration

    @last_open_date_duration.setter
    def last_open_date_duration(self, value):
        self._last_open_date_duration = value
    @property
    def main_business(self):
        return self._main_business

    @main_business.setter
    def main_business(self, value):
        self._main_business = value
    @property
    def off_shelf_num(self):
        return self._off_shelf_num

    @off_shelf_num.setter
    def off_shelf_num(self, value):
        self._off_shelf_num = value
    @property
    def on_sale_brand_list(self):
        return self._on_sale_brand_list

    @on_sale_brand_list.setter
    def on_sale_brand_list(self, value):
        if isinstance(value, list):
            self._on_sale_brand_list = list()
            for i in value:
                self._on_sale_brand_list.append(i)
    @property
    def on_sale_brand_num(self):
        return self._on_sale_brand_num

    @on_sale_brand_num.setter
    def on_sale_brand_num(self, value):
        self._on_sale_brand_num = value
    @property
    def on_sale_item_num(self):
        return self._on_sale_item_num

    @on_sale_item_num.setter
    def on_sale_item_num(self, value):
        self._on_sale_item_num = value
    @property
    def open_date_duration(self):
        return self._open_date_duration

    @open_date_duration.setter
    def open_date_duration(self, value):
        self._open_date_duration = value
    @property
    def operation_shop_num(self):
        return self._operation_shop_num

    @operation_shop_num.setter
    def operation_shop_num(self, value):
        self._operation_shop_num = value
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value
    @property
    def platform_list(self):
        return self._platform_list

    @platform_list.setter
    def platform_list(self, value):
        if isinstance(value, list):
            self._platform_list = list()
            for i in value:
                self._platform_list.append(i)
    @property
    def platform_num(self):
        return self._platform_num

    @platform_num.setter
    def platform_num(self, value):
        self._platform_num = value
    @property
    def platform_past_year(self):
        return self._platform_past_year

    @platform_past_year.setter
    def platform_past_year(self, value):
        self._platform_past_year = value
    @property
    def reg_city(self):
        return self._reg_city

    @reg_city.setter
    def reg_city(self, value):
        self._reg_city = value
    @property
    def reg_county(self):
        return self._reg_county

    @reg_county.setter
    def reg_county(self, value):
        self._reg_county = value
    @property
    def reg_duration(self):
        return self._reg_duration

    @reg_duration.setter
    def reg_duration(self, value):
        self._reg_duration = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def reg_province(self):
        return self._reg_province

    @reg_province.setter
    def reg_province(self, value):
        self._reg_province = value
    @property
    def sale_details(self):
        return self._sale_details

    @sale_details.setter
    def sale_details(self, value):
        if isinstance(value, list):
            self._sale_details = list()
            for i in value:
                if isinstance(i, SaleFeatureInfo):
                    self._sale_details.append(i)
                else:
                    self._sale_details.append(SaleFeatureInfo.from_alipay_dict(i))
    @property
    def sell_out_item_num(self):
        return self._sell_out_item_num

    @sell_out_item_num.setter
    def sell_out_item_num(self, value):
        self._sell_out_item_num = value
    @property
    def shop_num_past_year(self):
        return self._shop_num_past_year

    @shop_num_past_year.setter
    def shop_num_past_year(self, value):
        self._shop_num_past_year = value
    @property
    def shop_rating_list(self):
        return self._shop_rating_list

    @shop_rating_list.setter
    def shop_rating_list(self, value):
        if isinstance(value, list):
            self._shop_rating_list = list()
            for i in value:
                if isinstance(i, ShopRatingInfo):
                    self._shop_rating_list.append(i)
                else:
                    self._shop_rating_list.append(ShopRatingInfo.from_alipay_dict(i))
    @property
    def standard_amt_top_10_products(self):
        return self._standard_amt_top_10_products

    @standard_amt_top_10_products.setter
    def standard_amt_top_10_products(self, value):
        if isinstance(value, list):
            self._standard_amt_top_10_products = list()
            for i in value:
                if isinstance(i, ProductDetailInfo):
                    self._standard_amt_top_10_products.append(i)
                else:
                    self._standard_amt_top_10_products.append(ProductDetailInfo.from_alipay_dict(i))
    @property
    def standard_volume_top_10_products(self):
        return self._standard_volume_top_10_products

    @standard_volume_top_10_products.setter
    def standard_volume_top_10_products(self, value):
        if isinstance(value, list):
            self._standard_volume_top_10_products = list()
            for i in value:
                if isinstance(i, ProductDetailInfo):
                    self._standard_volume_top_10_products.append(i)
                else:
                    self._standard_volume_top_10_products.append(ProductDetailInfo.from_alipay_dict(i))
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_month_past_year:
            if hasattr(self.active_month_past_year, 'to_alipay_dict'):
                params['active_month_past_year'] = self.active_month_past_year.to_alipay_dict()
            else:
                params['active_month_past_year'] = self.active_month_past_year
        if self.active_shop_num:
            if hasattr(self.active_shop_num, 'to_alipay_dict'):
                params['active_shop_num'] = self.active_shop_num.to_alipay_dict()
            else:
                params['active_shop_num'] = self.active_shop_num
        if self.anchor_list:
            if isinstance(self.anchor_list, list):
                for i in range(0, len(self.anchor_list)):
                    element = self.anchor_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.anchor_list[i] = element.to_alipay_dict()
            if hasattr(self.anchor_list, 'to_alipay_dict'):
                params['anchor_list'] = self.anchor_list.to_alipay_dict()
            else:
                params['anchor_list'] = self.anchor_list
        if self.anchor_num:
            if hasattr(self.anchor_num, 'to_alipay_dict'):
                params['anchor_num'] = self.anchor_num.to_alipay_dict()
            else:
                params['anchor_num'] = self.anchor_num
        if self.business_list:
            if isinstance(self.business_list, list):
                for i in range(0, len(self.business_list)):
                    element = self.business_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_list[i] = element.to_alipay_dict()
            if hasattr(self.business_list, 'to_alipay_dict'):
                params['business_list'] = self.business_list.to_alipay_dict()
            else:
                params['business_list'] = self.business_list
        if self.closed_shop_num:
            if hasattr(self.closed_shop_num, 'to_alipay_dict'):
                params['closed_shop_num'] = self.closed_shop_num.to_alipay_dict()
            else:
                params['closed_shop_num'] = self.closed_shop_num
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.ent_status:
            if hasattr(self.ent_status, 'to_alipay_dict'):
                params['ent_status'] = self.ent_status.to_alipay_dict()
            else:
                params['ent_status'] = self.ent_status
        if self.ent_type:
            if hasattr(self.ent_type, 'to_alipay_dict'):
                params['ent_type'] = self.ent_type.to_alipay_dict()
            else:
                params['ent_type'] = self.ent_type
        if self.last_open_date_duration:
            if hasattr(self.last_open_date_duration, 'to_alipay_dict'):
                params['last_open_date_duration'] = self.last_open_date_duration.to_alipay_dict()
            else:
                params['last_open_date_duration'] = self.last_open_date_duration
        if self.main_business:
            if hasattr(self.main_business, 'to_alipay_dict'):
                params['main_business'] = self.main_business.to_alipay_dict()
            else:
                params['main_business'] = self.main_business
        if self.off_shelf_num:
            if hasattr(self.off_shelf_num, 'to_alipay_dict'):
                params['off_shelf_num'] = self.off_shelf_num.to_alipay_dict()
            else:
                params['off_shelf_num'] = self.off_shelf_num
        if self.on_sale_brand_list:
            if isinstance(self.on_sale_brand_list, list):
                for i in range(0, len(self.on_sale_brand_list)):
                    element = self.on_sale_brand_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.on_sale_brand_list[i] = element.to_alipay_dict()
            if hasattr(self.on_sale_brand_list, 'to_alipay_dict'):
                params['on_sale_brand_list'] = self.on_sale_brand_list.to_alipay_dict()
            else:
                params['on_sale_brand_list'] = self.on_sale_brand_list
        if self.on_sale_brand_num:
            if hasattr(self.on_sale_brand_num, 'to_alipay_dict'):
                params['on_sale_brand_num'] = self.on_sale_brand_num.to_alipay_dict()
            else:
                params['on_sale_brand_num'] = self.on_sale_brand_num
        if self.on_sale_item_num:
            if hasattr(self.on_sale_item_num, 'to_alipay_dict'):
                params['on_sale_item_num'] = self.on_sale_item_num.to_alipay_dict()
            else:
                params['on_sale_item_num'] = self.on_sale_item_num
        if self.open_date_duration:
            if hasattr(self.open_date_duration, 'to_alipay_dict'):
                params['open_date_duration'] = self.open_date_duration.to_alipay_dict()
            else:
                params['open_date_duration'] = self.open_date_duration
        if self.operation_shop_num:
            if hasattr(self.operation_shop_num, 'to_alipay_dict'):
                params['operation_shop_num'] = self.operation_shop_num.to_alipay_dict()
            else:
                params['operation_shop_num'] = self.operation_shop_num
        if self.person_name:
            if hasattr(self.person_name, 'to_alipay_dict'):
                params['person_name'] = self.person_name.to_alipay_dict()
            else:
                params['person_name'] = self.person_name
        if self.platform_list:
            if isinstance(self.platform_list, list):
                for i in range(0, len(self.platform_list)):
                    element = self.platform_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_list[i] = element.to_alipay_dict()
            if hasattr(self.platform_list, 'to_alipay_dict'):
                params['platform_list'] = self.platform_list.to_alipay_dict()
            else:
                params['platform_list'] = self.platform_list
        if self.platform_num:
            if hasattr(self.platform_num, 'to_alipay_dict'):
                params['platform_num'] = self.platform_num.to_alipay_dict()
            else:
                params['platform_num'] = self.platform_num
        if self.platform_past_year:
            if hasattr(self.platform_past_year, 'to_alipay_dict'):
                params['platform_past_year'] = self.platform_past_year.to_alipay_dict()
            else:
                params['platform_past_year'] = self.platform_past_year
        if self.reg_city:
            if hasattr(self.reg_city, 'to_alipay_dict'):
                params['reg_city'] = self.reg_city.to_alipay_dict()
            else:
                params['reg_city'] = self.reg_city
        if self.reg_county:
            if hasattr(self.reg_county, 'to_alipay_dict'):
                params['reg_county'] = self.reg_county.to_alipay_dict()
            else:
                params['reg_county'] = self.reg_county
        if self.reg_duration:
            if hasattr(self.reg_duration, 'to_alipay_dict'):
                params['reg_duration'] = self.reg_duration.to_alipay_dict()
            else:
                params['reg_duration'] = self.reg_duration
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
        if self.reg_province:
            if hasattr(self.reg_province, 'to_alipay_dict'):
                params['reg_province'] = self.reg_province.to_alipay_dict()
            else:
                params['reg_province'] = self.reg_province
        if self.sale_details:
            if isinstance(self.sale_details, list):
                for i in range(0, len(self.sale_details)):
                    element = self.sale_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sale_details[i] = element.to_alipay_dict()
            if hasattr(self.sale_details, 'to_alipay_dict'):
                params['sale_details'] = self.sale_details.to_alipay_dict()
            else:
                params['sale_details'] = self.sale_details
        if self.sell_out_item_num:
            if hasattr(self.sell_out_item_num, 'to_alipay_dict'):
                params['sell_out_item_num'] = self.sell_out_item_num.to_alipay_dict()
            else:
                params['sell_out_item_num'] = self.sell_out_item_num
        if self.shop_num_past_year:
            if hasattr(self.shop_num_past_year, 'to_alipay_dict'):
                params['shop_num_past_year'] = self.shop_num_past_year.to_alipay_dict()
            else:
                params['shop_num_past_year'] = self.shop_num_past_year
        if self.shop_rating_list:
            if isinstance(self.shop_rating_list, list):
                for i in range(0, len(self.shop_rating_list)):
                    element = self.shop_rating_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_rating_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_rating_list, 'to_alipay_dict'):
                params['shop_rating_list'] = self.shop_rating_list.to_alipay_dict()
            else:
                params['shop_rating_list'] = self.shop_rating_list
        if self.standard_amt_top_10_products:
            if isinstance(self.standard_amt_top_10_products, list):
                for i in range(0, len(self.standard_amt_top_10_products)):
                    element = self.standard_amt_top_10_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_amt_top_10_products[i] = element.to_alipay_dict()
            if hasattr(self.standard_amt_top_10_products, 'to_alipay_dict'):
                params['standard_amt_top_10_products'] = self.standard_amt_top_10_products.to_alipay_dict()
            else:
                params['standard_amt_top_10_products'] = self.standard_amt_top_10_products
        if self.standard_volume_top_10_products:
            if isinstance(self.standard_volume_top_10_products, list):
                for i in range(0, len(self.standard_volume_top_10_products)):
                    element = self.standard_volume_top_10_products[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.standard_volume_top_10_products[i] = element.to_alipay_dict()
            if hasattr(self.standard_volume_top_10_products, 'to_alipay_dict'):
                params['standard_volume_top_10_products'] = self.standard_volume_top_10_products.to_alipay_dict()
            else:
                params['standard_volume_top_10_products'] = self.standard_volume_top_10_products
        if self.uscc:
            if hasattr(self.uscc, 'to_alipay_dict'):
                params['uscc'] = self.uscc.to_alipay_dict()
            else:
                params['uscc'] = self.uscc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomCompanyFeatureInfo()
        if 'active_month_past_year' in d:
            o.active_month_past_year = d['active_month_past_year']
        if 'active_shop_num' in d:
            o.active_shop_num = d['active_shop_num']
        if 'anchor_list' in d:
            o.anchor_list = d['anchor_list']
        if 'anchor_num' in d:
            o.anchor_num = d['anchor_num']
        if 'business_list' in d:
            o.business_list = d['business_list']
        if 'closed_shop_num' in d:
            o.closed_shop_num = d['closed_shop_num']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'ent_status' in d:
            o.ent_status = d['ent_status']
        if 'ent_type' in d:
            o.ent_type = d['ent_type']
        if 'last_open_date_duration' in d:
            o.last_open_date_duration = d['last_open_date_duration']
        if 'main_business' in d:
            o.main_business = d['main_business']
        if 'off_shelf_num' in d:
            o.off_shelf_num = d['off_shelf_num']
        if 'on_sale_brand_list' in d:
            o.on_sale_brand_list = d['on_sale_brand_list']
        if 'on_sale_brand_num' in d:
            o.on_sale_brand_num = d['on_sale_brand_num']
        if 'on_sale_item_num' in d:
            o.on_sale_item_num = d['on_sale_item_num']
        if 'open_date_duration' in d:
            o.open_date_duration = d['open_date_duration']
        if 'operation_shop_num' in d:
            o.operation_shop_num = d['operation_shop_num']
        if 'person_name' in d:
            o.person_name = d['person_name']
        if 'platform_list' in d:
            o.platform_list = d['platform_list']
        if 'platform_num' in d:
            o.platform_num = d['platform_num']
        if 'platform_past_year' in d:
            o.platform_past_year = d['platform_past_year']
        if 'reg_city' in d:
            o.reg_city = d['reg_city']
        if 'reg_county' in d:
            o.reg_county = d['reg_county']
        if 'reg_duration' in d:
            o.reg_duration = d['reg_duration']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'reg_province' in d:
            o.reg_province = d['reg_province']
        if 'sale_details' in d:
            o.sale_details = d['sale_details']
        if 'sell_out_item_num' in d:
            o.sell_out_item_num = d['sell_out_item_num']
        if 'shop_num_past_year' in d:
            o.shop_num_past_year = d['shop_num_past_year']
        if 'shop_rating_list' in d:
            o.shop_rating_list = d['shop_rating_list']
        if 'standard_amt_top_10_products' in d:
            o.standard_amt_top_10_products = d['standard_amt_top_10_products']
        if 'standard_volume_top_10_products' in d:
            o.standard_volume_top_10_products = d['standard_volume_top_10_products']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


