#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniBaseinfoMultiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBaseinfoMultiQueryResponse, self).__init__()
        self._account_type = None
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._area = None
        self._business_license_no = None
        self._business_name = None
        self._category_names = None
        self._contact_email = None
        self._contact_mobile = None
        self._contact_name = None
        self._pid = None
        self._service_email = None
        self._service_phone = None

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value
    @property
    def category_names(self):
        return self._category_names

    @category_names.setter
    def category_names(self, value):
        self._category_names = value
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
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def service_email(self):
        return self._service_email

    @service_email.setter
    def service_email(self, value):
        self._service_email = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBaseinfoMultiQueryResponse, self).parse_response_content(response_content)
        if 'account_type' in response:
            self.account_type = response['account_type']
        if 'app_desc' in response:
            self.app_desc = response['app_desc']
        if 'app_english_name' in response:
            self.app_english_name = response['app_english_name']
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_slogan' in response:
            self.app_slogan = response['app_slogan']
        if 'area' in response:
            self.area = response['area']
        if 'business_license_no' in response:
            self.business_license_no = response['business_license_no']
        if 'business_name' in response:
            self.business_name = response['business_name']
        if 'category_names' in response:
            self.category_names = response['category_names']
        if 'contact_email' in response:
            self.contact_email = response['contact_email']
        if 'contact_mobile' in response:
            self.contact_mobile = response['contact_mobile']
        if 'contact_name' in response:
            self.contact_name = response['contact_name']
        if 'pid' in response:
            self.pid = response['pid']
        if 'service_email' in response:
            self.service_email = response['service_email']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
