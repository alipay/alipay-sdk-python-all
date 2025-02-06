#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaleInfo import SaleInfo


class CrossBorderEcomCompanyDetail(object):

    def __init__(self):
        self._active_month_past_year = None
        self._active_shop_num = None
        self._business_list = None
        self._closed_shop_num = None
        self._ent_name = None
        self._ent_status = None
        self._ent_type = None
        self._max_shop_operation_years = None
        self._off_shelf_num = None
        self._on_sale_item_num = None
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
        self._sell_country_list = None
        self._sell_out_item_num = None
        self._shop_num_past_year = None
        self._shop_positive_rating_list = None
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
    def max_shop_operation_years(self):
        return self._max_shop_operation_years

    @max_shop_operation_years.setter
    def max_shop_operation_years(self, value):
        self._max_shop_operation_years = value
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
    def shop_num_past_year(self):
        return self._shop_num_past_year

    @shop_num_past_year.setter
    def shop_num_past_year(self, value):
        self._shop_num_past_year = value
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
        if self.max_shop_operation_years:
            if hasattr(self.max_shop_operation_years, 'to_alipay_dict'):
                params['max_shop_operation_years'] = self.max_shop_operation_years.to_alipay_dict()
            else:
                params['max_shop_operation_years'] = self.max_shop_operation_years
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
        if self.shop_num_past_year:
            if hasattr(self.shop_num_past_year, 'to_alipay_dict'):
                params['shop_num_past_year'] = self.shop_num_past_year.to_alipay_dict()
            else:
                params['shop_num_past_year'] = self.shop_num_past_year
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
        o = CrossBorderEcomCompanyDetail()
        if 'active_month_past_year' in d:
            o.active_month_past_year = d['active_month_past_year']
        if 'active_shop_num' in d:
            o.active_shop_num = d['active_shop_num']
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
        if 'max_shop_operation_years' in d:
            o.max_shop_operation_years = d['max_shop_operation_years']
        if 'off_shelf_num' in d:
            o.off_shelf_num = d['off_shelf_num']
        if 'on_sale_item_num' in d:
            o.on_sale_item_num = d['on_sale_item_num']
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
        if 'sell_country_list' in d:
            o.sell_country_list = d['sell_country_list']
        if 'sell_out_item_num' in d:
            o.sell_out_item_num = d['sell_out_item_num']
        if 'shop_num_past_year' in d:
            o.shop_num_past_year = d['shop_num_past_year']
        if 'shop_positive_rating_list' in d:
            o.shop_positive_rating_list = d['shop_positive_rating_list']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


