#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicLifeaccountCreateModel(object):

    def __init__(self):
        self._agreement = None
        self._background = None
        self._biz_license_no = None
        self._brand_authorization = None
        self._brief_introduction = None
        self._business_license = None
        self._category_id = None
        self._contact_email = None
        self._contact_name = None
        self._contact_tel = None
        self._customer_tel = None
        self._logo = None
        self._menu_info = None
        self._name = None
        self._platform_account_id = None
        self._platform_unique_id = None
        self._user_id = None

    @property
    def agreement(self):
        return self._agreement

    @agreement.setter
    def agreement(self, value):
        self._agreement = value
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
    @property
    def biz_license_no(self):
        return self._biz_license_no

    @biz_license_no.setter
    def biz_license_no(self, value):
        self._biz_license_no = value
    @property
    def brand_authorization(self):
        return self._brand_authorization

    @brand_authorization.setter
    def brand_authorization(self, value):
        if isinstance(value, list):
            self._brand_authorization = list()
            for i in value:
                self._brand_authorization.append(i)
    @property
    def brief_introduction(self):
        return self._brief_introduction

    @brief_introduction.setter
    def brief_introduction(self, value):
        self._brief_introduction = value
    @property
    def business_license(self):
        return self._business_license

    @business_license.setter
    def business_license(self, value):
        self._business_license = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_tel(self):
        return self._contact_tel

    @contact_tel.setter
    def contact_tel(self, value):
        self._contact_tel = value
    @property
    def customer_tel(self):
        return self._customer_tel

    @customer_tel.setter
    def customer_tel(self, value):
        self._customer_tel = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def menu_info(self):
        return self._menu_info

    @menu_info.setter
    def menu_info(self, value):
        self._menu_info = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def platform_account_id(self):
        return self._platform_account_id

    @platform_account_id.setter
    def platform_account_id(self, value):
        self._platform_account_id = value
    @property
    def platform_unique_id(self):
        return self._platform_unique_id

    @platform_unique_id.setter
    def platform_unique_id(self, value):
        self._platform_unique_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement:
            if hasattr(self.agreement, 'to_alipay_dict'):
                params['agreement'] = self.agreement.to_alipay_dict()
            else:
                params['agreement'] = self.agreement
        if self.background:
            if hasattr(self.background, 'to_alipay_dict'):
                params['background'] = self.background.to_alipay_dict()
            else:
                params['background'] = self.background
        if self.biz_license_no:
            if hasattr(self.biz_license_no, 'to_alipay_dict'):
                params['biz_license_no'] = self.biz_license_no.to_alipay_dict()
            else:
                params['biz_license_no'] = self.biz_license_no
        if self.brand_authorization:
            if isinstance(self.brand_authorization, list):
                for i in range(0, len(self.brand_authorization)):
                    element = self.brand_authorization[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_authorization[i] = element.to_alipay_dict()
            if hasattr(self.brand_authorization, 'to_alipay_dict'):
                params['brand_authorization'] = self.brand_authorization.to_alipay_dict()
            else:
                params['brand_authorization'] = self.brand_authorization
        if self.brief_introduction:
            if hasattr(self.brief_introduction, 'to_alipay_dict'):
                params['brief_introduction'] = self.brief_introduction.to_alipay_dict()
            else:
                params['brief_introduction'] = self.brief_introduction
        if self.business_license:
            if hasattr(self.business_license, 'to_alipay_dict'):
                params['business_license'] = self.business_license.to_alipay_dict()
            else:
                params['business_license'] = self.business_license
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_tel:
            if hasattr(self.contact_tel, 'to_alipay_dict'):
                params['contact_tel'] = self.contact_tel.to_alipay_dict()
            else:
                params['contact_tel'] = self.contact_tel
        if self.customer_tel:
            if hasattr(self.customer_tel, 'to_alipay_dict'):
                params['customer_tel'] = self.customer_tel.to_alipay_dict()
            else:
                params['customer_tel'] = self.customer_tel
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.menu_info:
            if hasattr(self.menu_info, 'to_alipay_dict'):
                params['menu_info'] = self.menu_info.to_alipay_dict()
            else:
                params['menu_info'] = self.menu_info
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.platform_account_id:
            if hasattr(self.platform_account_id, 'to_alipay_dict'):
                params['platform_account_id'] = self.platform_account_id.to_alipay_dict()
            else:
                params['platform_account_id'] = self.platform_account_id
        if self.platform_unique_id:
            if hasattr(self.platform_unique_id, 'to_alipay_dict'):
                params['platform_unique_id'] = self.platform_unique_id.to_alipay_dict()
            else:
                params['platform_unique_id'] = self.platform_unique_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicLifeaccountCreateModel()
        if 'agreement' in d:
            o.agreement = d['agreement']
        if 'background' in d:
            o.background = d['background']
        if 'biz_license_no' in d:
            o.biz_license_no = d['biz_license_no']
        if 'brand_authorization' in d:
            o.brand_authorization = d['brand_authorization']
        if 'brief_introduction' in d:
            o.brief_introduction = d['brief_introduction']
        if 'business_license' in d:
            o.business_license = d['business_license']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_tel' in d:
            o.contact_tel = d['contact_tel']
        if 'customer_tel' in d:
            o.customer_tel = d['customer_tel']
        if 'logo' in d:
            o.logo = d['logo']
        if 'menu_info' in d:
            o.menu_info = d['menu_info']
        if 'name' in d:
            o.name = d['name']
        if 'platform_account_id' in d:
            o.platform_account_id = d['platform_account_id']
        if 'platform_unique_id' in d:
            o.platform_unique_id = d['platform_unique_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


