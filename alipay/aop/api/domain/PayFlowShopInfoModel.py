#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayFlowTransDetailInfoModel import PayFlowTransDetailInfoModel


class PayFlowShopInfoModel(object):

    def __init__(self):
        self._address = None
        self._card_no = None
        self._city = None
        self._company_name = None
        self._detail_list = None
        self._district = None
        self._extend = None
        self._first_date = None
        self._industry_level_1 = None
        self._industry_level_2 = None
        self._industry_level_3 = None
        self._industry_level_4 = None
        self._last_date = None
        self._ord_acnt_acv_12_m_suc = None
        self._ord_acnt_acv_1_m_suc = None
        self._ord_acnt_acv_3_m_suc = None
        self._ord_acnt_acv_6_m_suc = None
        self._ord_acnt_adf_12_m_suc = None
        self._ord_acnt_adf_1_m_suc = None
        self._ord_acnt_adf_3_m_suc = None
        self._ord_acnt_adf_6_m_suc = None
        self._ord_amt_acv_12_m_suc = None
        self._ord_amt_acv_1_m_suc = None
        self._ord_amt_acv_3_m_suc = None
        self._ord_amt_acv_6_m_suc = None
        self._ord_amt_adf_12_m_suc = None
        self._ord_amt_adf_1_m_suc = None
        self._ord_amt_adf_3_m_suc = None
        self._ord_amt_adf_6_m_suc = None
        self._platform_name = None
        self._prevent_spam_flag = None
        self._province = None
        self._reg_no = None
        self._shop_id = None
        self._shop_name = None
        self._sign_date = None
        self._uscc = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def detail_list(self):
        return self._detail_list

    @detail_list.setter
    def detail_list(self, value):
        if isinstance(value, list):
            self._detail_list = list()
            for i in value:
                if isinstance(i, PayFlowTransDetailInfoModel):
                    self._detail_list.append(i)
                else:
                    self._detail_list.append(PayFlowTransDetailInfoModel.from_alipay_dict(i))
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def first_date(self):
        return self._first_date

    @first_date.setter
    def first_date(self, value):
        self._first_date = value
    @property
    def industry_level_1(self):
        return self._industry_level_1

    @industry_level_1.setter
    def industry_level_1(self, value):
        self._industry_level_1 = value
    @property
    def industry_level_2(self):
        return self._industry_level_2

    @industry_level_2.setter
    def industry_level_2(self, value):
        self._industry_level_2 = value
    @property
    def industry_level_3(self):
        return self._industry_level_3

    @industry_level_3.setter
    def industry_level_3(self, value):
        self._industry_level_3 = value
    @property
    def industry_level_4(self):
        return self._industry_level_4

    @industry_level_4.setter
    def industry_level_4(self, value):
        self._industry_level_4 = value
    @property
    def last_date(self):
        return self._last_date

    @last_date.setter
    def last_date(self, value):
        self._last_date = value
    @property
    def ord_acnt_acv_12_m_suc(self):
        return self._ord_acnt_acv_12_m_suc

    @ord_acnt_acv_12_m_suc.setter
    def ord_acnt_acv_12_m_suc(self, value):
        self._ord_acnt_acv_12_m_suc = value
    @property
    def ord_acnt_acv_1_m_suc(self):
        return self._ord_acnt_acv_1_m_suc

    @ord_acnt_acv_1_m_suc.setter
    def ord_acnt_acv_1_m_suc(self, value):
        self._ord_acnt_acv_1_m_suc = value
    @property
    def ord_acnt_acv_3_m_suc(self):
        return self._ord_acnt_acv_3_m_suc

    @ord_acnt_acv_3_m_suc.setter
    def ord_acnt_acv_3_m_suc(self, value):
        self._ord_acnt_acv_3_m_suc = value
    @property
    def ord_acnt_acv_6_m_suc(self):
        return self._ord_acnt_acv_6_m_suc

    @ord_acnt_acv_6_m_suc.setter
    def ord_acnt_acv_6_m_suc(self, value):
        self._ord_acnt_acv_6_m_suc = value
    @property
    def ord_acnt_adf_12_m_suc(self):
        return self._ord_acnt_adf_12_m_suc

    @ord_acnt_adf_12_m_suc.setter
    def ord_acnt_adf_12_m_suc(self, value):
        self._ord_acnt_adf_12_m_suc = value
    @property
    def ord_acnt_adf_1_m_suc(self):
        return self._ord_acnt_adf_1_m_suc

    @ord_acnt_adf_1_m_suc.setter
    def ord_acnt_adf_1_m_suc(self, value):
        self._ord_acnt_adf_1_m_suc = value
    @property
    def ord_acnt_adf_3_m_suc(self):
        return self._ord_acnt_adf_3_m_suc

    @ord_acnt_adf_3_m_suc.setter
    def ord_acnt_adf_3_m_suc(self, value):
        self._ord_acnt_adf_3_m_suc = value
    @property
    def ord_acnt_adf_6_m_suc(self):
        return self._ord_acnt_adf_6_m_suc

    @ord_acnt_adf_6_m_suc.setter
    def ord_acnt_adf_6_m_suc(self, value):
        self._ord_acnt_adf_6_m_suc = value
    @property
    def ord_amt_acv_12_m_suc(self):
        return self._ord_amt_acv_12_m_suc

    @ord_amt_acv_12_m_suc.setter
    def ord_amt_acv_12_m_suc(self, value):
        self._ord_amt_acv_12_m_suc = value
    @property
    def ord_amt_acv_1_m_suc(self):
        return self._ord_amt_acv_1_m_suc

    @ord_amt_acv_1_m_suc.setter
    def ord_amt_acv_1_m_suc(self, value):
        self._ord_amt_acv_1_m_suc = value
    @property
    def ord_amt_acv_3_m_suc(self):
        return self._ord_amt_acv_3_m_suc

    @ord_amt_acv_3_m_suc.setter
    def ord_amt_acv_3_m_suc(self, value):
        self._ord_amt_acv_3_m_suc = value
    @property
    def ord_amt_acv_6_m_suc(self):
        return self._ord_amt_acv_6_m_suc

    @ord_amt_acv_6_m_suc.setter
    def ord_amt_acv_6_m_suc(self, value):
        self._ord_amt_acv_6_m_suc = value
    @property
    def ord_amt_adf_12_m_suc(self):
        return self._ord_amt_adf_12_m_suc

    @ord_amt_adf_12_m_suc.setter
    def ord_amt_adf_12_m_suc(self, value):
        self._ord_amt_adf_12_m_suc = value
    @property
    def ord_amt_adf_1_m_suc(self):
        return self._ord_amt_adf_1_m_suc

    @ord_amt_adf_1_m_suc.setter
    def ord_amt_adf_1_m_suc(self, value):
        self._ord_amt_adf_1_m_suc = value
    @property
    def ord_amt_adf_3_m_suc(self):
        return self._ord_amt_adf_3_m_suc

    @ord_amt_adf_3_m_suc.setter
    def ord_amt_adf_3_m_suc(self, value):
        self._ord_amt_adf_3_m_suc = value
    @property
    def ord_amt_adf_6_m_suc(self):
        return self._ord_amt_adf_6_m_suc

    @ord_amt_adf_6_m_suc.setter
    def ord_amt_adf_6_m_suc(self, value):
        self._ord_amt_adf_6_m_suc = value
    @property
    def platform_name(self):
        return self._platform_name

    @platform_name.setter
    def platform_name(self, value):
        self._platform_name = value
    @property
    def prevent_spam_flag(self):
        return self._prevent_spam_flag

    @prevent_spam_flag.setter
    def prevent_spam_flag(self, value):
        self._prevent_spam_flag = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value
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
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
    @property
    def uscc(self):
        return self._uscc

    @uscc.setter
    def uscc(self, value):
        self._uscc = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.detail_list:
            if isinstance(self.detail_list, list):
                for i in range(0, len(self.detail_list)):
                    element = self.detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_list[i] = element.to_alipay_dict()
            if hasattr(self.detail_list, 'to_alipay_dict'):
                params['detail_list'] = self.detail_list.to_alipay_dict()
            else:
                params['detail_list'] = self.detail_list
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.first_date:
            if hasattr(self.first_date, 'to_alipay_dict'):
                params['first_date'] = self.first_date.to_alipay_dict()
            else:
                params['first_date'] = self.first_date
        if self.industry_level_1:
            if hasattr(self.industry_level_1, 'to_alipay_dict'):
                params['industry_level_1'] = self.industry_level_1.to_alipay_dict()
            else:
                params['industry_level_1'] = self.industry_level_1
        if self.industry_level_2:
            if hasattr(self.industry_level_2, 'to_alipay_dict'):
                params['industry_level_2'] = self.industry_level_2.to_alipay_dict()
            else:
                params['industry_level_2'] = self.industry_level_2
        if self.industry_level_3:
            if hasattr(self.industry_level_3, 'to_alipay_dict'):
                params['industry_level_3'] = self.industry_level_3.to_alipay_dict()
            else:
                params['industry_level_3'] = self.industry_level_3
        if self.industry_level_4:
            if hasattr(self.industry_level_4, 'to_alipay_dict'):
                params['industry_level_4'] = self.industry_level_4.to_alipay_dict()
            else:
                params['industry_level_4'] = self.industry_level_4
        if self.last_date:
            if hasattr(self.last_date, 'to_alipay_dict'):
                params['last_date'] = self.last_date.to_alipay_dict()
            else:
                params['last_date'] = self.last_date
        if self.ord_acnt_acv_12_m_suc:
            if hasattr(self.ord_acnt_acv_12_m_suc, 'to_alipay_dict'):
                params['ord_acnt_acv_12_m_suc'] = self.ord_acnt_acv_12_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_acv_12_m_suc'] = self.ord_acnt_acv_12_m_suc
        if self.ord_acnt_acv_1_m_suc:
            if hasattr(self.ord_acnt_acv_1_m_suc, 'to_alipay_dict'):
                params['ord_acnt_acv_1_m_suc'] = self.ord_acnt_acv_1_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_acv_1_m_suc'] = self.ord_acnt_acv_1_m_suc
        if self.ord_acnt_acv_3_m_suc:
            if hasattr(self.ord_acnt_acv_3_m_suc, 'to_alipay_dict'):
                params['ord_acnt_acv_3_m_suc'] = self.ord_acnt_acv_3_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_acv_3_m_suc'] = self.ord_acnt_acv_3_m_suc
        if self.ord_acnt_acv_6_m_suc:
            if hasattr(self.ord_acnt_acv_6_m_suc, 'to_alipay_dict'):
                params['ord_acnt_acv_6_m_suc'] = self.ord_acnt_acv_6_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_acv_6_m_suc'] = self.ord_acnt_acv_6_m_suc
        if self.ord_acnt_adf_12_m_suc:
            if hasattr(self.ord_acnt_adf_12_m_suc, 'to_alipay_dict'):
                params['ord_acnt_adf_12_m_suc'] = self.ord_acnt_adf_12_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_adf_12_m_suc'] = self.ord_acnt_adf_12_m_suc
        if self.ord_acnt_adf_1_m_suc:
            if hasattr(self.ord_acnt_adf_1_m_suc, 'to_alipay_dict'):
                params['ord_acnt_adf_1_m_suc'] = self.ord_acnt_adf_1_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_adf_1_m_suc'] = self.ord_acnt_adf_1_m_suc
        if self.ord_acnt_adf_3_m_suc:
            if hasattr(self.ord_acnt_adf_3_m_suc, 'to_alipay_dict'):
                params['ord_acnt_adf_3_m_suc'] = self.ord_acnt_adf_3_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_adf_3_m_suc'] = self.ord_acnt_adf_3_m_suc
        if self.ord_acnt_adf_6_m_suc:
            if hasattr(self.ord_acnt_adf_6_m_suc, 'to_alipay_dict'):
                params['ord_acnt_adf_6_m_suc'] = self.ord_acnt_adf_6_m_suc.to_alipay_dict()
            else:
                params['ord_acnt_adf_6_m_suc'] = self.ord_acnt_adf_6_m_suc
        if self.ord_amt_acv_12_m_suc:
            if hasattr(self.ord_amt_acv_12_m_suc, 'to_alipay_dict'):
                params['ord_amt_acv_12_m_suc'] = self.ord_amt_acv_12_m_suc.to_alipay_dict()
            else:
                params['ord_amt_acv_12_m_suc'] = self.ord_amt_acv_12_m_suc
        if self.ord_amt_acv_1_m_suc:
            if hasattr(self.ord_amt_acv_1_m_suc, 'to_alipay_dict'):
                params['ord_amt_acv_1_m_suc'] = self.ord_amt_acv_1_m_suc.to_alipay_dict()
            else:
                params['ord_amt_acv_1_m_suc'] = self.ord_amt_acv_1_m_suc
        if self.ord_amt_acv_3_m_suc:
            if hasattr(self.ord_amt_acv_3_m_suc, 'to_alipay_dict'):
                params['ord_amt_acv_3_m_suc'] = self.ord_amt_acv_3_m_suc.to_alipay_dict()
            else:
                params['ord_amt_acv_3_m_suc'] = self.ord_amt_acv_3_m_suc
        if self.ord_amt_acv_6_m_suc:
            if hasattr(self.ord_amt_acv_6_m_suc, 'to_alipay_dict'):
                params['ord_amt_acv_6_m_suc'] = self.ord_amt_acv_6_m_suc.to_alipay_dict()
            else:
                params['ord_amt_acv_6_m_suc'] = self.ord_amt_acv_6_m_suc
        if self.ord_amt_adf_12_m_suc:
            if hasattr(self.ord_amt_adf_12_m_suc, 'to_alipay_dict'):
                params['ord_amt_adf_12_m_suc'] = self.ord_amt_adf_12_m_suc.to_alipay_dict()
            else:
                params['ord_amt_adf_12_m_suc'] = self.ord_amt_adf_12_m_suc
        if self.ord_amt_adf_1_m_suc:
            if hasattr(self.ord_amt_adf_1_m_suc, 'to_alipay_dict'):
                params['ord_amt_adf_1_m_suc'] = self.ord_amt_adf_1_m_suc.to_alipay_dict()
            else:
                params['ord_amt_adf_1_m_suc'] = self.ord_amt_adf_1_m_suc
        if self.ord_amt_adf_3_m_suc:
            if hasattr(self.ord_amt_adf_3_m_suc, 'to_alipay_dict'):
                params['ord_amt_adf_3_m_suc'] = self.ord_amt_adf_3_m_suc.to_alipay_dict()
            else:
                params['ord_amt_adf_3_m_suc'] = self.ord_amt_adf_3_m_suc
        if self.ord_amt_adf_6_m_suc:
            if hasattr(self.ord_amt_adf_6_m_suc, 'to_alipay_dict'):
                params['ord_amt_adf_6_m_suc'] = self.ord_amt_adf_6_m_suc.to_alipay_dict()
            else:
                params['ord_amt_adf_6_m_suc'] = self.ord_amt_adf_6_m_suc
        if self.platform_name:
            if hasattr(self.platform_name, 'to_alipay_dict'):
                params['platform_name'] = self.platform_name.to_alipay_dict()
            else:
                params['platform_name'] = self.platform_name
        if self.prevent_spam_flag:
            if hasattr(self.prevent_spam_flag, 'to_alipay_dict'):
                params['prevent_spam_flag'] = self.prevent_spam_flag.to_alipay_dict()
            else:
                params['prevent_spam_flag'] = self.prevent_spam_flag
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.reg_no:
            if hasattr(self.reg_no, 'to_alipay_dict'):
                params['reg_no'] = self.reg_no.to_alipay_dict()
            else:
                params['reg_no'] = self.reg_no
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
        if self.sign_date:
            if hasattr(self.sign_date, 'to_alipay_dict'):
                params['sign_date'] = self.sign_date.to_alipay_dict()
            else:
                params['sign_date'] = self.sign_date
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
        o = PayFlowShopInfoModel()
        if 'address' in d:
            o.address = d['address']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'city' in d:
            o.city = d['city']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'detail_list' in d:
            o.detail_list = d['detail_list']
        if 'district' in d:
            o.district = d['district']
        if 'extend' in d:
            o.extend = d['extend']
        if 'first_date' in d:
            o.first_date = d['first_date']
        if 'industry_level_1' in d:
            o.industry_level_1 = d['industry_level_1']
        if 'industry_level_2' in d:
            o.industry_level_2 = d['industry_level_2']
        if 'industry_level_3' in d:
            o.industry_level_3 = d['industry_level_3']
        if 'industry_level_4' in d:
            o.industry_level_4 = d['industry_level_4']
        if 'last_date' in d:
            o.last_date = d['last_date']
        if 'ord_acnt_acv_12_m_suc' in d:
            o.ord_acnt_acv_12_m_suc = d['ord_acnt_acv_12_m_suc']
        if 'ord_acnt_acv_1_m_suc' in d:
            o.ord_acnt_acv_1_m_suc = d['ord_acnt_acv_1_m_suc']
        if 'ord_acnt_acv_3_m_suc' in d:
            o.ord_acnt_acv_3_m_suc = d['ord_acnt_acv_3_m_suc']
        if 'ord_acnt_acv_6_m_suc' in d:
            o.ord_acnt_acv_6_m_suc = d['ord_acnt_acv_6_m_suc']
        if 'ord_acnt_adf_12_m_suc' in d:
            o.ord_acnt_adf_12_m_suc = d['ord_acnt_adf_12_m_suc']
        if 'ord_acnt_adf_1_m_suc' in d:
            o.ord_acnt_adf_1_m_suc = d['ord_acnt_adf_1_m_suc']
        if 'ord_acnt_adf_3_m_suc' in d:
            o.ord_acnt_adf_3_m_suc = d['ord_acnt_adf_3_m_suc']
        if 'ord_acnt_adf_6_m_suc' in d:
            o.ord_acnt_adf_6_m_suc = d['ord_acnt_adf_6_m_suc']
        if 'ord_amt_acv_12_m_suc' in d:
            o.ord_amt_acv_12_m_suc = d['ord_amt_acv_12_m_suc']
        if 'ord_amt_acv_1_m_suc' in d:
            o.ord_amt_acv_1_m_suc = d['ord_amt_acv_1_m_suc']
        if 'ord_amt_acv_3_m_suc' in d:
            o.ord_amt_acv_3_m_suc = d['ord_amt_acv_3_m_suc']
        if 'ord_amt_acv_6_m_suc' in d:
            o.ord_amt_acv_6_m_suc = d['ord_amt_acv_6_m_suc']
        if 'ord_amt_adf_12_m_suc' in d:
            o.ord_amt_adf_12_m_suc = d['ord_amt_adf_12_m_suc']
        if 'ord_amt_adf_1_m_suc' in d:
            o.ord_amt_adf_1_m_suc = d['ord_amt_adf_1_m_suc']
        if 'ord_amt_adf_3_m_suc' in d:
            o.ord_amt_adf_3_m_suc = d['ord_amt_adf_3_m_suc']
        if 'ord_amt_adf_6_m_suc' in d:
            o.ord_amt_adf_6_m_suc = d['ord_amt_adf_6_m_suc']
        if 'platform_name' in d:
            o.platform_name = d['platform_name']
        if 'prevent_spam_flag' in d:
            o.prevent_spam_flag = d['prevent_spam_flag']
        if 'province' in d:
            o.province = d['province']
        if 'reg_no' in d:
            o.reg_no = d['reg_no']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'sign_date' in d:
            o.sign_date = d['sign_date']
        if 'uscc' in d:
            o.uscc = d['uscc']
        return o


