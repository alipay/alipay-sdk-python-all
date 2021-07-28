#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinInsuranceUnifiedApplyModel(object):

    def __init__(self):
        self._additional_item = None
        self._apply_card_code = None
        self._apply_card_type = None
        self._apply_name = None
        self._defin_business_code = None
        self._defin_platform_access_type = None
        self._insure_end_date = None
        self._insure_start_date = None
        self._insured_card_code = None
        self._insured_card_type = None
        self._insured_name = None
        self._main_item_code = None
        self._main_item_content = None
        self._platform_code = None
        self._premium = None
        self._product_code = None
        self._rate = None
        self._request_no = None
        self._special = None
        self._subject_information = None

    @property
    def additional_item(self):
        return self._additional_item

    @additional_item.setter
    def additional_item(self, value):
        self._additional_item = value
    @property
    def apply_card_code(self):
        return self._apply_card_code

    @apply_card_code.setter
    def apply_card_code(self, value):
        self._apply_card_code = value
    @property
    def apply_card_type(self):
        return self._apply_card_type

    @apply_card_type.setter
    def apply_card_type(self, value):
        self._apply_card_type = value
    @property
    def apply_name(self):
        return self._apply_name

    @apply_name.setter
    def apply_name(self, value):
        self._apply_name = value
    @property
    def defin_business_code(self):
        return self._defin_business_code

    @defin_business_code.setter
    def defin_business_code(self, value):
        self._defin_business_code = value
    @property
    def defin_platform_access_type(self):
        return self._defin_platform_access_type

    @defin_platform_access_type.setter
    def defin_platform_access_type(self, value):
        self._defin_platform_access_type = value
    @property
    def insure_end_date(self):
        return self._insure_end_date

    @insure_end_date.setter
    def insure_end_date(self, value):
        self._insure_end_date = value
    @property
    def insure_start_date(self):
        return self._insure_start_date

    @insure_start_date.setter
    def insure_start_date(self, value):
        self._insure_start_date = value
    @property
    def insured_card_code(self):
        return self._insured_card_code

    @insured_card_code.setter
    def insured_card_code(self, value):
        self._insured_card_code = value
    @property
    def insured_card_type(self):
        return self._insured_card_type

    @insured_card_type.setter
    def insured_card_type(self, value):
        self._insured_card_type = value
    @property
    def insured_name(self):
        return self._insured_name

    @insured_name.setter
    def insured_name(self, value):
        self._insured_name = value
    @property
    def main_item_code(self):
        return self._main_item_code

    @main_item_code.setter
    def main_item_code(self, value):
        self._main_item_code = value
    @property
    def main_item_content(self):
        return self._main_item_content

    @main_item_content.setter
    def main_item_content(self, value):
        self._main_item_content = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def premium(self):
        return self._premium

    @premium.setter
    def premium(self, value):
        self._premium = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def special(self):
        return self._special

    @special.setter
    def special(self, value):
        self._special = value
    @property
    def subject_information(self):
        return self._subject_information

    @subject_information.setter
    def subject_information(self, value):
        self._subject_information = value


    def to_alipay_dict(self):
        params = dict()
        if self.additional_item:
            if hasattr(self.additional_item, 'to_alipay_dict'):
                params['additional_item'] = self.additional_item.to_alipay_dict()
            else:
                params['additional_item'] = self.additional_item
        if self.apply_card_code:
            if hasattr(self.apply_card_code, 'to_alipay_dict'):
                params['apply_card_code'] = self.apply_card_code.to_alipay_dict()
            else:
                params['apply_card_code'] = self.apply_card_code
        if self.apply_card_type:
            if hasattr(self.apply_card_type, 'to_alipay_dict'):
                params['apply_card_type'] = self.apply_card_type.to_alipay_dict()
            else:
                params['apply_card_type'] = self.apply_card_type
        if self.apply_name:
            if hasattr(self.apply_name, 'to_alipay_dict'):
                params['apply_name'] = self.apply_name.to_alipay_dict()
            else:
                params['apply_name'] = self.apply_name
        if self.defin_business_code:
            if hasattr(self.defin_business_code, 'to_alipay_dict'):
                params['defin_business_code'] = self.defin_business_code.to_alipay_dict()
            else:
                params['defin_business_code'] = self.defin_business_code
        if self.defin_platform_access_type:
            if hasattr(self.defin_platform_access_type, 'to_alipay_dict'):
                params['defin_platform_access_type'] = self.defin_platform_access_type.to_alipay_dict()
            else:
                params['defin_platform_access_type'] = self.defin_platform_access_type
        if self.insure_end_date:
            if hasattr(self.insure_end_date, 'to_alipay_dict'):
                params['insure_end_date'] = self.insure_end_date.to_alipay_dict()
            else:
                params['insure_end_date'] = self.insure_end_date
        if self.insure_start_date:
            if hasattr(self.insure_start_date, 'to_alipay_dict'):
                params['insure_start_date'] = self.insure_start_date.to_alipay_dict()
            else:
                params['insure_start_date'] = self.insure_start_date
        if self.insured_card_code:
            if hasattr(self.insured_card_code, 'to_alipay_dict'):
                params['insured_card_code'] = self.insured_card_code.to_alipay_dict()
            else:
                params['insured_card_code'] = self.insured_card_code
        if self.insured_card_type:
            if hasattr(self.insured_card_type, 'to_alipay_dict'):
                params['insured_card_type'] = self.insured_card_type.to_alipay_dict()
            else:
                params['insured_card_type'] = self.insured_card_type
        if self.insured_name:
            if hasattr(self.insured_name, 'to_alipay_dict'):
                params['insured_name'] = self.insured_name.to_alipay_dict()
            else:
                params['insured_name'] = self.insured_name
        if self.main_item_code:
            if hasattr(self.main_item_code, 'to_alipay_dict'):
                params['main_item_code'] = self.main_item_code.to_alipay_dict()
            else:
                params['main_item_code'] = self.main_item_code
        if self.main_item_content:
            if hasattr(self.main_item_content, 'to_alipay_dict'):
                params['main_item_content'] = self.main_item_content.to_alipay_dict()
            else:
                params['main_item_content'] = self.main_item_content
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.premium:
            if hasattr(self.premium, 'to_alipay_dict'):
                params['premium'] = self.premium.to_alipay_dict()
            else:
                params['premium'] = self.premium
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.special:
            if hasattr(self.special, 'to_alipay_dict'):
                params['special'] = self.special.to_alipay_dict()
            else:
                params['special'] = self.special
        if self.subject_information:
            if hasattr(self.subject_information, 'to_alipay_dict'):
                params['subject_information'] = self.subject_information.to_alipay_dict()
            else:
                params['subject_information'] = self.subject_information
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinInsuranceUnifiedApplyModel()
        if 'additional_item' in d:
            o.additional_item = d['additional_item']
        if 'apply_card_code' in d:
            o.apply_card_code = d['apply_card_code']
        if 'apply_card_type' in d:
            o.apply_card_type = d['apply_card_type']
        if 'apply_name' in d:
            o.apply_name = d['apply_name']
        if 'defin_business_code' in d:
            o.defin_business_code = d['defin_business_code']
        if 'defin_platform_access_type' in d:
            o.defin_platform_access_type = d['defin_platform_access_type']
        if 'insure_end_date' in d:
            o.insure_end_date = d['insure_end_date']
        if 'insure_start_date' in d:
            o.insure_start_date = d['insure_start_date']
        if 'insured_card_code' in d:
            o.insured_card_code = d['insured_card_code']
        if 'insured_card_type' in d:
            o.insured_card_type = d['insured_card_type']
        if 'insured_name' in d:
            o.insured_name = d['insured_name']
        if 'main_item_code' in d:
            o.main_item_code = d['main_item_code']
        if 'main_item_content' in d:
            o.main_item_content = d['main_item_content']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'premium' in d:
            o.premium = d['premium']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'rate' in d:
            o.rate = d['rate']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'special' in d:
            o.special = d['special']
        if 'subject_information' in d:
            o.subject_information = d['subject_information']
        return o


