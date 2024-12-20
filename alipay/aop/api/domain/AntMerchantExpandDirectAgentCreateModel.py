#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantContact import MerchantContact
from alipay.aop.api.domain.DirectAddressInfo import DirectAddressInfo


class AntMerchantExpandDirectAgentCreateModel(object):

    def __init__(self):
        self._auth_app_id = None
        self._business_license_mobile = None
        self._business_license_no = None
        self._business_license_pic = None
        self._contact_info = None
        self._date_limitation = None
        self._external_id = None
        self._leads_id = None
        self._long_term = None
        self._mcc_code = None
        self._merchant_account = None
        self._out_biz_no = None
        self._shop_address = None
        self._shop_name = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None
        self._special_license_pic = None

    @property
    def auth_app_id(self):
        return self._auth_app_id

    @auth_app_id.setter
    def auth_app_id(self, value):
        self._auth_app_id = value
    @property
    def business_license_mobile(self):
        return self._business_license_mobile

    @business_license_mobile.setter
    def business_license_mobile(self, value):
        self._business_license_mobile = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, MerchantContact):
            self._contact_info = value
        else:
            self._contact_info = MerchantContact.from_alipay_dict(value)
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def merchant_account(self):
        return self._merchant_account

    @merchant_account.setter
    def merchant_account(self, value):
        self._merchant_account = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        if isinstance(value, DirectAddressInfo):
            self._shop_address = value
        else:
            self._shop_address = DirectAddressInfo.from_alipay_dict(value)
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_scene_pic(self):
        return self._shop_scene_pic

    @shop_scene_pic.setter
    def shop_scene_pic(self, value):
        self._shop_scene_pic = value
    @property
    def shop_sign_board_pic(self):
        return self._shop_sign_board_pic

    @shop_sign_board_pic.setter
    def shop_sign_board_pic(self, value):
        self._shop_sign_board_pic = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        self._special_license_pic = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_app_id:
            if hasattr(self.auth_app_id, 'to_alipay_dict'):
                params['auth_app_id'] = self.auth_app_id.to_alipay_dict()
            else:
                params['auth_app_id'] = self.auth_app_id
        if self.business_license_mobile:
            if hasattr(self.business_license_mobile, 'to_alipay_dict'):
                params['business_license_mobile'] = self.business_license_mobile.to_alipay_dict()
            else:
                params['business_license_mobile'] = self.business_license_mobile
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = self.date_limitation.to_alipay_dict()
            else:
                params['date_limitation'] = self.date_limitation
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = self.long_term.to_alipay_dict()
            else:
                params['long_term'] = self.long_term
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.merchant_account:
            if hasattr(self.merchant_account, 'to_alipay_dict'):
                params['merchant_account'] = self.merchant_account.to_alipay_dict()
            else:
                params['merchant_account'] = self.merchant_account
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.shop_scene_pic:
            if hasattr(self.shop_scene_pic, 'to_alipay_dict'):
                params['shop_scene_pic'] = self.shop_scene_pic.to_alipay_dict()
            else:
                params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            if hasattr(self.shop_sign_board_pic, 'to_alipay_dict'):
                params['shop_sign_board_pic'] = self.shop_sign_board_pic.to_alipay_dict()
            else:
                params['shop_sign_board_pic'] = self.shop_sign_board_pic
        if self.special_license_pic:
            if hasattr(self.special_license_pic, 'to_alipay_dict'):
                params['special_license_pic'] = self.special_license_pic.to_alipay_dict()
            else:
                params['special_license_pic'] = self.special_license_pic
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandDirectAgentCreateModel()
        if 'auth_app_id' in d:
            o.auth_app_id = d['auth_app_id']
        if 'business_license_mobile' in d:
            o.business_license_mobile = d['business_license_mobile']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'date_limitation' in d:
            o.date_limitation = d['date_limitation']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'long_term' in d:
            o.long_term = d['long_term']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'merchant_account' in d:
            o.merchant_account = d['merchant_account']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_scene_pic' in d:
            o.shop_scene_pic = d['shop_scene_pic']
        if 'shop_sign_board_pic' in d:
            o.shop_sign_board_pic = d['shop_sign_board_pic']
        if 'special_license_pic' in d:
            o.special_license_pic = d['special_license_pic']
        return o


