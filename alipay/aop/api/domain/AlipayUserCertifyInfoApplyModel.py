#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyInfoApplyModel(object):

    def __init__(self):
        self._agent_auth_letter_picture = None
        self._agent_cert_card_assist_picture = None
        self._agent_cert_card_info_picture = None
        self._agent_cert_expired_date = None
        self._agent_cert_no = None
        self._agent_cert_type = None
        self._agent_name = None
        self._biz_from = None
        self._contact_mobile = None
        self._legal_cert_card_assist_picture = None
        self._legal_cert_card_info_picture = None
        self._legal_cert_expired_date = None
        self._legal_cert_no = None
        self._legal_cert_type = None
        self._legal_name = None
        self._org_address = None
        self._org_business_scope = None
        self._org_city = None
        self._org_country = None
        self._org_main_cert_expired_date = None
        self._org_main_cert_no = None
        self._org_main_cert_picture = None
        self._org_name = None
        self._org_province = None
        self._org_type = None
        self._register_capital = None
        self._user_id = None

    @property
    def agent_auth_letter_picture(self):
        return self._agent_auth_letter_picture

    @agent_auth_letter_picture.setter
    def agent_auth_letter_picture(self, value):
        self._agent_auth_letter_picture = value
    @property
    def agent_cert_card_assist_picture(self):
        return self._agent_cert_card_assist_picture

    @agent_cert_card_assist_picture.setter
    def agent_cert_card_assist_picture(self, value):
        self._agent_cert_card_assist_picture = value
    @property
    def agent_cert_card_info_picture(self):
        return self._agent_cert_card_info_picture

    @agent_cert_card_info_picture.setter
    def agent_cert_card_info_picture(self, value):
        self._agent_cert_card_info_picture = value
    @property
    def agent_cert_expired_date(self):
        return self._agent_cert_expired_date

    @agent_cert_expired_date.setter
    def agent_cert_expired_date(self, value):
        self._agent_cert_expired_date = value
    @property
    def agent_cert_no(self):
        return self._agent_cert_no

    @agent_cert_no.setter
    def agent_cert_no(self, value):
        self._agent_cert_no = value
    @property
    def agent_cert_type(self):
        return self._agent_cert_type

    @agent_cert_type.setter
    def agent_cert_type(self, value):
        self._agent_cert_type = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def legal_cert_card_assist_picture(self):
        return self._legal_cert_card_assist_picture

    @legal_cert_card_assist_picture.setter
    def legal_cert_card_assist_picture(self, value):
        self._legal_cert_card_assist_picture = value
    @property
    def legal_cert_card_info_picture(self):
        return self._legal_cert_card_info_picture

    @legal_cert_card_info_picture.setter
    def legal_cert_card_info_picture(self, value):
        self._legal_cert_card_info_picture = value
    @property
    def legal_cert_expired_date(self):
        return self._legal_cert_expired_date

    @legal_cert_expired_date.setter
    def legal_cert_expired_date(self, value):
        self._legal_cert_expired_date = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_cert_type(self):
        return self._legal_cert_type

    @legal_cert_type.setter
    def legal_cert_type(self, value):
        self._legal_cert_type = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value
    @property
    def org_address(self):
        return self._org_address

    @org_address.setter
    def org_address(self, value):
        self._org_address = value
    @property
    def org_business_scope(self):
        return self._org_business_scope

    @org_business_scope.setter
    def org_business_scope(self, value):
        self._org_business_scope = value
    @property
    def org_city(self):
        return self._org_city

    @org_city.setter
    def org_city(self, value):
        self._org_city = value
    @property
    def org_country(self):
        return self._org_country

    @org_country.setter
    def org_country(self, value):
        self._org_country = value
    @property
    def org_main_cert_expired_date(self):
        return self._org_main_cert_expired_date

    @org_main_cert_expired_date.setter
    def org_main_cert_expired_date(self, value):
        self._org_main_cert_expired_date = value
    @property
    def org_main_cert_no(self):
        return self._org_main_cert_no

    @org_main_cert_no.setter
    def org_main_cert_no(self, value):
        self._org_main_cert_no = value
    @property
    def org_main_cert_picture(self):
        return self._org_main_cert_picture

    @org_main_cert_picture.setter
    def org_main_cert_picture(self, value):
        self._org_main_cert_picture = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def org_province(self):
        return self._org_province

    @org_province.setter
    def org_province(self, value):
        self._org_province = value
    @property
    def org_type(self):
        return self._org_type

    @org_type.setter
    def org_type(self, value):
        self._org_type = value
    @property
    def register_capital(self):
        return self._register_capital

    @register_capital.setter
    def register_capital(self, value):
        self._register_capital = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_auth_letter_picture:
            if hasattr(self.agent_auth_letter_picture, 'to_alipay_dict'):
                params['agent_auth_letter_picture'] = self.agent_auth_letter_picture.to_alipay_dict()
            else:
                params['agent_auth_letter_picture'] = self.agent_auth_letter_picture
        if self.agent_cert_card_assist_picture:
            if hasattr(self.agent_cert_card_assist_picture, 'to_alipay_dict'):
                params['agent_cert_card_assist_picture'] = self.agent_cert_card_assist_picture.to_alipay_dict()
            else:
                params['agent_cert_card_assist_picture'] = self.agent_cert_card_assist_picture
        if self.agent_cert_card_info_picture:
            if hasattr(self.agent_cert_card_info_picture, 'to_alipay_dict'):
                params['agent_cert_card_info_picture'] = self.agent_cert_card_info_picture.to_alipay_dict()
            else:
                params['agent_cert_card_info_picture'] = self.agent_cert_card_info_picture
        if self.agent_cert_expired_date:
            if hasattr(self.agent_cert_expired_date, 'to_alipay_dict'):
                params['agent_cert_expired_date'] = self.agent_cert_expired_date.to_alipay_dict()
            else:
                params['agent_cert_expired_date'] = self.agent_cert_expired_date
        if self.agent_cert_no:
            if hasattr(self.agent_cert_no, 'to_alipay_dict'):
                params['agent_cert_no'] = self.agent_cert_no.to_alipay_dict()
            else:
                params['agent_cert_no'] = self.agent_cert_no
        if self.agent_cert_type:
            if hasattr(self.agent_cert_type, 'to_alipay_dict'):
                params['agent_cert_type'] = self.agent_cert_type.to_alipay_dict()
            else:
                params['agent_cert_type'] = self.agent_cert_type
        if self.agent_name:
            if hasattr(self.agent_name, 'to_alipay_dict'):
                params['agent_name'] = self.agent_name.to_alipay_dict()
            else:
                params['agent_name'] = self.agent_name
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.legal_cert_card_assist_picture:
            if hasattr(self.legal_cert_card_assist_picture, 'to_alipay_dict'):
                params['legal_cert_card_assist_picture'] = self.legal_cert_card_assist_picture.to_alipay_dict()
            else:
                params['legal_cert_card_assist_picture'] = self.legal_cert_card_assist_picture
        if self.legal_cert_card_info_picture:
            if hasattr(self.legal_cert_card_info_picture, 'to_alipay_dict'):
                params['legal_cert_card_info_picture'] = self.legal_cert_card_info_picture.to_alipay_dict()
            else:
                params['legal_cert_card_info_picture'] = self.legal_cert_card_info_picture
        if self.legal_cert_expired_date:
            if hasattr(self.legal_cert_expired_date, 'to_alipay_dict'):
                params['legal_cert_expired_date'] = self.legal_cert_expired_date.to_alipay_dict()
            else:
                params['legal_cert_expired_date'] = self.legal_cert_expired_date
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_cert_type:
            if hasattr(self.legal_cert_type, 'to_alipay_dict'):
                params['legal_cert_type'] = self.legal_cert_type.to_alipay_dict()
            else:
                params['legal_cert_type'] = self.legal_cert_type
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        if self.org_address:
            if hasattr(self.org_address, 'to_alipay_dict'):
                params['org_address'] = self.org_address.to_alipay_dict()
            else:
                params['org_address'] = self.org_address
        if self.org_business_scope:
            if hasattr(self.org_business_scope, 'to_alipay_dict'):
                params['org_business_scope'] = self.org_business_scope.to_alipay_dict()
            else:
                params['org_business_scope'] = self.org_business_scope
        if self.org_city:
            if hasattr(self.org_city, 'to_alipay_dict'):
                params['org_city'] = self.org_city.to_alipay_dict()
            else:
                params['org_city'] = self.org_city
        if self.org_country:
            if hasattr(self.org_country, 'to_alipay_dict'):
                params['org_country'] = self.org_country.to_alipay_dict()
            else:
                params['org_country'] = self.org_country
        if self.org_main_cert_expired_date:
            if hasattr(self.org_main_cert_expired_date, 'to_alipay_dict'):
                params['org_main_cert_expired_date'] = self.org_main_cert_expired_date.to_alipay_dict()
            else:
                params['org_main_cert_expired_date'] = self.org_main_cert_expired_date
        if self.org_main_cert_no:
            if hasattr(self.org_main_cert_no, 'to_alipay_dict'):
                params['org_main_cert_no'] = self.org_main_cert_no.to_alipay_dict()
            else:
                params['org_main_cert_no'] = self.org_main_cert_no
        if self.org_main_cert_picture:
            if hasattr(self.org_main_cert_picture, 'to_alipay_dict'):
                params['org_main_cert_picture'] = self.org_main_cert_picture.to_alipay_dict()
            else:
                params['org_main_cert_picture'] = self.org_main_cert_picture
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.org_province:
            if hasattr(self.org_province, 'to_alipay_dict'):
                params['org_province'] = self.org_province.to_alipay_dict()
            else:
                params['org_province'] = self.org_province
        if self.org_type:
            if hasattr(self.org_type, 'to_alipay_dict'):
                params['org_type'] = self.org_type.to_alipay_dict()
            else:
                params['org_type'] = self.org_type
        if self.register_capital:
            if hasattr(self.register_capital, 'to_alipay_dict'):
                params['register_capital'] = self.register_capital.to_alipay_dict()
            else:
                params['register_capital'] = self.register_capital
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
        o = AlipayUserCertifyInfoApplyModel()
        if 'agent_auth_letter_picture' in d:
            o.agent_auth_letter_picture = d['agent_auth_letter_picture']
        if 'agent_cert_card_assist_picture' in d:
            o.agent_cert_card_assist_picture = d['agent_cert_card_assist_picture']
        if 'agent_cert_card_info_picture' in d:
            o.agent_cert_card_info_picture = d['agent_cert_card_info_picture']
        if 'agent_cert_expired_date' in d:
            o.agent_cert_expired_date = d['agent_cert_expired_date']
        if 'agent_cert_no' in d:
            o.agent_cert_no = d['agent_cert_no']
        if 'agent_cert_type' in d:
            o.agent_cert_type = d['agent_cert_type']
        if 'agent_name' in d:
            o.agent_name = d['agent_name']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'legal_cert_card_assist_picture' in d:
            o.legal_cert_card_assist_picture = d['legal_cert_card_assist_picture']
        if 'legal_cert_card_info_picture' in d:
            o.legal_cert_card_info_picture = d['legal_cert_card_info_picture']
        if 'legal_cert_expired_date' in d:
            o.legal_cert_expired_date = d['legal_cert_expired_date']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_cert_type' in d:
            o.legal_cert_type = d['legal_cert_type']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        if 'org_address' in d:
            o.org_address = d['org_address']
        if 'org_business_scope' in d:
            o.org_business_scope = d['org_business_scope']
        if 'org_city' in d:
            o.org_city = d['org_city']
        if 'org_country' in d:
            o.org_country = d['org_country']
        if 'org_main_cert_expired_date' in d:
            o.org_main_cert_expired_date = d['org_main_cert_expired_date']
        if 'org_main_cert_no' in d:
            o.org_main_cert_no = d['org_main_cert_no']
        if 'org_main_cert_picture' in d:
            o.org_main_cert_picture = d['org_main_cert_picture']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'org_province' in d:
            o.org_province = d['org_province']
        if 'org_type' in d:
            o.org_type = d['org_type']
        if 'register_capital' in d:
            o.register_capital = d['register_capital']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


