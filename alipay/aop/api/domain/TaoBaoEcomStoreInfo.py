#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleInfo import SaleInfo
from alipay.aop.api.domain.ShopRatingInfo import ShopRatingInfo


class TaoBaoEcomStoreInfo(object):

    def __init__(self):
        self._anchor_list = None
        self._anchor_num = None
        self._delivery_city = None
        self._delivery_county = None
        self._delivery_province = None
        self._main_business = None
        self._off_shelf_num = None
        self._on_sale_brand_list = None
        self._on_sale_brand_num = None
        self._on_sale_item_num = None
        self._org_name = None
        self._platform_scale = None
        self._platform_type = None
        self._reg_no = None
        self._sale_details = None
        self._sell_out_item_num = None
        self._shop_city = None
        self._shop_close_date = None
        self._shop_county = None
        self._shop_id = None
        self._shop_name = None
        self._shop_open_date = None
        self._shop_province = None
        self._shop_rating = None
        self._shop_status = None
        self._shop_type = None
        self._shop_way = None
        self._uscc = None

    @property
    def anchor_list(self):
        return self._anchor_list

    @anchor_list.setter
    def anchor_list(self, value):
        self._anchor_list = value
    @property
    def anchor_num(self):
        return self._anchor_num

    @anchor_num.setter
    def anchor_num(self, value):
        self._anchor_num = value
    @property
    def delivery_city(self):
        return self._delivery_city

    @delivery_city.setter
    def delivery_city(self, value):
        self._delivery_city = value
    @property
    def delivery_county(self):
        return self._delivery_county

    @delivery_county.setter
    def delivery_county(self, value):
        self._delivery_county = value
    @property
    def delivery_province(self):
        return self._delivery_province

    @delivery_province.setter
    def delivery_province(self, value):
        self._delivery_province = value
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
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def platform_scale(self):
        return self._platform_scale

    @platform_scale.setter
    def platform_scale(self, value):
        self._platform_scale = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
    @property
    def sale_details(self):
        return self._sale_details

    @sale_details.setter
    def sale_details(self, value):
        if isinstance(value, list):
            self._sale_details = list()
            for i in value:
                if isinstance(i, SaleInfo):
                    self._sale_details.append(i)
                else:
                    self._sale_details.append(SaleInfo.from_alipay_dict(i))
    @property
    def sell_out_item_num(self):
        return self._sell_out_item_num

    @sell_out_item_num.setter
    def sell_out_item_num(self, value):
        self._sell_out_item_num = value
    @property
    def shop_city(self):
        return self._shop_city

    @shop_city.setter
    def shop_city(self, value):
        self._shop_city = value
    @property
    def shop_close_date(self):
        return self._shop_close_date

    @shop_close_date.setter
    def shop_close_date(self, value):
        self._shop_close_date = value
    @property
    def shop_county(self):
        return self._shop_county

    @shop_county.setter
    def shop_county(self, value):
        self._shop_county = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_open_date(self):
        return self._shop_open_date

    @shop_open_date.setter
    def shop_open_date(self, value):
        self._shop_open_date = value
    @property
    def shop_province(self):
        return self._shop_province

    @shop_province.setter
    def shop_province(self, value):
        self._shop_province = value
    @property
    def shop_rating(self):
        return self._shop_rating

    @shop_rating.setter
    def shop_rating(self, value):
        if isinstance(value, ShopRatingInfo):
            self._shop_rating = value
        else:
            self._shop_rating = ShopRatingInfo.from_alipay_dict(value)
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value
    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, value):
        self._shop_type = value
    @property
    def shop_way(self):
        return self._shop_way

    @shop_way.setter
    def shop_way(self, value):
        self._shop_way = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.anchor_list:
            if hasattr(self.anchor_list, 'to_alipay_dict'):
                params['anchor_list'] = self.anchor_list.to_alipay_dict()
            else:
                params['anchor_list'] = self.anchor_list
        if self.anchor_num:
            if hasattr(self.anchor_num, 'to_alipay_dict'):
                params['anchor_num'] = self.anchor_num.to_alipay_dict()
            else:
                params['anchor_num'] = self.anchor_num
        if self.delivery_city:
            if hasattr(self.delivery_city, 'to_alipay_dict'):
                params['delivery_city'] = self.delivery_city.to_alipay_dict()
            else:
                params['delivery_city'] = self.delivery_city
        if self.delivery_county:
            if hasattr(self.delivery_county, 'to_alipay_dict'):
                params['delivery_county'] = self.delivery_county.to_alipay_dict()
            else:
                params['delivery_county'] = self.delivery_county
        if self.delivery_province:
            if hasattr(self.delivery_province, 'to_alipay_dict'):
                params['delivery_province'] = self.delivery_province.to_alipay_dict()
            else:
                params['delivery_province'] = self.delivery_province
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
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.platform_scale:
            if hasattr(self.platform_scale, 'to_alipay_dict'):
                params['platform_scale'] = self.platform_scale.to_alipay_dict()
            else:
                params['platform_scale'] = self.platform_scale
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
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
        if self.shop_city:
            if hasattr(self.shop_city, 'to_alipay_dict'):
                params['shop_city'] = self.shop_city.to_alipay_dict()
            else:
                params['shop_city'] = self.shop_city
        if self.shop_close_date:
            if hasattr(self.shop_close_date, 'to_alipay_dict'):
                params['shop_close_date'] = self.shop_close_date.to_alipay_dict()
            else:
                params['shop_close_date'] = self.shop_close_date
        if self.shop_county:
            if hasattr(self.shop_county, 'to_alipay_dict'):
                params['shop_county'] = self.shop_county.to_alipay_dict()
            else:
                params['shop_county'] = self.shop_county
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_open_date:
            if hasattr(self.shop_open_date, 'to_alipay_dict'):
                params['shop_open_date'] = self.shop_open_date.to_alipay_dict()
            else:
                params['shop_open_date'] = self.shop_open_date
        if self.shop_province:
            if hasattr(self.shop_province, 'to_alipay_dict'):
                params['shop_province'] = self.shop_province.to_alipay_dict()
            else:
                params['shop_province'] = self.shop_province
        if self.shop_rating:
            if hasattr(self.shop_rating, 'to_alipay_dict'):
                params['shop_rating'] = self.shop_rating.to_alipay_dict()
            else:
                params['shop_rating'] = self.shop_rating
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        if self.shop_type:
            if hasattr(self.shop_type, 'to_alipay_dict'):
                params['shop_type'] = self.shop_type.to_alipay_dict()
            else:
                params['shop_type'] = self.shop_type
        if self.shop_way:
            if hasattr(self.shop_way, 'to_alipay_dict'):
                params['shop_way'] = self.shop_way.to_alipay_dict()
            else:
                params['shop_way'] = self.shop_way
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
        o = TaoBaoEcomStoreInfo()
        if 'anchor_list' in d:
            o.anchor_list = d['anchor_list']
        if 'anchor_num' in d:
            o.anchor_num = d['anchor_num']
        if 'delivery_city' in d:
            o.delivery_city = d['delivery_city']
        if 'delivery_county' in d:
            o.delivery_county = d['delivery_county']
        if 'delivery_province' in d:
            o.delivery_province = d['delivery_province']
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
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'platform_scale' in d:
            o.platform_scale = d['platform_scale']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'sale_details' in d:
            o.sale_details = d['sale_details']
        if 'sell_out_item_num' in d:
            o.sell_out_item_num = d['sell_out_item_num']
        if 'shop_city' in d:
            o.shop_city = d['shop_city']
        if 'shop_close_date' in d:
            o.shop_close_date = d['shop_close_date']
        if 'shop_county' in d:
            o.shop_county = d['shop_county']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_open_date' in d:
            o.shop_open_date = d['shop_open_date']
        if 'shop_province' in d:
            o.shop_province = d['shop_province']
        if 'shop_rating' in d:
            o.shop_rating = d['shop_rating']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'shop_way' in d:
            o.shop_way = d['shop_way']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


