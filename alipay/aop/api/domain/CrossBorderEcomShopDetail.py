#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleInfo import SaleInfo


class CrossBorderEcomShopDetail(object):

    def __init__(self):
        self._main_business = None
        self._off_shelf_num = None
        self._on_sale_item_num = None
        self._org_name = None
        self._platform_id = None
        self._reg_no = None
        self._sale_details = None
        self._sell_country_list = None
        self._sell_out_item_num = None
        self._shop_corp_city = None
        self._shop_corp_county = None
        self._shop_corp_province = None
        self._shop_id = None
        self._shop_name = None
        self._shop_open_years = None
        self._shop_positive_rating_list = None
        self._shop_status = None
        self._shop_type = None
        self._uscc = None

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
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
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
    def sell_country_list(self):
        return self._sell_country_list

    @sell_country_list.setter
    def sell_country_list(self, value):
        if isinstance(value, list):
            self._sell_country_list = list()
            for i in value:
                self._sell_country_list.append(i)
    @property
    def sell_out_item_num(self):
        return self._sell_out_item_num

    @sell_out_item_num.setter
    def sell_out_item_num(self, value):
        self._sell_out_item_num = value
    @property
    def shop_corp_city(self):
        return self._shop_corp_city

    @shop_corp_city.setter
    def shop_corp_city(self, value):
        self._shop_corp_city = value
    @property
    def shop_corp_county(self):
        return self._shop_corp_county

    @shop_corp_county.setter
    def shop_corp_county(self, value):
        self._shop_corp_county = value
    @property
    def shop_corp_province(self):
        return self._shop_corp_province

    @shop_corp_province.setter
    def shop_corp_province(self, value):
        self._shop_corp_province = value
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
    def shop_open_years(self):
        return self._shop_open_years

    @shop_open_years.setter
    def shop_open_years(self, value):
        self._shop_open_years = value
    @property
    def shop_positive_rating_list(self):
        return self._shop_positive_rating_list

    @shop_positive_rating_list.setter
    def shop_positive_rating_list(self, value):
        if isinstance(value, list):
            self._shop_positive_rating_list = list()
            for i in value:
                self._shop_positive_rating_list.append(i)
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
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
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
        if self.sell_country_list:
            if isinstance(self.sell_country_list, list):
                for i in range(0, len(self.sell_country_list)):
                    element = self.sell_country_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sell_country_list[i] = element.to_alipay_dict()
            if hasattr(self.sell_country_list, 'to_alipay_dict'):
                params['sell_country_list'] = self.sell_country_list.to_alipay_dict()
            else:
                params['sell_country_list'] = self.sell_country_list
        if self.sell_out_item_num:
            if hasattr(self.sell_out_item_num, 'to_alipay_dict'):
                params['sell_out_item_num'] = self.sell_out_item_num.to_alipay_dict()
            else:
                params['sell_out_item_num'] = self.sell_out_item_num
        if self.shop_corp_city:
            if hasattr(self.shop_corp_city, 'to_alipay_dict'):
                params['shop_corp_city'] = self.shop_corp_city.to_alipay_dict()
            else:
                params['shop_corp_city'] = self.shop_corp_city
        if self.shop_corp_county:
            if hasattr(self.shop_corp_county, 'to_alipay_dict'):
                params['shop_corp_county'] = self.shop_corp_county.to_alipay_dict()
            else:
                params['shop_corp_county'] = self.shop_corp_county
        if self.shop_corp_province:
            if hasattr(self.shop_corp_province, 'to_alipay_dict'):
                params['shop_corp_province'] = self.shop_corp_province.to_alipay_dict()
            else:
                params['shop_corp_province'] = self.shop_corp_province
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
        if self.shop_open_years:
            if hasattr(self.shop_open_years, 'to_alipay_dict'):
                params['shop_open_years'] = self.shop_open_years.to_alipay_dict()
            else:
                params['shop_open_years'] = self.shop_open_years
        if self.shop_positive_rating_list:
            if isinstance(self.shop_positive_rating_list, list):
                for i in range(0, len(self.shop_positive_rating_list)):
                    element = self.shop_positive_rating_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_positive_rating_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_positive_rating_list, 'to_alipay_dict'):
                params['shop_positive_rating_list'] = self.shop_positive_rating_list.to_alipay_dict()
            else:
                params['shop_positive_rating_list'] = self.shop_positive_rating_list
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
        o = CrossBorderEcomShopDetail()
        if 'main_business' in d:
            o.main_business = d['main_business']
        if 'off_shelf_num' in d:
            o.off_shelf_num = d['off_shelf_num']
        if 'on_sale_item_num' in d:
            o.on_sale_item_num = d['on_sale_item_num']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'sale_details' in d:
            o.sale_details = d['sale_details']
        if 'sell_country_list' in d:
            o.sell_country_list = d['sell_country_list']
        if 'sell_out_item_num' in d:
            o.sell_out_item_num = d['sell_out_item_num']
        if 'shop_corp_city' in d:
            o.shop_corp_city = d['shop_corp_city']
        if 'shop_corp_county' in d:
            o.shop_corp_county = d['shop_corp_county']
        if 'shop_corp_province' in d:
            o.shop_corp_province = d['shop_corp_province']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_open_years' in d:
            o.shop_open_years = d['shop_open_years']
        if 'shop_positive_rating_list' in d:
            o.shop_positive_rating_list = d['shop_positive_rating_list']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        if 'shop_type' in d:
            o.shop_type = d['shop_type']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


