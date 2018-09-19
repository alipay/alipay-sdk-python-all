#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandContractFacetofaceSignModel(object):

    def __init__(self):
        self._business_license_auth_pic = None
        self._business_license_no = None
        self._business_license_pic = None
        self._contact_email = None
        self._contact_mobile = None
        self._contact_name = None
        self._mcc_code = None
        self._out_biz_no = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None
        self._special_license_pic = None

    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        self._business_license_auth_pic = value
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
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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
        if self.business_license_auth_pic:
            if hasattr(self.business_license_auth_pic, 'to_alipay_dict'):
                params['business_license_auth_pic'] = self.business_license_auth_pic.to_alipay_dict()
            else:
                params['business_license_auth_pic'] = self.business_license_auth_pic
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
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AntMerchantExpandContractFacetofaceSignModel()
        if 'business_license_auth_pic' in d:
            o.business_license_auth_pic = d['business_license_auth_pic']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'shop_scene_pic' in d:
            o.shop_scene_pic = d['shop_scene_pic']
        if 'shop_sign_board_pic' in d:
            o.shop_sign_board_pic = d['shop_sign_board_pic']
        if 'special_license_pic' in d:
            o.special_license_pic = d['special_license_pic']
        return o


